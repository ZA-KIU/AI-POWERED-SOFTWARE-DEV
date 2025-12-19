# Lab 11: Multi-Vendor Fallbacks + Demo Day Sprint

**Building AI-Powered Applications | Week 13 Lab**  
**Date:** December 19, 2025  
**Duration:** 120 minutes  
**Focus:** Quick reliability implementation + demo preparation

---

## 🎯 Lab Objectives

By the end of this lab, you will:
- Implement basic multi-vendor fallback chain (OpenAI → Anthropic)
- Add automatic retry logic with exponential backoff
- Begin production of your 90-second demo video
- Structure your 10-minute final presentation
- Create sprint plan for final 7 days

---

## ⏱️ Lab Structure

### Part 1: Multi-Vendor Implementation (60 minutes)
**Goal:** Get fallbacks working reliably, not perfectly

### Part 2: Demo Day Workshop (60 minutes)
**Goal:** Start your video, plan your presentation, map your sprint

---

# Part 1: Multi-Vendor Fallbacks (60 minutes)

## Learning Objectives
- Build provider abstraction layer
- Implement automatic fallback chain
- Add basic cost tracking
- **Ship it and move on** ✅

---

## Setup (5 minutes)

### Prerequisites
- Working capstone application (deployed)
- API keys for OpenAI and Anthropic
- Python 3.8+
- Terminal access

### Environment Check
```bash
# Verify you have API keys
echo $OPENAI_API_KEY
echo $ANTHROPIC_API_KEY

# If missing, add them to your .env file
```

---

## Implementation Roadmap

### Step 1: Provider Abstraction (15 minutes)

Create a simple base class for all providers:

**File: `src/providers/base_provider.py`**
```python
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class ProviderResponse:
    """Standard response format from any provider"""
    content: str
    model: str
    tokens_used: int
    cost: float
    latency_ms: float

@dataclass
class ProviderError:
    """Standard error format"""
    error_type: str  # "rate_limit", "api_error", "timeout", "invalid_request"
    message: str
    retry_after: Optional[int] = None

class LLMProvider(ABC):
    """Base class for all LLM providers"""
    
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model
    
    @abstractmethod
    def generate(self, prompt: str, max_tokens: int = 500) -> ProviderResponse:
        """Generate completion from this provider"""
        pass
    
    @abstractmethod
    def classify_error(self, error: Exception) -> ProviderError:
        """Classify error for fallback decisions"""
        pass
```

---

### Step 2: OpenAI Provider (10 minutes)

**File: `src/providers/openai_provider.py`**
```python
from openai import OpenAI
import time
from .base_provider import LLMProvider, ProviderResponse, ProviderError

class OpenAIProvider(LLMProvider):
    # Pricing per 1M tokens (December 2025)
    PRICING = {
        "gpt-4o": {"input": 2.50, "output": 10.00},
        "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    }
    
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        super().__init__(api_key, model)
        self.client = OpenAI(api_key=api_key)
    
    def generate(self, prompt: str, max_tokens: int = 500) -> ProviderResponse:
        start = time.time()
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens
        )
        
        latency = (time.time() - start) * 1000
        
        # Calculate cost
        pricing = self.PRICING[self.model]
        input_cost = (response.usage.prompt_tokens / 1_000_000) * pricing["input"]
        output_cost = (response.usage.completion_tokens / 1_000_000) * pricing["output"]
        
        return ProviderResponse(
            content=response.choices[0].message.content,
            model=self.model,
            tokens_used=response.usage.total_tokens,
            cost=input_cost + output_cost,
            latency_ms=latency
        )
    
    def classify_error(self, error: Exception) -> ProviderError:
        error_msg = str(error).lower()
        
        if "rate_limit" in error_msg or "429" in error_msg:
            # Extract retry-after if available
            retry_after = 60  # Default
            return ProviderError("rate_limit", str(error), retry_after)
        
        elif "timeout" in error_msg:
            return ProviderError("timeout", str(error))
        
        elif "invalid" in error_msg or "400" in error_msg:
            return ProviderError("invalid_request", str(error))
        
        else:
            return ProviderError("api_error", str(error))
```

