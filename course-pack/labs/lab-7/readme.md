LAB 7: DESIGN REVIEW & TECHNICAL VALIDATION
Complete Package for AI-Powered Software Development Course

=============================================================================
CONTENTS
=============================================================================

This archive contains all materials for Week 7 Lab - the critical validation
checkpoint before Week 8 agent orchestration.

TOTAL: 11 files organized in clear structure

=============================================================================
FILE STRUCTURE
=============================================================================

lab-7/
├── README.md                           # Lab overview (STUDENTS READ FIRST)
├── homework-assignment.md              # Submission requirements (10 pages)
│
├── templates/                          # Students copy these
│   ├── design-review-template.md      # Main deliverable (8 pages)
│   ├── event-schema-template.md       # JSON schemas (10 pages)
│   └── smoke-test-checklist.md        # Validation tests (6 pages)
│
└── guides/                             # Students learn from these
    ├── event-schema-guide.md          # Schema design (4 pages)
    ├── performance-baseline-guide.md   # Performance measurement (5 pages)
    └── hypothesis-validation-guide.md  # Testing assumptions (6 pages)

=============================================================================
QUICK START
=============================================================================

1. EXTRACT THE ARCHIVE
   
   On Mac/Linux:
   $ tar -xzf lab-7-complete.tar.gz
   
   On Windows:
   - Right-click lab-7-complete.tar.gz
   - Extract with 7-Zip or WinRAR
   
   This creates a "lab-7" folder with all materials.

2. FOR INSTRUCTORS
   
   a) Read instructor-script.md FIRST (18 pages, worth it!)
   b) Review student GitHub repos before lab
   c) Follow script minute-by-minute during lab
   d) Grade using rubric.md after lab
   
3. FOR STUDENTS
   
   a) Read README.md to understand the lab
   b) Review homework-assignment.md for requirements
   c) Copy templates/ to your project docs/ folder
   d) Follow guides/ when building your deliverable

=============================================================================
KEY CONCEPTS
=============================================================================

This lab is a FORCING FUNCTION that:
   ✓ Validates students have working code (not just proposals)
   ✓ Documents event schemas (prevents debugging nightmares)
   ✓ Executes smoke tests (proves functionality)
   ✓ Measures performance (establishes baselines)
   ✓ Tests hypotheses (validates assumptions with data)
   ✓ Assesses readiness (honest evaluation before complexity)

WHY IT MATTERS:
   - Agent loops (Week 8) amplify problems 5-20x
   - Better to find issues now while system is simple
   - Catches red flags before students waste weeks

GRADING PHILOSOPHY:
   - Rewards honesty over perfection
   - Requires evidence over claims
   - Values documentation quality
   - Partial credit available for good faith effort

=============================================================================
WHAT STUDENTS SUBMIT
=============================================================================

Main deliverable: docs/design-review-week7.md containing:

   1. Architecture Validation (1-2 pages)
      - Updated architecture diagram
      - Component descriptions
      - Changes from Week 2 proposal
   
   2. Event Schema Documentation (2-3 pages)
      - JSON schemas for all events
      - Example instances
      - Validation rules
   
   3. Smoke Test Results (1-2 pages)
      - Pass/fail for each test
      - Evidence (logs, screenshots)
      - Mitigation plans for failures
   
   4. Performance Baseline (1 page)
      - Latency measurements (p50, p95, p99)
      - Token usage analysis
      - Cost calculations
   
   5. Hypothesis Validation (1-2 pages)
      - One tested assumption
      - Methodology and results
      - Implications for Week 8
   
   6. Readiness Assessment (1 page)
      - Can system handle agent complexity?
      - What must be fixed?
      - Action plan with deadlines

GRADING: 5 points (out of 25 total Capstone points)

=============================================================================
LAB SESSION STRUCTURE
=============================================================================

Total time: 2 hours

   0:00-0:05  | Introduction & Expectations
   0:05-0:35  | Team Demonstrations (5 min each)
   0:35-1:20  | Event Schema Workshop
   1:20-1:50  | Smoke Test Execution
   1:50-2:00  | Wrap-up & Readiness Assessment

CRITICAL: Instructor validates actual working demos, not slides.

=============================================================================
SUCCESS METRICS
=============================================================================

This lab succeeds if:
   ✓ Every team attempts a working demo
   ✓ Students document event schemas precisely
   ✓ Smoke tests reveal issues (that's GOOD!)
   ✓ Teams know what to fix before Week 8
   ✓ Instructor catches red flags early

This lab fails if:
   ✗ Students fake demos without running code
   ✗ No honest assessment of gaps
   ✗ Teams leave not knowing readiness
   ✗ Problems hidden until Week 10

=============================================================================

=============================================================================
VERSION
=============================================================================

Created: November 2025
For: Building AI-Powered Applications (CS-AI-2025)
Course: Week 7 - Design Review & Technical Validation
Instructor: Professor Zeshan Ahmad
Institution: Kutaisi International University

=============================================================================

Questions? Issues? Improvements?

This is production-tested material. Use it, adapt it, improve it.

Your students will thank you when Week 8 "just works" because they
validated their foundations properly in Week 7.

Good luck with the lab!

=============================================================================
