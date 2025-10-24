# Refined Capstone Proposal (Version 2)

**Project Name:** ReceiptVault - AI-Powered Expense Tracker  
**Team Members:** Sarah Chen, Michael Torres, Priya Patel  
**Date:** Week 4, October 24, 2024  
**Version:** 2.0 (Updated from Week 2 submission)

---

## 📋 Document Change Log

### What Changed Since Week 2?

| Section | Change Type | Summary |
|---------|-------------|---------|
| Problem Statement | **Refined** | Narrowed from "all small businesses" to "freelancers earning <$100K/year" based on user interviews |
| Technical Architecture | **Major Update** | Switched from Flask → FastAPI, MongoDB → PostgreSQL, added Cloudinary for image storage |
| Success Criteria | **Enhanced** | Added measurable metrics: >70% task completion, <3s latency, >85% accuracy |
| Risk Assessment | **Expanded** | Added 5 new risks discovered during prototyping: API costs, faded receipts, deployment complexity |
| Timeline | **Realistic** | Adjusted based on Week 3-4 velocity: we're 30% slower than initial estimates |

---

## 1. Problem Statement (Updated)

### The Problem

**Original (Week 2):**
> Small business owners waste significant time manually tracking expenses for tax purposes. Current solutions are either too expensive or too complex for businesses with limited revenue. We aim to build an AI-powered receipt scanner that extracts expense data automatically.

**Refined (Week 4):**

Freelance consultants and gig workers earning less than $100K annually face a critical tax compliance challenge: tracking business expenses for quarterly tax filings. These users process 150-300 receipts per year but lack the time or resources to use complex accounting software.

**Who experiences this problem?**  
Specifically: freelance designers, consultants, Uber/Lyft drivers, photographers, and independent contractors. Our Week 3-4 user research (6 interviews) revealed that 100% of freelancers in this category struggle with expense tracking, with 83% (5/6) admitting they've missed tax deductions due to lost receipts.

**Why is this problem significant?**  
Financial impact: The average freelancer loses $800-$1,200 annually in unclaimed deductions due to poor expense tracking (source: user interviews). Time impact: Manual entry takes 3-5 hours per week during tax season. Compliance risk: 4/6 interviewees reported anxiety about IRS audits due to incomplete records.

**What are current solutions and their limitations?**
- **QuickBooks Self-Employed** ($15/month): Too expensive for freelancers earning <$50K/year; complex setup requires 2+ hours
- **Expensify** ($4.99/month): Accurate but manual categorization required; no AI assistance
- **Spreadsheets** (Free): Completely manual; 100% human error rate; no receipt storage
- **Shoebox method** (Free): Physical receipts fade, get lost; no digital backup

**Why is AI appropriate for this problem?**  
AI-powered OCR can extract receipt data in <3 seconds with 85%+ accuracy, reducing manual data entry by 80%. Vision models (GPT-4o Vision) can handle poor-quality images, faded receipts, and handwritten amounts—tasks that traditional OCR fails at. Natural language processing enables smart categorization without complex rule configuration.

**Validation from Week 3-4:**
- Interviewed 6 freelancers (3 designers, 2 consultants, 1 photographer)
- 6/6 confirmed expense tracking is "most painful part of being freelance"
- 5/6 would pay $10-15/month for automated solution
- 4/6 currently lose receipts and miss deductions
- Average time spent on expense tracking: 15 hours per quarter

---

## 2. Target Users (Updated)

### User Personas

**Primary User: Maria the Freelance Consultant**

- **Demographics:** 34 years old, Atlanta GA, MBA from Georgia State, moderate tech comfort (uses Google Workspace daily, intimidated by complex software like QuickBooks)
- **Role/Context:** Self-employed management consultant, $85K/year revenue (pre-tax), works with 4-6 clients simultaneously, files quarterly estimated taxes
- **Goals:** 
  - Track all business expenses with <5 minutes effort per week
  - Generate quarterly tax reports in under 30 minutes
  - Maximize tax deductions (average 25% of expenses currently unclaimed)
  - Never lose a receipt again
- **Pain Points:** 
  - Loses paper receipts (finds crumpled receipts in purse 3 months later)
  - Forgets to log expenses until quarterly tax time, then scrambles
  - Can't afford $180/year for Expensify on top of CPA fees
  - Finds QuickBooks "overwhelming" and "designed for real businesses, not me"
  - Takes photos of receipts but never organizes them (500+ photos in Google Drive)
- **Current Behavior:** 
  - Takes photos with iPhone camera
  - Saves to Google Drive folder "Receipts 2024"
  - Manually enters into Excel template quarterly (takes 4-5 hours)
  - Often estimates amounts when receipts are unreadable
  - Hires CPA for $600/year but provides incomplete data
- **Success Metrics:** 
  - Would pay $12/month if it saves 2+ hours per week
  - Would upgrade to $20/month if it increases deductions by $500+/year
  - Needs mobile app (80% of receipts from phone)
  - Must integrate with Excel or Google Sheets (for CPA)

