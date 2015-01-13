def sum_negative(l):
	s = 0
	for el in l:
		if el < 0:
			s += el
			
	return s
	
print sum_negative(range(10, -10, -1))