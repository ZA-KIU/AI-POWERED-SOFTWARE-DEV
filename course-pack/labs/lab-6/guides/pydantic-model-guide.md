# Lab 6: Pydantic Models & Structured Outputs

**Course:** Building AI-Powered Applications  
**Week:** 6  
**Topics:** Function Calling, Structured Outputs, Schema Validation with Pydantic  
**Duration:** 2 hours  
**Prerequisites:** Completed Labs 1-5, Basic Python knowledge, OpenAI API access

---

## Learning Objectives

By the end of this lab, you will be able to:

1. ✅ Create Pydantic models to define data schemas
2. ✅ Use structured outputs with OpenAI's `response_format` parameter
3. ✅ Validate and parse LLM responses automatically
4. ✅ Handle nested and complex data structures
5. ✅ Integrate Pydantic models into your capstone project

---

## Table of Contents

1. [Introduction to Structured Outputs](#1-introduction-to-structured-outputs)
2. [Setup and Installation](#2-setup-and-installation)
3. [Exercise 1: Basic Pydantic Models](#3-exercise-1-basic-pydantic-models)
4. [Exercise 2: Contact Extraction](#4-exercise-2-contact-extraction)
5. [Exercise 3: Nested Data Structures](#5-exercise-3-nested-data-structures)
6. [Exercise 4: Review Analysis](#6-exercise-4-review-analysis)
7. [Exercise 5: Multi-Entity Extraction](#7-exercise-5-multi-entity-extraction)
8. [Capstone Integration](#8-capstone-integration)
9. [Troubleshooting](#9-troubleshooting)
10. [Additional Resources](#10-additional-resources)

---

## 1. Introduction to Structured Outputs

### Why Structured Outputs Matter

**The Problem:** LLMs return free-form text, which is:
- ❌ Unpredictable (format varies)
- ❌ Error-prone (missing fields, wrong types)
- ❌ Hard to parse (requires brittle regex/string manipulation)
- ❌ Unreliable (breaks your code)

**The Solution:** Structured outputs using Pydantic models:
- ✅ Guaranteed JSON schema compliance
- ✅ Automatic validation (types, ranges, formats)
- ✅ Type-safe access to fields
- ✅ Self-documenting code
- ✅ No manual parsing needed

### What You'll Build Today

You'll create Pydantic models for:
1. **Contact extraction** from emails
2. **Product review analysis** with sentiment and topics
3. **Multi-entity extraction** from complex documents
4. **Your capstone project** (custom use case)

### Key Concepts

**Pydantic Model:** A Python class that defines the structure of your data.

```python
from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    email: str
```

**Structured Output:** Using `response_format` to enforce schema:

```python
response = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[...],
    response_format=UserProfile  # Pass your Pydantic model here
)

user = response.choices[0].message.parsed  # Already a UserProfile object!
print(user.name)  # Type-safe access
```

---

## 2. Setup and Installation

### Prerequisites

**Check your Python version:**
```bash
python --version  # Should be 3.10+
```

**Install required packages:**
```bash
pip install openai pydantic python-dotenv --break-system-packages
```

**Verify installation:**
```bash
python -c "import openai, pydantic; print('✅ All packages installed')"
```

### Create Project Structure

```bash
mkdir lab-6-pydantic
cd lab-6-pydantic

# Create files
touch exercise_1.py
touch exercise_2.py
touch exercise_3.py
touch exercise_4.py
touch exercise_5.py
touch .env
touch .gitignore
```

**Add to .gitignore:**
```
.env
__pycache__/
*.pyc
.venv/
venv/
```

### Configure API Key

**Edit `.env`:**
```bash
OPENAI_API_KEY=your-api-key-here
```

**Or use Google AI Studio (free tier):**
```bash
# If using Google Gemini instead
GOOGLE_API_KEY=your-google-api-key-here
```

---

## 3. Exercise 1: Basic Pydantic Models

### Objective
Learn the fundamentals of creating Pydantic models and using them with structured outputs.

### Step 1: Create Your First Model

**File: `exercise_1.py`**

```python
from pydantic import BaseModel, Field, EmailStr
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define your first Pydantic model
class UserProfile(BaseModel):
    """A simple user profile"""
    name: str = Field(description="Full name of the user")
    age: int = Field(description="Age in years", ge=0, le=150)
    email: EmailStr = Field(description="Valid email address")
    bio: str | None = Field(default=None, description="Optional user bio")

# Test the model manually (before AI)
def test_model():
    """Test Pydantic validation"""
    
    # Valid data
    user1 = UserProfile(
        name="Alice Smith",
        age=28,
        email="alice@example.com",
        bio="Software engineer and coffee enthusiast"
    )
    print("✅ Valid user:", user1.model_dump())
    
    # Missing optional field (bio) - should work
    user2 = UserProfile(
        name="Bob Johnson",
        age=35,
        email="bob@example.com"
    )
    print("✅ Valid user (no bio):", user2.model_dump())
    
    # Invalid data - will raise ValidationError
    try:
        user3 = UserProfile(
            name="Charlie",
            age=200,  # Too old!
            email="not-an-email"  # Invalid email!
        )
    except Exception as e:
        print("❌ Validation error (expected):", str(e)[:100])

if __name__ == "__main__":
    test_model()
```

**Run it:**
```bash
python exercise_1.py
```

**Expected output:**
```
✅ Valid user: {'name': 'Alice Smith', 'age': 28, 'email': 'alice@example.com', 'bio': 'Software engineer...'}
✅ Valid user (no bio): {'name': 'Bob Johnson', 'age': 35, 'email': 'bob@example.com', 'bio': None}
❌ Validation error (expected): 2 validation errors for UserProfile
  age
    Input should be less than or equal to...
```

### Step 2: Use Model with OpenAI Structured Outputs

**Add this function to `exercise_1.py`:**

```python
def extract_user_profile_from_text(text: str) -> UserProfile:
    """Extract user profile from text using structured outputs"""
    
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": "Extract user profile information from the text."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        response_format=UserProfile
    )
    
    # The response is already parsed as a UserProfile object!
    return response.choices[0].message.parsed

# Test it
if __name__ == "__main__":
    test_model()
    print("\n--- Testing with AI Extraction ---\n")
    
    sample_text = """
    Hi, I'm Jane Doe, a 32-year-old data scientist. 
    You can reach me at jane.doe@techcorp.com. 
    I love working with Python and machine learning!
    """
    
    profile = extract_user_profile_from_text(sample_text)
    print("Extracted profile:")
    print(f"  Name: {profile.name}")
    print(f"  Age: {profile.age}")
    print(f"  Email: {profile.email}")
    print(f"  Bio: {profile.bio}")
```

**Run it again:**
```bash
python exercise_1.py
```

**Expected output:**
```
Extracted profile:
  Name: Jane Doe
  Age: 32
  Email: jane.doe@techcorp.com
  Bio: Data scientist who loves working with Python and machine learning
```

### ✅ Checkpoint

You've learned:
- ✅ How to create a Pydantic model with type annotations
- ✅ How to use `Field` for descriptions and validation
- ✅ How to use structured outputs with OpenAI's `parse` method
- ✅ The difference between manual validation and AI extraction

---

## 4. Exercise 2: Contact Extraction

### Objective
Extract structured contact information from emails or messages.

### Step 1: Define Contact Model

**File: `exercise_2.py`**

```python
from pydantic import BaseModel, EmailStr, Field
from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import Literal

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Contact(BaseModel):
    """Contact information extracted from text"""
    name: str = Field(description="Full name of the contact")
    email: EmailStr = Field(description="Email address")
    phone: str | None = Field(default=None, description="Phone number (if provided)")
    company: str | None = Field(default=None, description="Company or organization")
    role: str | None = Field(default=None, description="Job title or role")
    contact_reason: Literal["inquiry", "support", "sales", "other"] = Field(
        default="other",
        description="Reason for contact"
    )

def extract_contact(text: str) -> Contact:
    """Extract contact info from text"""
    
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": "You are a contact information extractor. Extract all relevant contact details from the message."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        response_format=Contact
    )
    
    return response.choices[0].message.parsed

# Test with sample emails
if __name__ == "__main__":
    test_cases = [
        """
        Hi there,
        
        I'm John Smith from TechCorp Inc. I'm the VP of Engineering 
        and I'm interested in learning more about your product. 
        You can reach me at john.smith@techcorp.com or 555-123-4567.
        
        Thanks,
        John
        """,
        
        """
        Hello! I'm Sarah Johnson, a freelance designer. 
        Contact me at sarah@designstudio.com if you need help 
        with your website redesign. I'd love to discuss your project!
        """,
        
        """
        Support request: My account isn't working. 
        Email me back at customer@example.com.
        - Alex
        """
    ]
    
    for i, email_text in enumerate(test_cases, 1):
        print(f"\n--- Email {i} ---")
        print(email_text.strip())
        print("\n--- Extracted Contact ---")
        
        contact = extract_contact(email_text)
        print(f"Name: {contact.name}")
        print(f"Email: {contact.email}")
        print(f"Phone: {contact.phone or 'Not provided'}")
        print(f"Company: {contact.company or 'Not provided'}")
        print(f"Role: {contact.role or 'Not provided'}")
        print(f"Contact Reason: {contact.contact_reason}")
```

**Run it:**
```bash
python exercise_2.py
```

### Step 2: Add Validation and Business Logic

**Add this to `exercise_2.py`:**

```python
from pydantic import validator

class Contact(BaseModel):
    """Contact information with validation"""
    name: str = Field(description="Full name of the contact")
    email: EmailStr = Field(description="Email address")
    phone: str | None = Field(default=None, description="Phone number")
    company: str | None = Field(default=None, description="Company name")
    role: str | None = Field(default=None, description="Job title")
    contact_reason: Literal["inquiry", "support", "sales", "other"] = Field(
        default="other"
    )
    priority: Literal["high", "medium", "low"] = Field(
        default="medium",
        description="Priority level based on role and reason"
    )
    
    @validator('phone')
    def clean_phone(cls, v):
        """Remove non-numeric characters from phone"""
        if v:
            return ''.join(filter(str.isdigit, v))
        return v
    
    def is_high_priority(self) -> bool:
        """Check if this is a high-priority contact"""
        high_priority_roles = ["ceo", "cto", "vp", "director", "founder"]
        if self.role:
            return any(title in self.role.lower() for title in high_priority_roles)
        return False
    
    def get_crm_category(self) -> str:
        """Categorize contact for CRM system"""
        if self.contact_reason == "sales":
            return "Lead"
        elif self.contact_reason == "support":
            return "Support Ticket"
        elif self.contact_reason == "inquiry":
            return "Prospect"
        else:
            return "General Contact"
```

### ✅ Checkpoint

You've learned:
- ✅ How to use `Literal` types for restricted values
- ✅ How to use `validator` for custom validation logic
- ✅ How to add methods to Pydantic models for business logic
- ✅ How to handle optional fields with `| None` syntax

---

## 5. Exercise 3: Nested Data Structures

### Objective
Work with complex, nested Pydantic models for real-world data structures.

### Step 1: Define Nested Models

**File: `exercise_3.py`**

```python
from pydantic import BaseModel, Field
from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import List

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Address(BaseModel):
    """Physical address"""
    street: str
    city: str
    state: str
    zip_code: str
    country: str = "USA"

class SocialMedia(BaseModel):
    """Social media profile"""
    platform: str
    username: str
    url: str | None = None

class Company(BaseModel):
    """Company information"""
    name: str
    website: str | None = None
    industry: str | None = None
    size: str | None = Field(
        default=None,
        description="Company size: small, medium, large, enterprise"
    )

class EnhancedContact(BaseModel):
    """Enhanced contact with nested data"""
    name: str
    email: str
    phone: str | None = None
    company: Company | None = None
    address: Address | None = None
    social_media: List[SocialMedia] = Field(default_factory=list)
    interests: List[str] = Field(
        default_factory=list,
        description="List of professional interests or skills"
    )
    notes: str | None = Field(
        default=None,
        description="Additional notes or context"
    )

def extract_enhanced_contact(text: str) -> EnhancedContact:
    """Extract detailed contact info with nested structures"""
    
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": "Extract comprehensive contact information including company details, address, social media, and interests. Return all available information in structured format."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        response_format=EnhancedContact
    )
    
    return response.choices[0].message.parsed

# Test with rich contact data
if __name__ == "__main__":
    sample_bio = """
    Emily Chen is the Director of Product at DataViz Inc., a medium-sized 
    data analytics company based at 123 Tech Street, San Francisco, CA 94105.
    
    She's passionate about machine learning, data visualization, and UX design.
    Emily graduated from Stanford with a degree in Computer Science.
    
    You can find her on Twitter @emilychen and LinkedIn at linkedin.com/in/emilychen.
    Her email is emily.chen@dataviz.com and phone is 415-555-0123.
    
    DataViz Inc. specializes in business intelligence tools and has a presence
    at www.dataviz.com.
    """
    
    print("--- Extracting from bio ---\n")
    print(sample_bio)
    
    contact = extract_enhanced_contact(sample_bio)
    
    print("\n--- Extracted Enhanced Contact ---\n")
    print(f"Name: {contact.name}")
    print(f"Email: {contact.email}")
    print(f"Phone: {contact.phone}")
    
    if contact.company:
        print(f"\nCompany:")
        print(f"  Name: {contact.company.name}")
        print(f"  Website: {contact.company.website}")
        print(f"  Industry: {contact.company.industry}")
        print(f"  Size: {contact.company.size}")
    
    if contact.address:
        print(f"\nAddress:")
        print(f"  {contact.address.street}")
        print(f"  {contact.address.city}, {contact.address.state} {contact.address.zip_code}")
    
    if contact.social_media:
        print(f"\nSocial Media:")
        for social in contact.social_media:
            print(f"  {social.platform}: {social.username}")
    
    if contact.interests:
        print(f"\nInterests: {', '.join(contact.interests)}")
    
    if contact.notes:
        print(f"\nNotes: {contact.notes}")
```

**Run it:**
```bash
python exercise_3.py
```

### Step 2: Serialize to Database

**Add this to `exercise_3.py`:**

```python
import json

def save_contact_to_json(contact: EnhancedContact, filename: str):
    """Save contact to JSON file"""
    with open(filename, 'w') as f:
        json.dump(contact.model_dump(), f, indent=2)
    print(f"✅ Saved contact to {filename}")

def load_contact_from_json(filename: str) -> EnhancedContact:
    """Load contact from JSON file"""
    with open(filename, 'r') as f:
        data = json.load(f)
    return EnhancedContact(**data)

# Add to main block
if __name__ == "__main__":
    # ... (previous code)
    
    # Save and load
    save_contact_to_json(contact, "contact.json")
    loaded_contact = load_contact_from_json("contact.json")
    print(f"\n✅ Loaded contact: {loaded_contact.name}")
```

### ✅ Checkpoint

You've learned:
- ✅ How to create nested Pydantic models
- ✅ How to use `List` types for arrays
- ✅ How to serialize models to JSON for database storage
- ✅ How to deserialize JSON back to Pydantic objects

---

## 6. Exercise 4: Review Analysis

### Objective
Build a product review analyzer that extracts sentiment, topics, and actionable insights.

### Complete Implementation

**File: `exercise_4.py`**

```python
from pydantic import BaseModel, Field
from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import List, Literal

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ReviewAnalysis(BaseModel):
    """Structured analysis of a product review"""
    
    # Sentiment
    sentiment: Literal["positive", "negative", "neutral", "mixed"] = Field(
        description="Overall sentiment of the review"
    )
    rating_prediction: int = Field(
        description="Predicted star rating (1-5) based on review text",
        ge=1,
        le=5
    )
    
    # Topics
    key_topics: List[str] = Field(
        description="Main topics mentioned (e.g., 'quality', 'price', 'shipping')"
    )
    
    # Specific feedback
    pros: List[str] = Field(
        default_factory=list,
        description="Positive aspects mentioned"
    )
    cons: List[str] = Field(
        default_factory=list,
        description="Negative aspects mentioned"
    )
    
    # Actionable insights
    is_spam: bool = Field(
        default=False,
        description="Whether this review appears to be spam"
    )
    needs_response: bool = Field(
        description="Whether this review requires a company response"
    )
    urgency: Literal["low", "medium", "high"] = Field(
        description="Response urgency level"
    )
    
    # Structured data extraction
    mentioned_features: List[str] = Field(
        default_factory=list,
        description="Specific product features mentioned"
    )
    comparison_to_competitors: str | None = Field(
        default=None,
        description="Competitor comparisons if mentioned"
    )
    
    # Summary
    one_sentence_summary: str = Field(
        description="Brief one-sentence summary of the review"
    )

def analyze_review(review_text: str) -> ReviewAnalysis:
    """Analyze a product review and extract structured insights"""
    
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": """You are a product review analyzer. Extract sentiment, topics, 
                pros/cons, and determine if the review needs a response. Be thorough and accurate."""
            },
            {
                "role": "user",
                "content": f"Analyze this product review:\n\n{review_text}"
            }
        ],
        response_format=ReviewAnalysis
    )
    
    return response.choices[0].message.parsed

# Test with different review types
if __name__ == "__main__":
    reviews = [
        {
            "text": """
            This laptop is amazing! The battery life easily lasts 12 hours, and the 
            screen is incredibly sharp. Setup was a breeze. My only complaint is that 
            it's a bit pricey compared to competitors, but you definitely get what you 
            pay for. Would recommend to anyone needing a reliable work machine.
            """,
            "expected_sentiment": "positive"
        },
        {
            "text": """
            Terrible experience. The product arrived damaged, customer service was 
            unhelpful, and it stopped working after just 2 weeks. Complete waste of 
            money. I'm demanding a full refund. Do NOT buy this.
            """,
            "expected_sentiment": "negative"
        },
        {
            "text": """
            It's okay. Does what it's supposed to do. Nothing special, but nothing 
            terrible either. Price is reasonable. Shipping took a while but arrived 
            safely. 3 stars.
            """,
            "expected_sentiment": "neutral"
        }
    ]
    
    for i, review in enumerate(reviews, 1):
        print(f"\n{'='*60}")
        print(f"REVIEW {i}")
        print(f"{'='*60}")
        print(review["text"].strip())
        
        analysis = analyze_review(review["text"])
        
        print(f"\n--- Analysis ---")
        print(f"Sentiment: {analysis.sentiment} (predicted rating: {analysis.rating_prediction}/5)")
        print(f"One-sentence summary: {analysis.one_sentence_summary}")
        print(f"\nKey Topics: {', '.join(analysis.key_topics)}")
        
        if analysis.pros:
            print(f"\nPros:")
            for pro in analysis.pros:
                print(f"  ✅ {pro}")
        
        if analysis.cons:
            print(f"\nCons:")
            for con in analysis.cons:
                print(f"  ❌ {con}")
        
        if analysis.mentioned_features:
            print(f"\nMentioned Features: {', '.join(analysis.mentioned_features)}")
        
        print(f"\n🚨 Needs Response: {'YES' if analysis.needs_response else 'No'}")
        print(f"⏰ Urgency: {analysis.urgency}")
        print(f"🛡️ Is Spam: {'YES' if analysis.is_spam else 'No'}")
```

**Run it:**
```bash
python exercise_4.py
```

### ✅ Checkpoint

You've learned:
- ✅ How to model complex business logic with Pydantic
- ✅ How to extract actionable insights from unstructured text
- ✅ How to use boolean flags for decision-making
- ✅ How to create comprehensive analysis systems

---

## 7. Exercise 5: Multi-Entity Extraction

### Objective
Extract multiple entities of different types from a single document.

### Complete Implementation

**File: `exercise_5.py`**

```python
from pydantic import BaseModel, Field
from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import List
from datetime import date

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Person(BaseModel):
    """A person mentioned in the document"""
    name: str
    role: str | None = None
    organization: str | None = None

class Event(BaseModel):
    """An event mentioned in the document"""
    name: str
    date: str = Field(description="Date in YYYY-MM-DD format if specified")
    location: str | None = None
    description: str | None = None

class Product(BaseModel):
    """A product or service mentioned"""
    name: str
    category: str | None = None
    price: float | None = Field(default=None, description="Price if mentioned")
    features: List[str] = Field(default_factory=list)

class Organization(BaseModel):
    """An organization or company"""
    name: str
    type: str | None = Field(
        default=None,
        description="Type: company, nonprofit, government, etc."
    )
    industry: str | None = None

class DocumentEntities(BaseModel):
    """All entities extracted from a document"""
    
    people: List[Person] = Field(
        default_factory=list,
        description="All people mentioned in the document"
    )
    events: List[Event] = Field(
        default_factory=list,
        description="All events mentioned"
    )
    products: List[Product] = Field(
        default_factory=list,
        description="All products or services mentioned"
    )
    organizations: List[Organization] = Field(
        default_factory=list,
        description="All organizations mentioned"
    )
    
    # Document metadata
    main_topic: str = Field(description="Primary topic of the document")
    key_takeaways: List[str] = Field(
        description="3-5 key takeaways from the document"
    )
    document_type: str = Field(
        description="Type of document: article, press release, email, report, etc."
    )

def extract_entities(document_text: str) -> DocumentEntities:
    """Extract all entities from a document"""
    
    response = client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system",
                "content": """You are an entity extraction system. Extract all people, 
                events, products, and organizations mentioned in the document. Be thorough 
                and accurate. Include as much detail as available."""
            },
            {
                "role": "user",
                "content": f"Extract entities from this document:\n\n{document_text}"
            }
        ],
        response_format=DocumentEntities
    )
    
    return response.choices[0].message.parsed

# Test with a complex document
if __name__ == "__main__":
    sample_document = """
    TechCorp Inc. Announces Partnership with DataFlow Solutions
    
    San Francisco, CA - October 15, 2024
    
    TechCorp Inc., a leading enterprise software company, today announced a strategic 
    partnership with DataFlow Solutions, a Boston-based data analytics startup. The 
    partnership will integrate DataFlow's AI-powered analytics platform, DataInsight Pro, 
    into TechCorp's flagship product, EnterpriseHub.
    
    "This partnership represents a major milestone for both companies," said Jennifer 
    Martinez, CEO of TechCorp Inc. "DataFlow's cutting-edge technology will enhance 
    our customers' ability to make data-driven decisions."
    
    Dr. Robert Chen, CTO of DataFlow Solutions, added: "We're excited to bring our 
    technology to TechCorp's extensive customer base of over 10,000 enterprises."
    
    The integration is expected to launch in Q1 2025, with pricing starting at $99 
    per user per month. Both companies will showcase the integrated solution at the 
    upcoming DataSummit conference in New York on November 20-22, 2024.
    
    Key features of the integration include:
    - Real-time data visualization
    - Predictive analytics powered by machine learning
    - Automated report generation
    - Custom dashboard creation
    
    About TechCorp Inc.:
    Founded in 2010, TechCorp is a leading provider of enterprise software solutions 
    in the SaaS industry, serving Fortune 500 companies worldwide.
    
    About DataFlow Solutions:
    DataFlow Solutions is a data analytics company specializing in AI-powered business 
    intelligence tools for the technology sector.
    """
    
    print("Extracting entities from press release...\n")
    
    entities = extract_entities(sample_document)
    
    print("="*60)
    print("ENTITY EXTRACTION RESULTS")
    print("="*60)
    
    print(f"\n📄 Document Type: {entities.document_type}")
    print(f"📌 Main Topic: {entities.main_topic}")
    
    print(f"\n🔑 Key Takeaways:")
    for i, takeaway in enumerate(entities.key_takeaways, 1):
        print(f"  {i}. {takeaway}")
    
    print(f"\n👥 People ({len(entities.people)}):")
    for person in entities.people:
        print(f"  • {person.name}")
        if person.role:
            print(f"    Role: {person.role}")
        if person.organization:
            print(f"    Organization: {person.organization}")
    
    print(f"\n🏢 Organizations ({len(entities.organizations)}):")
    for org in entities.organizations:
        print(f"  • {org.name}")
        if org.type:
            print(f"    Type: {org.type}")
        if org.industry:
            print(f"    Industry: {org.industry}")
    
    print(f"\n📦 Products ({len(entities.products)}):")
    for product in entities.products:
        print(f"  • {product.name}")
        if product.category:
            print(f"    Category: {product.category}")
        if product.price:
            print(f"    Price: ${product.price}")
        if product.features:
            print(f"    Features:")
            for feature in product.features:
                print(f"      - {feature}")
    
    print(f"\n📅 Events ({len(entities.events)}):")
    for event in entities.events:
        print(f"  • {event.name}")
        print(f"    Date: {event.date}")
        if event.location:
            print(f"    Location: {event.location}")
        if event.description:
            print(f"    Description: {event.description}")
```

**Run it:**
```bash
python exercise_5.py
```

### ✅ Checkpoint

You've learned:
- ✅ How to extract multiple entity types from complex documents
- ✅ How to work with lists of Pydantic models
- ✅ How to structure data for knowledge graph construction
- ✅ How to handle document-level metadata

---

## 8. Capstone Integration

### Your Turn: Create a Model for Your Project

Now apply what you've learned to your capstone project!

### Step 1: Identify Your Use Case

What structured data does your project need to extract? Examples:

- **Recipe app:** Recipe model with ingredients, steps, nutrition info
- **Study buddy:** Question model with topic, difficulty, answer
- **Customer support:** Ticket model with category, priority, sentiment
- **Code reviewer:** CodeIssue model with severity, file, line number
- **Content moderator:** ContentAnalysis model with safety scores, topics

### Step 2: Design Your Model

**File: `capstone_model.py`**

```python
from pydantic import BaseModel, Field
from typing import List, Literal

# REPLACE THIS WITH YOUR ACTUAL USE CASE
class YourCapstoneModel(BaseModel):
    """
    TODO: Replace with your capstone project's data model
    
    Example for a recipe app:
    """
    recipe_name: str = Field(description="Name of the recipe")
    cuisine: str = Field(description="Type of cuisine")
    difficulty: Literal["easy", "medium", "hard"] = Field(
        description="Difficulty level"
    )
    prep_time_minutes: int = Field(description="Preparation time in minutes", ge=0)
    cook_time_minutes: int = Field(description="Cooking time in minutes", ge=0)
    servings: int = Field(description="Number of servings", ge=1)
    
    ingredients: List[str] = Field(
        description="List of ingredients with quantities"
    )
    instructions: List[str] = Field(
        description="Step-by-step cooking instructions"
    )
    
    dietary_tags: List[Literal["vegetarian", "vegan", "gluten-free", "dairy-free", "nut-free"]] = Field(
        default_factory=list,
        description="Dietary restriction tags"
    )
    
    nutrition_info: dict | None = Field(
        default=None,
        description="Optional nutrition information"
    )

# TODO: Add your extraction function here
def extract_your_data(text: str) -> YourCapstoneModel:
    """Extract structured data for your capstone project"""
    # Implement using patterns from exercises above
    pass
```

### Step 3: Test with Real Data

Create test cases from your capstone project:

```python
# Add to capstone_model.py
if __name__ == "__main__":
    # Test with real data from your project
    sample_input = """
    [Replace with actual sample input for your project]
    """
    
    result = extract_your_data(sample_input)
    print(result.model_dump_json(indent=2))
```

### Step 4: Integrate into Your Capstone

**Where to use structured outputs in your capstone:**

1. **User input processing:** Parse and validate user requests
2. **API responses:** Return consistent JSON structures
3. **Database writes:** Ensure data integrity before saving
4. **Multi-agent coordination:** Structure messages between agents
5. **Evaluation:** Extract metrics from test outputs

**Example integration:**

```python
# In your capstone project's main API endpoint
from fastapi import FastAPI, HTTPException
from capstone_model import YourCapstoneModel, extract_your_data

app = FastAPI()

@app.post("/extract", response_model=YourCapstoneModel)
async def extract_endpoint(text: str):
    """API endpoint using structured outputs"""
    try:
        result = extract_your_data(text)
        
        # Save to database
        db.save(result.model_dump())
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

---

## 9. Troubleshooting

### Common Issues and Solutions

#### Issue 1: "ImportError: cannot import name 'EmailStr'"

**Solution:**
```bash
pip install pydantic[email] --break-system-packages
```

#### Issue 2: "Model doesn't have required fields"

**Problem:** LLM didn't extract all required fields.

**Solution:** Make fields optional with `| None` or add descriptions:

```python
class MyModel(BaseModel):
    required_field: str
    optional_field: str | None = Field(
        default=None,
        description="Detailed description helps LLM extract this"
    )
```

#### Issue 3: "Validation error: value is not a valid email"

**Problem:** LLM returned invalid email format.

**Solution:** Use custom validator or change to regular `str`:

```python
from pydantic import validator

class Contact(BaseModel):
    email: str  # Use str instead of EmailStr
    
    @validator('email')
    def validate_email(cls, v):
        if '@' not in v:
            # Try to fix common issues
            if 'at' in v:
                v = v.replace(' at ', '@')
        return v
```

#### Issue 4: "API returns refusal or doesn't follow schema"

**Problem:** Content policy violation or ambiguous prompt.

**Solutions:**
1. **Check content:** Ensure input doesn't violate policies
2. **Improve system prompt:** Be more specific about extraction rules
3. **Use examples:** Add few-shot examples in prompt
4. **Handle refusals:**

```python
response = client.beta.chat.completions.parse(...)

if response.choices[0].message.refusal:
    print(f"LLM refused: {response.choices[0].message.refusal}")
    # Handle refusal case
else:
    result = response.choices[0].message.parsed
```

#### Issue 5: "Cost is too high"

**Solutions:**
1. Use `gpt-4o-mini` instead of `gpt-4o` (5x cheaper)
2. Reduce system prompt length
3. Cache common extractions
4. Use smaller context windows

```python
# Use cheaper model
model="gpt-4o-mini-2024-07-18"  # vs. "gpt-4o-2024-08-06"
```

---

## 10. Additional Resources

### Documentation

**Pydantic:**
- Official docs: https://docs.pydantic.dev/
- Field validation: https://docs.pydantic.dev/latest/concepts/validators/
- JSON Schema: https://docs.pydantic.dev/latest/concepts/json_schema/

**OpenAI Structured Outputs:**
- Guide: https://platform.openai.com/docs/guides/structured-outputs
- API reference: https://platform.openai.com/docs/api-reference/chat/create

### Best Practices

1. **Start simple:** Begin with basic models, add complexity gradually
2. **Use descriptions:** Field descriptions help the LLM extract correctly
3. **Validate early:** Test models manually before using with AI
4. **Handle errors:** Always check for `refusal` and validation errors
5. **Document your models:** Add docstrings and examples
6. **Version your schemas:** Track changes to models over time
7. **Test edge cases:** What happens with missing data? Invalid formats?

### Advanced Topics (Optional)

**Custom validators:**
```python
from pydantic import validator

class MyModel(BaseModel):
    price: float
    
    @validator('price')
    def price_must_be_positive(cls, v):
        if v <= 0:
            raise ValueError('Price must be positive')
        return v
```

**Model inheritance:**
```python
class BaseContact(BaseModel):
    name: str
    email: str

class ExtendedContact(BaseContact):
    phone: str
    company: str
```

**Dynamic models:**
```python
def create_model_from_schema(schema: dict) -> BaseModel:
    # Create Pydantic model dynamically from JSON schema
    pass
```

---

## Homework Assignment

### Task: Create 3 Pydantic Models for Your Capstone

**Due:** End of Week 6  
**Points:** Part of Lab 6 grade  
**Deliverables:** Python file with 3 models + tests

### Requirements

Create **three Pydantic models** that you'll use in your capstone project:

1. **Input Model:** Structure for user input/requests
2. **Output Model:** Structure for your system's responses
3. **Internal Model:** Structure for data you'll store/process

Each model must have:
- [ ] At least 5 fields with appropriate types
- [ ] At least 2 optional fields with defaults
- [ ] Descriptive field descriptions
- [ ] At least 1 validation rule (validator or Field constraint)
- [ ] A docstring explaining the model's purpose

### Submission Format

**File: `capstone_pydantic_models.py`**

```python
"""
Pydantic Models for [Your Capstone Project Name]
Team: [Team Members]
Week 6 Lab Homework
"""

from pydantic import BaseModel, Field
# ... other imports

# Model 1: Input
class YourInputModel(BaseModel):
    """[Description of what this model represents]"""
    # Your fields here
    pass

# Model 2: Output  
class YourOutputModel(BaseModel):
    """[Description]"""
    # Your fields here
    pass

# Model 3: Internal
class YourInternalModel(BaseModel):
    """[Description]"""
    # Your fields here
    pass

# Tests
if __name__ == "__main__":
    # Test each model with sample data
    # Show that validation works
    pass
```

### Grading Rubric

| Criteria | Points |
|----------|--------|
| Three complete models | 30% |
| Appropriate field types | 20% |
| Validation rules | 20% |
| Documentation (docstrings, descriptions) | 15% |
| Working tests | 15% |

### Example Submission

See `capstone_model.py` for a complete example.

---

## Lab Complete! 🎉

You've learned how to:
- ✅ Create Pydantic models for data validation
- ✅ Use structured outputs with OpenAI
- ✅ Extract complex entities from text
- ✅ Build production-ready data pipelines
- ✅ Integrate models into your capstone project

### Next Steps

1. **Complete homework:** Create 3 models for your capstone
2. **Integrate into capstone:** Replace manual parsing with Pydantic
3. **Week 7:** User testing with structured outputs
4. **Week 8:** Iterate based on feedback

### Questions?

- **Office hours:** [Time and location]
- **Discord:** #week-6-pydantic channel
- **Email:** zeshan.ahmad@kiu.edu.ge

---

**Lab 6 Materials Created By:** Professor Zeshan Ahmad  
**Course:** Building AI-Powered Applications (CS-AI-2025)  
**Institution:** Kutaisi International University
