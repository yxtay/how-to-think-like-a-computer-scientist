def average(lst):
	s = 0
	n = 0
	for el in lst:
		s += int(el)
		n += 1
	
	return s / n

infile = open("studentdata.txt")
line = infile.readline()
while line:
	values = line.split()
	print values[0], average(values[1:])
	line = infile.readline()

infile.close()