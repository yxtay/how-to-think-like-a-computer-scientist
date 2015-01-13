def int_list(lst):
	outlist = []
	for el in lst:
		outlist.append(int(el))
	
	return outlist

infile = open("studentdata.txt")
line = infile.readline()
while line:
	values = line.split()
	scores = int_list(values[1:])
	print values[0], min(scores), max(scores)
	line = infile.readline()

infile.close()