from google import genai
from google.genai import types
from pydantic import BaseModel

class Recipe(BaseModel):
    name: str
    description: str
    ingredients: list[str]
    steps: list[str]

client = genai.Client(api_key="AIzaSyCp5BwMYEzozwnV7gUOYjHMMr0lGT6Vbjk")

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents='Provide a classic recipe for chocolate chip cookies.',
    config=types.GenerateContentConfig(
        response_mime_type='application/json',
        response_schema=Recipe,
    ),
)

# response.text is guaranteed to be valid JSON matching the schema
print(response.text)

print('---' * 20)

# Access the response as a Pydantic object
parsed_response = response.parsed
print(parsed_response)