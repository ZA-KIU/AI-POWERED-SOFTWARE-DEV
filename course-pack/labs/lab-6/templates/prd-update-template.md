# PRD Update Template: Week 4 Design Review

**Team Name:** [Your Team Name]  
**Project Title:** [Your Project Title]  
**Submission Date:** [Date]  
**Milestone:** Design Review (5 points)  
**Due:** Friday, Week 4, 11:59 PM

---

## Purpose of This Update

This document builds on your Week 2 Capstone Proposal.
- Built your first working prototype (even if minimal)
- Learned more about your technical constraints
- Refined your understanding of user needs
- Started implementing core features

This update focuses on **technical depth** and **implementation planning** based on what you've learned in Weeks 3-4.

---

## Submission Checklist

Before submitting, ensure you have:

- [ ] Updated architecture diagram (v2) with ALL components
- [ ] Detailed evaluation plan with specific metrics and tests
- [ ] Token usage estimate with cost calculations
- [ ] Refined backlog (15+ GitHub issues for Weeks 5-8)
- [ ] Updated repository structure in `/docs/design-review.md`
- [ ] All diagrams exported and committed (`.png` or `.svg`)
- [ ] No spelling/grammar errors
- [ ] Professional formatting

**Submit by:** Committing `docs/design-review.md` to your GitHub repo and posting repo URL to course submission system.

---

## Section 1: Architecture Diagram (v2) — 35% of grade

### Requirements

Your updated architecture diagram must include:

1. **All Components with Labels**
   - Frontend (framework/technology)
   - Backend API (framework/technology)
   - Database (type and provider)
   - AI/ML services (specific models)
   - Vector store (if using RAG)
   - External APIs or services
   - Queue system (if async processing)

2. **Data Flows with Arrows**
   - User input → Processing → Output
   - Where data is stored and retrieved
   - API calls to external services
   - Real-time vs. async flows

3. **Technology Choices Labeled**
   - Be specific: "GPT-4o" not "OpenAI"
   - "PostgreSQL on Supabase" not "database"
   - "React 18 with Next.js 14" not "frontend"

4. **Audio Processing Pipeline** (if applicable)
   - Input format (e.g., .mp3, .wav)
   - Preprocessing steps (sampling rate, duration limits)
   - Audio provider choice (OpenAI Whisper, Google Speech-to-Text, etc.)
   - Storage and retention policy

### Architecture Diagram Checklist

- [ ] Shows frontend, backend, database, AI services
- [ ] Data flow arrows are clear and labeled
- [ ] Includes vector store (if using RAG)
- [ ] Shows queue/async workers (if applicable)
- [ ] Audio pipeline detailed (if audio project)
- [ ] Technology choices are specific (e.g., "Pinecone" not "vector DB")
- [ ] Includes error handling touchpoints
- [ ] Shows monitoring/logging (optional but recommended)

### Example Architecture Description

**Provide a 2-3 paragraph written description of your architecture:**

```markdown
## System Architecture Overview

[Describe your system at a high level. Example:]

Our system follows a client-server architecture with a React frontend communicating with a FastAPI backend. User queries are sent via REST API to the backend, which orchestrates calls to GPT-4o for natural language understanding and Pinecone for semantic search over our knowledge base of 10,000+ documents.

The backend preprocesses all queries by extracting intent and checking against a blocklist. Valid queries trigger a RAG pipeline: (1) embed the query using text-embedding-3-small, (2) retrieve top-5 documents from Pinecone, (3) construct a prompt with retrieved context, (4) call GPT-4o with structured output enforcement using Pydantic models, (5) return JSON to frontend. All responses are logged to PostgreSQL for evaluation and debugging.

For audio features, we accept .mp3 and .wav files up to 10MB, transcode to 16kHz mono using FFmpeg, and send to OpenAI Whisper API. Transcripts are cached in Redis with 1-hour TTL. Asynchronous jobs are queued in Celery with Redis as broker for batch processing of audio files uploaded in bulk.
```

### Tools for Creating Diagrams

