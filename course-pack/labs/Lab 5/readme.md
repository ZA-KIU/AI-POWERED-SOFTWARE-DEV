# Lab 5: PRD Creation & Technical Specification

**Week 5 | Building AI-Powered Applications**  
**Duration:** 2 hours in-class + independent work  
**Due:** November 7, 2025

## 🎯 Lab Overview

This week you'll transform your strategic planning from Lab 4 into a **production-ready Project Requirements Document (PRD)** that serves as the definitive source of truth for your capstone project. This PRD will provide the precise context that AI coding assistants (Cursor, Lovable, Replit, Windsurf, etc.) need for successful implementation.

You'll also design your **RAG/Knowledge Retrieval Strategy** and define **2-3 core functions** your AI system needs—preparing you for Week 6's function calling implementation.

## 📚 Learning Objectives

By the end of this lab, you will:

- Generate a comprehensive 18-section PRD using AI-assisted workflows
- Define your RAG/knowledge retrieval architecture and data sources
- Identify and specify 2-3 core functions your system requires
- Design Pydantic models for structured outputs
- Create JSON schemas for function calling (preparing for Week 6)
- Establish your project as "scaffolding-ready" for AI code generation

## 🔗 Connection to Course Flow

**From Week 4:** You completed strategic planning (proposal, architecture, risks, backlog)  
**This Week (5):** Transform strategy into technical specs + RAG design  
**To Week 6:** Implement function calling and structured outputs  

**Why This Matters:**
- Week 5 lecture covers RAG—you'll design your RAG strategy TODAY
- Week 6 lecture covers function calling—you'll define your functions TODAY
- A strong PRD = successful AI-assisted development in Weeks 7-15

## 📋 What's Due This Week

All deliverables go in your team's GitHub repo under `docs/week-5/`:

### Required Deliverables (15 points total)

| # | File Name | Points | Description |
|---|-----------|--------|-------------|
| 1 | `prd-full.md` | 8 | Complete 18-section Project Overview |
| 2 | `rag-strategy.md` | 3 | RAG architecture, data sources, chunking |
| 3 | `functions-spec.md` | 2 | 2-3 function definitions with JSON schemas |
| 4 | `pydantic-models.py` | 2 | Structured output models |

**Submission:** Push to GitHub by end of Week 5, submit repo link to LMS

---

## 🏗️ Part 1: Creating Your PRD (90 minutes)

### Step 1: Understand the PRD Template (10 min)

Your PRD follows the **18-Section Project Overview** structure specifically designed to:
- Eliminate "vibe coding" guesswork
- Provide precise context for AI coding assistants
- Serve as your project's single source of truth

**The 18 Sections:**

1. Project Goal & Core Problem
2. MVP Scope & Key Features
3. Target Audience
4. Technology Stack (with versions!)
5. High-Level Architecture
6. Core Components/Modules
7. Key UI/UX Considerations
8. Coding Standards & Quality Criteria
9. Testing Strategy
10. Initial Setup Steps
11. Key Architectural Decisions
12. Project Documentation
13. Repository Link
14. Dependencies & Third-Party Services
15. Security Considerations
16. Performance Requirements
17. Monitoring & Observability
18. Deployment & DevOps

### Step 2: Gather Your Materials (10 min)

**Pull together everything from Week 4:**
- `capstone-proposal-v2.md`
- `architecture-v2.md`
- `feature-roadmap.md`
- `evaluation-plan-v2.md`
- `cost-model-v2.md`
- `backlog-v2.md`

**Also identify:**
- Your technology stack choices (languages, frameworks, versions)
- API keys/services you'll need
- Your GitHub repository URL

### Step 3: Use the PRD Generator Prompt (40 min)

**Use the PRD Generator AI Prompt** (provided in `templates/prd-generator-prompt.md`)

**Process:**
1. Open Claude or ChatGPT
2. Paste the entire PRD generator prompt
3. Answer the initial context questions with your Week 4 materials
4. The AI will generate your complete 18-section PRD
5. Review and refine each section
6. Copy to `docs/week-5/prd-full.md`

**Pro Tips:**
- Be specific about technology versions (Python 3.11, React 18.2, etc.)
- Include actual numbers for performance requirements
- Don't skip sections—they're ALL important
- Use Mermaid diagrams for architecture (Section 5)

