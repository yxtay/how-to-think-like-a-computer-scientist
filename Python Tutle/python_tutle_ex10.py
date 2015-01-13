import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("blue")
alex.pensize(3)
alex.up()

for i in range(12):
	alex.forward(100)
	alex.down()
	alex.forward(10)
	alex.up()
	alex.forward(20)
	alex.stamp()
	alex.forward(-130)
	alex.left(30)
    
wn.exitonclick()