**Quote from Maria (User Interview #2, Oct 18):**
> "I'm so embarrassed to tell my accountant I lost receipts again. I know I'm leaving money on the table, but I just can't keep track of paper. If I could snap a photo and forget about it, that would be life-changing."

---

**Secondary User: James the Rideshare Driver**

- **Demographics:** 28 years old, Phoenix AZ, high school diploma, very tech-comfortable (Gen Z, uses apps constantly)
- **Role/Context:** Full-time Uber/Lyft driver, $42K/year gross income, treats gig work as small business, files quarterly taxes
- **Goals:**
  - Track gas, maintenance, car washes (biggest deductions)
  - Prove mileage and expenses to IRS if audited
  - Minimize time on "boring paperwork stuff"
  - Save for first house (needs every deduction)
- **Pain Points:**
  - Processes 200+ gas receipts per year (fills up 3-4x/week)
  - Thermal paper receipts fade within weeks
  - No time for data entry (driving 50+ hours/week)
  - Used Stride app but switched to paper because "too many taps"
  - Paranoid about IRS audit (heard horror stories from other drivers)
- **Current Behavior:**
  - Keeps receipts in glove box
  - Bulk-enters once per month (takes 2 hours, usually on Sunday)
  - Misses 20-30% of receipts that fell out or faded
  - Uses mileage deduction as backup (less optimal)
- **Success Metrics:**
  - Would pay $8-10/month if it captures ALL receipts reliably
  - Needs <10 seconds per receipt (upload while pumping gas)
  - Must work on old Android phone (budget device)
  - Wants proof of receipt in case of audit (timestamped photos)

**Quote from James (User Interview #4, Oct 20):**
> "Bro, I literally pump gas and the receipt fades before I get home. I probably lose $1,500 a year in deductions just from faded receipts. If your app lets me snap it right there at the pump, I'm in."

---

### User Validation

**How We Validated Our Users:**
- [x] Interviewed 6 potential users (Week 3-4)
  - 3 freelance designers (Atlanta area, recruited via Facebook groups)
  - 2 management consultants (LinkedIn outreach)
  - 1 professional photographer (Instagram DM)
- [x] Observed 2 users with current tools
  - Watched Maria manually enter 2 weeks of receipts into Excel (took 47 minutes)
  - Watched Sarah (freelance designer) use Expensify (confused by categorization)
- [x] Surveyed 12 people in target demographic
  - Posted in r/freelance, got 12 responses
  - 10/12 use manual tracking (spreadsheets or paper)
  - 2/12 use paid tools (both complained about cost or complexity)
- [x] Analyzed competitors' user reviews
  - QuickBooks Self-Employed: 3.2/5 stars, common complaint "too complicated"
  - Expensify: 4.1/5 stars, common complaint "expensive for solo users"
  - FreshBooks: 4.3/5 stars, common complaint "overkill for simple expense tracking"
- [ ] Posted in relevant communities and got [X] responses
  - Planned for Week 5: post in freelance Slack communities

**Key Insights from Validation:**

1. **Price Sensitivity is Real:**  
   Users in <$50K income bracket won't pay >$10/month. Users in $50-100K bracket max out at $15/month. Price is THE #1 barrier to adoption of existing tools.

2. **Faded Receipts are the Killer Problem:**  
   5/6 users mentioned faded thermal paper receipts as biggest pain point. Traditional OCR fails here—only AI can enhance and extract from poor quality images.

3. **Categorization is Confusing:**  
   Users don't know if "gas" is "fuel" or "auto expenses" or "mileage." They want ONE-CLICK categorization with smart defaults, not dropdowns with 50 options.

4. **Mobile-First is Non-Negotiable:**  
   6/6 users take photos with phones. Desktop web app is nice-to-have, but mobile is the primary interface. 80% of receipts happen "in the field" (gas stations, client lunches, office supply stores).

5. **Trust is Earned Through Transparency:**  
   Users want to SEE the extracted data and CONFIRM it's correct before it's saved. They don't trust "black box AI" that auto-saves without review. This is a compliance/audit concern.

6. **Integration with CPAs Matters:**  
   4/6 users hire accountants. They need CSV export that CPAs can import into their systems. "My CPA uses QuickBooks" came up 3 times.

---

## 3. Success Criteria (Updated & Measurable)

### Product Success Metrics

| Metric | Target (Week 15) | Measurement Method | Current Baseline (Week 4) |
|--------|------------------|-------------------|---------------------------|
| **Task Completion Rate** | >70% | User testing: % who complete "upload receipt → confirm data → save" without help | 45% (tested with 2 users, got confused on confirmation screen) |
| **Time to Complete Core Task** | <3 minutes | Timed during user testing: receipt photo → confirmed save | 4.2 minutes (slow due to upload time, will optimize) |
| **User Satisfaction (Post-Task)** | >4.0/5.0 | Survey after Week 7 & 14 testing (SUS + custom questions) | Not yet measured (Week 7 first test) |
| **Would Recommend** | >60% | "Would you recommend to a friend?" (Yes/No) | Not yet measured |
| **Perceived Accuracy** | >4.0/5.0 | "How accurate was the extracted data?" (1-5 scale) | 3.5/5.0 (2 test users, mixed results) |

**Rationale for Targets:**
- **70% task completion:** Industry standard for B2C SaaS usability. If <70%, UX needs major rework.
- **<3 minutes per receipt:** Target is 5x faster than manual entry (which takes 15 minutes on average per receipt including finding it, typing merchant, date, amount, items).
- **>4.0/5.0 satisfaction:** "Good" to "Excellent" range. <4.0 indicates poor product-market fit.
- **>60% recommendation:** Strong product-market fit signal. <50% means people wouldn't tell friends.

### Technical Success Metrics

| Metric | Target | Measurement Method | Current Performance |
|--------|--------|-------------------|---------------------|
| **AI Accuracy (Merchant)** | >95% | Golden set (50 receipts): exact match on merchant name | 82% (tested on 10 receipts, struggle with handwritten names) |
| **AI Accuracy (Date)** | >90% | Golden set: within ±1 day | 90% (tested on 10 receipts) |
| **AI Accuracy (Amount)** | >98%** | Golden set: within ±$0.01 (CRITICAL for taxes) | 70% (tested on 10 receipts, decimal errors on faded receipts) |
| **AI Accuracy (Items)** | >70% | Golden set: >70% of line items extracted | 60% (tested on 10 receipts, misses items often) |
| **Response Latency (P95)** | <3 seconds | Backend logging: time from upload to response | 4.5 seconds (TOO SLOW, needs optimization) |
| **API Uptime** | >99% | Monitoring dashboard (Vercel/Railway built-in) | Not yet deployed to production |
| **Cost per Query** | <$0.05 | Cost tracking logs (OpenAI usage × pricing) | $0.013 (✅ good, but can optimize to $0.003 with GPT-4o-mini) |
| **Token Usage per Query** | <1000 tokens | API response tracking | 1,300 tokens (needs prompt optimization) |

**Critical Finding:** Amount accuracy is only 70%—this is UNACCEPTABLE for a tax compliance tool. Users cannot have incorrect dollar amounts. This is our #1 priority to fix in Week 5-6.

**Why These Metrics Matter:**
- **Amount accuracy >98%:** Tax compliance is binary—wrong amount = audit risk. This is our core value prop, must be near-perfect.
- **Latency <3s:** User attention span threshold. >3s = users close app and abandon. Current 4.5s is borderline painful.
- **Cost <$0.05/query:** At 1,000 queries/month per user, $0.05 = $50/month cost. With $12/month pricing, we need <$0.03/query for 75% gross margin.

### Learning Goals (Team Member Level)

| Team Member | Learning Goal | Success Criteria | Progress (Week 4) |
|-------------|---------------|------------------|-------------------|
| Sarah Chen | Master RAG implementation | Successfully integrate vector DB, <300ms search latency | ⏸️ Deprioritized (RAG not needed for MVP) |
| Michael Torres | Build production FastAPI backend | Deployed API with >99% uptime, proper error handling | 🔄 50% done (API works locally, not deployed) |
| Priya Patel | Implement comprehensive testing | >80% code coverage, golden set with 50+ cases | ⏸️ Not started (planned Week 6) |

**Updated Learning Goals:**
- **Sarah:** Shifted focus to prompt engineering and image preprocessing (more relevant than RAG for receipt scanner)
- **Michael:** On track, needs deployment help (will pair with instructor in office hours Week 5)
- **Priya:** Will lead Week 6 golden set creation after UI stabilizes

---

## 4. Technical Architecture (Updated)

### Architecture Evolution

**What Changed Since Week 2:**

| Component | Week 2 Plan | Week 4 Reality | Why We Changed |
|-----------|-------------|----------------|----------------|
| **Frontend** | React on Netlify | React (Vite) on Vercel | Vercel has better FastAPI integration, faster deploys |
| **Backend** | Flask | FastAPI | Async support for streaming (future feature), automatic API docs, better type safety |
| **Database** | MongoDB | PostgreSQL | Relational structure better fits our data model (users → receipts → categories has clear relations) |
| **AI Model** | GPT-4 | GPT-4o-mini (80%) + GPT-4o (20%) | Cost optimization: mini works for clear receipts, full model for faded/complex cases |
| **Deployment** | Heroku | Railway | Free tier more generous ($5 credit/month), includes PostgreSQL, simpler setup |
| **Image Storage** | Not planned | Cloudinary | Need CDN for fast image loading, auto-optimization, 7-day retention for privacy |
| **Authentication** | Build ourselves | Clerk | Don't have time to build secure auth, Clerk's free tier perfect for MVP |

**Biggest Surprise:** We underestimated image upload time. Originally thought images would be <1MB, but iPhone photos are 3-5MB. Cloudinary's auto-compression saved us.

**Biggest Mistake:** We spent 6 hours trying to make MongoDB work before realizing our data is inherently relational. Should have started with PostgreSQL.

---

### Current Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER (Mobile Browser)                    │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ HTTPS
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    FRONTEND (React + Vite)                       │
│                       Deployed on Vercel                         │
│                                                                   │
│  Components:                                                      │
│  - UploadForm.jsx (image capture + upload)                       │
│  - ResultsDisplay.jsx (extracted data + edit)                    │
│  - HistoryView.jsx (past receipts)                               │
│  - ExportButton.jsx (download CSV)                               │
│                                                                   │
│  State Management: React Context API                             │
│  Styling: Tailwind CSS                                           │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ REST API (JSON)
                             │ POST /api/receipts
                             │ GET /api/receipts
                             │ PUT /api/receipts/:id
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                   BACKEND (FastAPI + Python 3.11)                │
│                       Deployed on Railway                        │
│                                                                   │
│  Endpoints:                                                       │
│  - POST /api/receipts (upload + process)                         │
│  - GET /api/receipts (list user receipts)                        │
│  - PUT /api/receipts/:id (update/correct)                        │
│  - DELETE /api/receipts/:id (delete)                             │
│  - GET /api/export (CSV download)                                │
│                                                                   │
│  Services:                                                        │
│  - image_service.py (preprocessing, quality check)               │
│  - ai_service.py (OpenAI API calls)                              │
│  - receipt_service.py (business logic)                           │
└───────┬──────────────┬────────────────┬─────────────────────────┘
        │              │                │
        │              │                │
        ▼              ▼                ▼
┌──────────────┐ ┌──────────────┐ ┌──────────────────────┐
│ PostgreSQL   │ │ Cloudinary   │ │ OpenAI Vision API    │
│ (Railway)    │ │ (Image CDN)  │ │ (GPT-4o / 4o-mini)   │
│              │ │              │ │                      │
│ Tables:      │ │ Storage:     │ │ Models:              │
│ - users      │ │ - Receipt    │ │ - gpt-4o-mini (80%)  │
│ - receipts   │ │   images     │ │ - gpt-4o (20%)       │
│ - categories │ │ - 7-day      │ │                      │
│              │ │   retention  │ │ Structured output:   │
│              │ │              │ │ - JSON schema        │
└──────────────┘ └──────────────┘ └──────────────────────┘
                                    
┌─────────────────────────────────────────────────────────────────┐
│                    AUTHENTICATION (Clerk)                        │
│                                                                   │
│  - User signup/login                                             │
│  - OAuth (Google)                                                │
│  - JWT tokens                                                    │
└─────────────────────────────────────────────────────────────────┘
```

---

### Key Components

**1. Frontend (React + Vite)**

**Purpose:** User interface for uploading, reviewing, and managing receipts

**Tech Stack:**
- React 18.2 (component library)
- Vite 4.3 (build tool, faster than Webpack)
- Tailwind CSS (styling)
- React Context API (state management)
- Axios (HTTP client)

**Key Features:**
- Camera/file upload with preview
- Real-time upload progress bar
- Extracted data display with edit capability
- Receipt history view (list + search)
- CSV export button
- Mobile-responsive design

**Deployment:** Vercel (auto-deploy from GitHub main branch)

**URL:** https://receiptvault.vercel.app (staging)

---

**2. Backend (FastAPI + Python 3.11)**

**Purpose:** API server, business logic, AI integration

**Tech Stack:**
- FastAPI 0.104 (web framework)
- Python 3.11 (language)
- Pydantic (data validation)
- SQLAlchemy (ORM for PostgreSQL)
- OpenAI Python SDK (AI API client)
- Pillow (image preprocessing)

**Key Endpoints:**

| Method | Endpoint | Purpose | Auth | Response Time |
|--------|----------|---------|------|---------------|
| POST | `/api/receipts` | Upload + process receipt | Required | ~4.5s (target: 3s) |
| GET | `/api/receipts` | List user's receipts | Required | ~200ms |
| GET | `/api/receipts/:id` | Get single receipt | Required | ~150ms |
| PUT | `/api/receipts/:id` | Update receipt data | Required | ~180ms |
| DELETE | `/api/receipts/:id` | Delete receipt | Required | ~120ms |
| GET | `/api/export` | Download CSV | Required | ~500ms |
| GET | `/api/health` | Health check | No | ~50ms |

**Deployment:** Railway (auto-deploy from GitHub main branch)

**URL:** https://receiptvault-api.up.railway.app

---

**3. Database (PostgreSQL 15)**

**Purpose:** Store user data, receipt metadata, extracted information

**Schema:**

```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    clerk_user_id VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    last_login TIMESTAMP
);

-- Receipts table
CREATE TABLE receipts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,  -- Cloudinary URL
    merchant VARCHAR(255),
    date DATE,
    amount DECIMAL(10, 2),
    items JSONB,  -- Array of {name, price}
    category VARCHAR(100),
    confidence FLOAT,  -- 0-1 score
    notes TEXT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW(),
    
    -- Indexes for fast queries
    INDEX idx_user_id (user_id),
    INDEX idx_date (date),
    INDEX idx_created_at (created_at)
);

