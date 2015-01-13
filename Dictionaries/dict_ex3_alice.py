import string

infile = open("alice.txt", 'r')

count = {}

for line in infile:
	for word in line.lower().split():
		
		text = word.translate(string.maketrans("", ""), string.punctuation)
		
		if text.isalpha():
			if text in count:
				count[text] += 1
			else:
				count[text] = 1
			
keylist = count.keys()
keylist.sort()

outfile = open("alice_words.txt", 'w')

for word in keylist:
	outfile.write("%s %d\n" % (word, count[word]))
	
print("The word 'alice' appears " + str(count['alice']) + " times in the book.")