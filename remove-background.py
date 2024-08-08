from PIL import Image
from rembg import remove

input = Image.open('img.png')

output = remove(input)

output.save('output.png')