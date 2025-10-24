# Architecture Diagram Template & Guide

**Project Name:** [Your Project Name]  
**Version:** 2.0 (Updated Week 4)  
**Date:** [Date]

---

## 📐 Architecture Diagram

[INSERT YOUR DIAGRAM HERE]

**Diagram Formats Accepted:**
- PNG/JPG image (hand-drawn and scanned is fine!)
- Mermaid diagram (code-based, renders in Markdown)
- ASCII art diagram (text-based)
- Link to Figma/Lucidchart/Draw.io

**Required Elements in Your Diagram:**
- [ ] All system components (frontend, backend, database, APIs, etc.)
- [ ] Data flow arrows showing request/response paths
- [ ] Technology stack labels (specific versions)
- [ ] External dependencies (OpenAI, Auth services, etc.)
- [ ] Security boundaries (where auth happens)
- [ ] Latency annotations (target response times)

---

## 🏗️ Component Descriptions

### 1. Frontend

**Technology:** [e.g., React 18.2 + Vite 4.3]  
**Deployment:** [e.g., Vercel]  
**Purpose:** [Brief description]

**Key Responsibilities:**
- [ ] User interface rendering
- [ ] Form validation and input handling
- [ ] State management ([tool used, e.g., React Context, Redux])
- [ ] API communication with backend
- [ ] Error handling and loading states
- [ ] Client-side caching (if applicable)

**Notable Implementation Details:**
- Uses [specific library] for [specific purpose]
- Implements [pattern] for [reason]
- [Any other important details]

**Key Files/Components:**
```
src/
├── components/
│   ├── UploadForm.jsx      # Handles image uploads
│   ├── ResultsDisplay.jsx  # Shows extracted data
│   └── ErrorBoundary.jsx   # Error handling
├── hooks/
│   └── useApi.js           # Custom hook for API calls
└── App.jsx                 # Main app component
```

---

### 2. Backend

**Technology:** [e.g., FastAPI 0.104 + Python 3.11]  
**Deployment:** [e.g., Railway]  
**Purpose:** [Brief description]

**Key Responsibilities:**
- [ ] API endpoints ([list main routes])
- [ ] Authentication/authorization
- [ ] Business logic processing
- [ ] AI API integration (OpenAI, etc.)
- [ ] Database operations
- [ ] Image preprocessing (if applicable)
- [ ] Rate limiting and security

**API Endpoints:**

| Method | Endpoint | Purpose | Auth Required |
|--------|----------|---------|---------------|
| POST | `/api/upload` | Upload image for processing | Yes |
| GET | `/api/results/{id}` | Retrieve processed results | Yes |
| PUT | `/api/results/{id}` | Update/correct results | Yes |
| DELETE | `/api/results/{id}` | Delete result | Yes |
| GET | `/api/health` | Health check | No |

**Notable Implementation Details:**
- Uses [specific library] for [specific purpose]
- Implements [pattern] for [reason]
- [Any other important details]

**Key Files/Modules:**
```
app/
├── main.py              # FastAPI app initialization
├── routes/
│   ├── upload.py        # Upload endpoints
│   └── results.py       # Results CRUD
├── services/
│   ├── ai_service.py    # OpenAI integration
│   └── image_service.py # Image preprocessing
├── models/
│   └── schemas.py       # Pydantic models
└── database.py          # Database connection
```

---

### 3. Database

**Technology:** [e.g., PostgreSQL 15]  
**Deployment:** [e.g., Railway managed database]  
**Purpose:** [Brief description]

**Schema:**

