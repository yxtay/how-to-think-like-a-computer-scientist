import random
import turtle

def isInScreen(w,t):
    leftBound = - w.window_width() / 2
    rightBound = w.window_width() / 2
    topBound = w.window_height() / 2
    bottomBound = -w.window_height() / 2

    turtleX = t.xcor()
    turtleY = t.ycor()

    stillIn = turtleX > leftBound and turtleX < rightBound
    stillIn = stillIn and turtleY > bottomBound and turtleY < topBound

    return stillIn

t = turtle.Turtle()
wn = turtle.Screen()

t.shape('turtle')
while isInScreen(wn,t):
    t.right(360 * random.random() - 180)
    t.forward(50)

wn.exitonclick()