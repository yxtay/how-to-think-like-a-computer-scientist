import string

str = input("Please enter a sentence: ")

alphabet_count = {}
for ch in str.lower():
	if ch in string.ascii_lowercase:
		if ch in alphabet_count:
			alphabet_count[ch] += 1
		else:
			alphabet_count[ch] = 1
			
keylist = alphabet_count.keys()
keylist.sort()
for al in keylist:
	print al, alphabet_count[al]