-- Categories table (predefined + user custom)
CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    is_default BOOLEAN DEFAULT FALSE
);
```

**Sample Data:**
```json
{
  "id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "user_id": "u_abc123",
  "merchant": "Whole Foods Market",
  "date": "2024-10-15",
  "amount": 87.43,
  "items": [
    {"name": "Organic Bananas", "price": 3.99},
    {"name": "Almond Milk", "price": 4.99}
  ],
  "category": "Groceries",
  "confidence": 0.92,
  "notes": "Client lunch prep"
}
```

**Why PostgreSQL over MongoDB:**
- Clear relational structure (users → receipts)
- ACID compliance (critical for financial data)
- Better query performance for date ranges
- Built-in JSON support (JSONB for items array)
- Easier to export CSV (SQL is great for tabular data)

---

**4. AI Services (OpenAI Vision API)**

**Model Selection Strategy:**

```python
def choose_model(image):
    """
    Choose GPT-4o-mini for clear images, GPT-4o for poor quality.
    Saves 90% on API costs while maintaining accuracy.
    """
    quality_score = assess_image_quality(image)
    
    if quality_score > 0.7:
        return "gpt-4o-mini"  # Clear image
    else:
        return "gpt-4o"       # Faded/poor quality
```

**Prompt Structure (Optimized for 200 tokens):**

```python
SYSTEM_PROMPT = """
Extract receipt data: merchant, date, amount, items. 
Return JSON. Accuracy critical (tax purposes). 
Include confidence score (0-1) if uncertain.
"""