---

### Step 3: Anthropic Provider (10 minutes)

**File: `src/providers/anthropic_provider.py`**
```python
from anthropic import Anthropic
import time
from .base_provider import LLMProvider, ProviderResponse, ProviderError

class AnthropicProvider(LLMProvider):
    # Pricing per 1M tokens (December 2025)
    PRICING = {
        "claude-sonnet-4-20250514": {"input": 3.00, "output": 15.00},
        "claude-haiku-3-5-20241022": {"input": 0.80, "output": 4.00},
    }
    
    def __init__(self, api_key: str, model: str = "claude-haiku-3-5-20241022"):
        super().__init__(api_key, model)
        self.client = Anthropic(api_key=api_key)
    
    def generate(self, prompt: str, max_tokens: int = 500) -> ProviderResponse:
        start = time.time()
        
        response = self.client.messages.create(
            model=self.model,
            max_tokens=max_tokens,
            messages=[{"role": "user", "content": prompt}]
        )
        
        latency = (time.time() - start) * 1000
        
        # Calculate cost
        pricing = self.PRICING[self.model]
        input_cost = (response.usage.input_tokens / 1_000_000) * pricing["input"]
        output_cost = (response.usage.output_tokens / 1_000_000) * pricing["output"]
        
        return ProviderResponse(
            content=response.content[0].text,
            model=self.model,
            tokens_used=response.usage.input_tokens + response.usage.output_tokens,
            cost=input_cost + output_cost,
            latency_ms=latency
        )
    
    def classify_error(self, error: Exception) -> ProviderError:
        error_msg = str(error).lower()
        
        if "rate_limit" in error_msg or "429" in error_msg:
            return ProviderError("rate_limit", str(error), 60)
        elif "timeout" in error_msg:
            return ProviderError("timeout", str(error))
        elif "invalid" in error_msg:
            return ProviderError("invalid_request", str(error))
        else:
            return ProviderError("api_error", str(error))
```

---

### Step 4: Simple Fallback Chain (15 minutes)

**File: `src/providers/router.py`**
```python
import asyncio
import time
from typing import List
from .base_provider import LLMProvider, ProviderResponse, ProviderError

class SimpleRouter:
    """Dead-simple fallback chain: try each provider until one works"""
    
    def __init__(self, providers: List[LLMProvider], max_retries: int = 3):
        self.providers = providers
        self.max_retries = max_retries
    
    def generate(self, prompt: str, max_tokens: int = 500) -> ProviderResponse:
        """Try each provider in order until one succeeds"""
        
        for attempt, provider in enumerate(self.providers):
            for retry in range(self.max_retries):
                try:
                    print(f"Trying {provider.model} (attempt {retry + 1})...")
                    response = provider.generate(prompt, max_tokens)
                    print(f"✓ Success with {provider.model}")
                    return response
                
                except Exception as e:
                    error = provider.classify_error(e)
                    print(f"✗ Error: {error.error_type} - {error.message}")
                    
                    # If rate limited, wait and retry same provider
                    if error.error_type == "rate_limit" and retry < self.max_retries - 1:
                        wait_time = 2 ** retry  # Exponential backoff: 1s, 2s, 4s
                        print(f"  Waiting {wait_time}s before retry...")
                        time.sleep(wait_time)
                        continue
                    
                    # If invalid request, don't retry - fail immediately
                    if error.error_type == "invalid_request":
                        raise Exception(f"Invalid request: {error.message}")
                    
                    # Otherwise, try next provider
                    break
        
        raise Exception("All providers failed")
```

---

### Step 5: Quick Integration Test (5 minutes)

