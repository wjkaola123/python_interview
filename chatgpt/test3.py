from google import genai

client = genai.Client(api_key="AIzaSyCp5BwMYEzozwnV7gUOYjHMMr0lGT6Vbjk")

response = client.models.generate_content(
    model="gemini-3-flash-preview", contents="Why is the sky blue?"
)
print(response.text)