# User message is just the image, no text needed
```

**Structured Output (JSON Schema):**

```python
from pydantic import BaseModel
from typing import List

class ReceiptItem(BaseModel):
    name: str
    price: float

class ReceiptData(BaseModel):
    merchant: str
    date: str  # ISO format YYYY-MM-DD
    amount: float
    items: List[ReceiptItem]
    confidence: float

# OpenAI enforces this schema
response = client.chat.completions.create(
    model=model_name,
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": [{"type": "image_url", "image_url": {"url": image_url}}]}
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "receipt_extraction",
            "schema": ReceiptData.model_json_schema()
        }
    }
)
```

**Token Usage:**
- System prompt: 200 tokens
- Image: ~1,000 tokens (varies by resolution)
- Output: ~300 tokens
- **Total: ~1,500 tokens per query**

**Cost Calculation (Optimized):**
- 80% GPT-4o-mini: 1,500 tokens × $0.0003/1K = $0.00045/query
- 20% GPT-4o: 1,500 tokens × $0.01/1K = $0.015/query
- **Blended: $0.003/query** (vs. $0.015 with GPT-4o only)

---

### Data Flow for Core User Action

**User Flow: Upload Receipt**

```
1. User opens app, taps "Scan Receipt"
   ↓
2. Takes photo or selects from gallery
   ↓
3. Frontend shows preview + "Upload" button
   ↓
4. User taps "Upload"
   ↓
5. Frontend:
   a. Validates file (JPEG/PNG/HEIC, <10MB)
   b. Compresses image to 1024×1024 (client-side)
   c. Shows loading spinner: "Analyzing receipt..."
   d. POST /api/receipts with FormData(image)
   ↓
6. Backend (FastAPI):
   a. Authenticates user (validates Clerk JWT)
   b. Uploads image to Cloudinary
   c. Receives Cloudinary URL + optimized image
   d. Preprocesses image (enhance contrast if needed)
   e. Assesses image quality (0-1 score)
   f. Chooses model: quality >0.7 → GPT-4o-mini, else → GPT-4o
   g. Calls OpenAI Vision API with structured output
   h. Receives JSON: {merchant, date, amount, items, confidence}
   i. Validates data (amount is positive, date is valid)
   j. Stores in PostgreSQL (receipts table)
   k. Returns JSON to frontend with receipt_id
   ↓
7. Frontend:
   a. Hides loading spinner
   b. Shows "Extracted Data" screen:
      - Merchant (editable text field)
      - Date (editable date picker)
      - Amount (editable currency field)
      - Items list (add/remove/edit)
      - Category dropdown (auto-selected based on merchant)
      - Confidence indicator (high/medium/low)
   c. Buttons: "Save" / "Cancel"
   ↓
8. User reviews data, makes corrections if needed
   ↓
9. User taps "Save"
   ↓
10. Frontend sends PUT /api/receipts/:id with updated data
    ↓
11. Backend updates PostgreSQL
    ↓
12. Frontend shows success toast: "Receipt saved!"
    ↓
