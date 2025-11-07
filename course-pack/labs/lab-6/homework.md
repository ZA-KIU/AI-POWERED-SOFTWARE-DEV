# Lab 6 Homework Assignment: Sprint 1 Delivery

**Building AI-Powered Applications | Due: End of Week 6**

---

## Overview

This is your first major development sprint. You're transforming your PRD and architecture into working code. By the end of this week, you must have a **testable, demonstrable MVP** that combines RAG retrieval with function calling to solve your users' core problem.

**Points:** 15 (part of Capstone Project's 25 points)  
**Due Date:** [Check course calendar - typically Friday 11:59 PM]  
**Submission:** Via course LMS with links to Lovable, GitHub, and demo video

---

## Core Requirements

### 1. MVP Prototype (4 points)

#### What You Must Build:

**Minimum Viable Prototype Requirements:**
- [ ] **One complete user flow works end-to-end**
  - User inputs query/request
  - System retrieves relevant context (RAG)
  - System calls appropriate function(s)
  - System returns structured, cited response
  
- [ ] **RAG/Hybrid RAG implementation**
  - Document corpus embedded and indexed
  - Vector similarity search operational
  - Top-k retrieval (minimum k=3)
  - Source citations included in responses
  
- [ ] **Function calling integration**
  - Minimum 2 functions defined
  - JSON schemas properly structured
  - Pydantic validation on all parameters
  - Complete execution loop
  
- [ ] **Basic UI**
  - Input field for user queries
  - Display area for AI responses
  - Loading state indicator
  - Error message display
  
- [ ] **Deployed and accessible**
  - Live on Lovable.dev or equivalent
  - Public URL provided
  - Instructor can access without credentials (or guest credentials provided)

#### Quality Bar:

**Excellent (4/4):**
- All requirements met flawlessly
- Handles edge cases gracefully
- Professional UX with clear feedback
- Fast response times (<5s typical)
- Code is clean and well-organized

**Good (3/4):**
- All requirements met
- Some edge cases not handled
- Basic but functional UX
- Response times acceptable
- Code is readable

**Acceptable (2/4):**
- Core functionality works but inconsistent
- Missing some citations or validation
- Minimal UI with rough edges
- Some errors not handled
- Code needs cleanup

**Needs Revision (1/4):**
- Core functionality partially works
- Major bugs or missing features
- UI barely functional
- Many errors
- Code is messy

---

### 2. RAG Implementation (4 points)

#### Detailed Requirements:

**Document Processing:**
- [ ] Chunking strategy implemented
  - Chunk size: 300-800 tokens (justify your choice)
  - Overlap: 20-50 tokens for context preservation
  - Metadata preserved (source, page, section, etc.)
  
- [ ] Embedding generation
  - Model used (e.g., text-embedding-3-small, all-MiniLM-L6-v2)
  - Dimensions documented
  - Cost per embedding calculated
  
- [ ] Vector storage
  - Technology choice documented (FAISS, Pinecone, Qdrant, pgvector, Weaviate)
  - Index structure explained
  - Retrieval latency measured

**Retrieval Pipeline:**
- [ ] Query embedding generation
- [ ] Similarity search with configurable top-k
- [ ] Re-ranking or filtering (optional but recommended)
- [ ] Context assembly for LLM prompt

**Response Generation:**
- [ ] Retrieved chunks integrated into system prompt
- [ ] Source attribution included
- [ ] Citation format consistent (e.g., [Source: doc_name, page X])
- [ ] Fallback handling when no relevant context found

#### What to Document:

In your sprint report, include:
```markdown
## RAG Configuration

**Documents:**
- Total documents indexed: [X]
- Total chunks created: [Y]
- Average chunk size: [Z tokens]
- Embedding model: [model name]
- Vector database: [technology]

**Performance:**
- Average retrieval time: [X ms]
- Average embedding cost: [$X per query]
- Retrieval accuracy (informal testing): [X/10 relevant]

**Example Queries:**
1. Query: "[example]"
   - Retrieved chunks: [Y]
   - Sources cited: [Z]
   - Response quality: [Good/Fair/Poor]
```

---

### 3. Function Calling Integration (4 points)

#### Detailed Requirements:

**Function Definitions:**
- [ ] Minimum 2 functions, maximum 5
- [ ] Each function has:
  - Clear, specific name (e.g., `search_knowledge_base`, not just `search`)
  - Comprehensive description for the LLM
  - Well-defined parameter schema
  - Return type specification
  - Example usage documented

**Parameter Validation:**
- [ ] Pydantic models for ALL function parameters
- [ ] Type hints throughout
- [ ] Validation rules (min/max, regex, enum constraints)
- [ ] Helpful error messages
- [ ] Default values where appropriate

**Execution Logic:**
- [ ] Functions actually perform stated action
- [ ] Error handling for failures
- [ ] Timeout handling for slow operations
- [ ] Logging of function calls
- [ ] Return structured, parseable results

**LLM Integration:**
- [ ] Tool schemas properly formatted for your LLM provider
- [ ] Tool choice logic implemented (auto/required/none)
- [ ] Function call detection working
- [ ] Result passing back to LLM for final response
- [ ] Multi-turn conversation support (if function needs follow-up)

#### Example Function Specification:

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class DocumentType(str, Enum):
    PDF = "pdf"
    MARKDOWN = "markdown"
    HTML = "html"
    ALL = "all"

class SearchKnowledgeBase(BaseModel):
    """
    Search the knowledge base for relevant documents using semantic search.
    Use this when the user asks a question that requires information from our documents.
    """
    query: str = Field(
        description="The search query. Be specific and include key terms."
    )
    limit: int = Field(
        default=5,
        ge=1,
        le=20,
        description="Maximum number of results to return"
    )
    document_type: Optional[DocumentType] = Field(
        default=DocumentType.ALL,
        description="Filter by document type"
    )
    minimum_relevance: float = Field(
        default=0.7,
        ge=0.0,
        le=1.0,
        description="Minimum relevance score (0.0-1.0)"
    )

def search_knowledge_base(params: SearchKnowledgeBase) -> dict:
    """
    Execute knowledge base search with the given parameters.
    
    Returns:
        {
            "results": List[dict],  # Each with keys: text, source, score
            "count": int,
            "query_embedding_time_ms": float,
            "search_time_ms": float
        }
    """
    # Implementation here
    pass
```

#### What to Document:

```markdown
## Function Calling Configuration

**Functions Implemented:**
1. **search_knowledge_base**
   - Purpose: Retrieve relevant documents
   - Parameters: query (str), limit (int, default=5)
   - Returns: List of documents with scores
   - Typical use: User asks question requiring our data

2. **get_user_context**
   - Purpose: Fetch user preferences/history
   - Parameters: user_id (str)
   - Returns: User profile dict
   - Typical use: Personalization

**Integration:**
- LLM Provider: [OpenAI/Anthropic/etc]
- Function call detection: [Automatic/Manual trigger]
- Average function execution time: [X ms]
- Function call success rate: [X/10 successful]
```

---

### 4. Documentation (2 points)

#### Required Documentation:

**Sprint 1 Report** (`docs/sprint-1-report.md`):
- [ ] Sprint goal and what you achieved
- [ ] Features implemented (with evidence)
- [ ] Technical decisions and justifications
- [ ] Challenges faced and how you overcame them
- [ ] Known issues and limitations
- [ ] Metrics (latency, cost, accuracy estimates)
- [ ] Next sprint priorities (Week 7-8)

**Updated PRD** (`docs/capstone-proposal.md`):
- [ ] Reflects any scope changes since Week 2
- [ ] Architecture updated with actual tech stack
- [ ] Success criteria updated with progress indicators
- [ ] Risk assessment updated (what risks materialized?)
- [ ] Timeline adjusted if needed

**README Updates** (root `README.md`):
- [ ] Project description current
- [ ] Setup instructions accurate
- [ ] Environment variables documented in .env.example
- [ ] How to run locally
- [ ] How to deploy
- [ ] Known issues section

**Code Documentation**:
- [ ] Docstrings on all functions
- [ ] Inline comments on complex logic
- [ ] Type hints throughout
- [ ] Configuration documented

---

### 5. Demo Video (1 point)

#### Requirements:

**Format:**
- Length: 2-4 minutes (strict limit)
- Video: Screen recording (Loom, QuickTime, OBS)
- Audio: Voice-over explaining what's happening
- Quality: 720p minimum, clear audio

**Content:**
- [ ] Introduction (10 seconds): Team name, project title
- [ ] Demo (90-180 seconds):
  - Show the ONE core user flow
  - Input a real user query
  - Show RAG retrieval happening (display sources)
  - Show function being called
  - Show final structured response
  - Show error handling (submit invalid input)
- [ ] Technical highlights (30 seconds):
  - Quick code walkthrough of one key component
  - Show your vector database or function definitions
- [ ] Wrap-up (10 seconds):
  - What's next in Sprint 2
  - Link to try it yourself

**Delivery:**
- Upload to YouTube or Vimeo (unlisted is fine)
- Add captions/subtitles (optional but recommended)
- Include link in submission

---

## Submission Checklist

Before submitting, verify ALL of these:

### Code & Deployment
- [ ] Code pushed to GitHub (main branch)
- [ ] All Sprint 1 GitHub issues closed
- [ ] Sprint 2 issues created for Week 7-8
- [ ] No sensitive data in repository (API keys, passwords)
- [ ] .gitignore configured properly
- [ ] Dependencies listed (requirements.txt or package.json)
- [ ] Deployed to Lovable.dev (or equivalent)
- [ ] Live URL accessible
- [ ] Instructor has access (or guest credentials provided)

### Documentation
- [ ] `docs/sprint-1-report.md` complete
- [ ] `docs/capstone-proposal.md` updated
- [ ] Root `README.md` updated
- [ ] Code has docstrings and comments
- [ ] `.env.example` file present

### Deliverables
- [ ] Demo video recorded and uploaded
- [ ] Video link accessible (test in incognito window)
- [ ] All links in submission form work

### Testing
- [ ] Tested one complete user flow successfully
- [ ] Tested error handling (bad inputs)
- [ ] Tested on different device/browser
- [ ] Verified all citations work
- [ ] Verified all functions execute

---

## Submission Format

Submit via course LMS with the following information:

```
Team Name: [Your Team Name]
Project Title: [Your Project Title]

=== LINKS ===
Lovable Project: [URL with access for zeshan.ahmad@kiu.edu.ge]
GitHub Repository: [URL]
Live MVP Deployment: [URL]
Demo Video: [YouTube/Vimeo URL]

=== SPRINT 1 SUMMARY ===
Sprint Goal: [1-2 sentence description]

Features Implemented:
- RAG: [Specific implementation details]
- Functions: [Which functions, what they do]
- Other: [Any additional features]

Core User Flow:
[Describe the ONE flow that works end-to-end]

Known Issues:
- [Issue 1]
- [Issue 2]

=== TEAM INFO ===
Team Members:
- [Name 1] - [Role] - [GitHub username]
- [Name 2] - [Role] - [GitHub username]  
- [Name 3] - [Role] - [GitHub username]

Time Invested:
- Planning: [X hours]
- Coding: [Y hours]
- Documentation: [Z hours]
- Total: [Total hours]

=== OPTIONAL BONUSES ===
[ ] Streaming responses implemented
[ ] Advanced error recovery
[ ] User authentication
[ ] Testing suite
[ ] Exceptional UI/UX
[ ] Other: [Describe]
```

---

## Grading Rubric

| Component | Points | Excellent (100%) | Good (75%) | Acceptable (50%) | Needs Work (<50%) |
|-----------|--------|------------------|------------|------------------|-------------------|
| **MVP Prototype** | 4 | All requirements met, polished, handles edge cases | All requirements met, minor issues | Core functionality works, some gaps | Many issues, incomplete |
| **RAG Implementation** | 4 | Perfect retrieval, citations, performance documented | Good retrieval, citations work, basic docs | Retrieval works inconsistently | Poor retrieval quality |
| **Function Calling** | 4 | 3+ functions, perfect integration, Pydantic validation | 2 functions, good integration | Functions work but rough integration | Functions barely work |
| **Documentation** | 2 | Comprehensive, clear, professional | Complete, readable | Minimal but sufficient | Missing key sections |
| **Demo Video** | 1 | Professional, engaging, clear | Clear demonstration | Functional demo | Poor quality or incomplete |

**Total: 15 points**

**Bonus Points** (up to +3):
- Streaming responses: +1
- User authentication/sessions: +1
- Comprehensive testing: +1
- Advanced error recovery: +1
- Exceptional UI/UX: +1
- Other impressive features: +0.5 each

---

## Late Submission Policy

- **0-24 hours late:** -10% (1.5 points)
- **24-48 hours late:** -25% (3.75 points)
- **48-72 hours late:** -50% (7.5 points)
- **>72 hours late:** Requires instructor approval, may not be accepted

**Extensions:** Must be requested 48+ hours before deadline with valid reason. Medical/family emergencies accommodated with documentation.

---

## Common Mistakes to Avoid

### Technical Issues:
1. **Environment variables not set** - Always use .env files, never hardcode keys
2. **CORS errors** - Configure your backend properly for cross-origin requests
3. **Vector search returning gibberish** - Check your embedding model matches index
4. **Function not being called** - Make descriptions extremely clear and specific
5. **Pydantic validation failing silently** - Log validation errors to debug

### Project Issues:
1. **Scope too large** - Cut features ruthlessly to get ONE flow working
2. **Waiting until last minute** - Start coding immediately after lab
3. **Not testing incrementally** - Test each piece as you build it
4. **Poor Git hygiene** - Commit often with meaningful messages
5. **No error handling** - Always handle errors gracefully

### Documentation Issues:
1. **README doesn't match reality** - Keep it updated as you develop
2. **Sprint report too vague** - Be specific with examples and metrics
3. **No code comments** - Future you (next week) will hate current you
4. **Demo video too long** - Edit ruthlessly, stay under 4 minutes
5. **Forgetting to update PRD** - Show how your thinking evolved

---

## Getting Unstuck

### If you're stuck for >1 hour on a technical issue:

1. **Search the error message** - Likely someone solved it on Stack Overflow
2. **Read the docs** - Official documentation usually has the answer
3. **Try the simplest version** - Remove complexity until it works
4. **Ask your team** - Fresh eyes help
5. **Ask in course forum** - Peer help is fastest
6. **Email instructor** - Provide specific error messages and code snippets

### If your team is stuck on scope/decisions:

1. **Review your sprint goal** - Does this decision support it?
2. **Cut features** - When in doubt, cut
3. **Make a decision and move forward** - Perfect is the enemy of done
4. **Document why** - Explain your reasoning for future reference

---

## Sprint 1 Success Stories

### What "Good" Looks Like:

**Team A: Student Assistant Chatbot**
- RAG implementation: Indexed 50 PDFs (course materials), chunked with 500 token chunks
- Functions: `search_course_materials()`, `check_assignment_status()`
- Demo: Student asks "When is the midterm?" → Searches syllabus → Returns date with citation
- Notable: Implemented confidence scores, only returns answers with >0.7 relevance

**Team B: Recipe Recommendation System**
- RAG implementation: 1000 recipes embedded, metadata filters (dietary restrictions)
- Functions: `search_recipes()`, `get_nutritional_info()`, `save_to_favorites()`
- Demo: "Find me a vegan dinner under 30 minutes" → Searches, filters, returns 3 recipes
- Notable: Hybrid search (keyword + semantic) improved results 40%

**Team C: Legal Document Analyzer**
- RAG implementation: 200 legal documents, hierarchical chunking (section-aware)
- Functions: `analyze_contract()`, `find_precedents()`
- Demo: Upload contract → Identifies key clauses → Flags potential issues with citations
- Notable: Uses GPT-4 for analysis, GPT-3.5-turbo for search (cost optimization)

---

## Resources

### Official Documentation:
- [Lovable.dev Docs](https://lovable.dev/docs)
- [OpenAI Function Calling](https://platform.openai.com/docs/guides/function-calling)
- [Anthropic Claude Tools](https://docs.anthropic.com/claude/docs/tool-use)
- [Pydantic V2 Documentation](https://docs.pydantic.dev/2.0/)
- [FAISS Wiki](https://github.com/facebookresearch/faiss/wiki)

### Tutorials:
- [RAG from Scratch](https://youtube.com/watch?v=sVcwVQRHIc8) (video)
- [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/)
- [Function Calling Best Practices](https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models)

### Tools:
- [Loom](https://loom.com) - Quick screen recording
- [draw.io](https://draw.io) - Architecture diagrams
- [Postman](https://postman.com) - API testing
- [Insomnia](https://insomnia.rest) - API testing alternative

---

## Looking Ahead: Week 7

Next week you'll:
- Conduct **first user testing** with your MVP
- Implement **streaming responses** for better UX
- Add **real-time conversational state management**
- Begin **Sprint 2** based on user feedback

**Prepare for Week 7:**
- Recruit 3-5 test users from your target audience
- Prepare test scenarios and observation script
- Set up analytics/logging to track user behavior
- Create feedback form

---

## Final Reminders

1. **This is a sprint, not a marathon** - Ship something working, iterate later
2. **Communication is key** - Daily standups with your team
3. **Document as you go** - Don't leave it for the night before
4. **Test, test, test** - Every component, every integration
5. **Ask for help early** - Don't waste days on blockers

**You've got this!** By the end of this week, you'll have transformed your idea into a working prototype. That's a huge accomplishment. Focus on making ONE thing work really well, and you'll be set up perfectly for user testing in Week 7.

Good luck! 🚀

---

**Questions?** Post in course forum or email zeshan.ahmad@kiu.edu.ge
