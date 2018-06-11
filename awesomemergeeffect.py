from PIL import Image #FAIL
#necessary the same size
sensei = Image.open("sensei.jpg")
waterfall = Image.open("pill.jpg")
r1, g1, b1 = sensei.split()
r2, g2, b2 = waterfall.split()

#new_img = Image.merge("RGB", (r, g, b))
#new_img = Image.merge("RGB", (b, g, r))

new_img = Image.merge("RGB", (r2, g1, b2))

new_img.show()