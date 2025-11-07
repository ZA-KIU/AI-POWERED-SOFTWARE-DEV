# Lovable.dev Setup Guide

**Quick Guide to Setting Up Your Project on Lovable**

---

## What is Lovable.dev?

Lovable.dev is a rapid development platform for building full-stack web applications. It provides:
- Pre-configured development environment
- Instant deployment
- Built-in AI assistance
- Easy sharing and collaboration

**Perfect for:** Quick prototyping, MVP development, demo apps

---

## Step 1: Create Account (5 min)

1. Go to [lovable.dev](https://lovable.dev)
2. Sign up with GitHub, Google, or email
3. Verify your email
4. Complete profile (optional)

**Free Tier Includes:**
- Unlimited projects
- Instant deployment
- Custom domains
- 100 GB bandwidth/month

---

## Step 2: Create New Project (5 min)

### Option A: Start from Scratch
1. Click "New Project"
2. Choose template:
   - React + TypeScript (recommended for most teams)
   - React + JavaScript
   - Next.js (if you need SSR)
   - Vite + React (fastest)
3. Name your project
4. Click "Create"

### Option B: Import from GitHub
1. Click "Import from GitHub"
2. Connect your GitHub account
3. Select repository
4. Configure build settings
5. Deploy

**Recommended for Sprint 1:** Start from scratch with React + TypeScript template

---

## Step 3: Configure Environment Variables (10 min)

### In Lovable Dashboard:
1. Go to Project Settings
2. Click "Environment Variables"
3. Add your API keys:

```
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-ant-...
VITE_API_URL=http://localhost:5000  # For development
```

### Security Best Practices:
- ✅ Store keys in environment variables
- ✅ Use `.env.example` for documentation
- ✅ Never commit `.env` files
- ❌ Never hardcode API keys in code
- ❌ Never commit keys to GitHub

---

## Step 4: Project Structure (10 min)

### Recommended Structure:
```
your-project/
├── src/
│   ├── components/      # React components
│   │   ├── ChatInterface.tsx
│   │   ├── ResponseDisplay.tsx
│   │   └── LoadingSpinner.tsx
│   ├── services/        # API calls
│   │   ├── rag.ts
│   │   ├── functions.ts
│   │   └── llm.ts
│   ├── types/           # TypeScript types
│   │   └── index.ts
│   ├── utils/           # Helper functions
│   │   └── format.ts
│   ├── App.tsx          # Main app
│   └── main.tsx         # Entry point
├── public/              # Static assets
├── .env.example         # Environment template
├── package.json         # Dependencies
├── tsconfig.json        # TypeScript config
└── README.md            # Documentation
```

---

## Step 5: Install Dependencies (5 min)

### Essential Packages:
```bash
# AI SDKs
npm install openai @anthropic-ai/sdk

# State management (if needed)
npm install zustand

# HTTP client
npm install axios

# Form handling
npm install react-hook-form

# UI components (optional)
npm install @radix-ui/react-dialog @radix-ui/react-toast
```

### Update package.json:
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "openai": "^4.20.0",
    "@anthropic-ai/sdk": "^0.9.0",
    "axios": "^1.6.0",
    "zustand": "^4.4.0"
  }
}
```

---

## Step 6: Basic API Setup (15 min)

### Create API Service:
```typescript
// src/services/llm.ts
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: import.meta.env.VITE_OPENAI_API_KEY,
  dangerouslyAllowBrowser: true // Only for prototyping!
});

export async function chat(message: string): Promise<string> {
  const response = await client.chat.completions.create({
    model: 'gpt-4o-mini',
    messages: [{ role: 'user', content: message }],
  });
  
  return response.choices[0].message.content || '';
}
```

**⚠️ Security Note:** The `dangerouslyAllowBrowser: true` flag is ONLY for prototyping. In production, always call OpenAI from your backend!

---

## Step 7: Connect Frontend (20 min)

### Simple Chat Interface:
```typescript
// src/App.tsx
import { useState } from 'react';
import { chat } from './services/llm';

