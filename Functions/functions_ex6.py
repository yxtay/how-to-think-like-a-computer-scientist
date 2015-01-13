import turtle

def drawPoly(someturtle, somesides, somesize):
    
    for i in range(somesides):
        someturtle.forward(somesize)
        someturtle.left(360 / somesides)

def drawEquitriangle(someturtle, somesize):
    drawPoly(someturtle, 3, somesize)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("red")

# drawPoly(tess, 8, 50)
drawEquitriangle(tess, 100)

wn.exitonclick()