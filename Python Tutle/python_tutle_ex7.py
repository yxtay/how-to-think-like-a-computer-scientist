import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

for angle in [160, -43, 270, -97, -43, 200, -940, 17, -86]:
    alex.left(angle)
    alex.forward(100)
print alex.heading(), alex.position()
    
wn.exitonclick()