**Users Table:**
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    last_login TIMESTAMP
);
```

**[Main Data Table] Table:**
```sql
CREATE TABLE receipts (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    image_url TEXT,
    merchant VARCHAR(255),
    date DATE,
    amount DECIMAL(10, 2),
    items JSONB,
    category VARCHAR(100),
    confidence FLOAT,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP
);
```

**Relationships:**
- One user → Many [records]
- [Other relationships]

**Indexes:**
- `user_id` (for fast user queries)
- `created_at` (for sorting)
- [Other indexes]

**Notable Implementation Details:**
- Using JSONB for flexible item storage
- Partitioning strategy: [if applicable]
- Backup strategy: [if implemented]

---

### 4. AI Services

**Primary AI Service:** [e.g., OpenAI GPT-4o Vision API]

**API Configuration:**
- **Model:** [e.g., gpt-4o-mini for 80% of queries, gpt-4o for complex cases]
- **Max Tokens:** [e.g., 1000]
- **Temperature:** [e.g., 0.3 for consistency]
- **Structured Output:** [Yes/No, format used]

**Prompt Structure:**
```
System Prompt: [Brief summary or actual prompt if short]
User Input: [Format of user input]
Expected Output: [JSON structure or format]
```

**Model Selection Logic:**
```python
def choose_model(image_quality_score):
    if image_quality_score > 0.7:
        return "gpt-4o-mini"  # Clear image, use cheaper model
    else:
        return "gpt-4o"       # Poor quality, use better model
