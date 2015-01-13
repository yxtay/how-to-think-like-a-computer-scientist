import turtle

sides = int(input("Number of sides: "))
length = int(input("Length of side: "))
color = input("Line color: ")
fillcolor = input("Fill color: ")

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color(color)
alex.fillcolor(fillcolor)

alex.begin_fill()
for i in range(sides):
    alex.forward(length)
    alex.left(360 / sides)
alex.end_fill()
    
wn.exitonclick()