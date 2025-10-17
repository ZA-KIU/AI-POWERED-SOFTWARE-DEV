const API_KEY = "AIzaSyDcYymMvnHgfg3ej66gLcrnFE7W0w2WYvs"; // forgothow to access from env, but is it that crucial for the first assignment?

function estimateTokens(text) {
  return Math.ceil(text.length / 4);
}

function calculateCost(inputTokens, outputTokens) {
  const INPUT_COST_PER_1K = 0.00025;
  const OUTPUT_COST_PER_1K = 0.0005;
  const inputCost = (inputTokens / 1000) * INPUT_COST_PER_1K;
  const outputCost = (outputTokens / 1000) * OUTPUT_COST_PER_1K;
  return {
    input: inputCost,
    output: outputCost,
    total: inputCost + outputCost
  };
}

async function fetchWithRetry(url, options, maxRetries = 3) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      const response = await fetch(url, options);
      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }
      return response;
    } catch (error) {
      console.error(`Attempt ${attempt + 1} failed:`, error.message);
      if (attempt === maxRetries - 1) throw error;
      const delay = Math.pow(2, attempt) * 1000;
      console.log(`Retrying in ${delay}ms...`);
      await new Promise((resolve) => setTimeout(resolve, delay));
    }
  }
}

async function generateTextStreaming() {
  const prompt = document.getElementById("promptInput").value;
  const outputDiv = document.getElementById("output");
  const costDisplay = document.getElementById("costDisplay");
  const copyButton = document.getElementById("copyButton");

  if (!prompt.trim()) {
    alert("Please enter a prompt!");
    return;
  }

  copyButton.disabled = true;
  outputDiv.textContent = "";
  costDisplay.textContent = "Cost: calculating...";

  const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:streamGenerateContent?key=${API_KEY}`; 

  const options = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      contents: [
        {
          role: "user",
          parts: [{ text: prompt }]
        }
      ]
    })
  };

  const startTime = Date.now();
  try {
    const response = await fetchWithRetry(url, options);
    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    let fullText = "";
    let finalInputTokens = 0;
    let finalOutputTokens = 0;
    let buffer = ""; 

    while (true) {
      const { done, value } = await reader.read();
      if (done) break;

      const chunk = decoder.decode(value, { stream: true }); 
      buffer += chunk;
      
      const lines = buffer.split("\n");
      buffer = lines.pop(); 

      for (const line of lines) {
        const trimmedLine = line.trim();
        if (!trimmedLine || trimmedLine === ',') continue;
        
        if (trimmedLine.includes('"text":')) {
          const match = trimmedLine.match(/"text":\s*"(.*)"/);
          if (match && match[1]) {
            let text = match[1];
            text = text.replace(/\\n/g, '\n')
                       .replace(/\\"/g, '"')
                       .replace(/\\\\/g, '\\');
            
            fullText += text;
            outputDiv.textContent += text;
          }
        }
        
        if (trimmedLine.includes('"promptTokenCount":')) {
          const match = trimmedLine.match(/"promptTokenCount":\s*(\d+)/);
          if (match) finalInputTokens = parseInt(match[1]);
        }
        
        if (trimmedLine.includes('"candidatesTokenCount":')) {
          const match = trimmedLine.match(/"candidatesTokenCount":\s*(\d+)/);
          if (match) finalOutputTokens = parseInt(match[1]);
        }
      }
    }

    if (fullText.trim() === "") {
      outputDiv.textContent = "Request finished but no text was generated. This is due to an empty response.";
      costDisplay.textContent = "";
      return;
    }

    const cost = calculateCost(finalInputTokens, finalOutputTokens);
    const duration = Date.now() - startTime;

    costDisplay.textContent = `Cost: $${cost.total.toFixed(6)} (In: ${finalInputTokens} tokens, Out: ${finalOutputTokens} tokens)`;
    console.log(`Duration: ${duration}ms`);

    copyButton.disabled = false;

  } catch (error) {
    outputDiv.textContent = "Error: " + error.message;
    costDisplay.textContent = "";
  }
}

function copyToClipboard() {
  const outputDiv = document.getElementById("output");
  const textToCopy = outputDiv.textContent;
  const copyButton = document.getElementById("copyButton");

  navigator.clipboard.writeText(textToCopy).then(() => {
    copyButton.textContent = "Copied!";
    copyButton.disabled = true;
    setTimeout(() => {
      copyButton.textContent = "Copy to Clipboard";
      if (outputDiv.textContent.trim() !== "") copyButton.disabled = false;
    }, 2000);
  }).catch(err => {
    console.error("Copy failed: ", err);
    alert("Failed to copy text. See console for details.");
  });
}

function setFooter() {
  const footer = document.getElementById("footerContent");
  const today = new Date().toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric"
  });
  footer.textContent = `© ${today} chkhikvadze.konstant@kiu.edu.ge`;
}

window.generateTextStreaming = generateTextStreaming;
window.copyToClipboard = copyToClipboard;
window.onload = setFooter;