from google import genai
from PIL import Image
from io import BytesIO

client = genai.Client()

prompt = """
Create a picture of my dog eating a roast chicken in a fancy restaurant under the gemini constellation and here is a rabbit waiter serving him.
"""
image = Image.open('cat.png')

# Create the chat
chat = client.chats.create(model='gemini-2.5-flash-image')
# Send the image and ask for it to be edited
response = chat.send_message([prompt, image])

# Get the text and the image generated
for i, part in enumerate(response.candidates[0].content.parts):
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save(f'dog_{i}.png') # Multiple images can be generated

# Continue iterating
chat.send_message('Can you make it a bananas foster?')