13. Redirects to receipt history view
```

**Total Time (Target vs. Current):**

| Step | Target | Current | Status |
|------|--------|---------|--------|
| Frontend validation | <100ms | 50ms | ✅ |
| Image compression | <500ms | 300ms | ✅ |
| Image upload to Cloudinary | <1000ms | 1,800ms | ⚠️ TOO SLOW |
| Image preprocessing | <200ms | 150ms | ✅ |
| OpenAI API call | <2000ms | 2,500ms | ⚠️ SLOW |
| Database write | <100ms | 80ms | ✅ |
| Frontend render | <200ms | 100ms | ✅ |
| **TOTAL (P95)** | **<3000ms** | **~4500ms** | 🔴 MUST OPTIMIZE |

**Optimization Plan (Week 5):**
1. Use Cloudinary's CDN for faster uploads (expect 800ms → 400ms)
2. Optimize prompt to reduce tokens (expect 2500ms → 1800ms API call)
3. Add Redis caching for duplicate receipts (expect 40% cache hit rate)

**Target after optimization: <2.5 seconds** 🎯

---

## 5. Risk Assessment (Updated & Expanded)

### Risk Matrix

| Risk ID | Risk | Likelihood | Impact | Severity | Status |
|---------|------|------------|--------|----------|--------|
| R1 | API cost overruns | HIGH | HIGH | 🔴 CRITICAL | Mitigating |
| R2 | Amount extraction accuracy <95% | HIGH | HIGH | 🔴 CRITICAL | Monitoring |
| R3 | Team member unavailable (midterms) | HIGH | MEDIUM | 🟡 HIGH | Planning |
| R4 | Poor quality receipt photos (faded) | HIGH | MEDIUM | 🟡 HIGH | Researching |
| R5 | No production deployment experience | HIGH | MEDIUM | 🟡 HIGH | In progress |
| R6 | Scope creep (too many features) | MEDIUM | MEDIUM | 🟢 MEDIUM | Controlled |
| R7 | User adoption (no one uses it) | MEDIUM | MEDIUM | 🟢 MEDIUM | Validating |
| R8 | Database performance at scale | LOW | MEDIUM | 🟢 MEDIUM | Not urgent |
| R9 | Receipt image storage costs | LOW | LOW | ⚪ LOW | Monitoring |
| R10 | Privacy/GDPR compliance gaps | MEDIUM | HIGH | 🟡 HIGH | Planning (Week 11) |

---

### Critical Risks (Detailed)

#### 🔴 Risk R1: API Cost Overruns

**Description:** Without proper cost controls, OpenAI API costs could exhaust our $100 semester budget in days.

**What Happened (Week 3-4):**
- Spent $8.62 in 2 days of testing (53 queries)
- At this rate: $8.62 × 15 = $129.30/month → WAY OVER BUDGET
- Root cause: Using GPT-4o for everything, verbose prompts, no caching

**Likelihood:** HIGH (80%) - We WILL go over budget without changes  
**Impact:** HIGH - Blocks development and testing if budget exhausted  
**Severity:** 🔴 CRITICAL

**Triggers:**
- Inefficient prompts (too many tokens)
- No caching for repeated queries
- Testing without cost tracking
- Batch processing without rate limits

**Preventive Mitigation (Week 4-5):**
1. ✅ **DONE (Week 4):** Set up cost tracking dashboard (Google Sheets)
2. ✅ **DONE (Week 4):** Implement rate limiting (100 requests/hour per user)
3. ⏳ **IN PROGRESS (Week 4):** Switch to GPT-4o-mini for 80% of queries (expect 90% cost reduction)
4. 📅 **PLANNED (Week 5):** Add Redis caching (40% cache hit rate expected)
5. 📅 **PLANNED (Week 5):** Optimize prompts (500 tokens → 200 tokens)

**Cost Projection After Mitigation:**
- Before: $0.0125/query × 5,000 queries = $62.50
- After: $0.003/query × 5,000 queries = $15.00 (76% savings!)

**Contingency Plan (If Risk Occurs):**
- **Immediate:** Pause all non-essential API calls
- **Week 5+:** Switch to GPT-4o-mini exclusively (no hybrid), apply for OpenAI credits
- **Last Resort:** Reduce scope (cut item extraction, only extract merchant/date/amount)

**Monitoring:**
- Daily cost dashboard (check every morning before standup)
- Alert if daily cost >$3 (Zapier → Slack notification)
- Weekly budget review in Monday standup

**Owner:** Michael Torres (Backend Lead)  
**Next Review:** Every Monday in standup

**Status:** 🟡 Mitigating (optimizations in progress, on track to resolve by Week 5)

---

#### 🔴 Risk R2: Amount Extraction Accuracy <95%

**Description:** If amount extraction is inaccurate, users could claim wrong tax deductions, exposing them to IRS audits. This destroys trust and user adoption.

**What Happened (Week 3-4):**
- Tested on 10 receipts: 7/10 perfect, 2/10 off by pennies, 1/10 completely wrong (faded receipt, AI hallucinated "$45.67" when actual was "$145.67")
- Current accuracy: ~70% exact match
- Root cause: Faded receipts, decimal point confusion, handwritten amounts

**Likelihood:** HIGH (70%) - Faded receipts are common  
**Impact:** HIGH - User trust destroyed, potential legal liability  
**Severity:** 🔴 CRITICAL

**What We've Learned:**
- Faded thermal paper receipts are THE biggest problem (3/10 test receipts were faded)
- AI sometimes misreads decimal points: "$1.234" vs. "$12.34"
- Handwritten amounts (food trucks, small businesses) fail 50% of the time

**Preventive Mitigation:**
1. ✅ **DONE (Week 4):** User confirmation workflow (ALWAYS require manual review, never auto-save amounts)
2. ✅ **DONE (Week 4):** Add confidence scoring (flag amounts with confidence <0.8 in red)
3. 📅 **PLANNED (Week 5):** Create golden set with 50 diverse receipts (20 faded, 10 handwritten)
4. 📅 **PLANNED (Week 6):** Implement multi-pass verification:
   - Pass 1: Extract amount
   - Pass 2: Ask AI "Does this amount seem reasonable for [merchant]?"
   - Pass 3: If confidence <0.7, prompt user: "We're unsure. Please verify this amount."
5. 📅 **PLANNED (Week 6):** Add image preprocessing (enhance contrast for faded receipts using Pillow):
   ```python
   from PIL import ImageEnhance
   enhancer = ImageEnhance.Contrast(image)
   enhanced_image = enhancer.enhance(2.0)  # Double contrast
   ```
6. 📅 **PLANNED (Week 7):** Add confidence scoring breakdown:
   - High (>0.9): Green check mark, no warning
   - Medium (0.7-0.9): Yellow warning: "Please verify"
   - Low (<0.7): Red warning: "Low confidence, manual entry recommended"

**Acceptance Criteria (Week 7):**
- Golden set (50 receipts): >95% amount accuracy
- User testing: 0 complaints about wrong amounts
- Confidence scoring: <0.7 flags 100% of incorrect amounts

**Contingency Plan:**
- If golden set shows <95%: Add preprocessing, try GPT-4o exclusively for amounts, consider hybrid OCR+LLM
- If production accuracy drops: Add "Beta" warning, require human review for amounts >$100
- If user reports wrong amount: Investigate immediately, add to golden set, retrain/adjust

**Monitoring:**
- Golden set regression tests (run weekly after Week 5)
- User edit rate for amounts (track in analytics)
- Production accuracy dashboard (% of amounts edited by users)

**Owner:** Sarah Chen (AI/ML Lead)  
**Next Review:** Week 5 (after golden set created)

**Status:** 🔴 Critical (actively working on solution, Week 5-6 focused effort)

---

[Additional risks R3-R10 would continue here with similar detail...]

---

## 6. Project Timeline & Milestones (Realistic)

### Weekly Breakdown

| Week | Focus | Deliverables | Owner | Status |
|------|-------|-------------|--------|--------|
| 1 | Setup | Team formation, idea finalized | All | ✅ Complete |
| 2 | Planning | Proposal v1, team contract, dev environment setup | All | ✅ Complete |
| 3 | Core Flow | Basic query → LLM → response (receipt upload working) | Michael | ✅ Complete |
| 4 | **Design Review** | **Proposal v2, architecture v2, evaluation plan, feature roadmap** | **All** | **🔄 In Progress** |
| 5 | Optimization | Golden set creation (50 receipts), prompt optimization, GPT-4o-mini integration | Sarah | 📅 Planned |
| 6 | Safety | Image preprocessing, confidence scoring, error handling, multi-pass verification | Sarah + Michael | 📅 Planned |
| 7 | User Testing 1 | First user feedback round (5 participants), iterate on UX | All | 📅 Planned |
| 8 | Iteration | Implement top 3 improvements from Week 7 testing | All | 📅 Planned |
| 9 | **Midterm Exam** | Study week (reduced project work, bug fixes only) | All | 📅 Planned |
| 10 | Deployment | Deploy to production (Railway), monitoring setup (Sentry), CI/CD (GitHub Actions) | Michael | 📅 Planned |
| 11 | **Safety Audit** | Red teaming, bias testing, privacy review (GDPR compliance check) | All | 📅 Planned |
| 12 | Evaluation | Golden set regression (full 50 receipts), performance benchmarking | Priya | 📅 Planned |
| 13 | Production Polish | Bug fixes based on Week 12 testing, UX improvements, CSV export refinement | All | 📅 Planned |
| 14 | User Testing 2 | Final validation round (5 NEW participants), measure against Week 7 baseline | All | 📅 Planned |
| 15 | **Final Demo** | Presentation (10 min), demo video (3 min), case study write-up, GitHub README | All | 📅 Planned |

---

### Major Milestones

**✅ Milestone 1: Proposal v1 (Week 2)** - COMPLETE
- **Submitted:** October 10, 2024
- **Grade:** 9/10 points
- **Feedback:** "Good start, but problem statement too broad. Narrow your target user."
- **Action Taken:** Interviewed 6 users, narrowed to freelancers earning <$100K

---

**🔄 Milestone 2: Design Review (Week 4)** - IN PROGRESS
- **Due:** October 25, 2024
- **Points:** 5/25 total capstone points
- **Deliverables:**
  1. ✅ This document (Refined Proposal v2)
  2. ⏳ AI-generated feature roadmap (due Friday)
  3. ✅ Updated architecture diagram (see Section 4)
  4. ⏳ Comprehensive evaluation plan (due Friday)
  5. ✅ Token usage & cost model (see Section 10)
  6. ⏳ Prioritized backlog v2 (due Friday)
  7. ⏳ Team health check (due Friday)

**Current Status:** 60% complete, on track to finish by Friday EOD

---

**🎯 Milestone 3: Safety & Evaluation Audit (Week 11)**
- **Due:** December 6, 2024
- **Points:** 3/25 total capstone points
- **Deliverables:**
  - Red team testing results (10 adversarial test cases)
  - Bias evaluation (test across 3+ demographics)
  - Golden set regression (50 receipts, >95% accuracy)
  - Error taxonomy (categorize all failure modes)
  - Telemetry implementation plan (what we'll monitor post-course)

**Preparation Plan:**
- Week 5: Create golden set (50 receipts covering diverse cases)
- Week 6: Implement confidence scoring and error handling
- Week 10: Deploy monitoring tools (Sentry for error tracking)
- Week 11: Run full audit

---

**🎯 Milestone 4: Final Demo (Week 15)**
- **Due:** December 20, 2024
- **Points:** 7/25 total capstone points
- **Deliverables:**
  - Live product demo (10 minutes, all 3 team members present)
  - Demo video (3 minutes, published on YouTube, embedded in README)
  - Case study write-up (5 pages: problem, solution, results, learnings)
  - Public GitHub repo with:
    - Comprehensive README (setup instructions, architecture, screenshots)
    - Deployment guide (how to deploy your own instance)
    - API documentation (all endpoints documented)
    - License (MIT)
  - CI/CD pipeline (GitHub Actions: lint, test, deploy on merge to main)

**Success Criteria:**
- All target metrics hit (see Section 3)
- Product is actually deployed and usable (not just localhost)
- Demo is smooth (no crashes during presentation)
- Code is clean and documented (ready for hiring managers to review)

---

### Velocity Tracking (Reality Check)

**Week 3 Planned vs. Actual:**
- **Planned:** 30 hours team effort, basic prototype working, API deployed
- **Actual:** 25 hours team effort, basic prototype working (localhost only, not deployed)
- **Lesson:** We underestimated debugging time by 30%, overestimated productivity

**Week 4 Adjusted Expectations:**
- **Plan:** 30 hours team effort → **Expect:** 20 hours of real progress (accounting for midterm prep, debugging overhead)
- **Realistic Output:** Complete 3-4 major tasks (not the 6 we originally hoped)

**Realistic Team Capacity per Week:**
- **Sarah Chen:** 12 hours/week (consistent, reliable)
- **Michael Torres:** 10 hours/week (has 2 other demanding courses)
- **Priya Patel:** 15 hours/week (most available, but less backend experience)
- **Total:** ~37 hours/week THEORETICAL → ~25 hours/week PRACTICAL (after meetings, debugging, context switching)

**What This Means:**
- We can realistically complete 10-12 major features by Week 15 (not 20)
- Must prioritize ruthlessly: P1 features only, defer everything else
- Buffer time for unexpected issues (deployment problems, API changes, sick days)

---

## 7. Team Health & Collaboration

### What's Working Well (Week 4 Assessment)

✅ **Communication:**
- Daily Slack check-ins at 9am working great
- Response time usually <2 hours (even on weekends)
- Good use of voice calls for complex technical discussions (2-3x/week)
- GitHub PR reviews happening within 24 hours

✅ **Technical Collaboration:**
- Pair programming sessions 2x/week (Sarah + Michael on backend) very effective
- Code reviews are constructive and teaching-focused
- Shared knowledge of codebase (all 3 can fix bugs in any part)

✅ **Task Ownership:**
- Clear division: Sarah=AI/prompts, Michael=backend/infra, Priya=frontend/UX
- Everyone contributing meaningfully (no one feeling left out or overworked)
- No major conflicts over technical decisions (healthy debate, then consensus)

✅ **Morale:**
- Team is excited about the project (we're solving a real problem we personally face!)
- Good energy in meetings (laughing, joking, not burnt out)

---

### What Needs Improvement

⚠️ **Documentation:**
- **Problem:** Inline code comments are sparse, new team members would struggle
- **Impact:** Hard to context-switch between tasks, slows down onboarding
- **Fix:** Week 5 sprint: spend 2 hours documenting all major functions and components
- **Owner:** Priya (will create doc template, all team members contribute)

---

⚠️ **Testing:**
- **Problem:** No automated tests yet, manual testing is time-consuming, regressions slipping through
- **Impact:** Broke production 2x in Week 3 due to untested changes
- **Fix:** Week 6 sprint: allocate full week to writing tests, aim for >50% code coverage
- **Owner:** Priya (will lead testing effort, pair with others to write tests)

---

⚠️ **Workload Balance:**
- **Problem:** Michael is doing 60% of backend work because he has most FastAPI experience. Sarah and Priya less confident with backend.
- **Impact:** Michael working 15 hours/week (over target), risk of burnout. If Michael gets sick or overwhelmed during midterms, we're blocked.
- **Fix:** 
  1. Cross-training sessions (Week 5): Michael teaches Sarah basic FastAPI in 2-hour pairing session
  2. Documentation (Week 5): Michael documents backend architecture in `/docs/backend-guide.md`
  3. Task redistribution (Week 6): Sarah takes next backend task (confidence scoring logic) with Michael as reviewer
- **Owner:** Michael (teaching) + Sarah (learning)

---

### Updated Team Contract (Changes from Week 2)

**Adjusted Meeting Schedule:**
- ~~3x/week~~ → **2x/week in-person** (Wednesdays 6-8pm library, Saturdays 10am-12pm Starbucks)
- Daily async Slack check-ins (9am each day: "What I'm working on today")
- Ad-hoc pair programming as needed (scheduled via Slack)

**Rationale:** 3x/week was overkill, too much meeting overhead. 2x/week + daily Slack is sufficient.

---

**Adjusted Roles:**
- **Sarah Chen:** AI/prompts + image preprocessing (expanded scope to include preprocessing)
- **Michael Torres:** Backend + deployment + architecture (same, but deployment is bigger than expected)
- **Priya Patel:** Frontend + UX + testing lead (NEW: will own all testing efforts starting Week 6)

**Rationale:** Priya wants to learn testing, and we desperately need tests. Win-win.

---

**Decision-Making Process:**
- **Technical decisions:** Majority vote AFTER trying both approaches in quick prototype (no endless debates)
- **Scope cuts:** Unanimous agreement required (everyone must consent to cutting a feature)
- **Urgent issues:** Any team member can make call independently, but must document rationale in Slack + notify team ASAP

**Example:** Michael decided to switch from MongoDB to PostgreSQL without full team vote because we were stuck for 6 hours. He posted rationale in Slack, team agreed retroactively. This was the right call.

---

## 8. Summary: Key Changes Since Week 2

### Problem & Solution
- ✅ **Narrowed target user:** from "all small businesses" to "freelancers with <$100K revenue" based on 6 user interviews
- ✅ **Validated problem:** 100% of interviewees confirmed expense tracking is top pain point
- ✅ **Refined solution:** Focus on MOBILE-FIRST (80% of receipts happen in field), not desktop

### Technical Architecture
- ✅ **Switched Flask → FastAPI** for async support and better developer experience
- ✅ **Switched MongoDB → PostgreSQL** for relational data model and CSV export ease
- ✅ **Added GPT-4o-mini** for 80% of queries (90% cost savings vs. GPT-4o only)
- ✅ **Added Cloudinary** for image storage, CDN, auto-optimization
- ✅ **Added Clerk** for authentication (OAuth, JWT, free tier perfect for MVP)
- ✅ **Deployed prototype** to Railway staging (not production yet)

### Success Metrics
- ✅ **Added specific, measurable targets:** >70% task completion, <3s latency, >85% accuracy
- ✅ **Baseline measurements:** Tested with 2 users (45% task completion, 4.2 min per receipt)
- ✅ **Cost tracking:** $0.013/query current (target: <$0.003 with optimizations)
- ✅ **Identified critical gap:** Amount accuracy only 70% (MUST fix Week 5-6)

### Risk Management
- ✅ **Identified 5 new risks** from prototyping: API costs, faded receipts, deployment complexity, midterm availability, amount accuracy
- ✅ **Implemented cost controls:** tracking dashboard, rate limiting, model switching plan
- ✅ **Created mitigation roadmap:** Week-by-week plan to address top 3 critical risks

### Scope Adjustments
- ❌ **Removed RAG** from MVP (not essential for receipt scanner, overkill)
- ❌ **Removed batch upload** (nice-to-have, can add post-course)
- ❌ **Removed advanced categorization** (simple dropdown is sufficient for MVP)
- ✅ **Kept core extraction + confidence scoring** (essential for trust)
- ✅ **Added image preprocessing** (CRITICAL for faded receipts)

### Team Dynamics
- ✅ **Realistic velocity:** ~25 hours/week practical capacity (vs. 37 hours theoretical)
- ✅ **Cross-training plan:** Michael teaching Sarah backend to mitigate bus factor
- ✅ **Adjusted meeting schedule:** 3x/week → 2x/week (reduced overhead)
- ✅ **Testing ownership:** Priya will lead Week 6 testing sprint

---

## 9. Appendix

### A. Technology Research Summary

**Why FastAPI over Flask?**
- **Researched:** Read FastAPI docs, compared benchmarks, watched tutorial videos
- **Prototyped:** Built "Hello World" in both, FastAPI felt more modern
- **Decision:** FastAPI chosen for:
  - Automatic API docs (Swagger UI out of the box)
  - Better type safety (Pydantic models catch bugs early)
  - Async support (future-proofing for streaming responses)
  - Active community (Stack Overflow answers are recent)
- **Tradeoff:** Slightly steeper learning curve, but worth it
- **Source:** https://fastapi.tiangolo.com

**Why PostgreSQL over MongoDB?**
- **Researched:** Compared data models, read articles on "SQL vs NoSQL for financial data"
- **Prototyped:** Spent 6 hours on MongoDB before giving up (relations were painful)
- **Decision:** PostgreSQL chosen for:
  - Clear relational structure (users → receipts is one-to-many)
  - ACID guarantees (critical for financial data)
  - Better CSV export (SQL query → CSV is trivial)
  - JSONB support (get flexibility of NoSQL for items array)
- **Tradeoff:** Less flexible schema, migrations are more work
- **Source:** Railway tutorial, Postgres docs

---

### B. User Interview Notes Summary

**Participant 1 (Freelance Designer, Atlanta, 29F):**
- **Pain point:** "I lose receipts ALL THE TIME. I find them crumpled in my purse 3 months later."
- **Need:** "I just want to take a photo and forget about it. No categories, no tags, just photo and done."
- **Would pay:** "$10/month if it's stupid simple. I'm not paying $15 for QuickBooks that I don't understand."
- **Quote:** "Can it remind me to take a photo when I'm at Staples? Like, location-based reminder?"

**Participant 2 (Management Consultant, 34F, Atlanta) - Maria:**
- **Pain point:** "My accountant charges me extra because my records are a mess. I know it's my fault."
- **Need:** "Auto-categorization would be HUGE. I have no idea if 'Uber' is 'travel' or 'transportation' or what."
- **Would pay:** "$15/month if it saves me 2+ hours per week. Time is money."
- **Quote:** "I'm so embarrassed to tell my accountant I lost receipts again. I know I'm leaving money on the table."

[Include summaries from all 6 interviews - User #3 through #6]

---

### C. Cost Calculation Details

**Current Cost Model (Week 4, No Optimization):**
```
GPT-4o (current):
- System prompt: 500 tokens × $0.0025/1K = $0.00125
- User query: 200 tokens × $0.0025/1K = $0.0005
- Image: ~1,000 tokens (varies)
- Output: 600 tokens × $0.015/1K = $0.009
- Total per query: ~$0.0125
- Monthly (1,000 queries): $12.50
```

**Projected Cost (Week 6, With All Optimizations):**
```
80% GPT-4o-mini, 20% GPT-4o, prompt optimization, caching:
- Mini (800 queries): 800 × $0.0002 = $0.16
- Full (200 queries): 200 × $0.003 = $0.60
- Cache hits (40%): 400 queries @ $0 = $0.00
- Total monthly: $0.76 (94% reduction!)
```

---

### D. Architecture Diagrams

[Diagram shown in Section 4 - see above]

---

### E. Week 3-4 Prototype Screenshots

[Would include actual screenshots here - example:]

**Screenshot 1: Upload Screen**
- Clean mobile interface
- Camera/file upload buttons
- Preview before upload

**Screenshot 2: Results Screen**
- Extracted data in editable fields
- Confidence indicator (green check for high, yellow warning for medium)
- Save/Cancel buttons

**Screenshot 3: History View**
- List of past receipts
- Sort by date
- Search by merchant
- Export CSV button

---

**Document Version:** 2.0  
**Last Updated:** October 24, 2024 (Week 4)  
**Next Review:** Week 7 (after user testing Round 1)

---

## ✅ Review Checklist

Before submitting, we verified:

- [x] All sections updated from Week 2 version
- [x] Specific changes documented with rationale (see Section 8 summary)
- [x] Measurable success metrics with targets (Section 3)
- [x] Architecture diagram included and explained (Section 4)
- [x] All known risks documented with mitigation plans (Section 5)
- [x] Realistic timeline based on Week 3-4 velocity (Section 6)
- [x] Team health assessment completed (Section 7)
- [x] All team members reviewed and approved ✅ Sarah ✅ Michael ✅ Priya
- [x] Proofread for typos and clarity
- [x] Links and references verified

---

**Team Sign-Off:**

✅ **Sarah Chen** - Reviewed and approved, October 24, 2024  
✅ **Michael Torres** - Reviewed and approved, October 24, 2024  
✅ **Priya Patel** - Reviewed and approved, October 24, 2024

**Submitted:** October 24, 2024, 11:59 PM EST  
**Grade:** [To be determined by instructor]
