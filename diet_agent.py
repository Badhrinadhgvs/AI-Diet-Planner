from phi.agent import Agent
from phi.model.groq import Groq
import re
# Set up Groq API Key (replace 'your_groq_api_key' with actual key)
import os

# Ensure the API key is properly set
GROQ_API_KEY = os.getenv("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")  # Ensure this is correctly loaded

if not GROQ_API_KEY:
    raise ValueError("Groq API key is missing. Set it in your environment variables.")

# Define the AI Agent
diet_agent = Agent(
    name="diet_ai",
    model=Groq(id="deepseek-r1-distill-llama-70b"),  # Choose the Groq model
    role="""
    You are a personalized diet planner. 
    - Ask for user details (age, weight, height, activity level, dietary restrictions).
    - Generate a detailed daily diet plan with calorie count.
    - Give nutritional advice based on user needs.
    - Recommend alternative foods based on preferences.
    """,
    instructions=["The Text should be less that 5 Lines","Provide a Detailed Table format of plan with time stamps"]
)
def clean_response(response_text):
    """Remove <think>...</think> from the AI response"""
    return re.sub(r"<think>.*?</think>", "", response_text, flags=re.DOTALL).strip()
def get_diet_plan(user_input):
    """Function to get diet plan from the AI agent."""
    response = diet_agent.run(user_input)
    return clean_response(response.content)
