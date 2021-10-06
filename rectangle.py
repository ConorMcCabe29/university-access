from turtle import *

speed(0)

penup()
goto(-15, -50)
pendown()

color("brown")
begin_fill()

for i in range(2):
	forward(30)
	right(90)
	forward(40)
	right(90)
end_fill()

y = -50
width = 240
height = 25
begin_fill()
while width > 20:
	width = width - 25 # Smaller higher it goes
	x = 0 - width / 2 # start pos for x
	color("green")
	penup()
	goto(x, y)
	pendown()
	for i in range(2):
		forward(width)
		left(90)
		forward(height)
		left(90)
		y = y + height # increasing in lvls
end_fill()


