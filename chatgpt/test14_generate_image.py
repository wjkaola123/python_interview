from google import genai
from google.genai import types
from PIL import Image

prompt =  "创建一张近距离观看海王星表面的图片, 以站在星球表面的视角生成，色彩鲜艳，细节丰富，8K分辨率。"

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=prompt,
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("star_3.png")