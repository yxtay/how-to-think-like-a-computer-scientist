infile = open("studentdata.txt")
line = infile.readline()
while line:
	values = line.split()
	if len(values) >= 7:
		print values[0]
	line = infile.readline()

infile.close()