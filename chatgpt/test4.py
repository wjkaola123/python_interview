from google import genai
from PIL import Image

client = genai.Client(api_key="AIzaSyCp5BwMYEzozwnV7gUOYjHMMr0lGT6Vbjk")
image = Image.open('123.jpg')

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=[image, 'Describe this image in detail.'],
)

print(response.text)