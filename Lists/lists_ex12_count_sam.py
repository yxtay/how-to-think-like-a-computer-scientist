def count_till_sam(l):
	n = 0
	for el in l:
		n += 1
		if el.lower() == "sam":
			break
	
	return n
	
print count_till_sam(["james", "jack", "sam", "jill"])