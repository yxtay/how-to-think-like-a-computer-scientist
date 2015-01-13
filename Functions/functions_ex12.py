import turtle

def drawSprite(t, legs, length):
    for i in range(legs):
        t.forward(length)
        t.forward(-length)
        t.right(360 / legs)

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("red")

drawSprite(alex, 15, 120)

wn.exitonclick()