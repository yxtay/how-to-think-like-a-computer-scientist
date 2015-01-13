infile = open("alice_words.txt", 'r')

count = {}

for line in infile:
	key, value = line.split()
	count[key] = value
	
longest = 0
for key in count:
	if len(key) > longest:
		longest = len(key)
		long_key = key
		
print long_key, longest