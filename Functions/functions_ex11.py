import turtle

def drawStar(t, corners):
    for i in range(corners):
        t.forward(100)
        t.right(180 - 360 / (2 * corners))

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("red")

drawStar(alex, 9)

wn.exitonclick()