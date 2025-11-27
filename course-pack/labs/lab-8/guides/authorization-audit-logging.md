"""
Quick Start: Minimal Production Agent
Copy and adapt this to your capstone.
"""

import openai
import logging
import json
from datetime import datetime
from tenacity import retry, stop_after_attempt, wait_exponential
from pydantic import BaseModel

class MinimalProductionAgent:
    """Minimal agent with essential safety features."""
    
    def __init__(self, tools, max_iterations=5, cost_limit=1.0):
        self.tools = tools
        self.max_iterations = max_iterations
        self.cost_limit = cost_limit
        self.total_cost = 0.0
        
        # Setup logging
        logging.basicConfig(
            filename='agent_audit.log',
            level=logging.INFO,
            format='%(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def run(self, user_query):
        """Execute agent with safety features."""
        messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_query}
        ]
        
        for iteration in range(self.max_iterations):
            # Check cost limit
            if self.total_cost >= self.cost_limit:
                return {
                    "success": False,
                    "result": "Cost limit exceeded",
                    "cost": self.total_cost
                }
            
            # Call LLM with timeout
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=messages,
                    tools=self.tools,
                    timeout=30
                )
                self.total_cost += 0.01  # Estimate, replace with actual
            except Exception as e:
                self.logger.error(f"LLM call failed: {e}")
                return {
                    "success": False,
                    "result": "Service error",
                    "cost": self.total_cost
                }
            
            message = response.choices[0].message
            
            # Done?
            if not message.tool_calls:
                return {
                    "success": True,
                    "result": message.content,
                    "cost": self.total_cost
                }
            
            # Execute tools
            messages.append(message)
            for tool_call in message.tool_calls:
                result = self._execute_tool(
                    tool_call.function.name,
                    tool_call.function.arguments
                )
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": json.dumps(result)
                })
        
        # Max iterations reached
        return {
            "success": False,
            "result": "Could not complete in time",
            "cost": self.total_cost
        }
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(min=1, max=10)
    )
    def _execute_tool(self, tool_name, args):
        """Execute tool with retry."""
        try:
            # TODO: Add your tool execution logic
            # TODO: Add authorization check
            # TODO: Add input validation
            # TODO: Add logging
            
            result = {"status": "success", "data": "..."}
            return result
        except Exception as e:
            self.logger.error(f"Tool {tool_name} failed: {e}")
            return {"error": str(e)}
