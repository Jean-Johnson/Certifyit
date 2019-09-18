from PIL import Image, ImageDraw, ImageFont
x=-1
y=-1
def test():
	loop=''
	print("[+]Press 'q' to quit testing")
	while loop!='q':
		global x,y
		x,y=map(int, input().split())
		image = Image.open('certificate.jpg')
		draw = ImageDraw.Draw(image)
#font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
		msg = "Jean"
		color='rgb(0,0,0)'
		draw.text((x,y),msg,fill=color)
		image.save('save.jpg')
		image.show()
		loop=input("[+]Enter q to quit")
if __name__=="__main__":
	while True:
		cho=int(input("1) Test image to get dimensions\n2)Add names\n"))
		if cho==1:
			test()
		else:
			print("under development")
			break
