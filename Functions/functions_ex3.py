import turtle

def drawPoly(someturtle, somesides, somesize):
    
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360 / somesides)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("red")

drawPoly(tess, 8, 50)

wn.exitonclick()