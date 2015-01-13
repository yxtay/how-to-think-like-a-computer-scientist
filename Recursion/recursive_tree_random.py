import turtle
import random

def tree(branchLen,t):
    width = t.width()
    t.width(branchLen // 10)
    if branchLen < 15:
        t.color('green')
    if branchLen > 5:
        t.forward(branchLen)
        right = random.randrange(15,46)
        t.right(right)
        tree(branchLen-random.randrange(10,21),t)
        left = right + random.randrange(15,46)
        t.left(left)
        tree(branchLen-random.randrange(10,21),t)
        t.right(left - right)
        t.backward(branchLen)
        t.color('brown')
    t.width(width)
    

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("brown")
    tree(120,t)
    myWin.exitonclick()

main()
