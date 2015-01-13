import string

def encryptChar(ch, mapping):
	out_ch = ch
	if ch.lower() in string.ascii_lowercase:
		out_ch = mapping[string.ascii_lowercase.index(ch.lower())]
	return out_ch

def encrypt(msg, mapping):
	out_msg = ''
	for ch in msg.lower():
		out_msg += encryptChar(ch, mapping)
		
	return(out_msg)
	
def decryptChar(ch, mapping):
	out_ch = ch
	if ch.lower() in mapping:
		out_ch = string.ascii_lowercase[mapping.index(ch.lower())]
	return out_ch
	
def decrypt(msg, mapping):
	out_msg = ''
	for ch in msg.lower():
		out_msg += decryptChar(ch, mapping)
		
	return(out_msg)
	
p = "Hello World"
map = 'qwertyuiopasdfghjklzxcvbnm'

print(map)
encrypt_p = encrypt(p, map)
print(encrypt_p)
print(decrypt(encrypt_p, map))