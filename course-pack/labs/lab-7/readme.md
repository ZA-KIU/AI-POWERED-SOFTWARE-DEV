# Lab 7: Design Review & Technical Validation

**Building AI-Powered Applications | Week 7**

## Critical Checkpoint: Before You Build Agent Loops

This lab is a **required validation checkpoint** before Week 8's agent orchestration. You've spent Weeks 3-6 building foundational capabilities (basic LLM integration, multimodal I/O, RAG, function calling). Now you must **prove your foundation is solid** before adding the complexity of multi-step agent workflows.

**Why This Matters:** Agent orchestration (Week 8) will amplify any existing issues by 5-20x. A small latency problem becomes a cascade. A vague data schema becomes chaos. This lab gates you from proceeding until you've validated your architecture works.

---

## Lab Objectives

By the end of this 2-hour lab session, you will:

1. **Demonstrate a working prototype** - Not slides or promises, actual running code from Weeks 3-6
2. **Document event schemas** - Precise JSON contracts for all system interactions
3. **Execute smoke tests** - Prove end-to-end data flow works reliably
4. **Validate one hypothesis** - Use real data to test a core design assumption
5. **Assess readiness** - Determine if your architecture can handle agent complexity

---

## What's Due (Week 7 Homework)

**Deliverable:** Design Review Document (5 points toward Capstone)

**Submission:** Updated GitHub repository with `docs/design-review-week7.md`

**Due:** End of Week 7

See [Homework Assignment](./homework-assignment.md) for complete requirements.

---

## Lab Format (2 Hours)

### Part 1: Team Demonstrations (30 min)
- 3-5 teams present 5-minute working demos
- Instructor validates: "Show me it working right now"
- Peer feedback on architecture choices

### Part 2: Event Schema Workshop (45 min)
- Define JSON schemas for all key system events
- Document data contracts between components
- Validate schema completeness

### Part 3: Smoke Test Execution (30 min)
- Run through validation checklist as a team
- Collect performance baseline measurements
- Document results and gaps

### Part 4: Hypothesis Validation & Refinement (15 min)
- Review one tested design assumption with data
- Identify architecture changes needed before Week 8
- Plan Week 8 readiness tasks

---

## Prerequisites (Complete BEFORE Lab)

You must bring to lab:

### 1. Working Prototype
- **Functional code** from Weeks 3-6 that runs on your laptop
- Not broken, not "almost working" - actually working
- Can demonstrate core functionality live

### 2. Test Data Ready
- Sample inputs prepared (text, images, audio as applicable)
- API keys loaded and validated
- Database populated with test data (if using RAG)

### 3. Logs Collected
- At least 10 example requests with full request/response logs
- Error examples if you have them
- Performance measurements (latency, tokens, cost)

### 4. Initial Event Schemas Drafted
- Start the `docs/event-schemas.md` file
- Draft schemas for your 3-5 most critical events
- Bring questions about schema design

---

## Success Criteria

You're ready for Week 8 if you can answer "YES" to all:

- ✅ Can you demo your app working end-to-end right now?
- ✅ Do you have documented JSON schemas for all key events?
- ✅ Can you show logs from at least 10 successful requests?
- ✅ Do you know your baseline latency and cost per request?
- ✅ Have you validated at least one design assumption with data?
- ✅ Have you identified and planned fixes for critical gaps?

If any answer is "NO" - that's what this lab helps you fix.

---

## Files & Templates

**Templates (Copy These):**
- [Design Review Template](./templates/design-review-template.md) - Main deliverable structure
- [Event Schema Template](./templates/event-schema-template.md) - JSON schema format
- [Smoke Test Checklist](./templates/smoke-test-checklist.md) - Validation checklist

**Guides (Read These):**
- [Event Schema Guide](./guides/event-schema-guide.md) - How to define robust schemas
- [Performance Baseline Guide](./guides/performance-baseline-guide.md) - How to measure correctly
- [Hypothesis Validation Guide](./guides/hypothesis-validation-guide.md) - How to test assumptions

**Grading:**
- [Rubric](./rubric.md) - How the 5-point Design Review is graded

---

## Common Questions

### "Our app isn't finished yet, can we skip this?"

**No.** This lab doesn't require a finished app - it requires a **working foundation**. Even if you only have basic LLM integration working, that's enough to validate schemas and performance.

### "We don't have RAG/functions implemented yet"

**That's fine.** Document the schemas you *will* use, run smoke tests on what you *do* have, and identify what needs to be built.

### "Can we do the smoke test at home?"

**No.** The lab is structured so the instructor can help you debug issues live. Having help available is critical.

### "What if we fail the smoke test?"

**That's actually good.** Better to discover issues now than after building complex agent loops on top.

---

## Final Reminder

**This lab is a forcing function.** It intentionally creates pressure to validate your work before adding complexity. That pressure is productive - it catches problems early when they're easy to fix.

Don't skip the prep work. Don't fake the demo. Don't skip the smoke test.

**You've got this.**
