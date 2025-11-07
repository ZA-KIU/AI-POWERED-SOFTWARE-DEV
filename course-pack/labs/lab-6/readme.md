# Lab 6: Capstone Sprint 1 - MVP Implementation

**Building AI-Powered Applications | Week 6**

---

## Overview

Welcome to Sprint 1 of your capstone development! This week marks a critical transition from planning to implementation. You'll take everything you've learned about RAG (Week 5) and function calling (Week 6) and turn your PRD into working code using Lovable.dev as your development platform.

**What You're Building This Week:**
- First working iteration of your MVP with RAG or hybrid RAG
- Function calling integration for at least 2-3 core actions
- Structured outputs with Pydantic validation
- Basic conversational state management (preview of Week 7)
- Testable, demonstrable prototype

**Why This Lab Matters:**
By Week 7, you'll be doing your first user testing round. You need a functional prototype NOW. This sprint is where your architecture becomes reality.

---

## Learning Objectives

By the end of this lab, you will be able to:

1. **Scaffold a full-stack AI application** using Lovable.dev with proper project structure
2. **Implement RAG or hybrid RAG** that retrieves relevant context and cites sources
3. **Integrate function calling** to give your AI real-world capabilities
4. **Validate structured outputs** using Pydantic models for type safety
5. **Manage conversational state** across multi-turn interactions
6. **Deploy a testable MVP** that can be used for user testing in Week 7

---

## Prerequisites

**Before Lab:**
- [ ] Week 6 lecture content reviewed (function calling, structured outputs, schemas)
- [ ] Your PRD from Week 2 is updated (if needed)
- [ ] Your architecture from Week 4 Design Review is finalized
- [ ] You have identified 2-3 core functions your AI needs
- [ ] You have sample data or documents for RAG testing
- [ ] Lovable.dev account created (free tier is fine)
- [ ] API keys secured (OpenAI, Anthropic, or your chosen LLM)

**Technical Setup:**
```bash
# Install required packages
pip install openai anthropic pydantic python-dotenv requests --break-system-packages

# Or for Node.js projects
npm install openai @anthropic-ai/sdk zod axios dotenv
```

---

## In-Lab Activities (2 Hours)

### Part 1: Sprint Planning & Architecture Review (30 min)

**Objective:** Align as a team on Sprint 1 scope and technical approach.

**Activities:**
1. **Sprint Goal Definition** (10 min)
   - What is the ONE core user flow you're implementing?
   - What does "done" look like by end of week?
   - What are you explicitly NOT building this sprint?

2. **Technical Stack Finalization** (10 min)
   - Confirm: LLM provider, vector database, frontend framework
   - Verify: Everyone has API access and credentials
   - Test: Quick "Hello World" in Lovable.dev

3. **Sprint Backlog Creation** (10 min)
   - Break down your sprint goal into 5-8 tasks
   - Assign tasks to team members
   - Identify dependencies and blockers

**Deliverable:** Sprint backlog in GitHub Issues with "Sprint 1" milestone

---

### Part 2: RAG Pipeline Implementation (45 min)

**Objective:** Build or refine your RAG system with proper chunking, embedding, and retrieval.

**Activities:**

**Step 1: Document Preparation (10 min)**
```python
# Example: Chunking with overlap
from typing import List

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """
    Split text into overlapping chunks for better context preservation.
    """
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    
    return chunks

# Test with your documents
sample_doc = "Your document content here..."
chunks = chunk_text(sample_doc)
print(f"Created {len(chunks)} chunks")
```

**Step 2: Embedding Generation (15 min)**
```python
from openai import OpenAI

client = OpenAI()

def embed_chunks(chunks: List[str]) -> List[List[float]]:
    """
    Generate embeddings for document chunks.
    """
    embeddings = []
    for chunk in chunks:
        response = client.embeddings.create(
            model="text-embedding-3-small",
            input=chunk
        )
        embeddings.append(response.data[0].embedding)
    return embeddings

# Generate and store embeddings
embeddings = embed_chunks(chunks)
```

**Step 3: Vector Store Setup (10 min)**
- Choose: FAISS (local), Pinecone (cloud), or pgvector (PostgreSQL)
- Index your embeddings
- Test retrieval with sample queries

**Step 4: RAG Integration Test (10 min)**
- Query your vector store
- Retrieve top-k most relevant chunks
- Pass to LLM with proper prompt structure
- Verify citations are included

**Deliverable:** Working RAG pipeline that retrieves and cites sources

---

### Part 3: Function Calling Setup (45 min)

**Objective:** Define and implement 2-3 core functions your AI can call.

**Activities:**

**Step 1: Function Identification (10 min)**
Ask: What actions does your AI need to perform?