### Step 4: Critical Sections Deep Dive (30 min)

**Focus extra attention on these sections:**

**Section 4: Technology Stack**
```markdown
| Category | Technology | Version | Notes |
|----------|------------|---------|-------|
| Language | Python | 3.11.4 | |
| Backend | FastAPI | 0.104.1 | Async support |
| Frontend | React | 18.2.0 | |
| LLM API | OpenAI | 1.3.5 | GPT-4o primary |
| Vector DB | Pinecone | 2.2.4 | Serverless plan |
| Database | PostgreSQL | 15.3 | Supabase hosted |
```

**Section 8: Coding Standards**
```markdown
- Style Guide: PEP 8 for Python, Airbnb for JavaScript
- Formatter: Black (Python), Prettier (JS)
- Linter: Ruff (Python), ESLint (JS)
- Top 5 Quality Criteria: Reliability, Security, Testability, Maintainability, Cost-efficiency
```

**Section 10: Initial Setup Steps**
```bash
git clone https://github.com/yourusername/yourproject
cd yourproject
cp .env.example .env
# Edit .env with your API keys
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
npm install
python app.py
```

---

## 🔍 Part 2: RAG Strategy Design (30 minutes)

### What is RAG?

**Retrieval-Augmented Generation** solves the problem of LLMs lacking specific knowledge about YOUR data:
- Your documents
- Your database
- Your business logic
- Your user history

### Your RAG Strategy Document

Create `docs/week-5/rag-strategy.md` with these sections:

#### 1. Knowledge Sources

What data will your AI access?

**Example:**
```markdown
### Primary Knowledge Sources

1. **Company Policy Documents** (PDF, 50 files, ~500 pages)
   - Location: `/data/policies/`
   - Update frequency: Quarterly
   - Content: HR policies, safety procedures, benefits

2. **Product Catalog** (Database)
   - Source: PostgreSQL `products` table
   - Records: ~10,000 products
   - Fields: name, description, specs, price

3. **User History** (Database)
   - Source: PostgreSQL `user_actions` table
   - Records: ~50,000/month
   - Used for: Personalized recommendations
```

#### 2. RAG Architecture Choice

**Option A: Traditional RAG**
```
User Query → Embed Query → Vector Search → Retrieve Top K → 
Augment Prompt → LLM → Response
```

**Option B: Hybrid Search**
```
User Query → [Vector Search + Keyword Search] → Rerank → 
Retrieve Top K → Augment Prompt → LLM → Response
```

**Option C: No RAG (Hardcoded Context)**
```
User Query → Predefined Context → LLM → Response
```

Choose and justify your approach.

#### 3. Technical Implementation

```markdown
### Embedding Model
- Model: text-embedding-3-small
- Dimensions: 1536
- Cost: $0.02 per 1M tokens
- Why: Balance of quality and cost

### Vector Database
- Service: Pinecone (Serverless)
- Index name: project-knowledge-base
- Metric: Cosine similarity
- Why: Managed service, scales automatically

### Chunking Strategy
- Method: Recursive text splitter
- Chunk size: 1000 tokens
- Overlap: 200 tokens
- Why: Preserves context across chunks

### Retrieval Parameters
- Top K: 5 documents
- Similarity threshold: 0.7
- Reranking: Yes (cross-encoder)
```

#### 4. Citation Strategy

How will you show sources?

```markdown
### Citation Format
"According to the Employee Handbook (Section 3.2), remote work 
is allowed up to 2 days/week."

[Source: employee-handbook.pdf, page 15]
```

#### 5. RAG Alternatives (If Not Using RAG)

If your project doesn't need RAG:
- Explain why (e.g., using real-time API data instead)
- Describe your alternative data access pattern
- Show how you handle knowledge updates

---

## ⚙️ Part 3: Function Calling Specification (30 minutes)

### What Are Functions?

Functions let your AI **take actions** instead of just **talking about actions**:

**Without Functions:** "Here's how you could check the order status..."  
**With Functions:** *Actually checks database* "Order #12345 shipped yesterday"

### Your Functions Specification

Create `docs/week-5/functions-spec.md`

#### Step 1: Identify 2-3 Core Functions

