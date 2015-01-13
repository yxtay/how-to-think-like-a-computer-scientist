import turtle

def drawTriangle(t, length):
	for i in range(3):
		t.forward(length)
		t.right(120)

def drawSprite(t, legs, length):
    for i in range(legs):
        t.forward(length)
        drawTriangle(t, 10)
        t.forward(-length)
        t.right(360 / legs)


def drawSquare(t, sz):
    """Get turtle t to draw a square of sz side"""

    for i in range(4):
        t.forward(sz)
        drawSprite(t, 5, 20)
        t.left(90)


		
wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("red")

drawSquare(alex, 100)

wn.exitonclick()