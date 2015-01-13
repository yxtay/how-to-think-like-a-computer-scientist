import string

def rot13(inStr):
	outStr = ''
	for ch in inStr.lower():
		if ch in string.ascii_lowercase:
			outStr += string.ascii_lowercase[
				(string.ascii_lowercase.find(ch) + 13) % 26
			]
		else:
			outStr += ch
			
	return outStr
	
print(rot13('abcde'))
print(rot13('nopqr'))
print(rot13(rot13('since rot thirteen is symmetric you should see this message')))
