def sum_n1steven(l):
	s = 0
	for el in l:
		if el % 2 == 0:
			break
		else:
			s += el
			
	return s

print sum_n1steven(range(1, 10, 2))
print sum_n1steven(range(1, 10))
print sum_n1steven(range(2, 10))