export default function App() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    
    try {
      const result = await chat(input);
      setResponse(result);
    } catch (error) {
      setResponse('Error: ' + (error as Error).message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mx-auto p-4 max-w-2xl">
      <h1 className="text-3xl font-bold mb-4">AI Chat</h1>
      
      <form onSubmit={handleSubmit} className="mb-4">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Ask me anything..."
          className="w-full p-2 border rounded"
          disabled={loading}
        />
        <button 
          type="submit"
          className="mt-2 px-4 py-2 bg-blue-500 text-white rounded"
          disabled={loading}
        >
          {loading ? 'Thinking...' : 'Send'}
        </button>
      </form>
      
      {response && (
        <div className="p-4 border rounded bg-gray-50">
          {response}
        </div>
      )}
    </div>
  );
}
```

---

## Step 8: Deploy (5 min)

### In Lovable:
1. Save your changes (auto-saves every few seconds)
2. Click "Deploy" button
3. Wait 30-60 seconds for build
4. Get your public URL: `https://your-project.lovable.dev`

### Custom Domain (Optional):
1. Go to Project Settings → Domains
2. Add your custom domain
3. Update DNS records as shown
4. Wait for SSL certificate (5-10 min)

---

## Step 9: Testing (10 min)

### Test Checklist:
- [ ] Page loads without errors
- [ ] Input field accepts text
- [ ] Submit button triggers API call
- [ ] Loading state shows while processing
- [ ] Response displays correctly
- [ ] Error messages show if API fails
- [ ] Works in different browsers
- [ ] Works on mobile

### Debug Tips:
1. Open browser console (F12)
2. Check Network tab for API calls
3. Look for error messages
4. Verify environment variables are set
5. Test API key directly (curl or Postman)

---

## Common Issues & Solutions

### Issue: "API key not found"
**Solution:** Verify environment variables:
```bash
# In Lovable console
echo $VITE_OPENAI_API_KEY
```

### Issue: "CORS error"
**Solution:** For prototype, use `dangerouslyAllowBrowser: true`. For production, set up backend proxy.

### Issue: "Module not found"
**Solution:** Clear node_modules and reinstall:
```bash
rm -rf node_modules
npm install
```

### Issue: "Build failed"
**Solution:** Check build logs in Lovable dashboard. Common issues:
- TypeScript errors
- Missing dependencies
- Syntax errors

### Issue: "Deployment slow/stuck"
**Solution:**
1. Check Lovable status page
2. Try deploying again
3. Contact Lovable support if persistent

---

## Best Practices

### Development Workflow:
1. **Develop locally first** - Use `npm run dev`
2. **Test frequently** - Don't wait until deploy
3. **Commit often** - Small, working increments
4. **Deploy daily** - Catch integration issues early

### Code Organization:
- Keep components small (< 200 lines)
- Extract reusable logic to hooks
- Type everything with TypeScript
- Comment complex logic

### Performance:
- Lazy load heavy components
- Memoize expensive calculations
- Debounce API calls
- Show loading states

### Security:
- Never expose API keys in frontend
- Validate all user input
- Use HTTPS only (Lovable does this automatically)
- Implement rate limiting

---

## Next Steps

### After Basic Setup:
1. **Add RAG integration** - See RAG Implementation Guide
2. **Add function calling** - See Function Calling Guide
3. **Improve UI** - Add styling, components
4. **Add error handling** - Graceful degradation
5. **Optimize performance** - Caching, lazy loading

### Week 7 Prep:
- Set up user testing environment
- Add analytics/logging
- Create feedback mechanism
- Prepare demo scenarios

---

## Resources

### Lovable Documentation:
- [Official Docs](https://docs.lovable.dev)
- [Templates](https://lovable.dev/templates)
- [Examples](https://lovable.dev/examples)

### Video Tutorials:
- [Getting Started](https://youtube.com/watch?v=...)
- [Deployment Guide](https://youtube.com/watch?v=...)

### Community:
- [Discord](https://discord.gg/lovable)
- [GitHub Discussions](https://github.com/lovable/community)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/lovable)

---

## Troubleshooting Checklist

Before asking for help, check:
- [ ] Environment variables are set correctly
- [ ] API keys are valid and have credits
- [ ] Dependencies are installed (`npm install`)
- [ ] No console errors in browser
- [ ] Tried clearing cache and hard refresh
- [ ] Tested in incognito/private window
- [ ] Read error messages carefully
- [ ] Searched for error message online

**Still stuck?** Post in course forum with:
1. Exact error message
2. What you tried
3. Screenshots if relevant
4. Link to your Lovable project (make public temporarily)

---

Good luck building! 🚀
