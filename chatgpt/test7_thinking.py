from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyCp5BwMYEzozwnV7gUOYjHMMr0lGT6Vbjk")

response = client.models.generate_content(
    model='gemini-3-pro-preview',
    contents='What is AI?',
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level=types.ThinkingLevel.HIGH
        )
    )
)

# Access thoughts if returned
for part in response.candidates[0].content.parts:
    if part.thought:
        print(f"Thought: {part.text}")
    else:
        print(f"Response: {part.text}")