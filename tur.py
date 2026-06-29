import turtle
import keyboard
import time
skk=turtle.Turtle()
print("a s w d")
wn=turtle.Screen()
wn.bgcolor("light blue")
wn.title("Turtle")
skk.write("Gagans Simulator",align="center",font=("Courier",20,"bold"))
a=None
pos=[]
direct="east"
i=0
while True:
	ctemp=(round(skk.xcor()),round(skk.ycor()))
	if ctemp in pos:
		print(f"Hit {i}")
		i+=1
		
	if keyboard.is_pressed('a'):
		if skk.heading()!=180:
			skk.setheading(180)
			skk.forward(50)
		else:
			skk.forward(50)	
	elif keyboard.is_pressed('s'):
		if skk.heading()!=270:
			skk.setheading(270)
			skk.forward(50)
		else:
			skk.forward(50)
	elif keyboard.is_pressed('w'):
		if skk.heading()!=90:
			skk.setheading(90)
			skk.forward(50)
		else:
			skk.forward(50)
	elif keyboard.is_pressed('d'):
		if skk.heading()!=0:
			skk.setheading(0)
			skk.forward(50)
		else:
			skk.forward(50)
	elif keyboard.is_pressed('q'):
		
		skk.write("O",font=("Courier",20,"bold"))
		x=round(skk.xcor())
		y=round(skk.ycor())
		tom=[x,y]
		pos.append(tom)
		
	elif keyboard.is_pressed('e'):
		break
	time.sleep(0.1)
skk.write("Byeee",align="left",font=("Courier",50,"bold"))
turtle.done()


#sudo ./venv/bin/python3 tur.py to run the program