Examples:
- Search a knowledge base: `search_documents(query: str, limit: int)`
- Fetch user data: `get_user_profile(user_id: str)`
- Perform calculation: `calculate_cost(params: dict)`
- Send notification: `send_email(to: str, subject: str, body: str)`

**Step 2: Function Implementation (20 min)**
```python
from pydantic import BaseModel, Field
from typing import Optional

# Define Pydantic models for type safety
class SearchQuery(BaseModel):
    query: str = Field(description="Search query text")
    limit: int = Field(default=5, ge=1, le=20, description="Number of results")
    filter_type: Optional[str] = Field(default=None, description="Filter by document type")

# Implement function
def search_documents(params: SearchQuery) -> dict:
    """
    Search the document database and return relevant results.
    """
    # Your vector search logic here
    results = perform_vector_search(params.query, params.limit)
    
    return {
        "results": results,
        "count": len(results),
        "query": params.query
    }
```

**Step 3: LLM Integration (15 min)**
```python
# Define function schema for LLM
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_documents",
            "description": "Search the knowledge base for relevant information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of results to return",
                        "default": 5
                    }
                },
                "required": ["query"]
            }
        }
    }
]

# Call LLM with tools
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Find information about X"}],
    tools=tools,
    tool_choice="auto"
)

# Handle function calling
if response.choices[0].message.tool_calls:
    # Execute function and return results
    pass
```

**Deliverable:** 2-3 working functions integrated with your LLM

---

## Homework: Sprint 1 Implementation (Due End of Week 6)

### Required Deliverables

#### 1. Working MVP Prototype
- [ ] Deployed on Lovable.dev (or equivalent platform)
- [ ] At least ONE complete user flow works end-to-end
- [ ] RAG or hybrid RAG retrieves and cites relevant information
- [ ] 2-3 functions integrated and tested
- [ ] Basic error handling implemented

#### 2. Updated PRD & Architecture
- [ ] PRD reflects any scope changes from Week 2
- [ ] Architecture diagram updated with actual tech stack
- [ ] Data flow documented with example requests/responses
- [ ] API endpoints or interaction patterns documented

#### 3. Sprint 1 Report
- [ ] What you built (features implemented)
- [ ] What works (demo scenarios)
- [ ] What doesn't work yet (known issues)
- [ ] What you learned (technical insights)
- [ ] Next sprint plan (Week 7-8 goals)

#### 4. Demo Video
- [ ] 2-3 minute screen recording showing core functionality
- [ ] Voice-over explaining what's happening
- [ ] Shows both success cases and error handling
- [ ] Uploaded to YouTube/Vimeo (unlisted is fine)

#### 5. GitHub Updates
- [ ] Sprint 1 issues closed with proper commit references
- [ ] Sprint 2 issues created for Week 7-8
- [ ] README updated with setup instructions
- [ ] Code is documented and commented

---

## Technical Requirements

### MVP Must Include:

**1. RAG/Hybrid RAG Implementation**
- Document chunking with appropriate overlap
- Embedding generation and storage
- Vector similarity search
- Context integration in prompts
- Source attribution/citations

**2. Function Calling**
- At least 2 functions defined with JSON schemas
- Pydantic models for parameter validation
- Function execution logic
- Result integration back to LLM
- Complete request→function→response loop

**3. Structured Outputs**
- Pydantic models for all data structures
- Response validation
- Type safety throughout
- Error handling for validation failures

**4. Conversational State** (Preview Week 7)
- Multi-turn conversation support
- Message history management
- Context preservation across turns
- Session management (basic)

