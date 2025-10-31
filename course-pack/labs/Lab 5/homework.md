# Combined Homework: Week 4 + Week 5

**Course:** Building AI-Powered Applications
**Due:** Friday, November 7, 2025 by 23:59 Asia/Tbilisi
**Submit:** Push to GitHub. Post the repo link on the LMS.

---

## 📜 Scope

This is **one combined submission** that must include all deliverables for both Week 4 and Week 5.

## 📊 Grading

* **Total:** 20 points
* **Lab 4 (Design Review Milestone):** 5 points
* **Lab 5 (PRD and Technical Specs):** 15 points

---

## 📁 Repo Layout

Your repository for this homework must follow this exact structure

│   ├── week-4/

│   │   ├── capstone-proposal-v2.md

│   │   ├── feature-roadmap.md

│   │   ├── architecture-v2.png

│   │   ├── architecture-explanation.md

│   │   ├── evaluation-plan-v2.md

│   │   ├── cost-model-v2.md

│   │   ├── backlog-v2.md

│   │   └── team-health-week4.md

│   └── week-5/

│       ├── prd-full.md

│       ├── rag-strategy.md

│       ├── functions-spec.md

│       └── pydantic-models.py

---

## 🎯 Lab 4 Deliverables (All Required)

All files must be placed inside the `docs/week-4/` directory.

* `capstone-proposal-v2.md`
    * Sharpen problem statement with user input.
    * Update architecture to reflect Weeks 3-4 learnings.
    * Add measurable success criteria.
    * Refresh risks and timeline.
    * Add Week 3-4 learnings, decisions log, and open questions.
* `feature-roadmap.md`
    * Use AI to list pillars and tasks.
    * Mark features as **MVP** vs. **Later**.
    * Add a simple timeline.
* `architecture-v2.png` and `architecture-explanation.md`
    * Show components, data flow, versions, external services, auth, and failure paths.
    * Add latency targets where relevant.
    * Explain **all changes** since Week 2 and **why** they were made.
* `evaluation-plan-v2.md`
    * **Metrics:** product, technical, and business.
    * **Methods:** golden set, user tests, regression tests.
    * **Schedule:** A clear plan through Week 15.
    * **Tools:** Define tools for logging and feedback.
* `cost-model-v2.md`
    * Current usage baseline.
    * Projections and peak/edge cases.
    * **Savings plan:** model mix, prompt trimming, caching, batching.
    * Budget for the term.
* `backlog-v2.md`
    * Prioritize items: **P1** (critical path), **P2** (high value), **P3** (later).
    * Each item must have: user story, acceptance checks, tech notes, effort, owner, dependencies, and "done" rules.
* `team-health-week4.md`
    * What works well?
    * What needs improvement?
    * Any updates to your team contract?
    * Risk mitigation steps.

---

## 🚀 Lab 5 Deliverables (All Required)

All files must be placed inside the `docs/week-5/` directory.

* `prd-full.md`
    * Must use this 18-section outline:
        1.  Goal and Core Problem
        2.  MVP Scope and Features
        3.  Target Users
        4.  **Tech Stack (with versions)**
        5.  High-Level Architecture (add a simple Mermaid diagram or link image)
        6.  Components and Modules
        7.  Key UI and UX Points
        8.  Coding Standards and Quality
        9.  Testing Strategy
        10. Initial Setup Steps
        11. Architectural Decisions
        12. Documentation Plan
        13. Repository Link
        14. Dependencies and Services
        15. Security
        16. Performance Targets
        17. Monitoring and Observability
        18. Deployment and DevOps
    * **Keep versions explicit.** (e.g., Python `3.11.4`, FastAPI `0.104.1`, React `18.2.0`)
* `rag-strategy.md`
    * **Knowledge Sources:** Path/table, size, update frequency.
    * **Approach:** Traditional, hybrid, or none, and **why**.
    * **Implementation:** Embeddings model, vector store, chunking strategy, `K` value, similarity threshold, reranking (if any).
    * **Citations:** Format for citations.
    * If **no RAG**, explain your alternative data access plan clearly.
* `functions-spec.md`
    * Define 2-3 core functions.
    * **For each function:** purpose, when to call, params, returns, full **JSON schema**, example call, and safety notes.
    * Include a summary of the function-calling flow.
* `pydantic-models.py`
    * Define at least 3 Pydantic models.
    * Include field rules (e.g., `Field(...)`) and examples.
    * Models should align with your function inputs and outputs.

---

## 💡 Setup Hints

* **Coding Standards:** Use PEP 8 and Airbnb standards.
    * **Linters/Formatters:** Black and Prettier. Ruff and ESLint.
* **PRD Setup Steps:** Initial setup steps in the PRD should be copy-paste ready for a new developer.
* **Targets:** Quantify your performance and security targets (e.g., "P95 latency < 500ms", "scan dependencies with Snyk on every commit").

---

## ✨ Optional: Lovable Setup for Scaffolding

1.  Team lead creates an account at `lovable.dev`.
2.  **Plan:** Pro Plan 1
3.  **Code:** `KIUEDU` (for 100 credits for one month)
4.  Add billing details. **You must cancel before the month ends to avoid charges.**

---

## ✅ Checklist Before Submitting

### Week 4
- [ ] `capstone-proposal-v2.md`: Updated with learnings and decisions.
- [ ] `feature-roadmap.md`: Includes pillars and clear MVP scope.
- [ ] `architecture-v2.png` / `architecture-explanation.md`: Diagram and text are updated and match.
- [ ] `evaluation-plan-v2.md`: Contains clear metrics and a schedule.
- [ ] `cost-model-v2.md`: Has baseline, forecast, and savings plan.
- [ ] `backlog-v2.md`: Items are prioritized and have "done" rules.
- [ ] `team-health-week4.md`: Honest check-in added.

### Week 5
- [ ] `prd-full.md`: All 18 sections complete, with **exact versions**.
- [ ] `rag-strategy.md`: Strategy or clear alternative is defined.
- [ ] `functions-spec.md`: Includes JSON schemas and safety notes.
- [ ] `pydantic-models.py`: Models are defined and align with functions.

---

## ❗ Rules

1.  **One push** with all files by the deadline.
2.  No partial submissions will be graded.
3.  Use plain language and **exact versions** for all software.
4.  Keep all file paths exactly as listed in the `Repo Layout` section.

### Grading Notes
* Depth over fluff.
* Clear decisions with documented tradeoffs will score higher than vague claims.
* Working setup steps and measurable targets are critical for a good score.
