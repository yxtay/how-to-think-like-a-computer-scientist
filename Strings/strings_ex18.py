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