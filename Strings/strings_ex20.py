def removeDups(inStr):
	outStr = ''
	for ch in inStr:
		if ch not in outStr:
			outStr += ch
			
	return outStr
	
print(removeDups('Hello, World!'))