import turtle

def drawStar(t):
    for i in range(5):
        t.forward(100)
        t.right(144)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("red")

for i in range(5):
    drawStar(alex)
    alex.up()
    alex.forward(350)
    alex.right(144)
    alex.down()

wn.exitonclick()