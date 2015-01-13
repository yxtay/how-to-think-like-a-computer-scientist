import turtle

legs = int(input("Number of legs: "))

wn = turtle.Screen()
alex = turtle.Turtle()

for i in range(legs):
	alex.forward(100)
	alex.up()
	alex.forward(-100)
	alex.down()
	alex.left(360 / legs)
    
wn.exitonclick()