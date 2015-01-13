import turtle

def drawAngle(t, size):

    for i in range(2):
        t.forward(size)
        t.right(89)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("blue")
alex.right(180)

for i in range(1, 40):
    drawAngle(alex, 10 * i)

wn.exitonclick()