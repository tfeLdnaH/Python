from PIL import Image #FAILLLL

pill = Image.open("pill.jpg")
sensei = Image.open("sensei.jpg")

area = (100, 200, 100, 200)
sensei.paste(pill, area)

sensei.show()