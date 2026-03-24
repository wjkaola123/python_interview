import time
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

# image = Image.open('cat.png') # Optional

# Video generation is an async operation
operation = client.models.generate_videos(
    model='veo-3.0-fast-generate-001',
    prompt='Panning wide shot of an alien creature is hunting a male lion in the sunshine, they have a fierce battle in the savannah, cinematic lighting, 8k resolution',
    # image=image,
    config=types.GenerateVideosConfig(
        # person_generation='allow_adult',  # 'dont_allow' or 'allow_adult'
        aspect_ratio='16:9',  # '16:9' or '9:16'
        number_of_videos=1, # supported value is 1-4, use 1 by default
        duration_seconds=8, # supported value is 5-8
    ),
)

# Poll for completion
while not operation.done:
    time.sleep(20)
    operation = client.operations.get(operation)

for n, generated_video in enumerate(operation.response.generated_videos):
    client.files.download(file=generated_video.video) # just file=, no need for path= as it doesn't save yet
    generated_video.video.save(f'cat{n}.mp4')  # saves the video