**Ask yourself:**
1. What **external data** does my AI need to access?
2. What **actions** should my AI be able to take?
3. What **calculations** need to happen?

**Examples by project type:**

**Document Q&A System:**
- `search_documents(query, filters)` → Find relevant docs
- `log_query(user_id, query, response)` → Track analytics

**Customer Service Bot:**
- `check_order_status(order_id)` → Get order details
- `update_ticket(ticket_id, status, notes)` → Modify support ticket
- `escalate_to_human(ticket_id, reason)` → Hand off to agent

**Study Buddy App:**
- `search_course_materials(query, course_id)` → Find notes
- `save_study_session(topic, duration, quiz_score)` → Track progress
- `generate_practice_quiz(topic, difficulty)` → Create questions

**Content Moderation:**
- `check_user_history(user_id)` → Previous violations?
- `flag_content(content_id, reason, severity)` → Send to moderation
- `apply_action(user_id, action_type)` → Warn, suspend, or ban

#### Step 2: Write Function Specifications

**For EACH function, define:**

**Template:**
```markdown
### Function: function_name

**Purpose:** One sentence describing what this does

**When AI should call this:** 
Specific user intents or scenarios

**Parameters:**
- `param1` (string, required): Description
- `param2` (int, optional): Description, default: 5

**Returns:**
- Success: {JSON structure}
- Error: {error structure}

**JSON Schema:**
\`\`\`json
{
  "name": "function_name",
  "description": "Clear description of what this function does",
  "parameters": {
    "type": "object",
    "properties": {
      "param1": {
        "type": "string",
        "description": "What this parameter is for"
      },
      "param2": {
        "type": "integer",
        "description": "What this parameter is for",
        "default": 5
      }
    },
    "required": ["param1"]
  }
}
\`\`\`

**Example Call:**
\`\`\`python
result = check_order_status(order_id="12345")
# Returns: {"status": "shipped", "eta": "2025-11-02", "tracking": "1Z999AA1"}
\`\`\`

**Safety Considerations:**
- Validate order_id format (alphanumeric only)
- Check user owns this order before revealing data
- Rate limit: 10 calls/minute per user
```

**Real Example:**

````markdown
### Function: search_documents

**Purpose:** Search the knowledge base for documents matching a query

**When AI should call this:**
- User asks a question about policies, procedures, or company info
- User explicitly requests "search for X"
- AI needs more context to answer accurately

**Parameters:**
- `query` (string, required): Search query in natural language
- `filters` (object, optional): Filter by document type, date, etc.
- `max_results` (int, optional): Number of results to return, default: 5

**Returns:**
```json
{
  "results": [
    {
      "document_id": "doc_123",
      "title": "Remote Work Policy",
      "excerpt": "...relevant text snippet...",
      "relevance_score": 0.92,
      "source": "/policies/remote-work.pdf"
    }
  ],
  "total_found": 12
}
```

**JSON Schema:**
```json
{
  "name": "search_documents",
  "description": "Search the company knowledge base for documents matching a query. Returns relevant excerpts with source citations.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "The search query in natural language, e.g. 'remote work policy' or 'vacation days'"
      },
      "filters": {
        "type": "object",
        "properties": {
          "document_type": {
            "type": "string",
            "enum": ["policy", "procedure", "announcement", "guide"],
            "description": "Filter by document category"
          },
          "after_date": {
            "type": "string",
            "description": "ISO date string, only return docs updated after this date"
          }
        }
      },
      "max_results": {
        "type": "integer",
        "description": "Maximum number of results to return",
        "default": 5,
        "minimum": 1,
        "maximum": 20
      }
    },
    "required": ["query"]
  }
}
```

**Safety Considerations:**
- Sanitize query to prevent injection attacks
- Check user has permission to access returned documents
- Log all searches for audit trail
- Rate limit: 30 searches/minute per user
````

#### Step 3: Define Function Execution Flow

Show the **loop** that makes function calling work:

```markdown
### Function Calling Flow

1. **User Query** → AI receives message
2. **AI Decision** → Determines if function call needed
3. **Function Call** → AI generates function name + parameters (JSON)
4. **YOUR CODE executes the function** → Hits database/API
5. **Function Result** → You send result back to AI (JSON)
6. **AI Response** → AI synthesizes final answer with function data
7. **User sees result** → Natural language response with citations

**Critical Point:** The LLM does NOT run your code. It just tells you WHICH function to call and with WHAT parameters. YOU execute it.
```