**Recommended:**
- **draw.io** (free, web-based): https://app.diagrams.net/
- **Excalidraw** (free, sketch-style): https://excalidraw.com/
- **Mermaid** (code-to-diagram in markdown):
  ```markdown
  ```mermaid
  graph TD
    A[User] -->|Query| B[Frontend]
    B -->|HTTP POST| C[Backend API]
    C -->|Embed| D[OpenAI API]
    C -->|Search| E[Pinecone]
    C -->|Generate| F[GPT-4o]
  ```
  ```
- **Lucidchart** (paid, professional)

**Export your diagram as:**
- `.png` (recommended, universal)
- `.svg` (optional, scales better)

**Save to:** `docs/architecture-diagram-v2.png`

---

## Section 2: Evaluation Plan — 25% of grade

### Requirements

Your evaluation plan must define **how you will measure success** across three dimensions:

1. **Accuracy/Quality Metrics**
2. **Performance Metrics (Latency and Cost)**
3. **User Experience Metrics**

Each metric must include:
- **Name** (e.g., "Intent Classification Accuracy")
- **Definition** (exactly what you're measuring)
- **Target** (specific number, e.g., "≥ 90%")
- **Measurement Method** (how you'll test this)

### 2.1 Accuracy and Quality Metrics

Define at least **3 accuracy metrics** relevant to your project:

| Metric Name | Definition | Target | How We'll Measure It |
|-------------|------------|--------|---------------------|
| [Example: RAG Relevance] | % of retrieved documents rated as relevant by human evaluators | ≥ 85% | Create 50-item golden set; two team members independently rate; average scores |
| [Your Metric 1] | | | |
| [Your Metric 2] | | | |
| [Your Metric 3] | | | |

**Possible accuracy metrics (choose what applies):**
- Classification accuracy (if categorizing inputs)
- Extraction precision/recall (if extracting structured data)
- RAG relevance (if using retrieval)
- Response correctness (if answering questions)
- Hallucination rate (% of responses with false info)
- Sentiment accuracy (if analyzing sentiment)
- Translation quality (if translating)

### 2.2 Performance Metrics

Define **latency** and **cost** targets:

| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| **End-to-end latency** | [e.g., < 3 seconds] | Measure from user submit to response display; test with 20 queries; report p50, p95, p99 |
| **Cost per session** | [e.g., < $0.10] | Track API costs; divide by number of sessions; log in dashboard |
| **API call latency** | [e.g., < 1.5 seconds] | Measure LLM API response time; report p95 |

**Latency Targets:**
- Simple queries: < 2 seconds
- Complex queries (RAG, multiple tools): < 5 seconds
- Batch processing: < 30 seconds per item

**Cost Targets:**
- Free tier projects: $0 per session
- Paid tier projects: justify budget (e.g., < $0.05 per query)

### 2.3 User Experience Metrics

Define at least **2 UX metrics**:

| Metric | Target | How We'll Measure It |
|--------|--------|---------------------|
| [Example: User Satisfaction] | ≥ 4.0/5.0 average rating | Post-task survey with 5-point Likert scale; 10+ users |
| [Your UX Metric 1] | | |
| [Your UX Metric 2] | | |

**Possible UX metrics:**
- User satisfaction score (post-task survey)
- Task success rate (% of users who complete goal)
- Time to complete task
- Error recovery rate (% of users who recover from errors)
- Net Promoter Score (would you recommend this?)

### 2.4 Golden Set Creation Plan

**What is a golden set?** A curated set of test inputs with known expected outputs, used to measure accuracy and catch regressions.

**Your golden set plan:**

- **Size:** [e.g., 50 test cases]
- **Coverage:** [what types of inputs, edge cases, etc.]
- **Expected Outputs:** [how you'll define "correct" answers]
- **Creation Method:** [manual curation, crowdsourcing, synthetic generation?]
- **Maintenance Plan:** [how often you'll update it]

**Example:**

```markdown
We will create a golden set of 75 test queries covering:
- 25 simple factual questions (one-hop retrieval)
- 25 complex multi-step questions (multi-hop retrieval)
- 15 ambiguous queries (testing uncertainty handling)
- 10 adversarial queries (testing safety filters)

Each item includes: (1) user query, (2) expected retrieved documents (by ID), (3) expected answer (human-written), (4) edge case category. We'll create this in Week 5 and update monthly or after major prompt changes.
```

### 2.5 Testing Strategy

Describe your testing approach:

**Unit Tests:**
- [ ] Prompt templates (test with fixed inputs)
- [ ] Data preprocessing functions
- [ ] Pydantic model validation
- [ ] API endpoint logic

**Integration Tests:**
- [ ] End-to-end user flow (input → output)
- [ ] RAG pipeline (query → retrieve → generate)
- [ ] Error handling (malformed inputs, API failures)

**Evaluation Tests:**
- [ ] Golden set evaluation (weekly regression tests)
- [ ] Latency benchmarks (run before each milestone)
- [ ] Cost tracking (daily monitoring)

**User Testing:**
- [ ] Round 1: Week 7 (5-7 users, qualitative feedback)
- [ ] Round 2: Week 14 (10+ users, quantitative + qualitative)

---

## Section 3: Token Usage Plan — 20% of grade

### Requirements

Estimate your **monthly token usage** and **cost**. This helps you stay within budget and avoid surprise bills.

### 3.1 Usage Assumptions

Define your usage scenario:

- **Users per month:** [e.g., 500 sessions]
- **Queries per session:** [e.g., 5 queries]
- **Total queries per month:** [e.g., 2,500 queries]

### 3.2 Token Breakdown Per Query

Calculate tokens for a **typical query**:

| Component | Tokens | Explanation |
|-----------|--------|-------------|
| System prompt | [e.g., 200] | Your system instructions |
| User query | [e.g., 50] | Average user input length |
| Retrieved context (if RAG) | [e.g., 1,500] | Top-5 documents × 300 tokens each |
| Few-shot examples | [e.g., 300] | If using in-context examples |
| Conversation history | [e.g., 500] | Previous turns (if multi-turn) |
| **Total input tokens** | **[e.g., 2,550]** | Sum of above |
| Model response | [e.g., 150] | Average completion length |
| **Total tokens per query** | **[e.g., 2,700]** | Input + output |

### 3.3 Cost Calculation

Calculate costs using your provider's pricing:

**OpenAI GPT-4o Pricing (as of 2024):**
- Input: $2.50 / 1M tokens
- Output: $10.00 / 1M tokens

**Example Calculation:**

```
Total monthly queries: 2,500
Input tokens per query: 2,550
Output tokens per query: 150

Monthly input tokens: 2,500 × 2,550 = 6,375,000
Monthly output tokens: 2,500 × 150 = 375,000

Monthly cost:
  Input: 6.375M tokens × ($2.50 / 1M) = $15.94
  Output: 0.375M tokens × ($10.00 / 1M) = $3.75
  Total: $19.69/month
```

**Your Calculation:**

| Item | Amount |
|------|--------|
| Monthly queries | [number] |
| Input tokens per query | [number] |
| Output tokens per query | [number] |
| Monthly input tokens | [calculation] |
| Monthly output tokens | [calculation] |
| Input cost | $[amount] |
| Output cost | $[amount] |
| **Total monthly cost** | **$[amount]** |

### 3.4 Cost Optimization Strategies

List at least **3 strategies** to reduce costs:

1. **[Strategy 1, e.g., Caching]:** Cache common queries in Redis with 24-hour TTL; reduces redundant API calls by ~30%
2. **[Strategy 2, e.g., Prompt Compression]:** Shorten system prompt from 300 to 150 tokens; use prompt caching for static instructions
3. **[Strategy 3, e.g., Model Selection]:** Use GPT-4o-mini for simple queries (30% of traffic); reserve GPT-4o for complex queries
4. **[Optional: Batch Processing]:** Queue background tasks and batch API calls; reduces costs by ~15%

### 3.5 Monitoring and Alerts

**How you'll track costs:**
- [ ] Log every API call with token counts to database
- [ ] Daily cost dashboard (show spend vs. budget)
- [ ] Alert if daily spend exceeds $[threshold]
- [ ] Weekly cost report to team

**Tools:**
- OpenAI usage dashboard: https://platform.openai.com/usage
- Custom logging: Store tokens/costs in PostgreSQL
- Monitoring: Grafana or simple spreadsheet

### 3.6 Provider Pricing Comparison

**Compare at least 2 providers** (if applicable):

| Provider | Model | Input Cost | Output Cost | Notes |
|----------|-------|------------|-------------|-------|
| OpenAI | GPT-4o | $2.50/1M | $10.00/1M | Best quality |
| OpenAI | GPT-4o-mini | $0.15/1M | $0.60/1M | Fast, cheaper |
| Anthropic | Claude Sonnet 4.5 | $3.00/1M | $15.00/1M | Long context |
| Google | Gemini 1.5 Flash | $0.075/1M | $0.30/1M | **Free tier: 1,500 req/day** |
| [Your Choice] | | | | |

**Your provider choice:** [e.g., "Google Gemini 1.5 Flash for free tier; switch to GPT-4o-mini if we exceed limits"]

---

## Section 4: Refined Backlog — 20% of grade

### Requirements

Create **15+ GitHub Issues** for Weeks 5-8. Each issue must have:

1. **Clear title** (action-oriented)
2. **Description** (what needs to be done)
3. **Acceptance criteria** (definition of done)
4. **Labels** (e.g., `backend`, `frontend`, `ai`, `testing`)
5. **Milestone** (Week 5, 6, 7, or 8)
6. **Assignee** (who's responsible)

### 4.1 Backlog Structure

Organize issues by category:

**Week 5 (RAG Integration):**
- [ ] Issue #[X]: Set up Pinecone vector store and import documents
- [ ] Issue #[Y]: Implement embedding pipeline with text-embedding-3-small
- [ ] Issue #[Z]: Create retrieval function with relevance scoring
- [ ] Issue #[A]: Test RAG pipeline with 10 sample queries

**Week 6 (Function Calling & Structured Outputs):**
- [ ] Issue #[B]: Define Pydantic models for structured outputs
- [ ] Issue #[C]: Implement function calling for [specific tool]
- [ ] Issue #[D]: Add JSON schema validation to API responses
- [ ] Issue #[E]: Create unit tests for Pydantic models

**Week 7 (User Testing Round 1):**
- [ ] Issue #[F]: Recruit 5-7 users for testing
- [ ] Issue #[G]: Create user testing protocol and consent forms
- [ ] Issue #[H]: Conduct user testing sessions and collect feedback
- [ ] Issue #[I]: Analyze feedback and prioritize bugs/features

**Week 8 (Iteration & Optimization):**
- [ ] Issue #[J]: Fix top 3 bugs from user testing
- [ ] Issue #[K]: Implement top 2 feature requests
- [ ] Issue #[L]: Optimize latency (target: < 3 seconds p95)
- [ ] Issue #[M]: Add caching layer for common queries
- [ ] Issue #[N]: Set up cost monitoring dashboard

### 4.2 Example Issue Template

**Title:** Set up Pinecone vector store and import documents

**Description:**
Initialize Pinecone index with our knowledge base of 500 documents. Each document should be chunked into ~500-token segments and embedded using text-embedding-3-small.

**Acceptance Criteria:**
- [ ] Pinecone index created with 1536 dimensions (text-embedding-3-small)
- [ ] All 500 documents chunked and uploaded
- [ ] Metadata includes: document_id, title, source, chunk_index
- [ ] Verify search works with 5 test queries
- [ ] Document setup process in README

**Labels:** `backend`, `rag`, `week-5`  
**Milestone:** Week 5  
**Assignee:** @[team-member]

### 4.3 Issue Labels

Use these labels (create in GitHub):

- `frontend` - UI/UX work
- `backend` - API/server work
- `ai` - LLM/prompt engineering
- `rag` - Retrieval and vector search
- `testing` - QA and evaluation
- `bug` - Something broken
- `feature` - New functionality
- `optimization` - Performance improvements
- `documentation` - Docs and guides
- `week-5`, `week-6`, `week-7`, `week-8` - Timeline labels

### 4.4 Dependency Management

Identify **critical dependencies** (what blocks what):

```markdown
**Blocking Relationships:**
- Issue #[X] (Pinecone setup) blocks Issue #[C] (RAG pipeline)
- Issue #[B] (Pydantic models) blocks Issue #[D] (JSON validation)
- Issue #[H] (User testing) blocks Issue #[J] (Bug fixes)

**If we fall behind:**
1. Cut: [Nice-to-have feature]
2. Cut: [Secondary optimization]
3. Cut: [Advanced monitoring]

**Must-have by Week 8:**
- Working RAG pipeline
- Structured outputs with Pydantic
- User testing completed (Round 1)
```

---

## Submission Instructions

### Files to Submit

1. **docs/design-review.md** (this template, filled out)
2. **docs/architecture-diagram-v2.png** (or .svg)
3. **docs/evaluation-plan.md** (optional: separate file if preferred)
4. **docs/token-usage-budget.md** (optional: separate file if preferred)
5. **GitHub Issues:** 15+ issues created in your repo's Issues tab

### Repository Structure

Ensure your repo looks like this:

```
your-repo/
├── docs/
│   ├── team-contract.md (from Week 2)
│   ├── capstone-proposal.md (from Week 2)
│   ├── design-review.md ← NEW
│   ├── architecture-diagram-v2.png ← NEW
│   ├── evaluation-plan.md (optional)
│   └── token-usage-budget.md (optional)
├── src/ (with working code)
├── tests/ (with some tests)
└── .github/issues/ (15+ issues created)
```

### How to Submit

1. **Commit all files** to your repo
2. **Push to GitHub**
3. **Create 15+ GitHub Issues** with labels, milestones, assignees
4. **Submit repo URL** to course submission system
5. **Verify instructor has access** (if repo is private)

---

## Grading Rubric (5 points total)

| Component | Points | Criteria |
|-----------|--------|----------|
| **Architecture Diagram** | 1.75 | Complete diagram with all components, data flows, and technology choices. Clear visual representation. Written description is thorough. |
| **Evaluation Plan** | 1.25 | At least 3 accuracy metrics, latency/cost targets, UX metrics, golden set plan, testing strategy. Metrics are specific and measurable. |
| **Token Usage Plan** | 1.0 | Realistic usage assumptions, detailed token breakdown, cost calculation, 3+ optimization strategies, monitoring plan, provider comparison. |
| **Refined Backlog** | 1.0 | 15+ GitHub issues with clear titles, descriptions, acceptance criteria, labels, milestones, assignees. Issues cover Weeks 5-8. Dependency map included. |

**Deductions:**
- Missing components: -0.5 per component
- Vague/incomplete sections: -0.25 per section
- No GitHub issues created: -1.0
- Late submission: -10% per 24 hours

---

## Tips for Success

### Do's ✅
- **Be specific:** "GPT-4o via OpenAI API" not "LLM"
- **Show your work:** Include calculations for costs
- **Think ahead:** Plan for Weeks 5-8, not just this week
- **Use diagrams:** A picture is worth 1,000 words
- **Test assumptions:** Validate your cost estimates with actual API calls
- **Document decisions:** Explain why you chose X over Y

### Don'ts ❌
- **Don't be vague:** "Use AI" is not a plan
- **Don't over-promise:** Be realistic about what's achievable
- **Don't ignore costs:** Token usage matters
- **Don't skip the backlog:** You need a roadmap for Weeks 5-8
- **Don't wait until Friday:** Start early, iterate

---

## Common Mistakes to Avoid

### Mistake 1: Architecture diagram is too high-level
❌ **Bad:** Shows only "Frontend" → "Backend" → "AI"  
✅ **Good:** Shows React → FastAPI → GPT-4o + Pinecone, with data flows labeled

### Mistake 2: Evaluation metrics are not measurable
❌ **Bad:** "Users will like it"  
✅ **Good:** "≥ 4.0/5.0 average user satisfaction score from post-task survey (n=10)"

### Mistake 3: Token usage is a wild guess
❌ **Bad:** "Probably $10/month"  
✅ **Good:** "2,500 queries × 2,700 tokens = 6.75M tokens = $19.69/month (breakdown: ...)"

### Mistake 4: Backlog issues are too vague
❌ **Bad:** Issue #1: "Make it work"  
✅ **Good:** Issue #1: "Set up Pinecone index with text-embedding-3-small, upload 500 chunked documents, verify search with 5 test queries"

---

## FAQs

### Q: Can we change our architecture after this milestone?
**A:** Yes, but document why. Major changes after Week 6 are risky.

### Q: What if our cost estimate is too high?
**A:** Identify optimization strategies or switch to a cheaper model/provider. Instructor can advise.

### Q: How detailed should our evaluation plan be?
**A:** Specific enough that someone else could replicate your tests. Include exact metrics, targets, and measurement methods.

### Q: Do we need to implement everything in the backlog by Week 8?
**A:** Aim for 80% completion. Document what you cut and why in your Week 8 report.

### Q: Can we use free-tier APIs?
**A:** Yes! Google Gemini offers 1,500 requests/day for free. Document this in your cost plan.

---

## Resources

### Architecture Diagram Tools
- draw.io: https://app.diagrams.net/
- Excalidraw: https://excalidraw.com/
- Mermaid (in markdown): https://mermaid.js.org/
- Lucidchart: https://www.lucidchart.com/

### Token Calculators
- OpenAI Tokenizer: https://platform.openai.com/tokenizer
- Token Counter for Python: `tiktoken` library

### Pricing Pages
- OpenAI: https://openai.com/api/pricing/
- Anthropic: https://www.anthropic.com/pricing
- Google AI: https://ai.google.dev/pricing

### Evaluation Resources
- Golden Set Creation: Course Week 12 materials
- User Testing Guide: `lab-2/guides/irb-light-guide.md`

---

## Example: Filled-Out Design Review (Partial)

### Section 1: Architecture Diagram

![Architecture Diagram](./architecture-diagram-v2.png)

**System Overview:**

Our RecipeFinder app uses a React frontend (Next.js 14) that communicates with a FastAPI backend deployed on Render. When a user submits a query like "quick vegetarian dinner ideas," the backend:

1. Validates and preprocesses the query (check length, sanitize input)
2. Embeds the query using text-embedding-3-small (OpenAI)
3. Searches our Pinecone vector store (10,000 recipes indexed)
4. Retrieves top-5 relevant recipes with metadata
5. Constructs a prompt with retrieved recipes as context
6. Calls GPT-4o-mini with strict structured output (Pydantic RecipeResponse model)
7. Returns JSON to frontend, which renders recipe cards

**Data persistence:** User queries and responses are logged to PostgreSQL (Supabase) for evaluation and analytics. We cache embeddings for common queries in Redis with 24-hour TTL.

**Audio integration (future):** For voice queries, we'll accept .mp3 audio, transcode to 16kHz mono, send to Whisper API, and process the transcript through the same pipeline.

### Section 2: Evaluation Plan

#### Accuracy Metrics

| Metric | Definition | Target | Measurement Method |
|--------|------------|--------|-------------------|
| Retrieval Precision | % of retrieved recipes rated as relevant | ≥ 80% | Golden set of 50 queries; manual rating by 2 team members |
| Response Correctness | % of AI-generated recipes that are plausible | ≥ 90% | Human evaluation: does recipe make sense? |
| Hallucination Rate | % of responses with false ingredient info | ≤ 5% | Check against known recipe database |

#### Performance Metrics

| Metric | Target | Measurement |
|--------|--------|------------|
| End-to-end latency (p95) | < 3 seconds | Log timestamps; calculate p95 across 100 queries |
| Cost per query | < $0.02 | Track OpenAI token usage; divide total cost by query count |

#### User Experience

| Metric | Target | Measurement |
|--------|--------|------------|
| User satisfaction | ≥ 4.0/5.0 | Post-task survey (5-point scale), n=10 users in Week 7 |
| Task success rate | ≥ 85% | % of users who find a recipe they like within 3 queries |

[... continue with remaining sections ...]

---

**END OF TEMPLATE**

Save this as `docs/design-review.md` and start filling it out!