**File: `test_fallback.py`**
```python
import os
from src.providers.openai_provider import OpenAIProvider
from src.providers.anthropic_provider import AnthropicProvider
from src.providers.router import SimpleRouter

# Setup providers
openai = OpenAIProvider(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-4o-mini"
)

anthropic = AnthropicProvider(
    api_key=os.getenv("ANTHROPIC_API_KEY"),
    model="claude-haiku-3-5-20241022"
)

# Create router with fallback chain
router = SimpleRouter(providers=[openai, anthropic])

# Test
print("Testing fallback chain...")
response = router.generate("Write a haiku about AI")

print(f"\nResponse: {response.content}")
print(f"Model: {response.model}")
print(f"Cost: ${response.cost:.4f}")
print(f"Latency: {response.latency_ms:.0f}ms")
```

Run it:
```bash
python test_fallback.py
```

---

## ✅ Part 1 Checkpoint (60 minutes)

You should now have:
- ✅ Base provider interface working
- ✅ OpenAI provider with error handling
- ✅ Anthropic provider with error handling
- ✅ Simple fallback router working
- ✅ Basic cost tracking per request

**Good enough! Time to prep for demo day.** 🎬

---

# Part 2: Demo Day Workshop (60 minutes)

## Workshop Objectives
- Start your 90-second video
- Structure your 10-minute presentation
- Map your final 7-day sprint

---

## Section A: Video Production Workshop (25 minutes)

### Understanding the Format (5 minutes)

**Recommended Format: "Talking-Head + UI"**
- Founder on camera + product screen recording
- 0-15s: Hook (face on camera)
- 15-45s: Solution (UI overlay showing the "magic moment")
- 45-75s: Value (mix of face + metrics/results)
- 75-90s: Call to Action (face on camera with URL)

### Your Video Script Template (10 minutes)

**Fill this out as a team RIGHT NOW:**

```markdown
## 90-Second Video Script

### The Hook (0-15s) - FACE ON CAMERA
"I'm [Name], and we built [App] because [Pain Point]."
Example: "I'm Sarah, and we built TaxAI because I used to spend 4 hours every Sunday dreading tax prep..."

YOUR HOOK:
_______________________________________________
_______________________________________________

### The Solution (15-45s) - UI OVERLAY
"Then I built [App]. It [Core Feature]."
[SHOW: Screen recording of the "magic moment"]

YOUR SOLUTION (what to show on screen):
_______________________________________________
_______________________________________________

### The Value (45-75s) - MIX
"We saved X hours..." or "Users gave us 4.8 stars..."
[SHOW: Results, metrics, testimonials]

YOUR VALUE PROPS:
_______________________________________________
_______________________________________________

### Call to Action (75-90s) - FACE ON CAMERA
"Try it live at [URL]. Thank you."

YOUR CTA:
_______________________________________________
_______________________________________________
```

### Recording Plan (10 minutes)

**Equipment Needed:**
- Phone camera (or laptop webcam)
- Screen recording software (QuickTime, OBS, Loom)
- Good lighting (face the window)
- Quiet room

**Today's Homework (Due Monday):**
1. Record "talking head" segments (0-15s, 75-90s)
2. Record screen capture of your app's "magic moment" (15-45s)
3. Collect metrics/results for value section (45-75s)

**Editing (Monday-Tuesday):**
- Use iMovie, DaVinci Resolve (free), or CapCut
- Aim for 88-92 seconds (gives buffer)
- Export as MP4, 1080p

---

## Section B: Presentation Structure Workshop (25 minutes)

### 10-Minute Breakdown

**Reminder from slides:**
- 0:00-0:30 = Introduction (team, problem)
- 0:30-2:00 = Video Demo (play your 90-sec video)
- 2:00-8:00 = Live Demo (interact with app, show AI features)
- 8:00-10:00 = Case Study (architecture, tech decisions)

### Live Demo Planning (15 minutes)

**Plan your 5-6 minute live demo RIGHT NOW:**

```markdown
## Live Demo Script

### Opening (30 seconds)
"Let me show you how it actually works..."

DEMO STEP 1 (1 minute):
Action: ___________________________________
What AI does: ______________________________
Why it matters: ____________________________

DEMO STEP 2 (1 minute):
Action: ___________________________________
What AI does: ______________________________
Why it matters: ____________________________

DEMO STEP 3 (1 minute):
Action: ___________________________________
What AI does: ______________________________
Why it matters: ____________________________

### Highlight Multi-Vendor (30 seconds):
"Notice we're using [Provider]. If it fails, we automatically switch to [Backup]..."

### Closing (30 seconds):
"That's the core workflow. Now let me show you the architecture..."
```

