import string

def removeWhite(s):
    outs = ''    
    for ch in s.lower():
        if ch in string.ascii_lowercase:
            outs += ch
    return outs

def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])

print isPal(removeWhite("hello"))

# testEqual(isPal(removeWhite("x")),True)
# testEqual(isPal(removeWhite("radar")),True)
# testEqual(isPal(removeWhite("hello")),False)
# testEqual(isPal(removeWhite("")),True)
# testEqual(isPal(removeWhite("hannah")),True)
# testEqual(isPal(removeWhite("madam i'm adam")),True)
