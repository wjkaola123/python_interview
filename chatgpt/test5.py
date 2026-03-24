from google import genai

client = genai.Client(api_key="AIzaSyCp5BwMYEzozwnV7gUOYjHMMr0lGT6Vbjk")
# Upload
my_file = client.files.upload(file='video.mp4')

# Generate
response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=[my_file, 'What happens in this video?'],
)
print(response.text)

# You can delete files after use like this:
# client.files.delete(name=my_file.name)