**Critical Rules:**
- Test your demo 10+ times before presentation
- Have backup plan (video recording of demo if internet fails)
- Show the AI working in real-time
- Narrate what's happening

### Case Study Slides (10 minutes)

**You need 3-4 slides for the case study portion (8:00-10:00):**

**Slide 1: Architecture Diagram**
- Show: Frontend → Backend → Multi-Vendor LLMs
- Highlight: Fallback chain

**Slide 2: Tech Stack**
- Frontend: [Your framework]
- Backend: [Your framework]
- AI: OpenAI (primary), Anthropic (backup), Ollama (local)
- Deployment: Vercel/Railway
- Database: [Your choice]

**Slide 3: Key Decisions**
- Why we chose [Model]: [Reason]
- Why multi-vendor: Reliability + cost optimization
- Why [Framework]: [Reason]

**Slide 4: Metrics**
- Average latency: [X]ms
- Cost per query: $[X]
- Fallback success rate: [X]%
- User satisfaction: [X]/5

---

## Section C: Final Sprint Planning (10 minutes)

### 7-Day Countdown Checklist

**Today (Thursday Dec 19) - Lab:**
- ✅ Multi-vendor fallbacks working
- ✅ Video script written
- ✅ Demo flow mapped

**Friday (Dec 20):**
- Record video segments
- Test multi-vendor implementation in production
- Fix critical bugs

**Weekend (Dec 21-22):**
- Edit video
- Rehearse live demo 3+ times
- Write case study content

**Monday (Dec 23):**
- Final video due (embed in README)
- Complete case study document
- Rehearse full presentation

**Tuesday (Dec 24):**
- Final testing
- Backup plan ready
- Rehearse again

**Wednesday (Dec 25) - DEMO DAY 1:**
- Teams 1-23 present

**Thursday (Dec 26) - DEMO DAY 2:**
- Teams 24-45 present

---

## 📝 Deliverables (No Homework - All Sprint Work)

### By End of Lab Today:
1. ✅ Multi-vendor fallbacks working locally
2. ✅ Video script completed
3. ✅ Live demo flow mapped
4. ✅ Sprint plan for next 7 days

### By Monday Dec 23:
1. 90-second video completed and embedded in README
2. Case study document (2,500+ words)
3. Architecture diagram
4. Live demo tested 5+ times

### By Tuesday Dec 24 (Deadline):
1. Everything submitted to GitHub
2. Deployed URL accessible
3. Presentation slides ready
4. Backup plans in place

---

## 🚨 Common Pitfalls to Avoid

### Technical:
- Don't over-engineer fallbacks - simple is fine
- Don't skip error handling - you'll get rate limited
- Don't hardcode API keys - use .env
- Don't test only on localhost - test deployed app

### Demo Day:
- Don't talk too fast - rehearse with timer
- Don't skip the video - it drives 100+ signups
- Don't wing the live demo - test 10+ times
- Don't go over 10 minutes - you'll be cut off

---

## 📚 Resources

### Video Production:
- Loom (free screen recording): loom.com
- DaVinci Resolve (free editing): blackmagicdesign.com
- iMovie (Mac, free): Built-in

### Presentation:
- Google Slides: slides.google.com
- Figma (for diagrams): figma.com
- Canva: canva.com

### Testing:
- LoadForge (API testing): loadforge.com
- Golden test set: tests/integration/golden_set.json

---

## ✅ Success Criteria

By end of lab, you can:
- ✓ Simulate primary provider failure → automatic fallback works
- ✓ Explain your video structure to instructor
- ✓ Walk through your live demo flow (without running it)
- ✓ Show sprint plan for next 7 days

**You've got this. Time to ship. 🚀**

---

**Next:** Week 14 = Pure polish time (no lectures/labs, just office hours)  
**Demo Days:** December 25-26, 2025  
**Final Submission:** December 27, 2025
