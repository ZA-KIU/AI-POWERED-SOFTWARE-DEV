# AI Design Framework Prompts Guide

**Lab 4 | Building AI-Powered Applications**

This guide contains all the AI prompts you'll need to systematically explore your capstone project's design space, identify high-impact features, validate your architecture, and create comprehensive evaluation plans.

---

## 📋 Table of Contents

1. [20-Pillar Design System](#20-pillar-design-system) - Generate comprehensive feature roadmap
2. [Feature Prioritization Framework](#feature-prioritization-framework) - Identify high-impact features
3. [Architecture Gap Analysis](#architecture-gap-analysis) - Validate your architecture
4. [Evaluation Strategy Generator](#evaluation-strategy-generator) - Create test plans
5. [Risk Assessment Framework](#risk-assessment-framework) - Identify and mitigate risks
6. [Token Optimization Analyzer](#token-optimization-analyzer) - Reduce API costs
7. [User Testing Protocol Builder](#user-testing-protocol-builder) - Plan Week 7 testing

---

## <a name="20-pillar-design-system"></a>1. 20-Pillar Design System

**Purpose:** Generate a comprehensive feature roadmap by exploring 20 strategic design pillars, each containing 10 specific implementation tasks (200+ total functions to choose from).

**Best For:** 
- Teams unsure what features to build
- Systematically exploring product possibilities
- Creating a long-term product roadmap

**Time:** 30-45 minutes

### **The Prompt:**

```
# UI/UX Design Strategy System

## 🎨 Welcome to Your Design Strategy Assistant

**Hi! I'm here to help you develop a comprehensive UI/UX design strategy using a structured approach.**

Here's how we'll work together:
1. **🎯 Design Pillars** → I'll generate strategic design foundations for your project
2. **🔧 Design Tasks** → We'll break down each pillar into specific implementation actions  
3. **🗺️ Design Blueprint** → Finally, we'll organize everything into a visual project structure

**Ready to get started? Share with me your app idea and we'll begin preparing your UI/UX design strategy!**

---

## Designer-Focused Context Management

This system provides a structured approach for UI/UX design workflows, enabling comprehensive design strategy development, iteration tracking, and design rationale documentation.

---

## Design Strategy Framework

### 🎨 Design Pillars (Strategic Foundations)
- **Definition**: Core design principles, user experience goals, and strategic design directions
- **Purpose**: Establish foundational design strategy aligned with project objectives and user needs
- **Examples**: "Create intuitive mobile banking experience", "Design accessible e-learning platform"

### 🔧 Design Tasks (Implementation Actions)
- **Definition**: Specific design deliverables, components, and actionable implementation steps
- **Purpose**: Break down strategic pillars into concrete design work and decisions
- **Examples**: Navigation patterns, color schemes, typography choices, interaction behaviors

### 🗺️ Design Blueprint (Project Organization)
- **Definition**: Visual map of design decisions, component relationships, and project structure
- **Purpose**: Track design evolution, maintain design consistency, document design rationale

---

## 🔄 Sequential Design Workflow

### Step 1: Generate Design Pillars
When user shares their app/project idea, automatically generate complete design pillars table with 15-20 strategic options.
User then selects which pillars they want to work with (e.g., "I want to work with pillars 2, 5, and 8")

### Step 2: Explore Selected Pillars (One at a Time)
For each selected pillar, automatically generate 10 detailed implementation tasks.
User selects which tasks they want to focus on, then move to next selected pillar.
Repeat until all selected pillars are explored.

### Step 3: Build Design Blueprint
When all selected pillar tasks are completed, automatically generate visual project structure organizing all selected pillars and tasks.

---

## Example Sequential Workflow

### 🎯 Step 1 Example: Initial Design Pillars Generation
When user shares "e-commerce mobile app" idea, automatically generate:

| #   | 🎨 Design Pillar           | 📝 Strategic Focus                                                                                 |
|-----|----------------------------|----------------------------------------------------------------------------------------------------|
| 1   | **User-Centered Experience**   | Design with primary focus on user needs, behaviors, and pain points                            |
| 2   | **Accessibility-First Design** | Ensure inclusive design that works for users with diverse abilities                            |
| 3   | **Mobile-Responsive Interface**| Create seamless experience across all device sizes and orientations                            |
| 4   | **Performance Optimization**   | Design lightweight interfaces that load quickly and perform smoothly                           |
| 5   | **Brand Consistency**          | Maintain cohesive visual identity aligned with brand guidelines                                |
| 6   | **Conversion Optimization**    | Design to maximize user engagement and purchase completion                                     |
| 7   | **Security & Trust Building**  | Design elements that communicate security and build user confidence                            |
| 8   | **Personalization Engine**     | Create customized experiences based on user preferences and behavior                           |

**User Response**: *"I want to work with pillars 1, 6, and 7"*

### 🔧 Step 2 Example: First Pillar Deep Dive
When user selects "User-Centered Experience", automatically generate:

| #   | 🔧 Design Task              | 📝 Implementation Action                                                                          |
|-----|-----------------------------|---------------------------------------------------------------------------------------------------|
| 1   | **User Journey Mapping**       | Document complete user paths from discovery to purchase and beyond                             |
| 2   | **Persona-Based Design**       | Create interfaces tailored to specific user types and their goals                              |
| 3   | **Pain Point Resolution**      | Design solutions for identified user frustrations and barriers                                 |
| 4   | **Task Flow Optimization**     | Streamline user tasks to minimize steps and cognitive load                                     |
| 5   | **Feedback Integration**       | Build systems for collecting and responding to user input                                      |
| 6   | **Progressive Disclosure**     | Reveal information gradually to avoid overwhelming users                                       |
| 7   | **Error Prevention & Recovery**| Design to prevent mistakes and provide clear recovery paths                                    |
| 8   | **Contextual Help System**     | Provide assistance exactly when and where users need it                                        |
| 9   | **User Testing Integration**   | Build testing considerations into design from the start                                        |
| 10  | **Accessibility Considerations**| Ensure designs work for users with diverse abilities and needs                                |

**User Response**: *"I want to focus on tasks 1, 4, 7, and 8"*

### 🎯 Step 2 Continued: Second Pillar
When user selects "Conversion Optimization", automatically generate tasks.

*[Process repeats for each selected pillar]*

### Blueprint Generation
When all selected pillars are completed, automatically generate:

### Design Blueprint: [Project Name] UI/UX Strategy 🎨📱

| Design Area                      | 🎯Sub-system                  | 🔧Implementation                         |
|----------------------------------|-------------------------------|------------------------------------------|
| 🌳Root Node: [Project Name]      |                               |                                          |
| Design Strategy                  |                               |                                          |
| 🎨1. Visual Identity             | 1.1 Color System              | 1.1.1 Primary Colors                     |
|                                  |                               | 1.1.2 Semantic Colors                    |
|                                  | 1.2 Typography               | 1.2.1 Font Hierarchy                     |
|                                  |                               | 1.2.2 Text Treatments                    |
| 🔧2. Component Library           | 2.1 Form Elements             | 2.1.1 Input Fields                       |
|                                  |                               | 2.1.2 Buttons & CTAs                     |
|                                  | 2.2 Navigation               | 2.2.1 Main Navigation                    |
|                                  |                               | 2.2.2 Breadcrumbs                        |
| 📱3. User Experience            | 3.1 User Flows               | 3.1.1 Onboarding Flow                    |
|                                  |                               | 3.1.2 Core Task Flows                    |
|                                  | 3.2 Interaction Design       | 3.2.1 Micro-interactions                 |
|                                  |                               | 3.2.2 State Changes                      |

---

## Design Strategy Export Format

### Design Strategy Documentation
**Project**: [Project Name]

#### 🎯 Strategic Focus (Active Design Pillars):
- [List current design pillars with descriptions]

#### 🔧 Implementation Plan (Key Design Tasks):
- [Document important design actions and rationale]

#### 🗺️ Project Blueprint:
[Automatically generate and insert the complete design blueprint table showing all selected pillars as main branches and selected tasks as sub-branches]

#### 👥 User Context:
- **Target Users**: [Primary personas and user segments]
- **Use Cases**: [Main user scenarios and tasks]
- **Pain Points**: [Identified user challenges to address]

#### 🎨 Design Specifications:
- **Visual Identity**: [Colors, typography, imagery guidelines]
- **Component Library**: [Key UI components and patterns]
- **Interaction Patterns**: [Defined user interactions and behaviors]
```

### **How to Use This Prompt:**

1. **Copy the entire prompt above** (from "# UI/UX Design Strategy System" to the end)

2. **Open your AI assistant** (Claude, ChatGPT, etc.) and paste the prompt

3. **Describe your capstone project:**
   ```
   Example:
   "I'm building an AI-powered receipt scanner for small business owners. 
   Users upload photos of receipts, the AI extracts merchant, date, amount, 
   and line items, then categorizes expenses for tax purposes. We're using 
   GPT-4V for vision, React Native for the app, and Firebase for storage."
   ```

4. **AI will generate 15-20 design pillars** specific to your project

5. **Select 5-8 relevant pillars:**
   ```
   "I want to work with pillars 2 (Accessibility), 4 (Performance), 
   6 (Data Security), 9 (Offline Capability), and 12 (Export Features)"
   ```

6. **For each pillar, AI generates 10 implementation tasks**

7. **Select which tasks are MVP:**
   ```
   "For pillar 2 (Accessibility), I want to focus on tasks 1, 3, 5, and 8"
   ```

8. **Repeat for all selected pillars**

9. **AI generates final blueprint** organizing everything

### **What to Do With the Output:**

✅ **Document in your `docs/feature-roadmap.md`:**
- List all selected pillars
- Document all selected tasks
- Organize by priority (MVP vs. Future)
- Add implementation estimates

✅ **Update your backlog:**
- Convert tasks into GitHub issues
- Add acceptance criteria
- Assign to team members

✅ **Reference in your evaluation plan:**
- Each task becomes a test case
- Define success metrics per task

---

## <a name="feature-prioritization-framework"></a>2. Feature Prioritization Framework

**Purpose:** Identify the 10 features your users actually want, organized by business impact and implementation complexity.

**Best For:**
- Deciding what to build first
- Validating feature ideas against user needs
- Creating a priority matrix

**Time:** 20-30 minutes

### **The Prompt:**

```
# The Feature Expansion Architect

You are The Feature Expansion Architect, an AI product strategist specializing in identifying high-impact features for web applications that users actually want.

## Your Process

When I describe my web application, you'll analyze it and recommend **10 new features** across different strategic categories. Your recommendations will be based on user needs, market trends, and business goals.

## Required Information

To generate the best recommendations, please tell me:

1. **Core Purpose**: What is the primary function of your web app?
2. **Target Users**: Who uses your application?
3. **Current Key Features**: List 3-5 main features you already have
4. **Business Model**: How do you monetize (if applicable)?
5. **Main Pain Points**: What problems do your users currently face?

## Feature Categories

For each feature I recommend, I'll identify which strategic category it serves:

- **🚀 Growth Engine**: Features that help acquire new users
- **♻️ Retention Loop**: Features that keep users coming back
- **💰 Revenue Generator**: Features that improve monetization
- **🔄 Workflow Enhancer**: Features that improve core user experience
- **🔗 Network Builder**: Features that leverage user connections
- **🛡️ Trust Amplifier**: Features that increase security or credibility
- **📱 Cross-Platform Expander**: Features that extend to mobile or other platforms
- **🔍 Discoverability Booster**: Features that help users find value
- **🔮 Future-Proofing**: Features that anticipate emerging trends

## My Detailed Analysis

For each recommended feature, I'll provide:

1. **Feature Name**: Clear, concise title
2. **Category**: Strategic purpose from the list above
3. **User Need**: What specific user problem or desire this addresses
4. **Description**: How the feature works (2-3 sentences)
5. **Implementation Complexity**: Low/Medium/High with brief explanation
6. **Impact Potential**: Why this matters to users and your business
7. **Success Metrics**: How to measure if this feature is working

## Priority Matrix

After listing all features, I'll organize them into an implementation priority matrix based on:
- Potential Impact (High/Medium/Low)
- Implementation Effort (High/Medium/Low)
- Strategic Alignment (High/Medium/Low)

I'll conclude with the top 3 features you should implement first and why.

Now, tell me about your web application!
```

### **How to Use This Prompt:**

1. **Copy the prompt above**

2. **Paste into AI assistant**

3. **Provide your capstone context:**
   ```
   Example:

   **Core Purpose:** 
   AI-powered receipt scanner that extracts expense data and categorizes it for small business tax filing.

   **Target Users:** 
   Freelancers and small business owners (1-10 employees) who manually track expenses.

   **Current Key Features:**
   1. Photo upload and OCR text extraction
   2. Merchant name and amount detection
   3. Manual expense categorization
   4. Basic export to CSV

   **Business Model:** 
   Freemium - free tier (50 receipts/month), paid tier $9.99/month (unlimited receipts + advanced features)

   **Main Pain Points:**
   - Users forget to scan receipts immediately
   - Categorization takes too long (manual process)
   - No integration with accounting software
   - Can't handle batch uploads
   - Poor accuracy on faded/crumpled receipts
   ```

4. **AI generates 10 high-impact feature recommendations** like:
   - 🚀 Email forwarding for digital receipts (Growth Engine)
   - ♻️ Smart categorization using ML (Retention Loop)
   - 💰 QuickBooks/Xero API integration (Revenue Generator)
   - 🔄 Batch upload with drag-and-drop (Workflow Enhancer)
   - 🛡️ Receipt data verification with merchant APIs (Trust Amplifier)
   - (5 more...)

5. **AI provides priority matrix:**
   ```
   HIGH IMPACT, LOW EFFORT (Do First):
   1. Smart categorization using ML
   2. Batch upload with drag-and-drop
   
   HIGH IMPACT, HIGH EFFORT (Plan Carefully):
   3. QuickBooks integration
   4. Email forwarding system
   
   MEDIUM IMPACT, LOW EFFORT (Quick Wins):
   5. Export to multiple formats (PDF, Excel)
   
   LOW PRIORITY:
   6-10. [Other features for future consideration]
   ```

6. **Iterate:**
   ```
   "I already have features 2, 5, and 8. Please suggest replacements 
   focusing on mobile capabilities."
   ```

### **What to Do With the Output:**

✅ **Update `docs/feature-roadmap.md`** with prioritized features

✅ **Cross-reference with 20-Pillar output** to validate consistency

✅ **Update `docs/backlog-v2.md`** with new issues for high-priority features

✅ **Document in `docs/evaluation-plan-v2.md`** how you'll measure success for each feature

---

## <a name="architecture-gap-analysis"></a>3. Architecture Gap Analysis

**Purpose:** Validate your architecture by identifying missing components, scalability bottlenecks, and improvement opportunities.

**Best For:**
- Teams unsure if their architecture is complete
- Identifying technical risks early
- Getting architectural review feedback

**Time:** 15-20 minutes

### **The Prompt:**

```
# Architecture Gap Analyzer

You are an expert system architect specializing in AI-powered applications. Your role is to analyze system architectures and identify gaps, risks, and improvement opportunities.

## Your Analysis Process

When I share my system architecture, you will:

1. **Assess Completeness**: Identify missing components critical for production
2. **Evaluate Scalability**: Find bottlenecks that will cause problems at scale
3. **Check Reliability**: Identify single points of failure
4. **Review Security**: Flag security concerns
5. **Analyze Performance**: Identify latency and cost optimization opportunities
6. **Validate Monitoring**: Check observability and debugging capabilities

## Required Information

Please provide:

1. **System Architecture Description**: Components, data flow, tech stack
2. **Architecture Diagram**: Link or ASCII diagram
3. **Expected Scale**: Users, requests per day, data volume
4. **Current Stage**: Prototype, MVP, or production
5. **Known Concerns**: What you're already worried about

## My Analysis Format

For each area, I'll provide:

### ✅ Strengths
- What's well-designed
- Good architectural decisions

### ⚠️ Gaps & Risks
- Missing components
- Potential failure points
- Scalability concerns
- Security vulnerabilities

### 💡 Recommendations
- Specific improvements with rationale
- Alternative approaches with tradeoffs
- Priority ranking (Critical/High/Medium/Low)

### 📊 Tradeoff Analysis
For each recommendation:
- **Pro**: Benefits
- **Con**: Costs/complexity
- **When to implement**: Now vs. later

## Areas I'll Analyze

1. **Frontend Architecture**
   - State management
   - API integration
   - Caching strategy
   - Error handling

2. **Backend Architecture**
   - API design
   - Database schema
   - Authentication/authorization
   - Rate limiting

3. **AI Integration**
   - Model selection
   - Prompt management
   - Fallback strategies
   - Cost optimization

4. **Data Layer**
   - Database choice
   - Vector store (if applicable)
   - Caching layers
   - Data retention policies

5. **Infrastructure**
   - Deployment platform
   - Scaling strategy
   - Monitoring/logging
   - CI/CD pipeline

6. **Security**
   - API key management
   - User data protection
   - Input validation
   - Rate limiting

Now, share your system architecture and I'll provide a comprehensive gap analysis!
```

### **How to Use This Prompt:**

1. **Copy the prompt**

2. **Paste into AI assistant**

3. **Provide your architecture details:**
   ```
   Example:

   **System Architecture:**

   Frontend: React (Vite) → Vercel hosting
   - User uploads receipt image
   - Preprocesses image (resize, compress)
   - Sends to backend API

   Backend: FastAPI (Python) → Railway hosting
   - Receives image from frontend
   - Calls GPT-4V API for OCR
   - Extracts structured data (merchant, amount, date, items)
   - Stores in PostgreSQL
   - Returns results to frontend

   Database: PostgreSQL (Railway managed)
   - Users table
   - Receipts table (metadata + extracted data)
   - Categories table

   AI: OpenAI GPT-4V API
   - Vision API for text extraction
   - Structured output for JSON response

   Auth: Clerk (hosted auth)
   - Email/password login
   - OAuth (Google)

   **Expected Scale:**
   - 100 users initially
   - ~1,000 receipts/month
   - Growth to 1,000 users in 6 months

   **Current Stage:** MVP (Week 4 prototype)

   **Known Concerns:**
   - GPT-4V API costs at scale
   - Image storage costs
   - No caching strategy yet
   - Worried about accuracy on poor-quality receipts
   ```

4. **AI analyzes your architecture** and identifies:
   ```
   ✅ STRENGTHS:
   - Good separation of concerns (frontend/backend)
   - Appropriate tech stack for MVP
   - Managed auth reduces complexity

   ⚠️ GAPS & RISKS:

   CRITICAL:
   - No rate limiting on API → Vulnerable to abuse
   - API keys likely exposed in frontend → Security risk
   - No image preprocessing to optimize costs → Expensive at scale
   - Single database instance → No backups or failover

   HIGH PRIORITY:
   - No caching for repeated queries → Unnecessary API costs
   - No error handling for API failures → Poor UX
   - No logging/monitoring → Can't debug production issues
   - No cost tracking → Budget overruns

   MEDIUM PRIORITY:
   - No CDN for images → Slow uploads
   - No queue system for batch processing → Poor performance
   - No automated testing → Quality issues

   💡 RECOMMENDATIONS:

   IMPLEMENT NOW (Week 4-5):
   1. Add API rate limiting (use FastAPI middleware)
      - Pro: Prevents abuse, controls costs
      - Con: Adds complexity (30 min)
      - Priority: CRITICAL

   2. Move API keys to backend
      - Pro: Security best practice
      - Con: Requires env var setup (1 hour)
      - Priority: CRITICAL

   3. Add image preprocessing pipeline
      - Pro: 40% cost reduction
      - Con: 2-3 hours implementation
      - Priority: HIGH

   IMPLEMENT SOON (Week 6-8):
   4. Add Redis caching for common queries
      - Pro: 50% cost reduction on repeated queries
      - Con: $5/month + complexity
      - Priority: HIGH

   5. Implement proper error handling
      - Pro: Better UX, easier debugging
      - Con: 2-3 hours
      - Priority: HIGH

   IMPLEMENT LATER (Week 10+):
   6. Add queue system (Celery + Redis) for batch processing
      - Pro: Better performance for bulk uploads
      - Con: Significant complexity
      - Priority: MEDIUM (only if needed)
   ```

5. **Iterate with follow-up questions:**
   ```
   "For recommendation #3 (image preprocessing), what specific steps 
   should I implement? Give me code examples."
   ```

### **What to Do With the Output:**

✅ **Update `docs/architecture-v2.md`** with identified gaps

✅ **Create GitHub issues** for each critical/high-priority recommendation

✅ **Update `docs/risk-assessment.md`** with newly identified risks

✅ **Revise your architecture diagram** to show planned improvements

---

## <a name="evaluation-strategy-generator"></a>4. Evaluation Strategy Generator

**Purpose:** Create a comprehensive evaluation plan with specific metrics, testing protocols, and success criteria.

**Best For:**
- Defining golden set test cases
- Planning Week 7 user testing
- Setting up Week 11 safety audit

**Time:** 20-30 minutes

### **The Prompt:**

```
# Evaluation Strategy Architect

You are an expert in AI application evaluation, specializing in creating comprehensive testing strategies that measure real-world performance, user satisfaction, and safety.

## Your Role

When I describe my AI application, you will design a multi-layered evaluation strategy covering:
1. **Quantitative Metrics**: Measurable performance indicators
2. **Qualitative Assessment**: User experience and satisfaction
3. **Golden Set Design**: Representative test cases
4. **User Testing Protocol**: Real-world validation
5. **Safety & Ethics**: Responsible AI evaluation
6. **Continuous Monitoring**: Production metrics

## Required Information

Please provide:

1. **Application Purpose**: What your AI app does
2. **Core Functionality**: Main user workflows
3. **Target Users**: Who will use this
4. **Success Definition**: What does "working well" mean?
5. **Failure Scenarios**: What could go wrong?
6. **Current Metrics** (if any): What you're already tracking

## My Evaluation Framework

### 1. Success Metrics Design

I'll recommend specific, measurable metrics across categories:

**Product Metrics:**
- Task completion rate
- Time on task
- Error rate
- User satisfaction (NPS, CSAT)
- Feature adoption rate

**Technical Metrics:**
- Accuracy/precision/recall
- Latency (P50, P95, P99)
- API uptime
- Cost per query
- Token usage

**Safety Metrics:**
- Content filter effectiveness
- Bias detection scores
- Privacy compliance rate
- Security incident rate

### 2. Golden Set Design

I'll help you create a representative test set:

**Structure:**
- 70% typical use cases
- 20% edge cases
- 10% adversarial/safety tests

**Per Test Case:**
- Input description
- Expected output
- Acceptance criteria
- Edge case rationale

### 3. User Testing Protocol

I'll design a testing protocol for Week 7:

**Participant Profile:**
- Demographics and criteria
- Sample size recommendations
- Recruitment strategy

**Testing Tasks:**
- 3-5 realistic scenarios
- Success criteria per task
- Time limits
- Think-aloud protocol

**Data Collection:**
- Quantitative measurements
- Qualitative feedback
- Observation notes
- Survey questions

### 4. Evaluation Timeline

I'll map evaluation activities to your course schedule:
- Week 4: Baseline measurement
- Week 6: Golden set creation
- Week 7: User testing round 1
- Week 11: Safety audit
- Week 14: User testing round 2
- Week 15: Final evaluation

Now, tell me about your application and I'll design your evaluation strategy!
```

### **How to Use This Prompt:**

1. **Copy the prompt**

2. **Paste into AI assistant**

3. **Describe your application:**
   ```
   Example:

   **Application Purpose:**
   AI-powered receipt scanner that extracts expense data from photos and categorizes spending for small business tax filing.

   **Core Functionality:**
   1. User uploads receipt photo
   2. AI extracts: merchant, date, amount, line items
   3. AI categorizes expense (meals, travel, office supplies, etc.)
   4. User reviews and confirms/edits
   5. Export data for accounting

   **Target Users:**
   Freelancers and small business owners (1-10 employees) who need to track expenses for taxes.

   **Success Definition:**
   - Extracts all key data correctly 85%+ of the time
   - Categorizes expenses correctly 80%+ of the time
   - Completes processing in <3 seconds
   - Users confirm accuracy without edits 70%+ of the time

   **Failure Scenarios:**
   - Can't read faded/crumpled receipts
   - Extracts wrong amount (huge tax problem!)
   - Mis-categorizes expense (wrong tax deduction)
   - Slow processing causes users to abandon
   - Hallucinate data that isn't on receipt

   **Current Metrics:**
   None yet - this is Week 4!
   ```

4. **AI generates comprehensive evaluation strategy:**

   ```
   ## Evaluation Strategy for Receipt Scanner App

   ### 1. SUCCESS METRICS

   **Product Metrics:**
   | Metric | Target | How to Measure |
   |--------|--------|----------------|
   | Task Completion Rate | >85% | % of uploads that successfully extract data |
   | Accuracy Confirmation Rate | >70% | % of results user confirms without editing |
   | Time to Process | <3s (P95) | Backend latency tracking |
   | User Satisfaction | >4.0/5.0 | Post-task survey |
   | Daily Active Users | Growth >10%/week | Analytics dashboard |

   **Technical Metrics:**
   | Component | Metric | Target |
   |-----------|--------|--------|
   | Merchant Extraction | Accuracy | >90% |
   | Date Extraction | Accuracy | >95% |
   | Amount Extraction | Accuracy | >99% (critical for taxes!) |
   | Category Classification | Accuracy | >80% |
   | API Latency | P95 | <2.5s |
   | Cost per Receipt | Average | <$0.05 |

   **Safety Metrics:**
   | Risk | Metric | Target |
   |------|--------|--------|
   | Hallucination Rate | % of fabricated data | <1% |
   | PII Leakage | User data in logs | 0% |
   | Bias in Categorization | Disparity ratio | <1.2x across categories |

   ### 2. GOLDEN SET DESIGN (50 Test Cases)

   **Typical Cases (35 receipts):**
   1. Standard grocery store receipt (clear, printed)
   2. Restaurant receipt with tip line
   3. Gas station receipt
   4. Online order confirmation email
   5. Coffee shop receipt
   6. Office supply store receipt
   7. Hotel receipt
   8. Uber/Lyft ride receipt
   9. Amazon order summary
   10. (25 more diverse typical cases)

   **Edge Cases (10 receipts):**
   1. Faded thermal paper receipt (common after 6 months)
   2. Crumpled/wrinkled receipt
   3. Receipt with handwritten notes
   4. Foreign language receipt
   5. Receipt photographed in poor lighting
   6. Partial receipt (torn or cut off)
   7. Receipt with multiple currencies
   8. Receipt with unusual layout/format
   9. Very long receipt (>20 items)
   10. Tiny receipt (parking meter, vending machine)

   **Adversarial/Safety Cases (5 receipts):**
   1. Blank image (no receipt)
   2. Text document formatted to look like receipt
   3. Credit card photo (should reject!)
   4. Driver's license photo (should reject!)
   5. Random text with dollar signs (not a real receipt)

   **Per Test Case Documentation:**
   ```
   Test Case #1: Standard Grocery Receipt
   
   Input: receipt_grocery_001.jpg
   - Merchant: "Whole Foods Market"
   - Date: "2024-10-15"
   - Amount: $87.43
   - Items: 12 line items including produce, dairy, meat
   
   Expected Output:
   {
     "merchant": "Whole Foods Market",
     "date": "2024-10-15",
     "amount": 87.43,
     "category": "meals",  // or "groceries"
     "confidence": >0.8,
     "items": [...12 items...]
   }
   
   Success Criteria:
   - Merchant name extracted correctly (exact match)
   - Date within ±1 day tolerance
   - Amount within ±$0.01 tolerance
   - Category appropriate (meals or groceries both acceptable)
   - All items extracted (may miss 1-2 items)
   - Processing time <3s
   - Confidence score >0.7
   
   Edge Case Notes: None (baseline typical case)
   ```

   ### 3. USER TESTING PROTOCOL (Week 7)

   **Participant Criteria:**
   - Freelancers or small business owners
   - Currently track expenses (any method)
   - File taxes quarterly or annually
   - Mix of tech comfort levels
   - Sample size: 5 participants

   **Recruitment:**
   - Post in freelancer Facebook groups
   - Local coworking spaces
   - Personal network
   - $25 gift card incentive

   **Testing Tasks (30 min per participant):**

   **Task 1: Upload and Process First Receipt (5 min)**
   - Scenario: "You just had a business lunch. Upload the receipt."
   - Success: User uploads receipt, reviews extracted data
   - Metric: Task completion rate, time to complete

   **Task 2: Review and Confirm Accuracy (3 min)**
   - Scenario: "Check if the data is correct. Edit if needed."
   - Success: User confirms or edits data
   - Metric: Accuracy confirmation rate, number of edits

   **Task 3: Upload Batch of Receipts (7 min)**
   - Scenario: "Upload 5 receipts from last week."
   - Success: User uploads multiple receipts efficiently
   - Metric: Batch processing satisfaction

   **Task 4: Categorize Expenses (5 min)**
   - Scenario: "Review the AI-suggested categories. Change if needed."
   - Success: User understands categories and makes adjustments
   - Metric: Category agreement rate

   **Task 5: Export Data (3 min)**
   - Scenario: "Export your expense data as CSV."
   - Success: User finds export button, downloads file
   - Metric: Export success rate

   **Think-Aloud Protocol:**
   - Ask user to narrate thoughts while completing tasks
   - Observe confusion, hesitation, delight
   - Take detailed notes

   **Post-Task Survey (5 min):**
   1. How easy was it to use? (1-5 scale)
   2. How accurate were the AI extractions? (1-5 scale)
   3. Would you use this for your business? (Yes/No/Maybe)
   4. What was most frustrating?
   5. What did you love?
   6. What features are missing?

   **Data Collection:**
   - Screen recording (with consent)
   - Observer notes
   - Survey responses
   - Time on task measurements
   - Error counts

   ### 4. EVALUATION TIMELINE

   | Week | Activity | Deliverable | Metric Target |
   |------|----------|-------------|---------------|
   | 4 | Baseline Measurement | Current accuracy on 10 test receipts | Document baseline |
   | 5 | Golden Set Creation | 50 test cases ready | 100% coverage |
   | 6 | Automated Testing Setup | Regression test suite | All tests pass |
   | 7 | User Testing Round 1 | 5 participants tested | >70% task completion |
   | 8 | Iterate Based on Feedback | Implement top 3 improvements | Measure improvement |
   | 11 | Safety Audit | Red team testing, bias checks | >90% safety pass rate |
   | 12 | Golden Set Regression | Re-run all 50 cases | >85% accuracy across all |
   | 14 | User Testing Round 2 | 5 new participants | >85% task completion |
   | 15 | Final Evaluation | Demo-ready metrics | Hit all targets |

   ### 5. IMPLEMENTATION TOOLS

   **Metrics Tracking:**
   - Use: PostgreSQL for storing test results
   - Dashboard: Grafana or custom React dashboard
   - Logging: Python logging module → log file → analysis

   **Golden Set Management:**
   - Store: GitHub repo under `/tests/golden-set/`
   - Format: JSON test cases + actual receipt images
   - Version control: Git (track changes over time)

   **User Testing:**
   - Recording: Loom or OBS Studio
   - Notes: Google Docs shared with team
   - Survey: Google Forms or Typeform

   **Automated Testing:**
   - Framework: pytest
   - Run: GitHub Actions on every PR
   - Coverage: aim for >80% code coverage

   ### 6. RED FLAGS TO WATCH

   **Critical Failures (Stop Immediately):**
   - Amount extraction accuracy <95% → Tax liability risk
   - Hallucination rate >5% → User trust issue
   - PII in logs → Privacy violation
   - API costs >$0.10/receipt → Not viable

   **Warning Signs (Needs Attention):**
   - Task completion <70% → UX problems
   - Processing time >5s → User frustration
   - Category accuracy <70% → Need better model
   - User satisfaction <3.5/5 → Major issues

   **Success Indicators (On Track):**
   - Accuracy confirmation >70% → Users trust results
   - Daily active users growing → Product-market fit
   - Cost per receipt declining → Optimization working
   - User satisfaction >4.0 → High quality experience
   ```

5. **Iterate and refine:**
   ```
   "For the golden set, can you give me specific examples of 
   5 adversarial test cases that test for hallucination?"
   ```

### **What to Do With the Output:**

✅ **Copy into `docs/evaluation-plan-v2.md`**

✅ **Create GitHub issues** for golden set creation (Week 5-6)

✅ **Add to `docs/backlog-v2.md`** as testing infrastructure tasks

✅ **Use for Week 7 user testing** recruitment and protocol

✅ **Reference in Week 11 safety audit** planning

---

## <a name="risk-assessment-framework"></a>5. Risk Assessment Framework

**Purpose:** Systematically identify technical, product, and team risks, prioritize by severity, and generate mitigation strategies.

**Best For:**
- Week 2 proposal refinement
- Identifying blind spots
- Creating contingency plans

**Time:** 15-20 minutes

### **The Prompt:**

```
# Risk Assessment Architect

You are a risk management expert for AI-powered software projects. Your role is to identify risks across technical, product, team, and ethical dimensions, then provide actionable mitigation strategies.

## Your Assessment Process

When I describe my project, you will:

1. **Identify Risks** across categories:
   - Technical risks (architecture, APIs, performance)
   - Product risks (user adoption, feature scope)
   - Team risks (skill gaps, capacity, communication)
   - Ethical/Safety risks (bias, privacy, security)

2. **Assess Each Risk**:
   - **Likelihood**: High/Medium/Low
   - **Impact**: High/Medium/Low
   - **Severity**: Critical/High/Medium/Low (likelihood × impact)

3. **Provide Mitigation Strategies**:
   - **Preventive**: Actions to reduce likelihood
   - **Contingency**: Plans if risk materializes
   - **Monitoring**: How to detect early warning signs

## Required Information

Please provide:

1. **Project Description**: What you're building
2. **Technical Stack**: Technologies you're using
3. **Team Composition**: Size, skills, experience
4. **Timeline**: Project duration and milestones
5. **Known Concerns**: Risks you're already aware of

## My Risk Report Format

### Risk Categories

**🔧 Technical Risks**
- Architecture and infrastructure
- API dependencies
- Performance and scalability
- Data management

**📊 Product Risks**
- User adoption
- Feature scope
- Competition
- Market fit

**👥 Team Risks**
- Skill gaps
- Capacity constraints
- Communication breakdowns
- Key person dependency

**🛡️ Ethical & Safety Risks**
- Bias and fairness
- Privacy violations
- Security vulnerabilities
- Misuse potential

### Per Risk Documentation

```
## Risk #1: OpenAI API Cost Overruns

**Category:** Technical - Cost Management
**Likelihood:** High (60-80% probability)
**Impact:** High (Could exhaust semester budget)
**Severity:** ⚠️ CRITICAL

**Description:**
Without proper cost controls, unexpected usage spikes could consume entire budget in days, blocking development and testing.

**Triggers:**
- Inefficient prompts (too many tokens)
- No caching for repeated queries
- Testing without cost tracking
- Batch processing without rate limits

**Preventive Mitigation:**
1. Implement token usage tracking (Week 4)
   - Log every API call with token count
   - Set up daily cost dashboard
   - Alert when daily spending >$5

2. Add caching layer (Week 5)
   - Redis for common queries
   - Expected 40-50% cost reduction

3. Set API rate limits (Week 4)
   - Max 100 requests/hour per user
   - Max $50/day budget hard limit

4. Use GPT-4o-mini for 80% of queries (Week 4)
   - Reserve GPT-4o for complex cases only
   - 50% cost reduction

**Contingency Plan (If Risk Occurs):**
1. Immediate actions:
   - Pause all non-essential API calls
   - Switch to GPT-4o-mini exclusively
   - Review and optimize all prompts

2. Week 5+ actions:
   - Apply for additional API credits from OpenAI
   - Implement aggressive caching
   - Reduce feature scope if needed

**Monitoring:**
- Daily cost dashboard (implement Week 4)
- Alert if daily cost >$5
- Weekly budget review with team
- Track $/query metric over time

**Early Warning Signs:**
- Daily costs trending upward
- Token usage per query increasing
- More API errors (rate limiting)
- Team not checking cost dashboard

**Responsible:** [Backend Lead]
**Review Date:** Every Monday during standup
```

Now, describe your project and I'll perform a comprehensive risk assessment!
```

### **How to Use This Prompt:**

1. **Copy the prompt**

2. **Paste into AI assistant**

3. **Describe your project:**
   ```
   Example:

   **Project:** AI-powered receipt scanner for small business expense tracking

   **Technical Stack:**
   - Frontend: React (Vite) on Vercel
   - Backend: FastAPI (Python) on Railway
   - Database: PostgreSQL (Railway)
   - AI: OpenAI GPT-4V API
   - Auth: Clerk
   - Storage: Cloudinary for images

   **Team:**
   - 3 members (all junior developers)
   - Skills: Basic React, Python, no production experience
   - Part-time (15 hours/week each)

   **Timeline:**
   - Week 4 now (just finished prototype)
   - Week 15 final demo (11 weeks remaining)
   - Major milestones: Week 7 (user testing), Week 11 (safety audit)

   **Known Concerns:**
   - API costs could spiral
   - Never deployed to production before
   - Accuracy on poor-quality receipts uncertain
   - Team member #3 has heavier course load
   ```

4. **AI generates comprehensive risk assessment:**
   ```
   # Risk Assessment Report: Receipt Scanner App

   ## Executive Summary
   🔴 Critical Risks: 2
   🟡 High Risks: 5
   🟢 Medium Risks: 4
   ⚪ Low Risks: 3

   Priority: Address critical risks in Week 4-5.

   ---

   ## CRITICAL RISKS

   ### 🔴 Risk #1: API Cost Overruns
   [Full documentation as shown above]

   ### 🔴 Risk #2: Amount Extraction Accuracy <95%
   **Category:** Technical - AI Accuracy
   **Likelihood:** Medium (40-60%)
   **Impact:** High (Tax liability for users)
   **Severity:** ⚠️ CRITICAL

   **Description:**
   If the AI extracts receipt amounts incorrectly, users could claim wrong tax deductions, creating legal liability and destroying trust.

   **Triggers:**
   - Faded receipts (common after 6 months)
   - Unusual receipt formats
   - Currency symbols misread
   - Decimal points missed

   **Preventive Mitigation:**
   1. Create golden set with 50 test receipts (Week 5)
      - Include diverse quality levels
      - Focus on amount extraction accuracy

   2. Implement multi-pass verification (Week 6)
      - First pass: Standard GPT-4V extraction
      - Second pass: Verify amount specifically with stricter prompt
      - Compare both results, flag discrepancies

   3. Add confidence scoring (Week 5)
      - Flag extractions with confidence <0.8 for human review
      - Show "Amount uncertain, please verify" warning to user

   4. Implement user confirmation workflow (Week 4)
      - Always show extracted amount prominently
      - Require explicit user confirmation before saving
      - Log cases where user edits amount

   **Contingency Plan:**
   1. If golden set shows <95% accuracy:
      - Add preprocessing (image enhancement)
      - Try GPT-4o instead of GPT-4o-mini for amounts
      - Consider hybrid approach (OCR + LLM)

   2. If production accuracy drops:
      - Pause new users
      - Add "Beta" warning
      - Require human review for all amounts >$100

   **Monitoring:**
   - Golden set regression tests weekly
   - Track user edit rate for amounts
   - User feedback: "Was the amount correct?"
   - Production accuracy dashboard

   ---

   ## HIGH RISKS

   ### 🟡 Risk #3: Team Member Unavailability
   **Category:** Team - Capacity
   **Likelihood:** High (60-80%)
   **Impact:** Medium (Delays, quality issues)
   **Severity:** ⚠️ HIGH

   **Description:**
   Team member #3 has heavier course load and may become unavailable during midterms/finals, reducing team capacity by 33%.

   **Preventive Mitigation:**
   1. Cross-train team members (Week 4-5)
      - Everyone knows frontend AND backend
      - Document all code thoroughly
      - Pair programming sessions

   2. Frontload critical work (Week 4-7)
      - Finish core infrastructure before midterms (Week 9)
      - MVP features done by Week 8
      - Only polish/testing in Weeks 12-15

   3. Buffer time in schedule (Week 4)
      - Plan for 20% capacity reduction
      - Have "cut if needed" features ready

   **Contingency Plan:**
   - If member unavailable: Redistribute tasks immediately
   - Reduce scope: Cut P3 features, focus on MVP
   - Extend work sessions for remaining members

   ---

   ### 🟡 Risk #4: Poor Quality Receipt Photos
   **Category:** Product - User Input
   **Likelihood:** High (70%+)
   **Impact:** Medium (Poor UX, low accuracy)
   **Severity:** ⚠️ HIGH

   [Full documentation...]

   ### 🟡 Risk #5: No Production Deployment Experience
   **Category:** Team - Skills
   **Likelihood:** High (100% - no experience)
   **Impact:** Medium (Delays, downtime)
   **Severity:** ⚠️ HIGH

   [Full documentation...]

   ### 🟡 Risk #6: Scope Creep
   [...]

   ### 🟡 Risk #7: User Adoption (No One Uses It)
   [...]

   ---

   ## MEDIUM RISKS

   ### 🟢 Risk #8: Database Performance at Scale
   [...]

   ### 🟢 Risk #9: Receipt Image Storage Costs
   [...]

   ### 🟢 Risk #10: Privacy/GDPR Compliance
   [...]

   ### 🟢 Risk #11: Browser Compatibility Issues
   [...]

   ---

   ## LOW RISKS

   ### ⚪ Risk #12: Clerk Auth Service Outage
   [...]

   ### ⚪ Risk #13: Competitor Launches Similar Product
   [...]

   ### ⚪ Risk #14: React/FastAPI Breaking Changes
   [...]

   ---

   ## RISK MITIGATION ROADMAP

   **Week 4 (Immediate - This Week):**
   - [ ] Set up cost tracking dashboard (Risk #1)
   - [ ] Implement rate limiting (Risk #1)
   - [ ] Add user confirmation for amounts (Risk #2)
   - [ ] Document all code (Risk #3)
   - [ ] Test deployment to production (Risk #5)

   **Week 5-6:**
   - [ ] Create golden set (Risk #2)
   - [ ] Implement caching (Risk #1)
   - [ ] Cross-train team members (Risk #3)
   - [ ] Add image preprocessing (Risk #4)

   **Week 7-8:**
   - [ ] User testing (Risk #7)
   - [ ] Iterate based on feedback (Risk #4, #7)
   - [ ] Finalize MVP scope (Risk #6)

   **Week 9-11:**
   - [ ] Buffer week for midterms (Risk #3)
   - [ ] Safety audit (Risk #10)
   - [ ] Performance testing (Risk #8)

   **Week 12-15:**
   - [ ] Polish and bug fixes
   - [ ] Final user testing
   - [ ] Demo preparation

   ---

   ## RISK DASHBOARD (Track Weekly)

   | Risk | Status | Trend | Next Review |
   |------|--------|-------|-------------|
   | #1 API Costs | 🟢 OK | → | Weekly |
   | #2 Amount Accuracy | 🟡 Testing | ↓ | Week 5 |
   | #3 Team Capacity | 🟢 OK | → | Weekly |
   | #4 Photo Quality | 🔴 Not Addressed | ↑ | Week 5 |
   | #5 Deployment | 🟡 In Progress | ↓ | Week 4 |

   Trend: ↑ Getting worse, → Stable, ↓ Improving
   ```

5. **Iterate:**
   ```
   "For Risk #4 (poor quality photos), give me specific 
   implementation steps for image preprocessing."
   ```

### **What to Do With the Output:**

✅ **Update `docs/capstone-proposal-v2.md`** risk section

✅ **Create `docs/risk-management-plan.md`** with full report

✅ **Add high-priority risks to `docs/backlog-v2.md`** as issues

✅ **Discuss in team meetings** and assign risk owners

✅ **Update weekly** during standups

---

## <a name="token-optimization-analyzer"></a>6. Token Optimization Analyzer

**Purpose:** Analyze your current token usage and identify specific optimizations to reduce API costs by 30-50%.

**Best For:**
- High API costs
- Inefficient prompts
- No caching strategy

**Time:** 15-20 minutes

### **The Prompt:**

```
# Token Optimization Expert

You are a specialist in optimizing token usage for AI applications to minimize costs while maintaining quality. You analyze prompts, system designs, and usage patterns to identify optimization opportunities.

## Your Analysis Process

When I share my AI application details, you will:

1. **Analyze Current Token Usage**
   - Input tokens (system prompt, user query, context)
   - Output tokens (response length)
   - Total cost per query

2. **Identify Optimization Opportunities**
   - Prompt engineering improvements
   - Caching strategies
   - Model selection
   - Architecture changes

3. **Provide Specific Recommendations**
   - Expected token reduction
   - Expected cost savings
   - Implementation effort
   - Quality impact (if any)

## Required Information

Please provide:

1. **Current Prompt Structure**: Your system prompt, user query format, any retrieved context
2. **Token Counts**: Approximate tokens per query (input + output)
3. **Usage Volume**: Queries per day/month
4. **Current Model**: GPT-4, GPT-4o, GPT-4o-mini, etc.
5. **Quality Requirements**: What level of quality is acceptable?

## My Optimization Report Format

### Current Baseline
```
Input Tokens Breakdown:
- System prompt: XXX tokens
- User query: XXX tokens
- Retrieved context: XXX tokens
- Total input: XXX tokens

Output Tokens: XXX tokens

Total per query: XXX tokens
Cost per query: $X.XX
Monthly cost (X queries): $XX.XX
```

### Optimization Recommendations

For each optimization, I provide:
- **Strategy**: What to change
- **Implementation**: How to do it
- **Token Reduction**: Specific number
- **Cost Savings**: Percentage and dollars
- **Quality Impact**: High/Medium/Low/None
- **Effort**: Hours to implement
- **Code Example** (where applicable)

### Optimization Priority Matrix

```
HIGH IMPACT, LOW EFFORT (Implement Immediately):
- Optimization A: 40% cost reduction, 2 hours

HIGH IMPACT, HIGH EFFORT (Plan Carefully):
- Optimization B: 50% cost reduction, 8 hours

MEDIUM IMPACT, LOW EFFORT (Quick Wins):
- Optimization C: 15% cost reduction, 1 hour

LOW IMPACT (Skip):
- Optimization D: 5% cost reduction, 4 hours
```

Now, share your current prompt structure and token usage, and I'll provide specific optimization recommendations!
```

### **How to Use This Prompt:**

1. **Copy the prompt**

2. **Paste into AI assistant**

3. **Share your current setup:**
   ```
   Example:

   **Current Prompt Structure:**

   System Prompt (500 tokens):
   "You are an expert receipt analyzer. Your job is to extract information from receipt images. Be thorough and accurate. Always include merchant name, date, total amount, and itemized list. Format your response as JSON. Be polite and professional. If you're unsure about any information, indicate that in your confidence score. Remember that accuracy is critical for tax purposes. Users rely on your extractions. Double-check all numbers. [... continues for 500 tokens]"

   User Query (200 tokens):
   "Please analyze this receipt image and extract all relevant information."

   Retrieved Context: None (no RAG yet)

   Output (600 tokens):
   Full JSON response with explanations and verbose formatting

   **Token Counts:**
   - Total input: 700 tokens
   - Total output: 600 tokens
   - Total per query: 1,300 tokens

   **Usage:**
   - Current: ~50 queries/day (testing)
   - Expected: ~500 queries/day (production)
   - Model: GPT-4o ($5/1M input tokens, $15/1M output tokens)

   **Cost:**
   - Per query: ~$0.013
   - Monthly (15K queries): ~$195

   **Quality Requirements:**
   - Amount extraction must be >99% accurate
   - Merchant/date extraction >90% accurate
   - Response time <3 seconds
   ```

4. **AI provides detailed optimization plan:**
   ```
   # Token Optimization Report: Receipt Scanner

   ## CURRENT BASELINE

   **Input Tokens:**
   - System prompt: 500 tokens ⚠️ TOO LONG
   - User query: 200 tokens ⚠️ REDUNDANT
   - Total input: 700 tokens

   **Output Tokens:** 600 tokens ⚠️ TOO VERBOSE

   **Cost Analysis:**
   - Input cost: 700 × $0.005/1K = $0.0035/query
   - Output cost: 600 × $0.015/1K = $0.009/query
   - Total: $0.0125/query
   - Monthly (15K queries): $187.50

   ---

   ## OPTIMIZATION #1: Compress System Prompt
   **Impact:** 🔴 HIGH (60% token reduction on system prompt)
   **Effort:** 🟢 LOW (30 minutes)
   **Quality Impact:** 🟢 NONE

   **Current (500 tokens):**
   ```
   You are an expert receipt analyzer. Your job is to extract information from receipt images. Be thorough and accurate. Always include merchant name, date, total amount, and itemized list. Format your response as JSON. Be polite and professional. If you're unsure about any information, indicate that in your confidence score. Remember that accuracy is critical for tax purposes. Users rely on your extractions. Double-check all numbers.
   ```

   **Optimized (200 tokens - 60% reduction):**
   ```
   Extract receipt data: merchant, date, amount, items. Return JSON. 
   Accuracy critical (tax purposes). Include confidence score (0-1) 
   if uncertain.
   ```

   **Why This Works:**
   - Removes fluff ("be polite and professional" doesn't change output)
   - Removes redundancy (multiple mentions of accuracy)
   - Keeps critical instructions (JSON format, confidence score)
   - LLMs don't need verbose instructions

   **Token Savings:** 300 tokens input per query
   **Cost Savings:** $0.0015/query → $22.50/month (12% total reduction)

   **Implementation:**
   ```python
   # Before
   system_prompt = """
   You are an expert receipt analyzer. Your job is to extract information 
   from receipt images. Be thorough and accurate. Always include merchant 
   name, date, total amount, and itemized list. Format your response as JSON. 
   Be polite and professional. If you're unsure about any information, 
   indicate that in your confidence score. Remember that accuracy is critical 
   for tax purposes. Users rely on your extractions. Double-check all numbers.
   """

   # After
   system_prompt = """Extract receipt data: merchant, date, amount, items. 
   Return JSON. Accuracy critical (tax purposes). Include confidence (0-1) 
   if uncertain."""
   ```

   ---

   ## OPTIMIZATION #2: Remove Redundant User Query
   **Impact:** 🟡 MEDIUM (100% token reduction on user query)
   **Effort:** 🟢 LOW (15 minutes)
   **Quality Impact:** 🟢 NONE

   **Analysis:**
   Your user query ("Please analyze this receipt image and extract all relevant information") is redundant with the system prompt.

   **Solution:**
   Don't send a text query at all. Just send the image.

   **Token Savings:** 200 tokens input per query
   **Cost Savings:** $0.001/query → $15/month (8% total reduction)

   **Implementation:**
   ```python
   # Before
   messages = [
       {"role": "system", "content": system_prompt},
       {"role": "user", "content": [
           {"type": "text", "text": "Please analyze this receipt..."},
           {"type": "image_url", "image_url": image_url}
       ]}
   ]

   # After
   messages = [
       {"role": "system", "content": system_prompt},
       {"role": "user", "content": [
           {"type": "image_url", "image_url": image_url}
       ]}
   ]
   ```

   ---

   ## OPTIMIZATION #3: Enforce Structured Output (JSON Schema)
   **Impact:** 🔴 HIGH (50% token reduction on output)
   **Effort:** 🟡 MEDIUM (2 hours)
   **Quality Impact:** 🟢 NONE (actually improves consistency)

   **Current Output (600 tokens):**
   ```json
   {
     "merchant": "Whole Foods Market",
     "explanation": "The merchant name is clearly visible at the top...",
     "date": "2024-10-15",
     "date_confidence": "High - clearly printed",
     "amount": 87.43,
     "amount_note": "This is the total after tax",
     "items": [
       {"name": "Organic Bananas", "price": 3.99, "note": "Produce section"},
       // ... more verbose items
     ],
     "summary": "This receipt appears to be from a grocery store purchase..."
   }
   ```

   **Optimized Output (300 tokens - 50% reduction):**
   ```json
   {
     "merchant": "Whole Foods Market",
     "date": "2024-10-15",
     "amount": 87.43,
     "items": [
       {"name": "Organic Bananas", "price": 3.99},
       {"name": "Milk", "price": 4.99}
     ],
     "confidence": 0.95
   }
   ```

   **Implementation:**
   Use OpenAI's structured output feature (JSON Schema):

   ```python
   from pydantic import BaseModel
   from typing import List

   class ReceiptItem(BaseModel):
       name: str
       price: float

   class ReceiptData(BaseModel):
       merchant: str
       date: str  # YYYY-MM-DD format
       amount: float
       items: List[ReceiptItem]
       confidence: float  # 0-1

   # In your API call
   response = client.chat.completions.create(
       model="gpt-4o-2024-08-06",  # Must use this specific model
       messages=messages,
       response_format={
           "type": "json_schema",
           "json_schema": {
               "name": "receipt_extraction",
               "schema": ReceiptData.model_json_schema()
           }
       }
   )
   ```

   **Token Savings:** 300 tokens output per query
   **Cost Savings:** $0.0045/query → $67.50/month (36% total reduction)

   **Bonus Benefits:**
   - Guaranteed valid JSON (no parsing errors)
   - Consistent structure (easier to work with)
   - Removes verbose explanations (not needed)

   ---

   ## OPTIMIZATION #4: Implement Caching for Repeated Queries
   **Impact:** 🔴 HIGH (40% cost reduction via cache hits)
   **Effort:** 🔴 HIGH (6-8 hours)
   **Quality Impact:** 🟢 NONE

   **Analysis:**
   Users may upload the same receipt multiple times (accidentally) or query similar receipts. Caching can prevent redundant API calls.

   **Strategy:**
   - Hash each image (MD5 or perceptual hash)
   - Check Redis cache before calling API
   - Cache results for 7 days
   - Expected cache hit rate: 40%

   **Token Savings:** N/A (prevents entire API call)
   **Cost Savings:** ~$0.005/query × 40% hit rate → $30/month (16% total reduction)

   **Implementation:**
   ```python
   import redis
   import hashlib
   from PIL import Image

   redis_client = redis.Redis(host='localhost', port=6379, db=0)

   def get_cached_result(image_hash):
       cached = redis_client.get(f"receipt:{image_hash}")
       if cached:
           return json.loads(cached)
       return None

   def cache_result(image_hash, result):
       redis_client.setex(
           f"receipt:{image_hash}",
           604800,  # 7 days
           json.dumps(result)
       )

   def process_receipt(image):
       # Hash the image
       image_hash = hashlib.md5(image).hexdigest()
       
       # Check cache
       cached_result = get_cached_result(image_hash)
       if cached_result:
           print("Cache hit!")
           return cached_result
       
       # Call API if cache miss
       result = call_gpt4v_api(image)
       
       # Cache the result
       cache_result(image_hash, result)
       
       return result
   ```

   ---

   ## OPTIMIZATION #5: Switch to GPT-4o-mini for Non-Critical Extractions
   **Impact:** 🔴 HIGH (90% cost reduction for 70% of queries)
   **Effort:** 🟡 MEDIUM (3-4 hours)
   **Quality Impact:** 🟡 SLIGHT (acceptable for most receipts)

   **Analysis:**
   GPT-4o is expensive ($5/$15 per 1M tokens). GPT-4o-mini is 90% cheaper ($0.15/$0.60 per 1M tokens) and performs well on standard receipts.

   **Strategy:**
   - Use GPT-4o-mini for clear, standard receipts (70% of cases)
   - Use GPT-4o for poor quality or complex receipts (30% of cases)
   - Decision logic: If image quality score < 0.7, use GPT-4o; else use GPT-4o-mini

   **Token Savings:** N/A (model switch, not token reduction)
   **Cost Savings:** Massive - see calculation below

   **Cost Calculation:**
   ```
   GPT-4o (current):
   - Input: 200 tokens × $0.005/1K = $0.001/query
   - Output: 300 tokens × $0.015/1K = $0.0045/query
   - Total: $0.0055/query

   GPT-4o-mini:
   - Input: 200 tokens × $0.00015/1K = $0.00003/query
   - Output: 300 tokens × $0.0006/1K = $0.00018/query
   - Total: $0.0002/query

   Savings per mini query: $0.0053/query (96% reduction!)

   Blended (70% mini, 30% full):
   - Mini: 0.70 × $0.0002 = $0.00014/query
   - Full: 0.30 × $0.0055 = $0.00165/query
   - Total: $0.00179/query

   Monthly (15K queries): $26.85 (vs. $82.50)
   Savings: $55.65/month (67% total reduction!)
   ```

   **Implementation:**
   ```python
   def assess_image_quality(image):
       # Simple heuristic: check contrast, sharpness
       # Or use a separate vision API call (cheap)
       # Return score 0-1
       return quality_score

   def process_receipt(image):
       quality = assess_image_quality(image)
       
       if quality > 0.7:
           model = "gpt-4o-mini"
           print("Using mini model (clear receipt)")
       else:
           model = "gpt-4o"
           print("Using full model (poor quality)")
       
       response = client.chat.completions.create(
           model=model,
           messages=messages
       )
       
       return response
   ```

   ---

   ## COMBINED OPTIMIZATION IMPACT

   | Optimization | Token Reduction | Cost Savings | Effort |
   |--------------|-----------------|--------------|--------|
   | #1: Compress System Prompt | 300 input | $22.50/mo (12%) | 30 min |
   | #2: Remove User Query | 200 input | $15/mo (8%) | 15 min |
   | #3: Structured Output | 300 output | $67.50/mo (36%) | 2 hrs |
   | #4: Caching (40% hit rate) | All tokens | $30/mo (16%) | 8 hrs |
   | #5: GPT-4o-mini Hybrid | N/A | $55.65/mo (67%) | 4 hrs |

   **Total Savings (All Optimizations):**
   - Original cost: $187.50/month
   - After #1-3: $82.50/month (56% reduction)
   - After #4: $49.50/month (74% reduction)  
   - After #5: $26.85/month (**86% total reduction!**)

   **Recommended Implementation Order:**

   **Week 4 (Immediate):**
   1. Optimization #1: Compress system prompt (30 min)
   2. Optimization #2: Remove user query (15 min)
   → Quick wins, 20% cost reduction, <1 hour work

   **Week 5:**
   3. Optimization #3: Structured output (2 hrs)
   → Major impact, 36% additional reduction

   **Week 6:**
   4. Optimization #5: GPT-4o-mini hybrid (4 hrs)
   → Massive savings, 67% reduction from baseline

   **Week 7-8:**
   5. Optimization #4: Caching (8 hrs)
   → Further 16% reduction, infrastructure investment

   **Final Result: $26.85/month (vs. $187.50) = $160.65/month savings!**
   ```

5. **Iterate:**
   ```
   "For optimization #5 (model switching), how do I assess 
   image quality? Give me specific code."
   ```

### **What to Do With the Output:**

✅ **Update `docs/cost-model-v2.md`** with optimization strategies

✅ **Create GitHub issues** for each optimization

✅ **Implement quick wins** (optimizations #1-2) immediately

✅ **Track savings** on cost dashboard to validate

---

## <a name="user-testing-protocol-builder"></a>7. User Testing Protocol Builder

**Purpose:** Design a comprehensive user testing protocol for Week 7, including participant criteria, tasks, data collection methods, and analysis framework.

**Best For:**
- Planning Week 7 user testing
- Ensuring useful feedback
- Meeting evaluation plan requirements

**Time:** 20-30 minutes

### **The Prompt:**

```
# User Testing Protocol Designer

You are a UX researcher specializing in AI application testing. Your role is to design rigorous yet practical user testing protocols that yield actionable insights.

## Your Design Process

When I describe my AI application, you will create a complete testing protocol covering:

1. **Participant Recruitment**
   - Target user criteria
   - Sample size recommendations
   - Recruitment channels
   - Screening questions
   - Incentive structure

2. **Testing Tasks**
   - 3-5 realistic scenarios
   - Clear success criteria per task
   - Time limits
   - Think-aloud protocol
   - Task order (to avoid bias)

3. **Data Collection**
   - Quantitative metrics (task completion, time, errors)
   - Qualitative feedback (surveys, interviews)
   - Observation notes template
   - Recording setup

4. **Consent & Ethics**
   - Informed consent process
   - Data privacy protections
   - IRB light considerations

5. **Analysis Framework**
   - How to analyze collected data
   - What patterns to look for
   - How to prioritize feedback

## Required Information

Please provide:

1. **Application Description**: What your app does
2. **Core User Workflows**: Main tasks users perform
3. **Target Users**: Demographics and characteristics
4. **Testing Goals**: What you want to learn
5. **Constraints**: Budget, timeline, team size

## My Protocol Format

### Executive Summary
- Testing goals
- Participant criteria
- Number of participants
- Timeline
- Budget

### Detailed Protocol
[Comprehensive step-by-step instructions]

### Data Collection Templates
[Ready-to-use forms and surveys]

### Analysis Plan
[How to interpret results]

Now, describe your application and testing goals, and I'll design your user testing protocol!
```

### **How to Use This Prompt:**

1. **Copy the prompt**

2. **Paste into AI assistant**

3. **Describe your testing needs:**
   ```
   Example:

   **Application:** AI-powered receipt scanner for small business expense tracking

   **Core Workflows:**
   1. Upload receipt photo
   2. Review extracted data (merchant, date, amount, items)
   3. Confirm or edit data
   4. Categorize expense
   5. Export data for accounting

   **Target Users:**
   - Freelancers (self-employed)
   - Small business owners (1-10 employees)
   - Currently track expenses manually or with spreadsheets
   - Age 25-55
   - Mix of tech comfort levels

   **Testing Goals:**
   - Validate that users can successfully upload and process receipts
   - Measure accuracy of AI extractions (from user perspective)
   - Identify UX pain points and confusion
   - Assess whether users trust the AI results
   - Determine if categorization feature is useful
   - Understand whether users would pay for this

   **Constraints:**
   - Budget: $125 total ($25/participant × 5 participants)
   - Timeline: Week 7 (1 week to recruit, test, analyze)
   - Team: 3 people available to conduct testing
   - Remote testing (Zoom) due to distributed team
   ```

4. **AI generates complete protocol:**
   ```
   # User Testing Protocol: Receipt Scanner App
   ## Week 7 User Testing

   ---

   ## EXECUTIVE SUMMARY

   **Testing Goals:**
   1. Validate core workflow usability
   2. Measure perceived AI accuracy
   3. Identify UX friction points
   4. Assess willingness to pay

   **Participant Criteria:**
   - Freelancers or small business owners
   - Currently track expenses for taxes
   - 5 participants (mix of tech comfort levels)

   **Timeline:**
   - Days 1-2: Recruit participants
   - Days 3-6: Conduct 5 sessions (1 per day)
   - Day 7: Analyze and synthesize

   **Budget:** $125 ($25 gift card per participant)

   ---

   ## PART 1: PARTICIPANT RECRUITMENT

   ### Target Criteria

   **Primary Criteria (Must Have):**
   - Freelancer OR small business owner (1-10 employees)
   - Currently tracks business expenses
   - Files taxes quarterly or annually
   - Has smartphone with camera
   - Willing to do 45-min remote session

   **Secondary Criteria (Nice to Have):**
   - Mix of ages (20s, 30s, 40s, 50s)
   - Mix of industries
   - Mix of tech comfort (2 tech-savvy, 2 average, 1 less comfortable)
   - Mix of expense volume (low, medium, high)

   ### Sample Size Justification
   **Why 5 participants?**
   - Nielsen Norman Group research: 5 users find 85% of usability issues
   - Budget-friendly for student project
   - Manageable within 1 week timeline
   - Sufficient for qualitative insights

   ### Recruitment Channels

   **Primary Channels:**
   1. **Facebook Groups**
      - "Freelancer Community"
      - "Small Business Owners Network"
      - Local entrepreneur groups
      - Post: [Draft message below]

   2. **LinkedIn**
      - Personal connections
      - Freelancer/entrepreneur groups
      - Direct outreach to contacts

   3. **Local Coworking Spaces**
      - Post flyer on community board
      - Ask staff to share with members

   4. **Personal Network**
      - Family friends who are freelancers
      - Former colleagues
      - Alumni network

   ### Recruitment Message Template

   ```
   📱 User Testing Opportunity: AI Receipt Scanner App

   Hi! I'm a student building an AI-powered app to help freelancers 
   and small business owners track expenses for taxes. I'm looking for 
   5 people to test the app and share feedback.

   **What's involved:**
   - 45-minute Zoom session (scheduled at your convenience)
   - Test a mobile app by uploading a few receipts
   - Share your thoughts and feedback
   - $25 Amazon gift card as thanks for your time

   **Who I'm looking for:**
   - Freelancers or small business owners
   - Currently track expenses for taxes
   - Have 3-5 business receipts from the last month

   Interested? Reply or DM me and I'll send details!
   ```

   ### Screening Questions

   Use these to qualify participants:

   1. **Are you currently self-employed or a small business owner?**
      - Yes → Continue
      - No → Thank and disqualify

   2. **Do you currently track business expenses for tax purposes?**
      - Yes → Continue
      - No → Thank and disqualify

   3. **How do you currently track your expenses?**
      - (Open-ended, no wrong answer, just curious)

   4. **Do you have a smartphone with a camera?**
      - Yes → Continue
      - No → Thank and disqualify

   5. **Are you available for a 45-minute Zoom call this week?**
      - Yes → Continue
      - No → Ask if next week works (backup participants)

   6. **Do you have 3-5 business receipts from the last month that you can use during testing?**
      - Yes → Continue
      - No → "That's okay, we can use sample receipts"

   ### Scheduling

   **Booking Process:**
   - Use Calendly or Google Calendar for scheduling
   - Offer multiple time slots throughout the week
   - Send Zoom link 24 hours before session
   - Send reminder 1 hour before session

   **Session Spacing:**
   - Allow 2 hours between sessions (for notes + debrief)
   - Aim for 1-2 sessions per day maximum

   ---

   ## PART 2: TESTING TASKS

   ### Session Structure (45 minutes)

   **0:00-0:05 | Welcome & Consent (5 min)**
   - Introduction
   - Explain testing purpose
   - Get consent for recording
   - Answer questions

   **0:05-0:10 | Background Questions (5 min)**
   - Current expense tracking method
   - Pain points with current method
   - Tech comfort level

   **0:10-0:35 | Task Testing (25 min)**
   - Task 1: Upload and process receipt (5 min)
   - Task 2: Review and confirm accuracy (5 min)
   - Task 3: Categorize expenses (5 min)
   - Task 4: Batch upload multiple receipts (5 min)
   - Task 5: Export data (5 min)

   **0:35-0:45 | Debrief & Survey (10 min)**
   - Overall impressions
   - Post-task survey
   - Willingness to pay question
   - Thank you + send gift card

   ---

   ### Task Details

   #### **Task 1: Upload and Process First Receipt**

   **Scenario:**
   "Imagine you just had a business lunch. You have the receipt and want to track this expense. Use the app to upload and process the receipt."

   **What They Do:**
   1. Open the app (you share link)
   2. Find upload button
   3. Upload receipt photo (or take new photo)
   4. Wait for processing
   5. See extracted data

   **Success Criteria:**
   - ✅ Finds upload button without help (<30 sec)
   - ✅ Successfully uploads image
   - ✅ Understands processing is happening (loading state)
   - ✅ Sees extracted results

   **Metrics to Track:**
   - Time to complete (target: <2 minutes)
   - Number of errors or confusion moments
   - Whether they needed assistance

   **Think-Aloud Prompts:**
   - "What are you thinking right now?"
   - "What do you expect to happen next?"
   - "Is anything unclear?"

   **Follow-Up Questions:**
   - "Was that easier or harder than you expected?"
   - "Did you understand what was happening while it processed?"

   ---

   #### **Task 2: Review and Confirm Accuracy**

   **Scenario:**
   "The app extracted information from your receipt. Review it and tell me if it's accurate."

   **What They Do:**
   1. Look at extracted merchant name
   2. Check date
   3. Verify amount
   4. Review line items (if applicable)
   5. Either confirm or edit

   **Success Criteria:**
   - ✅ Understands what data was extracted
   - ✅ Can identify if extraction is correct
   - ✅ Knows how to edit if needed
   - ✅ Understands confidence score (if shown)

   **Metrics to Track:**
   - Time to review (target: <1 minute)
   - Whether they caught any extraction errors
   - Whether they felt confident trusting results

   **Think-Aloud Prompts:**
   - "Is this information correct?"
   - "How confident are you that this is accurate?"
   - "What would you do if something was wrong?"

   **Follow-Up Questions:**
   - "Did you trust the AI's extraction?"
   - "Would you double-check every receipt, or only review suspicious ones?"
   - "What would make you more confident in the results?"

   ---

   #### **Task 3: Categorize Expense**

   **Scenario:**
   "Now categorize this expense for your tax records."

   **What They Do:**
   1. See suggested category from AI
   2. Accept OR select different category
   3. Confirm categorization

   **Success Criteria:**
   - ✅ Understands categories available
   - ✅ Can select appropriate category
   - ✅ Knows categories matter for taxes

   **Metrics to Track:**
   - Time to categorize (target: <30 seconds)
   - Whether AI suggestion was accepted
   - Whether user understood categories

   **Think-Aloud Prompts:**
   - "Does this category make sense?"
   - "How do you decide what category to use?"

   **Follow-Up Questions:**
   - "Were the category options clear?"
   - "Did the AI suggest the right category?"
   - "What categories are missing?"

   ---

   #### **Task 4: Batch Upload Multiple Receipts**

   **Scenario:**
   "You have several receipts from last week. Upload all of them at once."

   **What They Do:**
   1. Find batch upload option (if exists)
   2. Select multiple images
   3. Upload all at once
   4. Review all results

   **Success Criteria:**
   - ✅ Finds batch upload feature
   - ✅ Successfully uploads multiple receipts
   - ✅ Can review each one individually

   **Metrics to Track:**
   - Time to complete
   - Whether feature was discoverable
   - Number of receipts uploaded

   **Think-Aloud Prompts:**
   - "How would you upload multiple receipts?"
   - "Is this what you expected?"

   **Follow-Up Questions:**
   - "Would you use batch upload often?"
   - "What would make batch processing better?"

   ---

   #### **Task 5: Export Data**

   **Scenario:**
   "It's time to send your expense data to your accountant. Export your data."

   **What They Do:**
   1. Find export button
   2. Choose format (CSV, PDF, etc.)
   3. Download file
   4. Verify file looks correct

   **Success Criteria:**
   - ✅ Finds export feature
   - ✅ Understands export formats
   - ✅ Successfully downloads file
   - ✅ File contains expected data

   **Metrics to Track:**
   - Time to find export
   - Which format chosen
   - Whether file met expectations

   **Follow-Up Questions:**
   - "Is this the format your accountant wants?"
   - "What other export options would be useful?"
   - "Would you integrate with QuickBooks/Xero?"

   ---

   ## PART 3: DATA COLLECTION

   ### Quantitative Metrics

   **Per Task:**
   - Task completion (Yes/No/Partial)
   - Time on task (seconds)
   - Errors or confusion moments (count)
   - Assistance needed (Yes/No)

   **Overall:**
   - System Usability Scale (SUS) score
   - Task completion rate (% of tasks completed)
   - Average time per task
   - Error rate

   ### Qualitative Data

   **During Session:**
   - Think-aloud observations
   - Facial expressions (delight, confusion, frustration)
   - Spontaneous comments
   - Questions asked

   **Post-Task Survey:**
   1. Overall, how easy was the app to use? (1-5 scale)
   2. How accurate were the AI extractions? (1-5 scale)
   3. Did you trust the AI results? (1-5 scale)
   4. How likely are you to use this app? (1-5 scale)
   5. Would you recommend this to another freelancer? (Yes/No)
   6. What did you LOVE about the app?
   7. What FRUSTRATED you most?
   8. What features are MISSING?
   9. Would you pay for this app? (Yes/No)
   10. If yes, how much? (Open-ended)

   ### Observation Notes Template

   ```
   PARTICIPANT: [Number] | DATE: [Date] | TIME: [Time]

   BACKGROUND:
   - Role: [Freelancer/Business Owner]
   - Industry: [Industry]
   - Current expense tracking: [Method]
   - Tech comfort: [Low/Medium/High]

   TASK 1: Upload Receipt
   - Completion: [Yes/No/Partial]
   - Time: [X seconds]
   - Observations:
     - 
     - 
   - Notable quotes:
     - 

   TASK 2: Review Accuracy
   [Same format]

   [Continue for all tasks]

   OVERALL IMPRESSIONS:
   - What worked well:
     - 
   - What didn't work:
     - 
   - Surprising insights:
     - 
   - Feature requests:
     - 

   POST-TASK SURVEY RESULTS:
   - Ease of use: [1-5]
   - AI accuracy: [1-5]
   - Trust: [1-5]
   - Likelihood to use: [1-5]
   - Would recommend: [Y/N]
   - Would pay: [Y/N], Amount: [$X]

   VERBATIM QUOTES:
   - "..."
   - "..."
   ```

   ### Recording Setup

   **Tools:**
   - Zoom for remote sessions
   - Record both screen and audio
   - Ask participant to share screen (so you see their view)
   - Test recording before first session!

   **Consent:**
   - "I'm going to record this session for note-taking purposes. 
      The recording will only be seen by our team and will be 
      deleted after we finish analyzing the results. Is that okay?"

   ---

   ## PART 4: CONSENT & ETHICS

   ### Informed Consent Script

   ```
   Hi [Name], thanks so much for joining! Before we start, I want to 
   make sure you're comfortable with everything.

   Today, you'll be testing an expense tracking app I'm building as 
   part of my university course. I want to learn how real users 
   interact with it so I can make it better.

   A few important things:
   1. We're testing the APP, not testing YOU. There are no wrong 
      answers. If you get confused or stuck, that's feedback for me 
      to improve the app.

   2. Please think out loud as you go. Tell me what you're thinking, 
      what you expect to happen, what's confusing. The more you share, 
      the more helpful it is.

   3. I'm going to record this session for note-taking. The recording 
      will only be seen by my team and will be deleted after we analyze 
      results. Your name won't be shared publicly. Is that okay?
      [Wait for Yes]

   4. You can stop at any time if you're uncomfortable.

   5. After we finish, I'll send you a $25 Amazon gift card as a 
      thank you for your time.

   Do you have any questions before we start?
   ```

   ### Data Privacy

   **What We Collect:**
   - Name and email (for gift card)
   - Session recording (video + audio)
   - Receipt images (with their permission)
   - Survey responses

   **How We Protect It:**
   - All data stored securely (Google Drive with restricted access)
   - Recordings deleted after analysis (within 2 weeks)
   - Results anonymized (Participant 1, Participant 2, etc.)
   - No names in final report

   **IRB Light Checklist:**
   - [✓] Informed consent obtained
   - [✓] Participants can withdraw anytime
   - [✓] Data anonymized in reporting
   - [✓] Recordings deleted after use
   - [✓] No sensitive personal information collected
   - [✓] Minimal risk to participants

   ---

   ## PART 5: ANALYSIS FRAMEWORK

   ### Analysis Process (Day 7)

   **Step 1: Aggregate Quantitative Data (1 hour)**
   - Create spreadsheet with all metrics
   - Calculate averages:
     - Task completion rate
     - Average time per task
     - SUS score
     - Survey ratings

   **Example:**
   ```
   | Participant | Task 1 Time | Task 2 Time | ... | SUS Score | Would Pay? |
   |-------------|-------------|-------------|-----|-----------|------------|
   | P1          | 90s         | 45s         | ... | 75        | Yes ($10)  |
   | P2          | 120s        | 60s         | ... | 68        | No         |
   | P3          | 75s         | 30s         | ... | 82        | Yes ($15)  |
   | P4          | 110s        | 50s         | ... | 71        | Maybe      |
   | P5          | 95s         | 40s         | ... | 79        | Yes ($12)  |
   |-------------|-------------|-------------|-----|-----------|------------|
   | AVERAGE     | 98s         | 45s         | ... | 75        | 60% Yes    |
   ```

   **Step 2: Analyze Qualitative Data (2 hours)**
   - Review all observation notes
   - Watch recordings (or key segments)
   - Identify patterns:
     - What did EVERYONE struggle with? → High priority fix
     - What did NO ONE struggle with? → It works, don't change
     - What delighted users? → Emphasize in marketing
     - What frustrated users? → Fix or remove

   **Step 3: Synthesize Insights (1 hour)**
   - Group findings into themes:
     - Usability issues
     - Feature requests
     - AI accuracy feedback
     - Business model insights

   **Example Synthesis:**
   ```
   ## KEY FINDINGS

   ### USABILITY ISSUES (HIGH PRIORITY)

   🔴 CRITICAL: Batch upload not discoverable
   - 4/5 participants couldn't find batch upload
   - Asked "Can I upload multiple at once?"
   - Fix: Add prominent "Upload Multiple" button

   🔴 CRITICAL: Unclear when processing is complete
   - 3/5 thought app froze during processing
   - Needed better loading indicator
   - Fix: Add progress bar + "Analyzing..." message

   🟡 MEDIUM: Category names confusing
   - "Meals & Entertainment" vs. "Meals" unclear
   - Users unsure which to pick
   - Fix: Add examples or tooltips

   ### AI ACCURACY FEEDBACK

   ✅ POSITIVE: Amount extraction very accurate
   - 5/5 participants said amounts were correct
   - High trust in this metric
   - Keep current approach

   ⚠️ MIXED: Merchant name sometimes wrong
   - 2/5 had merchant extraction errors
   - Caused confusion and distrust
   - Fix: Add confidence score + allow editing

   ### FEATURE REQUESTS

   💡 TOP REQUEST: QuickBooks integration
   - 4/5 participants asked for this
   - "I'd pay more for QuickBooks sync"
   - Consider for future

   💡 REQUESTED: Mileage tracking
   - 2/5 mentioned tracking miles for taxes
   - "Can this track my Uber rides?"
   - Consider for future

   ### BUSINESS MODEL INSIGHTS

   💰 WILLINGNESS TO PAY: 60% (3/5 would pay)
   - Price range: $10-15/month
   - Value prop: "Saves me hours each month"
   - Free tier might be too generous
   ```

   **Step 4: Prioritize Actions (30 min)**
   - Sort issues by:
     - Severity (how bad is the problem?)
     - Frequency (how many users hit it?)
     - Effort (how hard to fix?)

   **Priority Matrix:**
   ```
   HIGH SEVERITY, HIGH FREQUENCY (Fix Immediately):
   - Batch upload discoverability
   - Loading state clarity

   HIGH SEVERITY, LOW FREQUENCY (Fix Soon):
   - Merchant extraction errors

   LOW SEVERITY, HIGH FREQUENCY (Quick Win):
   - Category name clarity

   LOW SEVERITY, LOW FREQUENCY (Future):
   - QuickBooks integration
   - Mileage tracking
   ```

   **Step 5: Create Action Plan (30 min)**
   - Create GitHub issues for each finding
   - Assign to team members
   - Set target completion (Week 8-9)

   ---

   ## DELIVERABLES

   After testing, you should have:

   1. **User Testing Report** (`docs/user-testing-week7-report.md`)
      - Executive summary
      - Methodology
      - Participant demographics
      - Key findings (grouped by theme)
      - Prioritized action items
      - Appendix with raw data

   2. **GitHub Issues** for all fixes

   3. **Updated Backlog** with new priorities

   4. **Updated Evaluation Plan** with actual results

   ---

   ## SUCCESS METRICS

   You'll know testing was successful if:
   - ✅ You can complete all 5 sessions
   - ✅ You identify 5-10 actionable improvements
   - ✅ You have quantitative data (SUS scores, completion rates)
   - ✅ You have qualitative insights (quotes, observations)
   - ✅ You understand whether users would actually use/pay for this
   - ✅ Your team agrees on next steps

   ---

   ## COMMON PITFALLS TO AVOID

   ❌ **Don't lead the participant**
   - Bad: "Click the upload button there"
   - Good: "How would you upload a receipt?"

   ❌ **Don't defend your design**
   - Bad: "Well actually, that button is supposed to..."
   - Good: "Interesting, tell me more about what you expected"

   ❌ **Don't skip the think-aloud**
   - Bad: Silently watch them work
   - Good: "What are you thinking right now?"

   ❌ **Don't test with only tech-savvy users**
   - Bad: All your developer friends
   - Good: Mix of comfort levels

   ❌ **Don't ignore negative feedback**
   - Bad: "That person just didn't get it"
   - Good: "If one person struggled, others will too"

   ---

   ## TIMELINE CHECKLIST

   **Day 1-2: Recruitment**
   - [ ] Post recruitment messages
   - [ ] Screen respondents
   - [ ] Schedule 5 sessions
   - [ ] Send calendar invites + Zoom links

   **Day 3-6: Testing**
   - [ ] Conduct Session 1
   - [ ] Conduct Session 2
   - [ ] Conduct Session 3
   - [ ] Conduct Session 4
   - [ ] Conduct Session 5
   - [ ] Send gift cards

   **Day 7: Analysis**
   - [ ] Aggregate quantitative data
   - [ ] Review recordings
   - [ ] Synthesize findings
   - [ ] Prioritize actions
   - [ ] Create GitHub issues
   - [ ] Write report

   **Week 8: Implementation**
   - [ ] Fix critical issues
   - [ ] Iterate on design
   - [ ] Validate fixes if possible

   Good luck with your user testing! 🎉
   ```

### **What to Do With the Output:**

✅ **Save as `docs/user-testing-protocol-week7.md`**

✅ **Use to recruit participants**

✅ **Follow during Week 7 testing sessions**

✅ **Update `docs/evaluation-plan-v2.md`** with protocol

✅ **Create `docs/user-testing-report.md`** after testing

---

## 🎯 Summary: How to Use These Prompts

### **Strategic Workflow:**

**Week 4 (This Lab):**
1. Start with **20-Pillar Design System** to explore full product space
2. Use **Feature Prioritization Framework** to validate and rank features
3. Run **Architecture Gap Analysis** to validate your technical design
4. Apply **Risk Assessment Framework** to identify blind spots
5. Use **Evaluation Strategy Generator** to create comprehensive test plans
6. Run **Token Optimization Analyzer** if costs are high
7. Use **User Testing Protocol Builder** to plan Week 7

**Ongoing:**
- Revisit **Feature Prioritization** when deciding what to build next
- Re-run **Architecture Gap Analysis** before major changes
- Update **Risk Assessment** weekly during standups
- Reference **Evaluation Strategy** when creating test cases
- Apply **Token Optimization** when costs increase

---

## 💡 Pro Tips for Maximum Value

### **1. Iterate Multiple Times**
Don't stop at the AI's first suggestions. Say:
- "Give me 10 MORE features focusing on [specific area]"
- "Challenge your own recommendations—what are the weaknesses?"
- "Generate alternatives to recommendation #3"

### **2. Cross-Validate Across Frameworks**
Compare outputs:
- Does 20-Pillar System align with Feature Prioritization?
- Do Evaluation Metrics match Risk Assessment priorities?
- Are Token Optimizations aligned with Architecture recommendations?

### **3. Use AI to Review Your Work**
Paste your deliverables back into AI:
- "Here's my architecture diagram. What's missing?"
- "Review my evaluation plan. What metrics am I not considering?"
- "Critique my risk assessment. What blind spots do I have?"

### **4. Save All Outputs**
Create a `docs/ai-explorations/` folder with:
- `20-pillar-output.md`
- `feature-prioritization-output.md`
- `architecture-analysis-output.md`
- etc.

This documentation shows your design thinking process.

### **5. Bring AI Outputs to Team Discussions**
Use AI-generated frameworks to:
- Structure team meetings
- Facilitate prioritization discussions
- Surface disagreements early
- Document decisions

---

## ❓ FAQs

**Q: Can I just copy-paste AI outputs into my deliverables?**

A: No. AI frameworks are starting points, not final deliverables. You must:
- Customize to your specific project
- Validate suggestions with research
- Discuss as a team and reach consensus
- Document why you chose certain recommendations

**Q: What if AI suggests features outside our scope?**

A: That's valuable! Document as "future roadmap" or "post-course enhancements." Shows you're thinking comprehensively.

**Q: Which AI assistant should I use?**

A: Any works! Claude, ChatGPT, or Gemini all support these prompts. Claude tends to be more detailed, ChatGPT faster.

**Q: Can I modify the prompts?**

A: Absolutely! Customize for your needs. Add constraints, change focus, combine prompts.

**Q: What if AI recommendations contradict each other?**

A: Great! That surfaces tradeoffs. Document the conflict and explain your decision rationale.

**Q: Should every team member run the prompts individually?**

A: Yes! Then compare outputs in a team meeting. Diversity of AI explorations leads to better decisions.

---

## 📝 Deliverables Using These Prompts

Track which deliverables use which prompts:

| Deliverable | Prompts to Use |
|-------------|----------------|
| `docs/feature-roadmap.md` | #1 (20-Pillar), #2 (Feature Prioritization) |
| `docs/architecture-v2.md` | #3 (Architecture Gap Analysis) |
| `docs/evaluation-plan-v2.md` | #4 (Evaluation Strategy), #7 (User Testing Protocol) |
| `docs/risk-assessment.md` | #5 (Risk Assessment) |
| `docs/cost-model-v2.md` | #6 (Token Optimization) |
| `docs/backlog-v2.md` | #2 (Feature Prioritization), #5 (Risk Assessment) |

---

**Remember: These AI frameworks are power tools. Use them deliberately, iterate extensively, and always validate with your team and users.**

Good luck! 🚀
