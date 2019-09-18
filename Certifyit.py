from PIL import Image, ImageDraw, ImageFont
image = Image.open('test.jpg')
draw = ImageDraw.Draw(image)
#font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
(x,y) = (50,50)
msg = "Jean"
color='rgb(0,0,0)'

draw.text((x,y),msg,fill=color)
image.save('save.jpg')
image.show()
