from turtle import *

speed(0)
bgcolor("grey")
hideturtle()

penup()
goto(-15, -50)
pendown()

color("brown")
begin_fill()

# Tree trunk, make square then double it
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


# move pen to the other side
penup()
setpos(-300, 0)
pendown()


pencolor('pink')

# do curve
def curve():
    for i in range(200):
        right(1)
        forward(1)
        

# Ballsack
fillcolor("pink")
begin_fill()
circle(50)
end_fill()

# move pen to the other side
penup()
setpos(-200, 0)
pendown()

fillcolor("pink")
begin_fill()
circle(50)
end_fill()

# moving around the cursor
left(90)
forward(250)

pencolor("purple")
# head of the penis
fillcolor("purple")
begin_fill()
circle(50)
end_fill()


pencolor("pink")
# rectangular shaft
fillcolor("pink")
begin_fill()
left(90)
forward(100)

left(90)
forward(200)

left(90)
forward(100)
end_fill()

# creating the crack of the penis head
backward(45)
left(90)
forward(250)

# jizz
color("white")
pensize(10)

curve()



#Words 
penup()
setpos(-200,500)
pendown()
write("Merry Christmas",  font=("Arial", 10, "bold"))

penup()
setpos(-100,-400)
write("Fuckers",  font=("Arial", 10, "bold"))


done()




