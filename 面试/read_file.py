import struct
import tracemalloc
import base64

from PIL import Image

tracemalloc.start()

file_path = 'me.jpg'
with open(file_path, 'rb') as f:
    f_content = f.read()
    content = base64.b64encode(f_content)
# image = Image.open(file_path)
# print('width:', image.width)
# print('height:', image.height)
# print('size:', image.size)
# print('mode:', image.mode)
# print('format:', image.format)
# print('readonly:', image.readonly)
# print('info', image.info)

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")

for stat in top_stats[:10]:
    print(stat)
