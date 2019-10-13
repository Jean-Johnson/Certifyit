from PIL import Image, ImageDraw, ImageFont
x=-1
y=-1
def test(msg):
	global x,y
	#x,y=map(int, input(f"enter cords for the {msg}").split())
	x,y = 50,90
	image = Image.open('certificate.jpg')
	draw = ImageDraw.Draw(image)
	#font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
	color='rgb(0,0,0)'
	draw.text((x,y),msg,fill=color)
	image.save('save.jpg')
	image.show() #optional can be removed
if __name__=="__main__":
	while True:
		cho=int(input("1) Test image to get dimensions\n2)Add names\n"))
		if cho==1:
			test(input("enter the name"))
		else:
			print("[+]Enter the names:: \n")
			limit = 'a';
			names=[]
			while limit=='a':
				names.append(input("enter name :: \n"))
				cont = input("continue adding names? :: Y/N")
				if(cont=='Y'):
					continue
				else:
					break
			for name in names:
				test(name)
			break
