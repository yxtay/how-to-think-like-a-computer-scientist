import turtle

def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        t.left(90)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("red")

for i in range(5):
    drawSquare(alex,20)
    alex.up()
    alex.forward(20 * 2)
    alex.down()

wn.exitonclick()