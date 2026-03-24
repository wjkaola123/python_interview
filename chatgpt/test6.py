from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyCp5BwMYEzozwnV7gUOYjHMMr0lGT6Vbjk")

with open('video.mp4', 'rb') as f:
    video_bytes = f.read()

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=[
        types.Part.from_bytes(
            data=video_bytes,
            mime_type='video/mp4',
        ),
        '请用中文描述视频内容.'
    ]
)
print(response.text)