import string

def countAll(text):
    letters = {}
    
    for ch in text.lower():
        if ch in string.ascii_lowercase:
            if ch in letters:
                letters[ch] += 1
            else:
                letters[ch] = 1
    
    return letters
    
print(countAll('this is a random text'))