---

## 📊 Part 4: Pydantic Models (30 minutes)

### Why Pydantic?

Structured outputs eliminate this:
```python
# 😱 Fragile parsing
response = "The contact is John Smith, john@example.com, 555-1234"
# Now write regex to extract... hope format doesn't change...
```

And give you this:
```python
# ✅ Guaranteed structure
contact = Contact(
    name="John Smith",
    email="john@example.com", 
    phone="555-1234"
)
```

### Your Pydantic Models

Create `docs/week-5/pydantic-models.py`

**For EACH major data structure in your project, create a Pydantic model.**

#### Example Models

````python
from pydantic import BaseModel, EmailStr, Field
from typing import List, Literal, Optional
from datetime import datetime

# ========================================
# USER MODELS
# ========================================

class UserProfile(BaseModel):
    """User profile information"""
    name: str = Field(description="User's full name")
    email: EmailStr = Field(description="User's email address")
    age: int = Field(ge=13, le=120, description="User's age, must be 13+")
    interests: List[str] = Field(description="List of user interests")
    account_type: Literal["free", "pro", "enterprise"] = Field(
        description="User's subscription tier"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "name": "Jane Smith",
                "email": "jane@example.com",
                "age": 25,
                "interests": ["AI", "programming", "music"],
                "account_type": "pro"
            }
        }

# ========================================
# DOCUMENT ANALYSIS MODELS
# ========================================

class DocumentExtraction(BaseModel):
    """Structured data extracted from a document"""
    title: str = Field(description="Document title")
    author: Optional[str] = Field(None, description="Document author if available")
    date: Optional[datetime] = Field(None, description="Publication date")
    summary: str = Field(description="3-5 sentence summary")
    key_topics: List[str] = Field(description="Main topics discussed")
    sentiment: Literal["positive", "neutral", "negative"] = Field(
        description="Overall sentiment"
    )
    
# ========================================
# SEARCH RESULT MODELS
# ========================================

class SearchResult(BaseModel):
    """Single search result with source"""
    document_id: str
    title: str
    excerpt: str = Field(description="Relevant excerpt from document")
    relevance_score: float = Field(ge=0.0, le=1.0)
    source: str = Field(description="File path or URL")
    
class SearchResponse(BaseModel):
    """Complete search response with multiple results"""
    query: str
    results: List[SearchResult]
    total_found: int
    search_time_ms: float

# ========================================
# FUNCTION CALL MODELS
# ========================================

class OrderStatusCheck(BaseModel):
    """Parameters for checking order status"""
    order_id: str = Field(pattern=r"^[A-Z0-9]{5,10}$", description="Order ID (5-10 alphanumeric characters)")
    
class OrderDetails(BaseModel):
    """Order status information"""
    order_id: str
    status: Literal["pending", "processing", "shipped", "delivered", "cancelled"]
    created_at: datetime
    estimated_delivery: Optional[datetime] = None
    tracking_number: Optional[str] = None
    items: List[str]
    total: float = Field(ge=0)

# ========================================
# ERROR MODELS
# ========================================

class ErrorResponse(BaseModel):
    """Standardized error response"""
    error_code: str
    error_message: str
    details: Optional[dict] = None
    timestamp: datetime = Field(default_factory=datetime.now)

# ========================================
# USAGE EXAMPLES
# ========================================

if __name__ == "__main__":
    # Example 1: Create a user profile
    user = UserProfile(
        name="John Doe",
        email="john@example.com",
        age=30,
        interests=["sports", "cooking"],
        account_type="free"
    )
    print(user.model_dump_json(indent=2))
    
    # Example 2: Parse AI output into structured format
    ai_output = {
        "order_id": "ABC12345",
        "status": "shipped",
        "created_at": "2025-10-25T10:00:00Z",
        "estimated_delivery": "2025-11-02T17:00:00Z",
        "tracking_number": "1Z999AA1",
        "items": ["Widget A", "Gadget B"],
        "total": 149.99
    }
    order = OrderDetails(**ai_output)
    print(f"Order {order.order_id} status: {order.status}")
    
    # Example 3: Validation catches errors
    try:
        bad_user = UserProfile(
            name="Kid",
            email="not-an-email",
            age=10,  # Too young!
            interests=[],
            account_type="premium"  # Invalid tier!
        )
    except Exception as e:
        print(f"Validation error: {e}")
