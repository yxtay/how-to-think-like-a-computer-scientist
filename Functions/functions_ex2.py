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

for i in range(1, 6):
    drawSquare(alex,20 * i)
    alex.up()
    alex.forward(-10)
    alex.right(90)
    alex.forward(10)
    alex.left(90)
    alex.down()

wn.exitonclick()