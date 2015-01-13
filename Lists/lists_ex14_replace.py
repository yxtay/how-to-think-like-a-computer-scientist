import unittest

def replace(lst, item, replace_with):
	return replace_with.join(lst.split(item))

# assertEqual(replace('Mississippi', 'i', 'I'), 'MIssIssIppI')
print replace('Mississippi', 'i', 'I')

s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
# assertEqual(replace(s, 'om', 'am'),
       # 'I love spam!  Spam is my favorite food.  Spam, spam, spam, yum!')
print replace(s, 'om', 'am')

# assertEqual(replace(s, 'o', 'a'),
       # 'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!')
print replace(s, 'o', 'a')