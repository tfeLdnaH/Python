from PIL import Image
from PIL import ImageFilter

waterfall = Image.open("waterfall.jpg")

#black_white = waterfall.convert("L")#L = means black and white
#black_white.show()

blur = waterfall.filter(ImageFilter.BLUR)
detail = waterfall.filter(ImageFilter.DETAIL)
edges = waterfall.filter(ImageFilter.FIND_EDGES)
#blur.show()
#detail.show()
edges.show()