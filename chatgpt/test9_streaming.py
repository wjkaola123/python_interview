from google import genai

client = genai.Client(api_key="AIzaSyCp5BwMYEzozwnV7gUOYjHMMr0lGT6Vbjk")

response = client.models.generate_content_stream(
    model='gemini-3-flash-preview',
    contents='写一个关于太空探索的短篇小说',
)

for chunk in response:
    print(chunk.text, end='')