````

### Why These Models Matter

**For Week 6 Function Calling:**
- Define what your functions return
- Automatic validation
- Type safety

**For AI-Assisted Development:**
- Cursor/Lovable/Replit will see these schemas
- Generate correct code automatically
- Catch errors at development time, not runtime

---

## ✅ Completion Checklist

Use this to verify you're done:

### PRD (`prd-full.md`)
- [ ] All 18 sections completed
- [ ] Technology versions specified (not "latest")
- [ ] Architecture diagram included (Mermaid or image)
- [ ] At least 3 architectural decisions justified
- [ ] Setup steps are copy-pasteable commands
- [ ] Security & performance requirements quantified

### RAG Strategy (`rag-strategy.md`)
- [ ] Knowledge sources identified (what data?)
- [ ] RAG architecture chosen and justified
- [ ] Embedding model + vector DB specified
- [ ] Chunking strategy defined
- [ ] Citation format shown with example
- [ ] OR justified why RAG isn't needed

### Functions Spec (`functions-spec.md`)
- [ ] 2-3 functions identified
- [ ] Each function has complete JSON schema
- [ ] Parameter types and validation rules clear
- [ ] Return structures documented
- [ ] Safety considerations addressed
- [ ] Example usage shown for each function

### Pydantic Models (`pydantic-models.py`)
- [ ] At least 3 Pydantic models defined
- [ ] Field descriptions provided
- [ ] Validation rules included (ranges, patterns)
- [ ] Example data in Config class
- [ ] Models align with function specs

### Repository Structure
```
your-repo/
├── docs/
│   └── week-5/
│       ├── prd-full.md
│       ├── rag-strategy.md
│       ├── functions-spec.md
│       └── pydantic-models.py
└── README.md (updated with Week 5 progress)
```

---

## 🎓 Instructor Support

### Office Hours This Week
**CRITICAL:** Come to office hours if you need help with:
- Choosing the right RAG architecture for your project
- Determining which functions your system needs
- Understanding Pydantic validation

**Times:** [See syllabus]

### Common Pitfalls

❌ **"We'll figure out the tech stack later"**  
✅ Specify versions NOW. Cursor needs exact dependencies.

❌ **"Our function will 'handle orders'"**  
✅ Be specific: `check_order_status(order_id: str) → OrderDetails`

❌ **"We might need RAG"**  
✅ Decide now. Yes with specific vector DB, or No with alternative approach.

❌ **Vague descriptions: "AI helps users"**  
✅ Precise: "AI searches 50 policy PDFs, returns top 5 matches with citations"

---

## 🚀 Next Steps

### Preparing for Week 6 Lab
You'll implement your functions! Bring:
- Your functions-spec.md
- Your pydantic-models.py
- A working Python environment

### Quiz Prep
Week 5 quiz covers Weeks 1-5 (RAG, embeddings, vector search)

### Thursday Lab Preview
We'll implement one of your functions together using the OpenAI function calling API. Make sure your specs are ready!

---

## 📚 Resources

### PRD Examples
- [Google Docs PRD Template](https://docs.google.com/document/d/1-example)
- [Notion PRD Example](https://notion.so/example)

### RAG Resources
- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)
- [Pinecone Chunking Guide](https://www.pinecone.io/learn/chunking-strategies/)
- [OpenAI Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)

### Function Calling
- [OpenAI Function Calling Docs](https://platform.openai.com/docs/guides/function-calling)
- [Anthropic Tool Use (Claude)](https://docs.anthropic.com/claude/docs/tool-use)

### Pydantic
- [Pydantic Docs](https://docs.pydantic.dev/)
- [Pydantic with OpenAI](https://platform.openai.com/docs/guides/structured-outputs)

---

**Remember:** Your PRD is not just a document—it's the blueprint that will guide every line of code you write (or AI writes for you) for the rest of the semester. Invest the time now!