```

**Fallback Strategy:**
- Primary: OpenAI API
- Fallback 1: [If OpenAI is down, what happens?]
- Fallback 2: [Ultimate fallback, e.g., return error with cached retry]

**Notable Implementation Details:**
- Caching strategy: [e.g., Redis for repeated queries]
- Rate limiting: [e.g., 100 requests/hour per user]
- Cost tracking: [How you monitor costs]

---

### 5. Authentication

**Technology:** [e.g., Clerk]  
**Purpose:** User authentication and authorization

**Authentication Flow:**
```
1. User signs up/logs in → Clerk handles auth
2. Clerk returns JWT token
3. Frontend stores JWT in localStorage (or httpOnly cookie)
4. All API requests include: Authorization: Bearer {jwt}
5. Backend validates JWT with Clerk
6. If valid, proceed with request
7. If invalid, return 401 Unauthorized
```

**Supported Auth Methods:**
- [ ] Email/password
- [ ] OAuth (Google, GitHub, etc.)
- [ ] Magic links
- [ ] Social login ([specific providers])

**Security Considerations:**
- JWTs expire after [X hours]
- Refresh token rotation: [Yes/No]
- CSRF protection: [Implementation]

---

### 6. External Services

#### Image Storage

**Service:** [e.g., Cloudinary]  
**Purpose:** Store uploaded images  
**Configuration:**
- Max file size: [e.g., 10MB]
- Allowed formats: [e.g., JPG, PNG, HEIC]
- Retention policy: [e.g., 7 days, then auto-delete]
- CDN: [Yes/No]

#### Other Services

**[Service Name]:** [e.g., Sentry for error tracking]  
**Purpose:** [Brief description]  
**Why Chosen:** [Justification]

---

## 🔄 Data Flow Diagrams

### Primary User Flow: [Main Action]

**Example: Upload and Process Receipt**

```
┌─────────┐         ┌──────────┐         ┌─────────┐         ┌─────────┐
│ User    │         │ Frontend │         │ Backend │         │ OpenAI  │
│ Browser │         │ (React)  │         │ (FastAPI│         │ API     │
└────┬────┘         └────┬─────┘         └────┬────┘         └────┬────┘
     │                   │                    │                   │
     │ 1. Upload image   │                    │                   │
     │──────────────────>│                    │                   │
     │                   │ 2. POST /api/upload│                   │
     │                   │ (with image)       │                   │
     │                   │───────────────────>│                   │
     │                   │                    │ 3. Preprocess img │
     │                   │                    │                   │
     │                   │                    │ 4. Call Vision API│
     │                   │                    │──────────────────>│
     │                   │                    │                   │
     │                   │                    │ 5. Return JSON    │
     │                   │                    │<──────────────────│
     │                   │                    │ 6. Store in DB    │
     │                   │                    │                   │
     │                   │ 7. Return result   │                   │
     │                   │<───────────────────│                   │
     │ 8. Display result │                    │                   │
     │<──────────────────│                    │                   │
     │                   │                    │                   │

Total Time: ~3 seconds
- Frontend validation: 50ms
- Image upload: 800ms
- Preprocessing: 150ms
- OpenAI API: 2000ms
- Database write: 80ms
- Frontend render: 100ms
```

**Error Scenarios:**

**Scenario 1: OpenAI API is down**
```
Backend receives 503 from OpenAI
↓
Backend returns 503 to frontend with message:
  "AI service temporarily unavailable. Please try again in a few minutes."
↓
Frontend displays error message
↓
User can retry or save for later
```

**Scenario 2: Invalid image format**
```
User uploads .exe file
↓
Frontend validation catches invalid format
↓
Shows error: "Please upload a JPG, PNG, or HEIC image"
↓
Does not send to backend
```

---

### Secondary Flow: [Another Important Flow]

[Diagram or description]

---

## ⚡ Performance & Latency

### Latency Budget

| Component | Target (P95) | Current | Status | Optimization Plan |
|-----------|--------------|---------|--------|-------------------|
| Frontend load | <1s | 800ms | ✅ Good | None needed |
| API response time | <3s | 4.5s | ⚠️ Needs work | Optimize prompt, add caching |
| Database query | <100ms | 80ms | ✅ Good | Add index on user_id |
| Image upload | <500ms | 800ms | ⚠️ Needs work | Use CDN, compress images |
| AI API call | <2s | 2.5s | ⚠️ Needs work | Reduce prompt tokens |

**Overall User Experience Target:** <5 seconds from upload to results display  
**Current Performance:** ~6.5 seconds  
**Gap:** 1.5 seconds to optimize

---

### Scalability Considerations

**Current Capacity:**
- Expected users: 10-50 during course
- Expected requests: 100-500/day
- Database size: <1GB

**Scaling Bottlenecks:**
- [ ] Database connections (limited to 10 on free tier)
- [ ] AI API rate limits (100 requests/hour)
- [ ] Image storage costs (could exceed budget at >1000 users)
- [ ] Backend memory (512MB on free tier)

**Scaling Strategy (If Needed Post-Course):**
- Add database connection pooling
- Implement aggressive caching (Redis)
- Upgrade to paid tiers
- Add CDN for images

---

## 🔒 Security Architecture

### Security Layers

**Layer 1: Frontend**
- Input validation (file type, size)
- HTTPS only
- Content Security Policy (CSP)
- No API keys exposed in client code

**Layer 2: Backend**
- JWT validation on all protected endpoints
- Rate limiting (100 req/hour per user)
- Input sanitization
- SQL injection protection (using ORMs)
- CORS configured to allow only frontend domain

**Layer 3: Database**
- Encrypted at rest (provider default)
- Encrypted in transit (SSL)
- Limited access (only backend can connect)
- Regular backups (if implemented)

**Layer 4: External Services**
- API keys stored in environment variables
- Never committed to Git
- Rotated regularly (if applicable)
- Least privilege access (read-only when possible)

### Threat Model

**Threats Considered:**
1. **Unauthorized access to data**
   - Mitigation: JWT authentication on all endpoints
   - Status: ✅ Implemented

2. **API key theft**
   - Mitigation: Keys only in backend, environment variables
   - Status: ✅ Implemented

3. **Prompt injection**
   - Mitigation: Input sanitization, system prompt guardrails
   - Status: ⏳ Planned for Week 6

4. **DoS attack**
   - Mitigation: Rate limiting
   - Status: ✅ Implemented

5. **SQL injection**
   - Mitigation: Using ORMs with parameterized queries
   - Status: ✅ Implemented

---

## 💰 Cost Architecture

### Cost Breakdown (Monthly Estimate)

| Service | Free Tier | Current Usage | Paid Tier Cost | Notes |
|---------|-----------|---------------|----------------|-------|
| Vercel (Frontend) | ✅ Unlimited | ~100 deploys | $0 | Within free tier |
| Railway (Backend + DB) | ✅ $5 credit | ~$3/month | $0 | Using free tier |
| OpenAI API | ❌ Pay-per-use | ~$10/month | $10 | 1000 queries @ $0.01 each |
| Cloudinary (Images) | ✅ 25GB/month | ~1GB/month | $0 | Within free tier |
| Clerk (Auth) | ✅ 10K users | ~10 users | $0 | Within free tier |
| **TOTAL** | - | - | **~$10/month** | Well within budget |

**Cost Optimizations:**
- Using GPT-4o-mini for 80% of queries (saves $40/month)
- Implementing caching for repeated queries (saves $5/month)
- Compressing images before storage (saves bandwidth)
- Auto-deleting old images after 7 days (saves storage)

---

## 🔄 Architecture Evolution

### Changes from Week 2 to Week 4

| Component | Week 2 | Week 4 | Reason for Change |
|-----------|--------|--------|-------------------|
| Backend | Flask | FastAPI | Needed async for streaming, better type safety |
| Database | MongoDB | PostgreSQL | Relational structure better fit for our data model |
| AI Model | GPT-4 only | GPT-4o-mini + GPT-4o | Cost optimization without sacrificing quality |
| Deployment | Heroku | Railway | Better free tier, simpler setup |
| Caching | None | Redis (planned) | Reduce API costs on repeated queries |

### Future Improvements (Post-Week 4)

**Week 5-6:**
- [ ] Add Redis caching layer
- [ ] Implement automated testing (pytest + GitHub Actions)
- [ ] Add monitoring/logging (Sentry)

**Week 8-10:**
- [ ] Add database backups (automated daily)
- [ ] Implement proper error handling across all endpoints
- [ ] Add health check endpoints for monitoring

**Week 12-14:**
- [ ] Performance optimization (code profiling, query optimization)
- [ ] Security hardening (penetration testing, OWASP checklist)
- [ ] Documentation updates (API docs, deployment guide)

---

## 🛠️ Development & Deployment

### Local Development Setup

**Requirements:**
- Node.js 18+
- Python 3.11+
- PostgreSQL 15+ (or use Railway remote DB)
- Git

**Setup Steps:**
```bash
# 1. Clone repository
git clone [repo-url]
cd [project-name]

# 2. Install frontend dependencies
cd frontend
npm install

# 3. Install backend dependencies
cd ../backend
pip install -r requirements.txt

# 4. Configure environment variables
cp .env.example .env
# Edit .env with your API keys

# 5. Run database migrations (if applicable)
python migrate.py

# 6. Start backend
uvicorn main:app --reload

# 7. Start frontend (in new terminal)
cd ../frontend
npm run dev
```

**Environment Variables:**

```bash
# Backend (.env)
DATABASE_URL=postgresql://user:pass@host:5432/dbname
OPENAI_API_KEY=sk-...
CLERK_API_KEY=sk-...
CLOUDINARY_URL=cloudinary://...

# Frontend (.env)
VITE_API_URL=http://localhost:8000
VITE_CLERK_PUBLISHABLE_KEY=pk-...
```

---

### Deployment Pipeline

**Current Deployment:**
- Frontend: Push to main → Vercel auto-deploys
- Backend: Push to main → Railway auto-deploys
- Database: Managed by Railway, auto-backups (if enabled)

**CI/CD Pipeline (Planned):**
```
1. Push to GitHub
   ↓
2. GitHub Actions runs:
   - Linting (ESLint, Black)
   - Type checking (TypeScript, mypy)
   - Unit tests (Jest, pytest)
   - Integration tests
   ↓
3. If all pass:
   - Deploy to staging
   - Run smoke tests
   ↓
4. Manual approval:
   - Deploy to production
```

---

## 🧪 Testing Strategy

### Testing Layers

**Frontend Tests:**
- Unit tests: Component behavior (Jest + React Testing Library)
- Integration tests: User flows (Playwright)
- Visual regression: Screenshot comparison (Percy, if time permits)

**Backend Tests:**
- Unit tests: Business logic (pytest)
- Integration tests: API endpoints (pytest + httpx)
- Database tests: CRUD operations (pytest + fixtures)
- AI tests: Mock OpenAI responses (pytest + mocking)

**End-to-End Tests:**
- Happy path: Full user journey works
- Error scenarios: Graceful error handling
- Performance: Latency within targets

---

## 📊 Monitoring & Observability

### Logging Strategy

**What We Log:**
- All API requests (method, endpoint, user, timestamp)
- All errors (stack traces, context)
- AI API calls (tokens used, cost, latency)
- Database queries (slow queries >100ms)

**Where Logs Go:**
- Development: Console
- Production: [Service, e.g., Sentry, LogRocket]

**Log Format:**
```json
{
  "timestamp": "2024-10-24T10:30:00Z",
  "level": "INFO",
  "user_id": "uuid",
  "endpoint": "/api/upload",
  "latency_ms": 3500,
  "tokens_used": 1200,
  "cost_usd": 0.012
}
```

---

### Metrics Dashboard (Planned)

**Key Metrics to Track:**
- Requests per day
- Average latency (P50, P95, P99)
- Error rate (4xx, 5xx)
- Cost per day
- Active users

**Dashboard Tool:** [e.g., Grafana, Vercel Analytics, custom]

---

## 🔧 Architecture Decisions

### Key Decisions & Tradeoffs

**Decision 1: FastAPI vs. Flask**
- **Chose:** FastAPI
- **Pro:** Async support, automatic API docs, type safety
- **Con:** Smaller ecosystem, less Stack Overflow answers
- **Tradeoff:** Accepted steeper learning curve for better developer experience

**Decision 2: PostgreSQL vs. MongoDB**
- **Chose:** PostgreSQL
- **Pro:** Strong ACID guarantees, better for relational data
- **Con:** Less flexible schema, more complex migrations
- **Tradeoff:** Accepted stricter schema for data integrity

**Decision 3: Clerk vs. Build Our Own Auth**
- **Chose:** Clerk
- **Pro:** Production-ready, OAuth built-in, free tier
- **Con:** Vendor lock-in, less control
- **Tradeoff:** Accepted vendor dependency to focus on core features

**Decision 4: GPT-4o-mini vs. GPT-4o**
- **Chose:** Hybrid (80% mini, 20% full)
- **Pro:** 90% cost savings while maintaining quality
- **Con:** More complex routing logic
- **Tradeoff:** Added complexity for significant cost savings

---

## 📚 References & Resources

**Architecture Patterns Used:**
- REST API design
- MVC pattern (frontend)
- Service layer pattern (backend)
- Repository pattern (database access)

**Inspiration:**
- [Similar projects you studied]
- [Architecture patterns you researched]

**Documentation:**
- FastAPI: https://fastapi.tiangolo.com
- React: https://react.dev
- PostgreSQL: https://postgresql.org/docs

---

## ✅ Architecture Review Checklist

Before finalizing, verify:

- [ ] All components documented
- [ ] Data flows clearly shown
- [ ] Technology choices justified
- [ ] Security considerations addressed
- [ ] Performance targets defined
- [ ] Cost breakdown provided
- [ ] Scalability considerations noted
- [ ] Error handling strategy defined
- [ ] Testing strategy outlined
- [ ] Deployment process documented
- [ ] Changes from Week 2 highlighted
- [ ] Future improvements planned

---

**Version:** 2.0  
**Last Updated:** Week 4, [Date]  
**Next Review:** Week 10 (before final optimization push)
