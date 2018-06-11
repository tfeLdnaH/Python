#from PIL import Image
#PIL is the old version and Pillow is new
from PIL import Image
img = Image.open("pill.jpg")
print(img.size)
print(img.format)

img.show()