"""
Pydantic Models Template
Week 5 | Building AI-Powered Applications

This file contains example Pydantic models for common use cases.
Copy and modify these for your specific project needs.

Installation: pip install pydantic
"""

from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import List, Literal, Optional, Dict, Any
from datetime import datetime
from enum import Enum

# ========================================
# EXAMPLE 1: USER MODELS
# ========================================

class UserProfile(BaseModel):
    """
    User profile information
    
    Use this for: User registration, profile updates, authentication responses
    """
    user_id: str = Field(description="Unique user identifier")
    name: str = Field(min_length=1, max_length=100, description="User's full name")
    email: EmailStr = Field(description="User's email address")
    age: int = Field(ge=13, le=120, description="User's age, must be 13+")
    interests: List[str] = Field(
        default_factory=list,
        max_length=10,
        description="List of user interests (max 10)"
    )
    account_type: Literal["free", "pro", "enterprise"] = Field(
        default="free",
        description="User's subscription tier"
    )
    created_at: datetime = Field(default_factory=datetime.now)
    
    class Config:
        json_schema_extra = {
            "example": {
                "user_id": "user_123",
                "name": "Jane Smith",
                "email": "jane@example.com",
                "age": 25,
                "interests": ["AI", "programming", "music"],
                "account_type": "pro",
                "created_at": "2025-10-25T10:00:00Z"
            }
        }

# ========================================
# EXAMPLE 2: DOCUMENT/SEARCH MODELS
# ========================================

class SearchResult(BaseModel):
    """
    Single search result with source citation
    
    Use this for: RAG search results, document retrieval
    """
    document_id: str = Field(description="Unique document identifier")
    title: str = Field(description="Document title")
    excerpt: str = Field(
        max_length=500,
        description="Relevant excerpt from document"
    )
    relevance_score: float = Field(
        ge=0.0,
        le=1.0,
        description="Similarity score (0-1)"
    )
    source: str = Field(description="File path or URL to source")
    metadata: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Additional metadata (author, date, etc.)"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "document_id": "doc_456",
                "title": "Remote Work Policy",
                "excerpt": "Employees may work remotely up to 2 days per week...",
                "relevance_score": 0.92,
                "source": "/policies/remote-work.pdf",
                "metadata": {"page": 15, "section": "3.2"}
            }
        }


class SearchResponse(BaseModel):
    """
    Complete search response with multiple results
    
    Use this for: Returning search results from RAG system
    """
    query: str = Field(description="The original search query")
    results: List[SearchResult] = Field(
        default_factory=list,
        description="List of search results"
    )
    total_found: int = Field(ge=0, description="Total number of matches")
    search_time_ms: float = Field(ge=0, description="Search execution time in milliseconds")
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "remote work policy",
                "results": [
                    {
                        "document_id": "doc_456",
                        "title": "Remote Work Policy",
                        "excerpt": "...",
                        "relevance_score": 0.92,
                        "source": "/policies/remote-work.pdf"
                    }
                ],
                "total_found": 12,
                "search_time_ms": 145.3
            }
        }

# ========================================
# EXAMPLE 3: ORDER/E-COMMERCE MODELS
# ========================================

class OrderStatus(str, Enum):
    """Order status enumeration"""
    PENDING = "pending"
    PROCESSING = "processing"
    SHIPPED = "shipped"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"
    REFUNDED = "refunded"


class OrderDetails(BaseModel):
    """
    Order status and details
    
    Use this for: E-commerce order tracking, customer service bots
    """
    order_id: str = Field(
        pattern=r"^[A-Z0-9]{5,10}$",
        description="Order ID (5-10 alphanumeric characters)"
    )
    status: OrderStatus = Field(description="Current order status")
    customer_email: EmailStr = Field(description="Customer email address")
    items: List[str] = Field(
        min_length=1,
        description="List of item names in the order"
    )
    total: float = Field(ge=0, description="Order total in USD")
    created_at: datetime = Field(description="Order creation timestamp")
    estimated_delivery: Optional[datetime] = Field(
        default=None,
        description="Estimated delivery date (if shipped)"
    )
    tracking_number: Optional[str] = Field(
        default=None,
        description="Shipping tracking number (if shipped)"
    )
    
    @field_validator('tracking_number')
    @classmethod
    def validate_tracking(cls, v: Optional[str]) -> Optional[str]:
        """Validate tracking number format if provided"""
        if v is not None and len(v) < 5:
            raise ValueError("Tracking number must be at least 5 characters")
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "order_id": "ABC12345",
                "status": "shipped",
                "customer_email": "customer@example.com",
                "items": ["Widget A", "Gadget B"],
                "total": 149.99,
                "created_at": "2025-10-25T10:00:00Z",
                "estimated_delivery": "2025-11-02T17:00:00Z",
                "tracking_number": "1Z999AA1"
            }
        }

