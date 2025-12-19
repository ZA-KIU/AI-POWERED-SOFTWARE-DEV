# Final Presentation & Submission Guide

**Building AI-Powered Applications | CS-AI-2025**  
**Demo Days:** December 25-26, 2025  
**Final Submission Deadline:** December 27, 2025, 11:59 PM

---

## 📋 Table of Contents

1. [Overview & Timeline](#overview--timeline)
2. [Repository Structure Requirements](#repository-structure-requirements)
3. [Documentation Requirements](#documentation-requirements)
4. [90-Second Video Guide](#90-second-video-guide)
5. [10-Minute Live Presentation](#10-minute-live-presentation)
6. [Case Study Template](#case-study-template)
7. [Submission Checklist](#submission-checklist)
8. [Grading Rubric](#grading-rubric)
9. [Common Questions](#common-questions)

---

## Overview & Timeline

### Key Dates

| Date | Event | Details |
|------|-------|---------|
| **Dec 20 (Fri)** | Lab 11 | Multi-vendor fallbacks implementation |
| **Dec 21-24** | Week 14 | Pure polish time (no lectures/labs) |
| **Dec 25 (Wed)** | Demo Day 1 | Teams 1-23 present |
| **Dec 26 (Thu)** | Demo Day 2 | Teams 24-45 present |
| **Dec 27 (Fri)** | Final Deadline | All materials due by 11:59 PM |

### Final Deliverables

Each team must submit:
1. ✅ **Working deployed application** (public URL)
2. ✅ **90-second demo video** (embedded in README)
3. ✅ **10-minute live presentation** (Dec 25-26)
4. ✅ **Complete GitHub repository** (all documentation)
5. ✅ **Comprehensive case study** (2,500-3,500 words)

---

## Repository Structure Requirements

### Complete File Tree

Your repository **MUST** include the following structure:

```
your-capstone/
│
├── README.md                    ⭐ CRITICAL
├── .env.example                 ⭐ CRITICAL
├── requirements.txt / package.json
├── Dockerfile (if applicable)
├── docker-compose.yml (if applicable)
├── .gitignore
│
├── src/                         # Your application code
│   ├── api/                     # Backend API
│   ├── components/              # Frontend components
│   ├── config/                  # Configuration files
│   └── utils/                   # Helper functions
│
├── tests/                       ⭐ CRITICAL FOLDER
│   ├── unit/                    # Unit tests
│   ├── integration/             # API integration tests
│   └── golden_set.json          ⭐ CRITICAL (from Week 11)
│
├── docs/                        ⭐ CRITICAL FOLDER
│   ├── ARCHITECTURE.md          ⭐ CRITICAL
│   ├── CASE_STUDY.md            ⭐ CRITICAL
│   ├── DEPLOYMENT.md            ⭐ CRITICAL
│   └── API.md
│
├── milestones/                  ⭐ CRITICAL FOLDER
│   ├── proposal.md              # Week 2
│   ├── design-review.md         # Week 4
│   ├── safety-audit.md          # Week 11
│   └── final-submission.md      # Week 15
│
└── presentation/                ⭐ CRITICAL FOLDER
    ├── demo-video.mp4           ⭐ CRITICAL (90 seconds)
    ├── slides.pdf               # Presentation slides
    └── script.md                # Demo script
```

---

## Documentation Requirements

### 1. README.md (CRITICAL FILE)

Your README.md **MUST** include all of the following sections:

#### Required Sections:

```markdown
# [Your Project Title]

[2-sentence description of what your app does and why it matters]

## 🎬 Demo Video

[Embed your 90-second video here]

[![Watch Demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)

## 🚀 Live Demo

**Try it now:** [https://your-deployed-app.vercel.app](https://your-deployed-app.vercel.app)

## ✨ Features

List your features with emphasis on AI capabilities:

- 🤖 **AI-Powered [Feature]**: Uses GPT-4o-mini to [specific task]
- 🔄 **Multi-Vendor Fallbacks**: Automatic failover (OpenAI → Anthropic → Ollama)
- 📊 **[Feature 2]**: [Description]
- 🔐 **[Feature 3]**: [Description]
- [etc.]

## 🛠️ Tech Stack

### Frontend
- Next.js 14
- TailwindCSS
- [Other libraries]

### Backend
- FastAPI / Express
- PostgreSQL
- Redis (caching)

### AI Models
- **Primary:** OpenAI GPT-4o-mini
- **Secondary:** Anthropic Claude Haiku
- **Local Fallback:** Ollama (Llama 3.1)

### Deployment
- Frontend: Vercel
- Backend: Railway
- CI/CD: GitHub Actions

## 📦 Setup Instructions

### Prerequisites
- Node.js 18+ / Python 3.11+
- PostgreSQL 14+
- API keys (OpenAI, Anthropic)

### Installation

\`\`\`bash
# Clone the repository
git clone https://github.com/your-team/your-capstone.git
cd your-capstone

# Copy environment variables
cp .env.example .env
# Edit .env with your API keys

# Install dependencies
npm install  # or pip install -r requirements.txt

# Run database migrations
npm run migrate  # or python manage.py migrate

# Start development server
npm run dev  # or python main.py
\`\`\`

The app will be available at `http://localhost:3000`

## 🔑 Environment Variables

See `.env.example` for all required variables:

```
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
DATABASE_URL=postgresql://localhost/db
JWT_SECRET=your_secret_here
```

## 📖 Usage Examples

### Example 1: [Core Feature]

[Screenshot or GIF]

```bash
# Command or code example
```

### Example 2: [Another Feature]

[Screenshot or GIF]

## 👥 Team

- **[Name 1]** - [Role] - [GitHub](https://github.com/username)
- **[Name 2]** - [Role] - [GitHub](https://github.com/username)
- **[Name 3]** - [Role] - [GitHub](https://github.com/username)

## 📄 Documentation

- [Architecture Overview](docs/ARCHITECTURE.md)
- [Complete Case Study](docs/CASE_STUDY.md)
- [Deployment Guide](docs/DEPLOYMENT.md)
- [API Documentation](docs/API.md)

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 🙏 Acknowledgments

- Professor Zeshan Ahmad
- Kutaisi International University
- [Any other acknowledgments]
```

---

### 2. .env.example (CRITICAL FILE)

Must include **ALL** environment variables needed to run your app:

```bash
# AI Providers
OPENAI_API_KEY=your_openai_key_here
ANTHROPIC_API_KEY=your_anthropic_key_here
OLLAMA_URL=http://localhost:11434  # if using Ollama

# Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
REDIS_URL=redis://localhost:6379

# Authentication
JWT_SECRET=your_secure_secret_here
SESSION_SECRET=your_session_secret_here

# Deployment
PORT=3000
NODE_ENV=production
ALLOWED_ORIGINS=https://your-app.com

# Optional: Third-party services
STRIPE_SECRET_KEY=your_stripe_key  # if applicable
SENDGRID_API_KEY=your_sendgrid_key  # if applicable
```

---

### 3. docs/ARCHITECTURE.md (CRITICAL FILE)

Must include:

```markdown
# System Architecture

## High-Level Overview

[Diagram showing: Frontend → Backend → AI Layer → Database]

## Architecture Diagram

```
┌─────────────┐
│   Client    │
│  (Browser)  │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Next.js    │
│  Frontend   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  FastAPI    │
│  Backend    │
└──────┬──────┘
       │
       ├──────────────┐
       ▼              ▼
┌──────────┐   ┌──────────┐
│ LLM      │   │PostgreSQL│
│ Router   │   │ Database │
└─────┬────┘   └──────────┘
      │
      ├─→ OpenAI (Primary)
      ├─→ Anthropic (Backup)
      └─→ Ollama (Local)
```

## Components

### Frontend Layer
- **Technology:** Next.js 14 with App Router
- **Styling:** TailwindCSS
- **State Management:** React Context / Zustand
- **Why:** Server-side rendering for SEO, fast performance

### Backend API
- **Technology:** FastAPI (Python)
- **Database:** PostgreSQL with SQLAlchemy ORM
- **Caching:** Redis for session and API response caching
- **Why:** Async support for concurrent AI requests

### AI Router (Multi-Vendor)
- **Primary:** OpenAI GPT-4o-mini (speed + cost)
- **Secondary:** Anthropic Claude Haiku (reliability)
- **Tertiary:** Ollama Llama 3.1 (free local fallback)
- **Fallback Logic:** Automatic retry with exponential backoff

### Database Schema

[Include diagram or description of key tables]

### Security
- JWT authentication
- API key rotation (90 days)
- Rate limiting (100 req/min per user)
- PII redaction in logs

## Data Flow

1. User submits request via frontend
2. Next.js API route validates and forwards to backend
3. FastAPI processes request, calls LLM Router
4. Router tries providers in order until success
5. Response cached in Redis (5 min TTL)
6. Result returned to user

## Deployment Architecture

- **Frontend:** Vercel (automatic deployments from `main`)
- **Backend:** Railway (containerized with Docker)
- **Database:** Railway PostgreSQL instance
- **CI/CD:** GitHub Actions for testing and deployment

## Scalability Considerations

- Horizontal scaling ready (stateless backend)
- Database connection pooling (max 20 connections)
- Redis caching reduces LLM calls by ~40%
- CDN for static assets (Cloudflare)
```

---

### 4. docs/DEPLOYMENT.md (CRITICAL FILE)

Step-by-step deployment instructions:

```markdown
# Deployment Guide

## Prerequisites

- Vercel account (for frontend)
- Railway account (for backend + database)
- GitHub repository
- API keys (OpenAI, Anthropic)

## Backend Deployment (Railway)

### Step 1: Create Railway Project

```bash
# Install Railway CLI
npm i -g @railway/cli

# Login
railway login

# Initialize project
railway init
```

### Step 2: Configure Environment Variables

In Railway dashboard, add:
```
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
DATABASE_URL=[automatically provided by Railway]
JWT_SECRET=...
```

### Step 3: Deploy

```bash
railway up
```

Your backend will be at: `https://your-app.railway.app`

## Frontend Deployment (Vercel)

### Step 1: Connect GitHub Repository

1. Go to vercel.com
2. Click "New Project"
3. Import your GitHub repository
4. Select `frontend/` as root directory (if applicable)

### Step 2: Configure Environment Variables

Add in Vercel dashboard:
```
NEXT_PUBLIC_API_URL=https://your-backend.railway.app
```

### Step 3: Deploy

Vercel auto-deploys on push to `main` branch.

## Database Migration

```bash
# SSH into Railway backend
railway run python manage.py migrate
```

## CI/CD Pipeline

### GitHub Actions Workflow

See `.github/workflows/deploy.yml`:

```yaml
name: Deploy
on:
  push:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run tests
        run: npm test
  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Vercel
        run: vercel --prod --token=${{ secrets.VERCEL_TOKEN }}
```

## Monitoring

- **Uptime:** UptimeRobot (checks every 5 min)
- **Errors:** Sentry for error tracking
- **Logs:** Railway logs dashboard
- **Performance:** Vercel Analytics

## Troubleshooting

### Issue: API returns 500 errors
**Solution:** Check Railway logs, verify DATABASE_URL is set

### Issue: Frontend can't connect to backend
**Solution:** Verify CORS settings in backend, check API_URL

### Issue: Ollama fallback not working
**Solution:** Ensure Ollama is installed on Railway (may need custom Dockerfile)
```

---

### 5. Tests Required

Your `tests/` directory must include:

#### tests/golden_set.json (from Week 11)
```json
[
  {
    "id": "test_001",
    "input": "What is 2+2?",
    "expected_output": "4",
    "category": "math"
  },
  {
    "id": "test_002",
    "input": "Summarize: [long text]",
    "expected_output": "[expected summary]",
    "category": "summarization"
  }
]
```

#### tests/unit/test_llm_router.py (example)
```python
def test_fallback_on_primary_failure():
    """Test that router falls back when primary fails"""
    router = LLMRouter(providers=[broken_provider, working_provider])
    result = router.generate("test prompt")
    assert result.provider == "working_provider"

def test_cost_tracking():
    """Test that costs are tracked correctly"""
    router = LLMRouter(providers=[openai_provider])
    result = router.generate("test prompt")
    assert result.cost > 0
    assert result.cost < 0.01  # sanity check
```

#### tests/integration/test_api.py (example)
```python
def test_generate_endpoint():
    """Test main generation endpoint"""
    response = client.post("/api/generate", json={
        "prompt": "Write a haiku about AI"
    })
    assert response.status_code == 200
    assert "content" in response.json()
```

#### End-to-end test
At minimum, one test that exercises the main user flow from start to finish.

---

## 90-Second Video Guide

### Video Format: "Talking-Head + UI"

Based on analysis of 500+ SaaS launches, this format drives **100+ new user signups in 24 hours** for real products.

### Video Structure (Exactly 90 Seconds)

#### **0-15s: The Hook (Face on Camera)**

**Visual:**
- Your face on camera
- Well-lit (face a window or use desk lamp)
- Clean background or blurred
- Eye contact with camera

**Script Template:**
```
"I'm [Name], and we built [App] because [emotional pain point]."
```

**Example:**
```
"I'm Sarah, and we built TaxAI because I used to spend 4 hours 
every Sunday dreading tax prep, missing time with my family."
```

**Why This Works:**
- Personal ("I" not "we")
- Emotional (describes pain, not features)
- Relatable (target users nod along)
- Specific (4 hours, every Sunday)

---

#### **15-45s: The Solution (UI Overlay)**

**Visual:**
- Screen recording of your app
- Show the "magic moment" (the wow factor)
- Smooth cursor movements
- No loading spinners (edit them out)

**Script Template:**
```
"Then I built [App]. [Describe what happens in the demo]."
```

**Example:**
```
"Then I built TaxAI. I upload my receipts, and Claude reads them 
instantly. The AI fills in every tax form automatically. What 
took 4 hours now takes 5 minutes."
```

**The "Magic Moment":**
Every video needs ONE specific second where the viewer says "Whoa."

**Don't say:** "It writes code."  
**Instead show:** Empty file → press Enter → watch code fill the screen in 2 seconds.

**Why This Works:**
- Shows, doesn't tell (actual screen recording)
- Focuses on ONE core flow (not everything)
- Highlights the AI (assignment requirement)
- Includes time savings or value metric

---

#### **45-75s: The Value (Mix of Face + Data)**

**Visual:**
- Cut between your face and results
- Show metrics, charts, testimonials
- Can include short user quotes

**Script Template:**
```
"[State the impact with numbers or testimonials]."
```

**Example:**
```
"We tested with 50 users. They saved an average of 3.5 hours. 
One user, Maria, said: 'I got my Saturday mornings back.' We 
calculated you'd save $280 per year just in stress and time."
```

**Metrics to Show:**
- Time saved per user
- Cost savings
- User ratings (4.8/5 stars)
- Number of users tested
- Testimonial quotes

**Why This Works:**
- Quantifies the benefit (hours, dollars, ratings)
- Includes social proof (testimonials)
- Connects to emotional outcome (got time back)

---

#### **75-90s: Call to Action (Face on Camera)**

**Visual:**
- Back to your face
- Same setup as opening
- Confident, direct eye contact

**Script Template:**
```
"Try it live at [URL]. Thank you."
```

**Example:**
```
"Try it live at taxai.app. Upload a receipt right now and see 
the magic yourself. Thank you."
```

**Why This Works:**
- Clear action (try it, visit URL)
- Repeats the URL (say it + show it on screen)
- Ends with gratitude (professional)

---

### Video Technical Specifications

| Requirement | Specification |
|-------------|--------------|
| **Duration** | 88-92 seconds (buffer for editing) |
| **Resolution** | 1080p minimum (1920x1080) |
| **Format** | MP4 (H.264 codec) |
| **Aspect Ratio** | 16:9 (landscape) |
| **File Size** | Under 50MB (for embedding) |
| **Audio** | Clear, no background noise |

---

### Recording Equipment

**Minimum:**
- Phone camera (or laptop webcam)
- Good lighting (natural or desk lamp)
- Quiet room
- Screen recording software (QuickTime, OBS, Loom)

**Recommended:**
- External microphone ($20-50)
- Ring light ($30)
- Backdrop or clean wall
- Video editing software (DaVinci Resolve - free)

---

### Recording Checklist

**Before Recording:**
- [ ] Script finalized (all 4 sections written)
- [ ] Quiet room secured
- [ ] Good lighting tested
- [ ] Phone/laptop charged
- [ ] Test recording (10-second clip)
- [ ] Screen recording app ready
- [ ] App deployed and tested

**Camera Setup (Talking Head):**
- [ ] Camera at eye level
- [ ] Face well-lit (no shadows)
- [ ] Clean/blurred background
- [ ] Phone in airplane mode
- [ ] Record 3-5 takes (pick best)

**Screen Recording Setup:**
- [ ] Close unnecessary tabs/windows
- [ ] Hide personal info (email, API keys)
- [ ] Record at 1080p
- [ ] Test flow 3 times before recording
- [ ] No loading spinners visible

---

### Editing Steps

**Software Options:**

Free:
- iMovie (Mac)
- DaVinci Resolve (Mac/Windows)
- CapCut (mobile/desktop)
- Canva Video (web)

Paid:
- Final Cut Pro (Mac)
- Adobe Premiere (Mac/Windows)

**Editing Workflow:**

1. **Import clips**
   - Talking-head segments (0-15s, 75-90s)
   - Screen recording (15-45s)
   - Metrics/results (45-75s)

2. **Arrange timeline**
   - 0-15s: Hook (face)
   - 15-45s: Solution (screen + voiceover)
   - 45-75s: Value (mix)
   - 75-90s: CTA (face)

3. **Add text overlays**
   - App name (appears at 3 seconds)
   - Key metrics (during value section)
   - URL (during CTA, large and clear)

4. **Polish**
   - Remove "ums" and long pauses
   - Smooth transitions
   - Consistent audio levels
   - Background music (optional, low volume)

5. **Export**
   - Format: MP4 (H.264)
   - Resolution: 1080p
   - Duration: 88-92 seconds
   - File size: Under 50MB

---

### Common Video Mistakes to Avoid

| ❌ Don't Do This | ✅ Do This Instead |
|-----------------|-------------------|
| Just screen recording (no face) | Start with your face (builds trust) |
| Talking too fast | Rehearse 3x, speak slowly |
| Showing everything | Pick ONE core flow |
| No clear CTA | End with face + URL clearly stated |
| Bad audio (echo, noise) | Test audio first (10-sec clip) |
| Over 90 seconds | Edit ruthlessly, keep it 88-90s |
| No metrics shown | Show impact (X hours saved, Y stars) |
| Generic hook | Emotional, specific pain point |

---

### Embedding in README

After exporting your video:

**Option 1: YouTube (Recommended)**

1. Upload to YouTube (unlisted or public)
2. Add to README.md:

```markdown
## 🎬 Demo Video

[![Watch Demo](https://img.youtube.com/vi/YOUR_VIDEO_ID/0.jpg)](https://www.youtube.com/watch?v=YOUR_VIDEO_ID)
```

**Option 2: GitHub Native**

```markdown
## 🎬 Demo Video

https://github.com/user-attachments/assets/your-video.mp4
```

**Option 3: Vimeo**

```markdown
## 🎬 Demo Video

[![Watch Demo](THUMBNAIL_URL)](https://vimeo.com/YOUR_VIDEO_ID)
```

---

## 10-Minute Live Presentation

### Presentation Structure (STRICT TIMING)

| Time | Section | Content | Duration |
|------|---------|---------|----------|
| **0:00-0:30** | Introduction | Team intro + problem statement | 30 sec |
| **0:30-2:00** | Video Demo | Play your 90-second video | 90 sec |
| **2:00-8:00** | Live Demo | Interact with app, show AI | 6 min |
| **8:00-10:00** | Case Study | Architecture + tech decisions | 2 min |
| **10:00** | **DONE** | Q&A if time remains | - |

⚠️ **If you go over 10 minutes, you will be cut off.**

---

### Section 1: Introduction (0:00-0:30)

**Template:**

```
"Hi, I'm [Name 1], [Name 2], and [Name 3].

We built [App Name] to solve [problem].

[One sentence about the problem magnitude or impact]

Let me show you what we built."
```

**Example:**

```
"Hi, I'm Sarah, Alex, and Mike.

We built TaxAI to eliminate the hours people waste on tax prep.

In the US alone, people spend 13 hours per year on taxes—that's 
4 billion hours of collective frustration.

Let me show you what we built."
```

**Best Practices:**
- Keep it to 30 seconds MAX
- All team members introduce themselves
- State the problem clearly
- Transition smoothly to video

---

### Section 2: Video Demo (0:30-2:00)

**What to Do:**

1. **Announce the video (5 seconds):**
   "Here's a 90-second demo of how it works."

2. **Play the video (90 seconds)**
   - Make sure audio works
   - Stand to the side (don't block screen)
   - **Don't talk over the video**

3. **Transition to live demo (5 seconds):**
   "Now let me show you the app live."

**Technical Checklist:**
- [ ] Video embedded in presentation slides (PowerPoint/Google Slides)
- [ ] OR video URL ready to click
- [ ] Audio tested in presentation room beforehand
- [ ] Backup: Video on USB drive
- [ ] Backup 2: Video on phone (can AirPlay/cast)

---

### Section 3: Live Demo (2:00-8:00)

**This is the most important section.** Plan every click.

#### Demo Planning Worksheet

```markdown
## Live Demo Script (6 minutes total)

### DEMO STEP 1 (90 seconds)
**What I'll do:** Open the app, log in as test user
**What the AI does:** Recognizes user, loads personalized dashboard
**What I'll say:** "Watch how the AI recognizes my preferences from 
                    past sessions..."
**Expected result:** Dashboard loads with AI-generated recommendations

### DEMO STEP 2 (90 seconds)
**What I'll do:** [Your core feature interaction]
**What the AI does:** [The "magic moment"]
**What I'll say:** "Now I'll [action], and the AI will [response]"
**Expected result:** [What the audience sees]

### DEMO STEP 3 (90 seconds)
**What I'll do:** [Another key feature]
**What the AI does:** [Second impressive capability]
**What I'll say:** "Notice how it handles [edge case/complexity]"
**Expected result:** [Demonstrable outcome]

### HIGHLIGHT: Multi-Vendor Fallback (90 seconds)
**What I'll demo:** Simulate primary provider failure
**How I'll do it:** [Temporarily disable OpenAI key OR show logs]
**What I'll say:** "Notice we're using OpenAI. Watch what happens 
                    if it fails... [trigger failure] ...and the 
                    system automatically switches to Anthropic in 
                    under 5 seconds."
**Expected result:** Seamless failover, app keeps working

### CLOSING (30 seconds)
**Final statement:** "That's the core workflow—AI-powered, reliable, 
                      and production-ready."
**Transition:** "Now let me show you the architecture behind this."
```

#### Live Demo Best Practices

**DO:**
- ✅ Show AI working in real-time (not preloaded responses)
- ✅ Narrate what's happening ("Now the AI is analyzing...")
- ✅ Highlight the "magic moment" (point it out explicitly)
- ✅ Show multi-vendor fallback if possible
- ✅ Keep each step under 2 minutes
- ✅ Have a test account with good demo data pre-loaded

**DON'T:**
- ❌ Show loading spinners for 30+ seconds (boring)
- ❌ Say "This usually works..." (destroys confidence)
- ❌ Skip explaining steps (audience gets lost)
- ❌ Go silent while app loads (keep talking, explain what's happening)
- ❌ Show admin panel or settings screens (users don't care)
- ❌ Try to show every single feature (focus on 3-4 key ones)

#### Backup Plans

**If Internet Fails:**
- **Plan A:** Use mobile hotspot (test speed beforehand)
- **Plan B:** Play pre-recorded demo video (narrate over it live)

**If Demo Breaks:**
- **Plan A:** Have test account with pre-loaded data
- **Plan B:** Show screenshots/video, explain what should happen
- **Plan C:** Jump to case study early, explain the tech

**If Running Short on Time:**
- Skip to the most impressive feature
- Show multi-vendor fallback (key requirement)
- Transition to case study

---

### Section 4: Case Study (8:00-10:00)

**You have 2 minutes. Need 3-4 slides MAXIMUM.**

#### Slide 1: Architecture Diagram (30 seconds)

**Show:**
```
User → Frontend (React/Next.js)
       ↓
   Backend API (FastAPI/Express)
       ↓
   LLM Router (Multi-Vendor)
       ├→ OpenAI (Primary)
       ├→ Anthropic (Backup)
       └→ Ollama (Local fallback)
```

**Say:**
```
"Here's our architecture. The frontend sends requests to our 
backend, which routes to multiple LLM providers. If OpenAI fails, 
we automatically fall back to Anthropic, then Ollama. This gave 
us 99.8% uptime in testing."
```

---

#### Slide 2: Tech Stack (30 seconds)

**Show:**
```
Frontend: Next.js 14, TailwindCSS, React Context
Backend: FastAPI, Python 3.11, PostgreSQL
AI: OpenAI (gpt-4o-mini), Anthropic (claude-haiku), Ollama (llama3.1)
Infrastructure: Vercel + Railway, CI/CD via GitHub Actions
```

**Say:**
```
"We chose Next.js for SSR and performance. FastAPI for async 
support—critical when handling multiple concurrent AI requests. 
Multi-vendor AI for reliability after researching the December 
2023 OpenAI outage that cost companies $14K in 6 hours."
```

---

#### Slide 3: Key Decisions (30 seconds)

**Show 3 bullet points:**

**Why Multi-Vendor?**
"OpenAI outage (Dec 2023) cost companies $14K/6hrs. We prevent that."

**Why GPT-4o-mini + Claude Haiku?**
"Cost optimization: Haiku for simple tasks ($0.80/1M tokens), 
GPT-4o-mini for complex ($0.15/1M). Saves 60% vs GPT-4 only."

**Why FastAPI?**
"Async support for concurrent AI requests. Handles 50+ simultaneous 
users without blocking."

---

#### Slide 4: Metrics (30 seconds)

**Show numbers:**
```
Performance:
  • Average latency: 1.2 seconds
  • Fallback success rate: 99.8%
  • Cost per query: $0.003

User Impact:
  • Time saved: 3.5 hours/week (average)
  • User rating: 4.8/5 stars (n=50 testers)
  • Cost reduction: 60% vs single-vendor
```

**Say:**
```
"Our app responds in 1.2 seconds on average. The multi-vendor 
fallback chain has 99.8% success rate. In user testing with 50 
people, we saved them 3.5 hours per week on average and received 
4.8 out of 5 stars."
```

**End with:**
```
"Thank you. Questions?"
```

---

### Presentation Rehearsal Requirements

**Minimum 3 practice sessions:**

**Rehearsal 1 (Sunday):**
- Run through entire 10 minutes
- Don't worry about perfection
- Identify sections that run long
- Time each section

**Rehearsal 2 (Monday):**
- Fix timing issues
- Practice transitions between speakers
- Test backup plans
- Get feedback from teammates

**Rehearsal 3 (Tuesday):**
- Final polish
- Use actual timer (10 min hard stop)
- Simulate demo day environment
- Verify all tech works

---

### Team Coordination

**Speaking Role Assignments (Recommended):**

| Section | Primary Speaker | Backup Speaker |
|---------|----------------|----------------|
| Introduction | Person 1 | Person 2 |
| Video (silent) | All watch | All watch |
| Live Demo | Person 2 | Person 1 |
| Case Study | Person 3 | Person 1 |
| Q&A | All participate | - |

**Why multiple speakers?**
- Shows team collaboration
- Keeps audience engaged
- Reduces pressure on any one person
- Demonstrates diverse contributions

**Pre-Presentation Team Meeting:**
- [ ] Confirm speaking roles
- [ ] Practice handoffs between speakers
- [ ] Test all technology together
- [ ] Agree on backup plan if someone freezes
- [ ] Verify everyone's slides/materials are ready

---

## Case Study Template

Your `docs/CASE_STUDY.md` must be **2,500-3,500 words** and follow this structure:

### Section 1: Executive Summary (200 words)

**What to include:**
- Problem you solved (1-2 sentences)
- Your solution (1-2 sentences)
- Key results (2-3 metrics)
- High-level overview for non-technical readers

**Example:**

```markdown
# Executive Summary

Students waste 5-10 hours per week organizing study materials across 
PDFs, slides, and notes. We built StudyAI, an AI-powered study 
assistant that automatically extracts, summarizes, and quizzes users 
on their course materials.

Our solution uses GPT-4o-mini with RAG (Retrieval-Augmented Generation) 
to answer questions based on uploaded documents. Multi-vendor fallbacks 
ensure 99.8% uptime. A smart quiz generator adapts difficulty based on 
user performance.

In testing with 50 university students:
• 3.5 hours saved per week (average)
• 85% pass rate improvement on practice exams
• 4.8/5 star rating
• $0.02 cost per study session

The app is deployed at studyai.app with 200+ active users.
```

---

### Section 2: Problem Definition (300 words)

**What to include:**
- What problem did you solve?
- Who experiences this problem?
- Why are existing solutions inadequate?
- User research findings (if applicable)

**Example Structure:**

```markdown
# Problem Definition

## The Core Problem

[Describe the problem in detail]

## Who Experiences This

[Target user persona and demographics]

## Existing Solutions Fall Short

Current alternatives include:
1. **[Solution A]**: [Why it fails]
2. **[Solution B]**: [Why it fails]
3. **[Solution C]**: [Why it fails]

## User Research

We interviewed 30 students and found:
• [Key finding 1]
• [Key finding 2]
• [Key finding 3]

[Include quotes from users if you have them]
```

---

### Section 3: Architecture & Tech Stack (500 words)

**What to include:**
- System architecture diagram
- Frontend: Framework, libraries, state management
- Backend: Framework, database, caching
- AI: Models used, routing strategy, fallbacks
- Infrastructure: Deployment, CI/CD, monitoring
- **Why you chose each technology** (critical!)

**Template:**

```markdown
# Architecture & Tech Stack

## System Architecture

[Insert architecture diagram]

```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Next.js    │
│  Frontend   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  FastAPI    │
│  Backend    │
└──────┬──────┘
       │
       ├─→ PostgreSQL (persistent data)
       ├─→ Redis (caching)
       └─→ LLM Router
           ├─→ OpenAI (primary)
           ├─→ Anthropic (backup)
           └─→ Ollama (local)
```

## Frontend

**Technology:** Next.js 14 with App Router

**Key Libraries:**
• TailwindCSS for styling
• Zustand for state management
• React Hook Form for form validation

**Why Next.js:**
We needed server-side rendering for SEO (so study guides could be 
found via Google). Next.js 14's App Router gave us streaming and 
suspense for better perceived performance. The built-in API routes 
eliminated the need for a separate backend for simple operations.

## Backend

**Technology:** FastAPI (Python 3.11)

**Database:** PostgreSQL 14 with SQLAlchemy ORM

**Caching:** Redis for:
• Session management (30-minute TTL)
• API response caching (5-minute TTL)
• Rate limiting (100 requests/hour per user)

**Why FastAPI:**
We needed async/await support to handle multiple concurrent AI 
requests without blocking. FastAPI's automatic OpenAPI docs made it 
easy to test APIs. Python was chosen for easy integration with ML 
libraries and LLM SDKs.

## AI Layer: Multi-Vendor Router

**Primary Provider:** OpenAI GPT-4o-mini
• Cost: $0.15/1M input tokens, $0.60/1M output
• Speed: ~1 second average latency
• Use case: 80% of queries (simple Q&A, summaries)

**Secondary Provider:** Anthropic Claude Haiku
• Cost: $0.80/1M input tokens, $4.00/1M output
• Reliability: 99.9% uptime (backup during OpenAI issues)
• Use case: 15% of queries (automatic fallback)

**Tertiary Provider:** Ollama (Llama 3.1 8B)
• Cost: Free (local)
• Speed: ~3 seconds (slower but guaranteed available)
• Use case: 5% of queries (final fallback)

**Fallback Strategy:**
1. Try OpenAI (max 3 retries with exponential backoff)
2. If rate limited or unavailable → try Anthropic
3. If all cloud providers fail → use local Ollama
4. Total failover time: <5 seconds

**Why Multi-Vendor:**
After researching the December 2023 OpenAI outage (6 hours, causing 
$14K loss for some companies), we decided to implement automatic 
fallbacks. This decision proved critical during testing when we hit 
OpenAI rate limits. The router seamlessly switched to Anthropic with 
zero user-facing downtime.

## Infrastructure

**Frontend Hosting:** Vercel
• Automatic deployments from `main` branch
• Global CDN (sub-100ms load times)
• Preview deployments for PRs

**Backend Hosting:** Railway
• Containerized deployment (Docker)
• Auto-scaling (1-3 instances based on load)
• Managed PostgreSQL instance

**CI/CD:** GitHub Actions
• Automated testing on every PR
• Automatic deployment on merge to `main`
• Rollback capability if deployment fails

## Security

• JWT authentication (15-minute access tokens)
• API key rotation every 90 days
• Rate limiting (100 requests/hour per user)
• PII redaction in logs (emails, names masked)
• HTTPS enforced (all traffic encrypted)
```

---

### Section 4: AI Implementation (600 words)

**What to include:**
- Prompt engineering techniques
- Model selection rationale
- Multi-vendor setup & fallbacks
- RAG implementation (if applicable)
- Function calling / tool use
- Evaluation methodology

**Template:**

```markdown
# AI Implementation

## Prompt Engineering

We use a three-layer prompting strategy:

### System Prompt (Context Setting)
```
You are StudyAI, an expert tutor helping university students. 
Your goal is to explain concepts clearly using the Feynman 
technique. Always:
1. Start with the simplest explanation
2. Use analogies from everyday life
3. Ask follow-up questions to check understanding
4. Never give direct answers to homework problems

Tone: Patient, encouraging, Socratic
```

### User Prompt Template
```
Context: {retrieved_documents}
Question: {user_question}
Student Background: {user_level}

Instructions: Answer the question using ONLY information from 
the context above. If the answer isn't in the context, say 
"I don't have that information in your study materials."
```

### Few-Shot Examples
We include 3 high-quality Q&A pairs in every prompt to guide 
response format and tone.

## Model Selection

**For Simple Q&A (80% of queries):**
• Model: GPT-4o-mini
• Max tokens: 500
• Temperature: 0.3 (more focused, less creative)
• Cost: $0.0001 per query (average)

**For Complex Explanations (15% of queries):**
• Model: Claude Haiku
• Max tokens: 1000
• Temperature: 0.7 (more expansive)
• Cost: $0.0004 per query (average)

**For Summaries (5% of queries):**
• Model: GPT-4o-mini
• Max tokens: 300
• Temperature: 0.1 (very focused)
• Cost: $0.00006 per query (average)

**Why These Choices:**
After A/B testing with 100 queries, GPT-4o-mini had:
• 92% accuracy on factual questions
• 1.2s average latency
• 5x cheaper than GPT-4

Claude Haiku was chosen as backup for its:
• 99.9% uptime (better than GPT-3.5-turbo historically)
• Longer context window (100K tokens vs 16K)
• Strong performance on educational content

## Multi-Vendor Implementation

[Code snippet showing provider abstraction]

```python
class LLMRouter:
    def __init__(self):
        self.providers = [
            OpenAIProvider(model="gpt-4o-mini"),
            AnthropicProvider(model="claude-haiku-3-5"),
            OllamaProvider(model="llama3.1:8b")
        ]
    
    def generate(self, prompt: str) -> Response:
        for provider in self.providers:
            try:
                return provider.generate(prompt)
            except RateLimitError:
                log_fallback(provider.name)
                continue
        raise AllProvidersFailedError()
```

**Fallback Metrics (from production):**
• OpenAI success rate: 95%
• Anthropic fallback triggered: 4.5%
• Ollama fallback triggered: 0.5%
• Total system uptime: 99.8%

## RAG Implementation

We use RAG (Retrieval-Augmented Generation) for answering questions 
about user-uploaded study materials.

**Embedding Pipeline:**
1. User uploads PDF/DOCX
2. Extract text using PyPDF2/python-docx
3. Chunk text (500 tokens, 50-token overlap)
4. Generate embeddings using text-embedding-3-small
5. Store in PostgreSQL with pgvector extension

**Retrieval at Query Time:**
1. User asks question
2. Embed question using same model
3. Cosine similarity search (retrieve top 5 chunks)
4. Concatenate chunks as context
5. Send to LLM with question

**Optimization:**
• Caching embeddings (reduce API calls by 80%)
• Hybrid search (keyword + semantic)
• Re-ranking using cross-encoder (improves relevance)

## Evaluation Methodology

**Golden Test Set (50 Q&A pairs from Week 11):**
• Covers key subject areas (math, history, science)
• Includes edge cases (ambiguous questions, multi-hop reasoning)
• Human-verified expected outputs

**Automated Metrics:**
• BLEU score: 0.78 (measures similarity to expected answer)
• Latency: 95th percentile < 2 seconds
• Cost per query: $0.0002 (average)

**Human Evaluation:**
• 10 students rated 100 responses
• Accuracy: 87% correct answers
• Helpfulness: 4.6/5 average
• Clarity: 4.8/5 average

**A/B Testing:**
We A/B tested GPT-4o vs GPT-4o-mini:
• Quality difference: 2% (not significant)
• Cost difference: 80% cheaper (very significant)
• Decision: Use GPT-4o-mini for 80% of queries
```

---

### Section 5: Cost Optimization (300 words)

**What to include:**
- Initial cost baseline
- Optimizations implemented
- Final cost per query
- Cost reduction percentage
- Cost projection at scale

**Template:**

```markdown
# Cost Optimization

## Initial Baseline (Week 8)

When we first deployed with GPT-4 only:
• Average cost per query: $0.012
• Projected monthly cost at 10K users: $1,200
• This was unsustainable for a student project

## Optimizations Implemented

### 1. Model Downgrade (50% savings)
Switched from GPT-4 to GPT-4o-mini for simple queries
• Before: $0.012 per query
• After: $0.006 per query
• Quality loss: <2% (measured with golden set)

### 2. Response Caching (30% savings)
Cache identical queries for 5 minutes using Redis
• Cache hit rate: 32%
• Saves ~$0.002 per cached query
• Total savings: 30% of API calls

### 3. Prompt Optimization (20% savings)
Reduced prompt length from 800 to 500 tokens
• Before: 800 input tokens average
• After: 500 input tokens average
• Response quality maintained (tested with golden set)

### 4. Smart Routing (15% savings)
Route to cheapest provider for simple queries
• Simple Q&A → GPT-4o-mini ($0.15/1M)
• Complex explanation → Claude Haiku ($0.80/1M)
• Only use expensive models when necessary

## Final Results

**Current costs:**
• Average cost per query: $0.0002
• 98% reduction from initial baseline
• Projected monthly cost at 10K users: $20

**Cost at Scale:**
• At 100K users: $200/month
• At 1M users: $2,000/month
• Sustainable with freemium model ($5/month premium tier)

## Cost Projection

[Include chart showing cost scaling]

• Break-even point: 2,000 premium users
• Target: 5% conversion rate (achievable based on similar SaaS)
• Revenue at 10K users: $2,500/month
• Profit margin: 92%
```

---

### Section 6: Challenges & Solutions (400 words)

**What to include:**
- Top 3-5 technical challenges you faced
- How you solved each one
- What you'd do differently
- Lessons learned

**Template:**

```markdown
# Challenges & Solutions

## Challenge 1: Rate Limiting Hell

**The Problem:**
During Week 9 testing, we hit OpenAI rate limits after just 50 
queries. The app would crash, showing cryptic 429 errors to users.

**Why It Happened:**
We were on OpenAI's free tier (3 requests/minute). Every user 
query triggered 2-3 API calls (embedding + generation + validation), 
instantly exhausting our quota.

**Our Solution:**
1. Implemented multi-vendor fallbacks (OpenAI → Anthropic → Ollama)
2. Added exponential backoff (wait 1s, 2s, 4s before retrying)
3. Cached embeddings (reduced API calls by 80%)
4. Upgraded to OpenAI tier 1 ($5 minimum spend)

**What We'd Do Differently:**
Start with multi-vendor from Day 1. We wasted 2 weeks debugging 
before implementing fallbacks. In production, vendor issues are 
inevitable—plan for them upfront.

**Lesson Learned:**
"Premature optimization is the root of all evil" doesn't apply to 
rate limiting. Handle it early or face production disasters.

---

## Challenge 2: RAG Retrieval Quality

**The Problem:**
Our RAG system was returning irrelevant context 40% of the time. 
Users would ask about "photosynthesis" and get chunks about "cellular 
respiration" instead.

**Why It Happened:**
We were using pure semantic search (cosine similarity on embeddings). 
Similar words ≠ similar meaning. "Photosynthesis" and "cellular 
respiration" are semantically close but contextually different.

**Our Solution:**
1. Hybrid search (keyword + semantic combined)
2. Re-ranking using cross-encoder model
3. Metadata filtering (search within specific documents/chapters)
4. Query expansion (rewrite user query into 2-3 variations)

**Results:**
• Retrieval accuracy: 42% → 87%
• User satisfaction: 3.2/5 → 4.6/5

**What We'd Do Differently:**
Test with real users earlier. We spent weeks optimizing for synthetic 
test cases, then discovered real users asked questions completely 
differently than we expected.

**Lesson Learned:**
The best evaluation metric is real user feedback. Start collecting 
it on Day 1, even if it's just 5-10 people.

---

## Challenge 3: Deployment Nightmares

**The Problem:**
Our app worked perfectly on localhost but crashed on Vercel within 
5 minutes of deployment. The logs showed cryptic "Function timeout" 
errors.

**Why It Happened:**
Vercel's free tier has a 10-second timeout for serverless functions. 
Our LLM calls took 15-30 seconds for long documents. The function 
would timeout before the LLM finished responding.

**Our Solution:**
1. Moved backend to Railway (no timeout limits)
2. Implemented streaming responses (show partial results)
3. Added loading indicators (users know it's working)
4. Set max_tokens=500 (prevent extremely long responses)

**What We'd Do Differently:**
Read the deployment platform docs BEFORE building. We designed our 
entire app around Vercel's constraints, then discovered they were 
too restrictive for AI apps.

**Lesson Learned:**
Deployment platform matters. AI apps need longer timeouts, streaming 
support, and persistent backend. Serverless isn't always the answer.

---

## Challenge 4: Cost Explosion (Solved in Section 5)

[Already covered in Cost Optimization section]

## Challenge 5: Testing Async Code

**The Problem:**
Our tests would randomly fail. The same test would pass 80% of the 
time and fail 20% with "asyncio event loop closed" errors.

**Why It Happened:**
We weren't properly cleaning up async resources between tests. Old 
event loops would leak into new tests, causing flaky failures.

**Our Solution:**
1. Use pytest-asyncio properly (with proper fixtures)
2. Close all clients explicitly in teardown
3. Use context managers for all resources
4. Add timeout to every async test (fail fast)

**What We'd Do Differently:**
Learn pytest-asyncio thoroughly before writing any tests. We wasted 
3 days debugging flaky tests that should've worked from the start.

**Lesson Learned:**
Async programming has footguns. Use the right tools and patterns 
from Day 1.
```

---

### Section 7: Results & Impact (300 words)

**What to include:**
- User testing results
- Performance metrics (latency, accuracy)
- User feedback quotes
- Business impact (if applicable)
- Future roadmap

**Template:**

```markdown
# Results & Impact

## User Testing Results

**Test Population:**
• 50 university students (25 freshmen, 25 upperclassmen)
• Testing period: 2 weeks (Nov 20 - Dec 4)
• Usage: Average 5 sessions per user, 3.5 hours total

**Quantitative Results:**

| Metric | Result |
|--------|--------|
| Time saved per week | 3.5 hours (average) |
| Practice exam pass rate | +15% vs control group |
| Questions answered | 850 total |
| Accuracy of answers | 87% correct |
| Average response time | 1.2 seconds |
| User satisfaction | 4.8/5 stars |

**Key Findings:**
• 92% of users said they would use it again
• 78% said it was better than existing study tools
• 65% would pay $5/month for premium features

## User Feedback

**Positive Quotes:**

> "This saved my semester. I was drowning in 300 pages of reading 
> for bio, and StudyAI helped me actually understand it instead of 
> just memorizing." - Sarah, Freshman

> "The quiz feature is genius. It knows exactly what I'm struggling 
> with and adapts the difficulty. Way better than Quizlet." 
> - Mike, Junior

**Constructive Feedback:**

> "Sometimes it's too verbose. I just want a quick answer, not a 
> 3-paragraph explanation." - Alex, Sophomore

> "Would love to see handwritten notes support. Currently only works 
> with typed PDFs." - Emma, Senior

## Performance Metrics

**System Performance:**
• 99.8% uptime over 2-week test period
• Average latency: 1.2 seconds (95th percentile: 2.3s)
• Zero critical errors
• Multi-vendor fallback triggered 4.5% of queries

**Cost Metrics:**
• Average cost per query: $0.0002
• Total testing cost: $17 (850 queries)
• Projected monthly cost at scale: $20 for 10K users

## Business Impact

**Potential Market:**
• 20 million university students in US
• Average study time: 15 hours/week
• If we save 3.5 hours/week → $280/year value (at $20/hour)

**Revenue Projections:**
• Freemium model: Free tier + $5/month premium
• Target: 5% conversion rate
• At 10K users: $2,500/month revenue
• Break-even: 2,000 premium users

## Future Roadmap

**Short-term (Next 3 months):**
1. Handwritten notes support (OCR integration)
2. Mobile app (React Native)
3. Spaced repetition system (long-term memory)
4. Group study rooms (collaborative features)

**Long-term (6-12 months):**
1. Video lecture transcription and summarization
2. Personalized study plans (ML-based recommendations)
3. Integration with Canvas/Blackboard (LMS)
4. Multi-language support (Spanish, French, Mandarin)

**Expansion Opportunities:**
• K-12 market (adapt for younger students)
• Professional certifications (CPA, CFA, etc.)
• Corporate training (onboarding materials)
```

---

### Case Study Formatting Requirements

**Total Length:** 2,500-3,500 words

**Must Include:**
- ✅ Diagrams (at least 2: architecture + one other)
- ✅ Code snippets (at least 3 examples)
- ✅ Screenshots (at least 4: key features)
- ✅ Tables (for metrics, comparisons)
- ✅ Quotes (from user testing, if applicable)

**Writing Style:**
- Professional but accessible
- Use bullet points for lists
- Include headers/subheaders for navigation
- Explain technical terms (not everyone is an expert)
- Show, don't just tell (examples, visuals)

---

## Submission Checklist

Use this checklist to ensure you have everything required:

### ✅ Product & Deployment

- [ ] **Deployed to production** (Vercel/Railway/other)
- [ ] **Public URL accessible** (no login required for demo)
- [ ] **Multi-vendor fallbacks implemented** (OpenAI + Anthropic minimum)
- [ ] **CI/CD pipeline working** (GitHub Actions or equivalent)
- [ ] **Golden test set passing** (from Week 11)
- [ ] **Mobile responsive** (tested on phone)

### ✅ Documentation

- [ ] **README.md comprehensive** (all sections from template)
- [ ] **Live demo URL in README** (prominent, working)
- [ ] **90-second video embedded** (YouTube/Vimeo/GitHub)
- [ ] **.env.example file** (all variables listed)
- [ ] **ARCHITECTURE.md with diagrams**
- [ ] **CASE_STUDY.md (2,500+ words)**
- [ ] **DEPLOYMENT.md** (step-by-step)
- [ ] **Setup instructions tested** (by someone who didn't build it)
- [ ] **Code comments** (for complex sections)
- [ ] **API.md** (if applicable)

### ✅ Tests

- [ ] **Golden test set** (tests/integration/golden_set.json)
- [ ] **Unit tests for core functions** (>70% coverage)
- [ ] **API integration tests** (major endpoints)
- [ ] **End-to-end test of main flow** (at least one)

### ✅ Video & Presentation

- [ ] **90-second video completed** (professionally edited)
- [ ] **Video exactly 88-92 seconds** (strict requirement)
- [ ] **Video uploaded & embedded** (README + presentation/demo-video.mp4)
- [ ] **Presentation slides created** (Google Slides/PowerPoint)
- [ ] **Slides rehearsed** (at least 3x)
- [ ] **Backup plan for demo failures** (screenshots, pre-recorded)
- [ ] **Presentation fits in 10 minutes** (timed)

### ✅ Team & Submission

- [ ] **Speaking roles assigned** (who presents what)
- [ ] **All team members contribute** (everyone speaks)
- [ ] **GitHub repo link submitted** (via course platform)
- [ ] **Deployed URL submitted** (via course platform)
- [ ] **Presentation date confirmed** (Dec 25 or 26)

### ⚠️ Warning Indicators

If any of these are true, fix them IMMEDIATELY:

- [ ] App crashes when accessing public URL
- [ ] Video over 95 seconds or under 85 seconds
- [ ] Missing CASE_STUDY.md or under 2,000 words
- [ ] No multi-vendor fallback implementation
- [ ] Presentation over 10 minutes
- [ ] .env.example missing critical variables
- [ ] Golden test set not passing
- [ ] No backup plan for demo

---

## Grading Rubric

### Total: 7 Points (30% of Final Grade)

#### Working Product (2.5 points)

| Criteria | Points | Description |
|----------|--------|-------------|
| **Deployed & Accessible** | 0.5 | Public URL works, no login required for demo |
| **Core AI Features Work** | 0.5 | Main AI functionality reliably functional |
| **Multi-Vendor Fallbacks** | 0.5 | OpenAI + Anthropic minimum, automatic failover |
| **Error Handling** | 0.5 | Graceful degradation, user-friendly messages |
| **Mobile Responsive** | 0.5 | Works on phone (basic functionality) |

**Deductions:**
- **-1.0 pt:** App not deployed or broken during demo
- **-0.5 pt:** Critical bugs during live demo

---

#### 90-Second Video (1.5 points)

| Criteria | Points | Description |
|----------|--------|-------------|
| **Quality** | 0.5 | Professional production, clear audio/video |
| **Story/Structure** | 0.5 | Follows hook-solution-value-CTA format |
| **Time** | 0.5 | 88-92 seconds (±2 sec acceptable) |

**Evaluation:**
- **Excellent (0.5):** Talking-head + UI, compelling hook, clear value, smooth editing
- **Good (0.4):** Clear structure, some production issues, acceptable quality
- **Acceptable (0.3):** Basic video, unclear structure, production issues
- **Poor (<0.3):** Missing sections, over/under time significantly

**Deductions:**
- **-0.5 pt:** Video missing or significantly over/under time (>95s or <85s)

---

#### Documentation (1.5 points)

| Criteria | Points | Description |
|----------|--------|-------------|
| **README Quality** | 0.5 | Complete, clear, video embedded, URL prominent |
| **Case Study** | 0.5 | 2,500+ words, all 7 sections, diagrams included |
| **Code Documentation** | 0.5 | Architecture docs, comments, setup instructions tested |

**Evaluation:**
- **Excellent (0.5 each):** Comprehensive, professional, easy to follow
- **Good (0.4 each):** Complete but lacks polish or clarity
- **Acceptable (0.3 each):** Missing minor sections, some confusion
- **Poor (<0.3 each):** Incomplete, unclear, missing critical sections

**Deductions:**
- **-0.5 pt:** Missing required documentation (README, case study, architecture)

---

#### Presentation (1.5 points)

| Criteria | Points | Description |
|----------|--------|-------------|
| **Delivery** | 0.5 | Clear speaking, confident, engaging |
| **Team Collaboration** | 0.5 | All members speak, smooth transitions |
| **Timing** | 0.5 | Exactly 10 minutes (±30 seconds acceptable) |

**Evaluation:**
- **Excellent (0.5):** Professional, polished, perfectly timed
- **Good (0.4):** Clear delivery, minor timing issues
- **Acceptable (0.3):** Adequate but rushed or too slow
- **Poor (<0.3):** Disorganized, over time, poor delivery

**Deductions:**
- **-0.5 pt:** Over 10 minutes (will be cut off)
- **-0.3 pt:** Only one person presents (team effort required)

---

### Automatic Deductions (Cumulative)

| Issue | Deduction |
|-------|-----------|
| App not deployed or broken | -1.0 pt |
| Video missing | -0.5 pt |
| Video over 95s or under 85s | -0.5 pt |
| Presentation over 10 minutes | -0.5 pt (cut off) |
| Missing case study | -0.5 pt |
| No multi-vendor fallback | -0.5 pt |
| Golden test set not passing | -0.3 pt |

**Maximum Deductions:** Cannot go below 0 points total

---

## Common Questions

### About the Video

**Q: Can we use animation instead of talking-head format?**  
A: You can, but talking-head + UI format has proven most effective (100+ signups in 24h for real launches). Animation is expensive and time-consuming. Only attempt if you have strong creative skills.

**Q: What if we're not comfortable on camera?**  
A: Practice helps! Record 10+ takes and pick the best. Alternatively, you can use voiceover over UI recording, but including your face builds more trust.

**Q: Can we exceed 90 seconds if our app is complex?**  
A: No. The 90-second limit is strict (±2 sec). If you can't explain it in 90 seconds, your messaging isn't clear enough. Simplify.

**Q: Where should we upload the video?**  
A: YouTube (unlisted) is recommended. Also include it in `presentation/demo-video.mp4` in your repo.

---

### About Multi-Vendor

**Q: Which providers are required?**  
A: Minimum: OpenAI + Anthropic. Recommended: Add Ollama as local fallback.

**Q: Do we need Ollama?**  
A: Highly recommended but not strictly required. It provides a free local fallback when cloud providers fail or rate limit.

**Q: What if we already built our app with single vendor?**  
A: Lab 11 (Friday) will guide you through adding fallbacks. It's about 1-2 hours of work with our templates.

---

### About Case Study

**Q: How long should the case study be?**  
A: 2,500-3,500 words. Include diagrams, code snippets, and screenshots.

**Q: What if we don't have user testing data?**  
A: Test with at least 5-10 people (classmates, friends, family). Get qualitative feedback even if not rigorous quantitative data.

**Q: Can we reuse content from weekly milestones?**  
A: Yes! Your proposal, design review, and safety audit should feed into the case study. Expand and polish them.

---

### About Presentation

**Q: What if our internet fails during live demo?**  
A: Have backup plan: (1) Mobile hotspot, (2) Pre-recorded demo video, (3) Screenshots with narration.

**Q: Can we go over 10 minutes?**  
A: No. You will be cut off. Practice with a timer. Aim for 9:30 to have buffer.

**Q: Do all team members have to speak?**  
A: Yes. It demonstrates collaboration and equal contribution.

---

### About Deployment

**Q: What deployment platforms are acceptable?**  
A: Frontend: Vercel, Netlify, Railway. Backend: Railway, Render, Heroku, fly.io. Any platform with public URL is fine.

**Q: Do we need a custom domain?**  
A: No. Subdomain from deployment platform is fine (e.g., `yourapp.vercel.app`).

**Q: What if deployment costs money?**  
A: Most platforms have generous free tiers. Railway: $5 free credit/month. Vercel: unlimited for hobby projects. You shouldn't need to pay.

---

### About Grading

**Q: How heavily is the video weighted?**  
A: Video is 1.5/7 points (21% of presentation grade). It's important but not everything.

**Q: What's the most important deliverable?**  
A: Working deployed product (2.5/7 points, 36%). Make sure your app works reliably.

**Q: Can we submit late?**  
A: No late submissions accepted. December 27 at 11:59 PM is the hard deadline. No exceptions.

---

## Timeline Reminder

| Date | Task | Status |
|------|------|--------|
| **Dec 20 (Fri)** | Lab 11: Add multi-vendor fallbacks | Required |
| **Dec 21-22 (Weekend)** | Record video, draft case study | Sprint |
| **Dec 23 (Mon)** | Finalize video, complete documentation | Deadline |
| **Dec 24 (Tue)** | Final testing, rehearse presentation | Polish |
| **Dec 25 (Wed)** | Demo Day 1 (Teams 1-23) | Present |
| **Dec 26 (Thu)** | Demo Day 2 (Teams 24-45) | Present |
| **Dec 27 (Fri)** | Final submission deadline | 11:59 PM |

---

## Support Resources

### Office Hours
- **Friday (Dec 20):** 2-4 PM - Video production help
- **Monday (Dec 23):** 10 AM-12 PM - Demo rehearsal
- **Tuesday (Dec 24):** All day - Final testing support

### Online Resources
- **GitHub:** All course materials and templates
- **YouTube:** Example demo videos
- **Documentation:** API docs, deployment guides

### Contact
- **Email:** For quick questions
- **Slack/Discord:** Real-time troubleshooting
- **Office Hours:** In-depth help

---

## Final Reminders

**You've learned everything you need.** You've built a full-stack AI application from scratch. You've deployed it to production. You've implemented advanced features like multi-vendor fallbacks and RAG.

**Now it's time to show the world what you've built.**

### 8 Days Until Demo Day

**Week 14 (Dec 20-24): Pure polish time**
- No lectures
- No labs
- Just you, your team, and your capstone

**Use it wisely:**
1. Fix bugs
2. Record video
3. Write case study
4. Practice presentation

**You've got this.** Make them legendary. 🚀

---

**Questions? Clarifications? Use office hours or Slack/Discord. See you at demo day!**

---

**Document Version:** 1.0  
**Last Updated:** December 19, 2025  
**Course:** Building AI-Powered Applications (CS-AI-2025)  
**Institution:** Kutaisi International University  
**Instructor:** Professor Zeshan Ahmad
