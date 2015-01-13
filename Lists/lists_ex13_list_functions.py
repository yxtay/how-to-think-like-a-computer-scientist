import random

def myCount(lst, item):
	n = 0
	for el in lst:
		if el == item:
			n += 1
			
	return(n)

def myIn(lst, item):
	for el in lst:
		if el == item:
			return True
			
	return False

def myReverse(lst):
	outList = []
	for el in lst:
		outList.insert(0, el)
		
	return outList

def myIndex(lst, item):
	for idx in range(len(lst)):
		if lst[idx] == item:
			return idx
			
	return -1

def myInsert(lst, idx, item):
	return lst[:idx] + [item] + lst[idx:]

myList = []	
for i in range(10):
	myList.append(random.randrange(0, 10))
	
print(myList)
print(myCount(myList, 1))
print(myIn(myList, 1))
print(myIn(myList, 10))
print(myReverse(myList))
print(myIndex(myList, 1))
print(myInsert(myList, 5, 'cat'))