import math
import turtle

wn = turtle.Screen()
wn.bgcolor('lightblue')
wn.setworldcoordinates(-10, -1.1, 370, 1.1)

fred = turtle.Turtle()

#your code here
for x in range(361):
    y = math.sin(math.radians(x))
    fred.goto(x, y)

wn.exitonclick()
