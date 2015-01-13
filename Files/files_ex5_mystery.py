import turtle

def draw(t, values):
	if len(values) == 2:
		t.goto(int(values[0]), int(values[1]))
	elif values[0] == "UP":
		t.up()
	elif values[0] == "DOWN":
		t.down()

alex = turtle.Turtle()
wn = turtle.Screen()

infile = open("mystery.txt")

line = infile.readline()
while line:
	values = line.split()
	draw(alex, values)
	line = infile.readline()

infile.close()

alex.hideturtle()
wn.exitonclick()