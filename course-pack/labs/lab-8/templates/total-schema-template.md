from pydantic import BaseModel, validator, Field
from typing import Optional, List

class SearchToolInput(BaseModel):
    """
    Input schema for search tool.
    Agent must provide these parameters to use the tool.
    """
    query: str = Field(
        ...,
        description="The search query string",
        min_length=1,
        max_length=500
    )
    
    max_results: int = Field(
        default=10,
        description="Maximum number of results to return",
        ge=1,  # greater than or equal to 1
        le=100  # less than or equal to 100
    )
    
    filters: Optional[List[str]] = Field(
        default=None,
        description="Optional filters to apply"
    )
    
    @validator('query')
    def query_not_empty(cls, v):
        """Ensure query is not just whitespace."""
        if not v or len(v.strip()) == 0:
            raise ValueError('Query cannot be empty')
        return v.strip()
    
    @validator('filters')
    def validate_filters(cls, v):
        """Ensure filters are valid."""
        if v is not None:
            valid_filters = {'recent', 'popular', 'academic'}
            for f in v:
                if f not in valid_filters:
                    raise ValueError(f'Invalid filter: {f}')
        return v


class SearchToolOutput(BaseModel):
    """
    Output schema for search tool.
    Ensures tool returns consistent structure.
    """
    status: str = Field(..., description="success or error")
    results: List[dict] = Field(default=[], description="List of results")
    count: int = Field(..., description="Number of results returned")
    error: Optional[str] = Field(default=None, description="Error message if failed")


# Usage in agent:
def search_tool(args: dict) -> dict:
    """Execute search with validated inputs."""
    try:
        # Validate input
        validated_input = SearchToolInput(**args)
        
        # Execute search
        results = perform_search(
            validated_input.query,
            validated_input.max_results,
            validated_input.filters
        )
        
        # Return validated output
        output = SearchToolOutput(
            status="success",
            results=results,
            count=len(results)
        )
        
        return output.dict()
        
    except ValidationError as e:
        return {
            "status": "error",
            "results": [],
            "count": 0,
            "error": str(e)
        }
