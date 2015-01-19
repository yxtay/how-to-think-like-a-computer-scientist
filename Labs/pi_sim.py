import turtle
import math
import random

fred = turtle.Turtle()
fred.up()
fred.tracer(100)

wn = turtle.Screen()
wn.setworldcoordinates(-1,-1,1,1)

insideCount = 0

numdarts = 1000
for i in range(numdarts):
    randx = random.random()
    randy = random.random()

    x = -1 + 2 * randx
    y = -1 + 2 * randy
    
    fred.goto(x, y)
    if fred.distance(0, 0) < 1:
        fred.dot(5, 'red')
        insideCount += 1
    else:
        fred.dot(5, 'blue')

print(insideCount * 4.0 / numdarts)
wn.exitonclick()
