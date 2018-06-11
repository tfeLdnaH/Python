from PIL import Image

sensei = Image.open("sensei.jpg")
square_sensei = sensei.resize((250, 250))

flip_sensei = sensei.transpose(Image.FLIP_LEFT_RIGHT)
spin_sensei = sensei.transpose(Image.ROTATE_90)

#square_sensei.show()
#sensei.show()
#flip_sensei.show()
#spin_sensei.show()