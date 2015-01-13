def reverse_list(lst):
	if len(lst) <= 1:
		return lst
	else:
		return reverse_list(lst[1:]) + [lst[0]]
		
print reverse_list(range(10))