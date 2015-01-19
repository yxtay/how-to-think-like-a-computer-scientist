import turtle

def drawSquare(t, sz):
    """Make turtle t draw a square of sz."""

    for i in range(4):
        t.forward(sz)
        t.left(90)

def drawPolygon(t, sz, n):
    for i in range(n):
        t.forward(sz)
        t.left(360 / n)
    
def drawTriangle(t, sz):
    drawPolygon(t, sz, 3)
    
def drawCircle(t, radius):
    circumference = 2 * 3.1415 * radius
    sideLength = circumference / 360
    drawPolygon(t, sideLength, 360)
    
def drawCircleCentred(t, radius):
    t.up()
    t.forward(radius)
    t.left(90)
    t.down()
    drawCircle(t, radius)
    t.up()
    t.left(90)
    t.forward(radius)
    t.left(180)
    t.down()
    
def drawFilledCircle(t, radius):
    t.begin_fill()
    drawCircle(t, radius)
    t.end_fill()
        
wn = turtle.Screen()

alex = turtle.Turtle()
alex.shape('turtle')
alex.color('green')

drawFilledCircle(alex, 100)

wn.exitonclick()