# ========================================
# EXAMPLE 4: CONTENT EXTRACTION MODELS
# ========================================

class DocumentExtraction(BaseModel):
    """
    Structured data extracted from a document
    
    Use this for: Document analysis, information extraction
    """
    title: str = Field(description="Document title")
    author: Optional[str] = Field(default=None, description="Document author if available")
    publication_date: Optional[datetime] = Field(default=None, description="Publication date")
    summary: str = Field(
        min_length=50,
        max_length=500,
        description="3-5 sentence summary"
    )
    key_topics: List[str] = Field(
        min_length=1,
        max_length=10,
        description="Main topics discussed (1-10 topics)"
    )
    sentiment: Literal["positive", "neutral", "negative"] = Field(
        description="Overall sentiment of the document"
    )
    entities: Optional[List[str]] = Field(
        default=None,
        description="Named entities mentioned (people, places, organizations)"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "The Future of AI in Healthcare",
                "author": "Dr. Jane Smith",
                "publication_date": "2025-10-15T00:00:00Z",
                "summary": "This paper explores how artificial intelligence is transforming healthcare delivery...",
                "key_topics": ["AI", "healthcare", "diagnostics", "patient care"],
                "sentiment": "positive",
                "entities": ["WHO", "Johns Hopkins", "Dr. Jane Smith"]
            }
        }

# ========================================
# EXAMPLE 5: FUNCTION CALL MODELS
# ========================================

class FunctionCallRequest(BaseModel):
    """
    Request to call a function (what AI sends)
    
    Use this for: Parsing function calls from LLM responses
    """
    function_name: str = Field(description="Name of the function to call")
    arguments: Dict[str, Any] = Field(
        default_factory=dict,
        description="Function arguments as key-value pairs"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "function_name": "check_order_status",
                "arguments": {
                    "order_id": "ABC12345",
                    "include_history": False
                }
            }
        }


class FunctionCallResponse(BaseModel):
    """
    Response from a function call (what we send back to AI)
    
    Use this for: Wrapping function results to send back to LLM
    """
    status: Literal["success", "error"] = Field(description="Function execution status")
    data: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Function result data (if success)"
    )
    error_code: Optional[str] = Field(
        default=None,
        description="Error code (if error)"
    )
    error_message: Optional[str] = Field(
        default=None,
        description="Human-readable error message (if error)"
    )
    execution_time_ms: float = Field(
        ge=0,
        description="Function execution time in milliseconds"
    )
    
    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "status": "success",
                    "data": {
                        "order_id": "ABC12345",
                        "status": "shipped"
                    },
                    "error_code": None,
                    "error_message": None,
                    "execution_time_ms": 145.2
                },
                {
                    "status": "error",
                    "data": None,
                    "error_code": "ORDER_NOT_FOUND",
                    "error_message": "No order found with ID XYZ99999",
                    "execution_time_ms": 23.5
                }
            ]
        }

# ========================================
# EXAMPLE 6: REVIEW/RATING MODELS
# ========================================

class ReviewAnalysis(BaseModel):
    """
    Sentiment and analysis of a review
    
    Use this for: Content moderation, review analysis
    """
    review_id: str = Field(description="Unique review identifier")
    sentiment: Literal["positive", "negative", "neutral", "mixed"] = Field(
        description="Overall sentiment"
    )
    rating_prediction: int = Field(
        ge=1,
        le=5,
        description="Predicted star rating (1-5)"
    )
    key_phrases: List[str] = Field(
        max_length=10,
        description="Important phrases from the review"
    )
    topics_mentioned: List[str] = Field(
        description="Topics discussed (e.g., 'customer service', 'shipping', 'quality')"
    )
    is_spam: bool = Field(description="Whether review appears to be spam")
    confidence_score: float = Field(
        ge=0.0,
        le=1.0,
        description="Confidence in the analysis (0-1)"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "review_id": "review_789",
                "sentiment": "positive",
                "rating_prediction": 5,
                "key_phrases": ["excellent service", "fast delivery", "high quality"],
                "topics_mentioned": ["customer service", "shipping", "product quality"],
                "is_spam": False,
                "confidence_score": 0.94
            }
        }

# ========================================
# EXAMPLE 7: ERROR RESPONSE MODEL
# ========================================

class ErrorResponse(BaseModel):
    """
    Standardized error response
    
    Use this for: Consistent error handling across your API
    """
    error_code: str = Field(description="Machine-readable error code")
    error_message: str = Field(description="Human-readable error message")
    details: Optional[Dict[str, Any]] = Field(
        default=None,
        description="Additional error details"
    )
    timestamp: datetime = Field(
        default_factory=datetime.now,
        description="When the error occurred"
    )
    request_id: Optional[str] = Field(
        default=None,
        description="Request ID for debugging"
    )
    
    class Config:
        json_schema_extra = {
            "example": {
                "error_code": "VALIDATION_ERROR",
                "error_message": "Invalid order ID format",
                "details": {
                    "field": "order_id",
                    "provided": "invalid!",
                    "expected": "5-10 alphanumeric characters"
                },
                "timestamp": "2025-10-31T15:30:00Z",
                "request_id": "req_abc123"
            }
        }

