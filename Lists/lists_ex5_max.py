import random

myList = []
for i in range(100):
	myList.append(random.randrange(0, 1000))
	
def max(l):
	m = None
	for el in l:
		if m < el:
			m = el
		
	return m
	
print(max([1, 3, 5, 7, 6, 4, 3]))
print(max(myList))