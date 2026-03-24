from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=[
        types.Content(role='user', parts=[types.Part.from_text(text='How does AI work?')]),
    ]
)
print(response.text)