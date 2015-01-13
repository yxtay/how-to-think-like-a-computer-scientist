def sum_even(l):
	s = 0
	for el in l:
		if el % 2 == 0:
			s += el
			
	return s
	
print sum_even(range(3))
print sum_even(range(10))