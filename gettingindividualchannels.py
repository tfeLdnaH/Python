from PIL import Image

sensei = Image.open("sensei.jpg")
#print(sensei.mode)
r, g, b = sensei.split()
#r.show()
#g.show()
#b.show()