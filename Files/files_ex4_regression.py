import turtle

def int_list(lst):
	outlist = []
	for el in lst:
		outlist.append(int(el))
	
	return outlist
	
def mean(xl):
	return sum(xl) / len(xl)
	
def sum_product(xl, yl):
	s = 0
	for i in range(len(xl)):
		s += xl[i] * yl[i]
		
	return s

def slope(xl, yl):
	mux = mean(xl)
	muy = mean(yl)
	n = len(xl)
	sxx = sum_product(xl, xl)
	sxy = sum_product(xl, yl)
	m = (sxy - n * mux * muy) / (sxx - n * mux ** 2)
	return m
	
def plotPoints(t, xl, yl):
	t.up()
	for i in range(len(xl)):
		t.goto(xl[i], yl[i])
		t.stamp()
	t.down()
	
def plotBestFit(t, xl, yl):
	mux = mean(xl)
	muy = mean(yl)
	m = slope(xl, yl)
	minx = min(xl)
	maxx = max(xl)
	y_minx = muy + m * (minx - mux)
	y_maxx = muy + m * (maxx - mux)
	
	t.up()
	t.goto(minx, y_minx)
	t.down()
	t.goto(maxx, y_maxx)

def plotRegression(t, xl, yl):
	t.color('black')
	plotPoints(t, xl, yl)
	t.color('blue')
	plotBestFit(t, xl, yl)

infile = open("labdata.txt")
line = infile.readline()
x = []
y = []

while line:
	values = line.split()
	x.append(values[0])
	y.append(values[1])
	line = infile.readline()

infile.close()

x = int_list(x)
y = int_list(y)

alex = turtle.Turtle()
alex.shape('circle')
alex.pensize(10)

border = 10
wn = turtle.Screen()
wn.setworldcoordinates(min(x)-border, min(y)-border, max(x)+border, max(x)+border)

plotRegression(alex, x, y)
alex.hideturtle()
wn.exitonclick()