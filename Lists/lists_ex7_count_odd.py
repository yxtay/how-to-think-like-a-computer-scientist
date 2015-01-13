def count_odd(l):
	n = 0
	for el in l:
		if el % 2 == 1:
			n += 1
			
	return n
	
print count_odd(range(3))
print count_odd(range(10))