**5. User Interface**
- Clean, functional UI (doesn't need to be beautiful)
- Input field for user queries
- Display area for responses
- Loading states
- Error messages

---

## Submission Instructions

### What to Submit:

1. **Lovable.dev Project Link**
   - Share access with instructor (zeshan.ahmad@kiu.edu.ge)
   - Ensure project is deployed and accessible

2. **GitHub Repository**
   - Updated with Sprint 1 code
   - Includes `docs/sprint-1-report.md`
   - Issues closed/updated
   - README reflects current state

3. **Demo Video Link**
   - YouTube/Vimeo URL in submission

4. **Deployment URL**
   - Live link to your MVP

### Submission Format:

```
Sprint 1 Submission - [Team Name]

Lovable Project: [URL]
GitHub Repo: [URL]
Demo Video: [URL]
Live MVP: [URL]

Team Members: [Names]
Sprint Goal: [1-sentence description]

Key Features Implemented:
- [Feature 1]
- [Feature 2]
- [Feature 3]

Known Issues:
- [Issue 1]
- [Issue 2]
```

---

## Grading Rubric (15 points total)

| Component | Points | Criteria |
|-----------|--------|----------|
| **RAG Implementation** | 4 | Proper chunking, embedding, retrieval, citations. Works reliably. |
| **Function Calling** | 4 | 2+ functions with schemas, validation, execution, integration. |
| **Structured Outputs** | 2 | Pydantic models used throughout. Type safety. Error handling. |
| **MVP Completeness** | 2 | At least ONE complete user flow works end-to-end. |
| **Documentation** | 2 | Sprint report, updated PRD, code comments, demo video. |
| **Code Quality** | 1 | Clean, readable, follows best practices. Git hygiene. |

**Bonus Points (up to +3):**
- Implements streaming responses (+1)
- Advanced error recovery (+1)
- User authentication/sessions (+1)
- Comprehensive testing suite (+1)
- Exceptional UI/UX (+1)

---

## Common Issues & Troubleshooting

### "My RAG retrieval is returning irrelevant results"
**Causes:** Poor chunking, wrong embedding model, insufficient context
**Solutions:**
- Try different chunk sizes (200-1000 tokens)
- Use better embeddings (text-embedding-3-large)
- Retrieve more chunks (top 5-10)
- Add metadata filters
- Experiment with hybrid search (keyword + semantic)

### "Function calling isn't being triggered"
**Causes:** Unclear function descriptions, missing parameters, model confusion
**Solutions:**
- Make function descriptions extremely specific
- Include examples in descriptions
- Test with explicit "use the X function" prompts
- Verify tool_choice parameter
- Check model supports function calling

### "Pydantic validation keeps failing"
**Causes:** Type mismatches, required fields missing, strict mode issues
**Solutions:**
- Make fields Optional when appropriate
- Provide default values
- Use Field descriptions for clarity
- Log validation errors for debugging
- Test schemas independently

### "Lovable.dev deployment failed"
**Causes:** Environment variables, dependency conflicts, build errors
**Solutions:**
- Check all env vars are set
- Review build logs carefully
- Test locally first
- Simplify dependencies
- Contact Lovable support

---

## Resources

### Templates
- [Sprint Report Template](./templates/sprint-report-template.md)
- [PRD Update Template](./templates/prd-update-template.md)
- [Function Schema Template](./templates/function-schema-template.md)
- [Pydantic Models Template](./templates/pydantic-models-template.md)

### Guides
- [Lovable.dev Setup Guide](./guides/lovable-setup-guide.md)
- [RAG Implementation Guide](./guides/rag-implementation-guide.md)
- [Function Calling Best Practices](./guides/function-calling-guide.md)
- [Pydantic Validation Guide](./guides/pydantic-guide.md)
- [Conversational State Management](./guides/conversation-state-guide.md)

### Examples
- [Example RAG Pipeline](./examples/rag-pipeline-example.py)
- [Example Function Definitions](./examples/function-definitions-example.py)
- [Example Pydantic Models](./examples/pydantic-models-example.py)
- [Example Sprint Report](./examples/sprint-report-example.md)

### External Resources
- [Lovable.dev Documentation](https://lovable.dev/docs)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [Pydantic Documentation](https://docs.pydantic.dev)
- [FAISS Tutorial](https://github.com/facebookresearch/faiss/wiki)
- [LangChain RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)

---

## Looking Ahead

### Week 7: User Testing & Streaming
- First user testing round with your MVP
- Implement streaming responses
- Real-time conversational state management
- Incorporate user feedback

### Week 8: Iteration & Optimization
- Refine based on user testing
- Optimize for latency and cost
- Add missing features
- Prepare for midterm exam

### Week 9: Midterm Exam
- Study week
- Focus on concepts from Weeks 1-8

---

## Getting Help

### During Lab:
- Ask your teammates first
- Flag down instructor or TAs
- Use course Slack/Discord channel

### Outside Lab:
- **Office Hours:** See Week 1 announcement
- **Email:** zeshan.ahmad@kiu.edu.ge (24hr response on weekdays)
- **Course Forum:** Post technical questions
- **Team Hours:** Schedule with your teammates

### Emergency Contacts:
- Technical blocker: Email instructor immediately
- Team conflict: Use your team contract escalation process
- Health/personal issue: Contact instructor privately

---

## Success Tips

1. **Start with the simplest version that works** - You can always add complexity later
2. **Test each component independently** - RAG alone, then functions alone, then together
3. **Commit early and often** - Small, working increments
4. **Use your team's strengths** - Frontend person on UI, backend person on API, AI person on models
5. **Document as you go** - Don't leave it until the last minute
6. **Demo to each other frequently** - Catch issues early
7. **Ask for help when stuck** - Don't waste hours on one problem

**Remember:** Perfect is the enemy of done. Ship something that works, then iterate!

Good luck with Sprint 1! 🚀
