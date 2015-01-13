import random

myList = []
for i in range(100):
	myList.append(random.randrange(0, 1000))
	
def average(l):
	s = 0
	n = 0
	for el in l:
		s += el
		n += 1
		
	return float(s) / n

print(average([1, 2, 3, 4]))
print(average(myList))