# ========================================
# USAGE EXAMPLES
# ========================================

if __name__ == "__main__":
    print("=" * 60)
    print("PYDANTIC MODELS - USAGE EXAMPLES")
    print("=" * 60)
    
    # Example 1: Create and validate a user profile
    print("\n1. Creating a User Profile:")
    user = UserProfile(
        user_id="user_001",
        name="John Doe",
        email="john@example.com",
        age=30,
        interests=["coding", "music"],
        account_type="pro"
    )
    print(user.model_dump_json(indent=2))
    
    # Example 2: Parse AI output into structured format
    print("\n2. Parsing Order Details from AI:")
    ai_output = {
        "order_id": "ABC12345",
        "status": "shipped",
        "customer_email": "customer@example.com",
        "items": ["Item 1", "Item 2"],
        "total": 99.99,
        "created_at": "2025-10-25T10:00:00Z",
        "estimated_delivery": "2025-11-02T17:00:00Z",
        "tracking_number": "1Z999AA1"
    }
    order = OrderDetails(**ai_output)
    print(f"Order {order.order_id} status: {order.status}")
    print(f"Arriving: {order.estimated_delivery}")
    
    # Example 3: Validation catches errors
    print("\n3. Validation Error Example:")
    try:
        bad_order = OrderDetails(
            order_id="INVALID!",  # Bad format
            status="shipped",
            customer_email="not-an-email",  # Invalid email
            items=[],  # Empty list not allowed
            total=-10,  # Negative not allowed
            created_at=datetime.now()
        )
    except Exception as e:
        print(f"❌ Validation failed (as expected):")
        print(f"   {str(e)[:100]}...")
    
    # Example 4: Search response
    print("\n4. Creating Search Response:")
    search = SearchResponse(
        query="remote work policy",
        results=[
            SearchResult(
                document_id="doc_1",
                title="Remote Work Guidelines",
                excerpt="Employees may work from home...",
                relevance_score=0.95,
                source="/policies/remote.pdf"
            )
        ],
        total_found=5,
        search_time_ms=142.5
    )
    print(f"Found {search.total_found} results in {search.search_time_ms}ms")
    
    # Example 5: Function call parsing
    print("\n5. Parsing Function Call from LLM:")
    function_call = FunctionCallRequest(
        function_name="check_order_status",
        arguments={"order_id": "ABC12345"}
    )
    print(f"Function: {function_call.function_name}")
    print(f"Arguments: {function_call.arguments}")
    
    # Example 6: Generate JSON Schema for LLM
    print("\n6. JSON Schema for OpenAI Function Calling:")
    schema = OrderDetails.model_json_schema()
    print("This schema can be passed to OpenAI's function calling API")
    print(f"Schema has {len(schema['properties'])} properties")
    
    print("\n" + "=" * 60)
    print("✅ All examples completed successfully!")
    print("=" * 60)

# ========================================
# TIPS FOR YOUR PROJECT
# ========================================

"""
TIPS FOR CREATING YOUR OWN MODELS:

1. **Start with your function return types**
   - Each function should return a Pydantic model
   - This ensures type safety and validation

2. **Use Field() for descriptions**
   - These descriptions appear in JSON schemas
   - LLMs use them to understand your data

3. **Add validation rules**
   - ge/le for numbers (greater/less than or equal)
   - min_length/max_length for strings
   - pattern for regex validation
   - Custom validators with @field_validator

4. **Provide examples**
   - Use Config.json_schema_extra for examples
   - Helps developers and LLMs understand format

5. **Use Literal and Enum for fixed options**
   - Better than plain strings
   - Catches typos at validation time

6. **Optional vs Required**
   - Optional[Type] = Field(default=None) for optional fields
   - No default = required field

7. **Nested models**
   - Models can contain other models
   - Example: OrderDetails contains List[OrderItem]

8. **Datetime handling**
   - Use datetime type for timestamps
   - Pydantic handles ISO format automatically

COMMON MISTAKES TO AVOID:

❌ Using "any" type without reason
❌ Forgetting descriptions (LLM won't understand)
❌ Not validating user inputs
❌ Making everything Optional (be specific!)
❌ Not providing example data

✅ DO THIS INSTEAD:
✅ Use specific types (str, int, Literal, Enum)
✅ Write clear descriptions for all fields
✅ Add validation rules (min, max, pattern)
✅ Mark fields as Optional only when truly optional
✅ Include examples in Config
"""
