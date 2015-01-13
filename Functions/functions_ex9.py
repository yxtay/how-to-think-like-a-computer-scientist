import turtle

def drawStar(t):
    for i in range(5):
        t.forward(100)
        t.right(144)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("red")

drawStar(alex)

wn.exitonclick()