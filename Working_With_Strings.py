# Working with strings
# count(sub, [start], [end]), case sensitive
a = 'jimmy is a great boy'
a.count('m')
print(a.count('m'))
print(a.count(a))      
print()

print('jimmy is a good boy'.count('g'))
print('jimmy is a good boy'.count('i', 1)) # Count from index i to end of string
print()

print('This is a string'.count('s', 4, 10)) # Count from index 4 to 10-1
print('This is a string'.count('T')) # Count 'T' case sensitive, only 1 T
print()

#endswith(suffix, [start], [end]), case sensitive
''' return True if the string ends with specified suffix,
otherwise return False, suffix can be a tuple of suffix to look for'''

# Check 'man' at index 4 to 6, check the entire string
print('man'.endswith('man'))

# Check from index 3 to the end of the string
print('Postman'.endswith('man', 3))

# Check from index 2 to 6-1
print('Postman'.endswith('man', 2, 6)) # false, n is in index 7-1

# check from index 2 to 7-1
print('Postman'.endswith('man', 2, 7))

# using a tuple of suffixes, (check from index 2 to 6-1)
print('Postman'.endswith(('man', 'ma'), 2, 6))
print()

#find/index(sub,[start], [end]) , case-sensitive
'''return the (index) in the string where the (first occurance) of
the substring sub is found, find returns -1 if sub not found'''
'''index() returns ValueError if sub is not found'''

print('This is a string'.find('s'))  # check entire string
print('This is a string'.find('s', 4)) # check from index 4 of end of string
print('This is a string'.find('s', 7, 11)) # check from index 7 to 11-1
print('This is a string'.find('s', 7, 10)) # check from index 7 to 10-1
print()
print('This is a string'.find('p')) # sub is not found
#print('This is a string'.index('p')) # Value error using index if is not found
print()

#isalnum() , all alphabetic and numeric 
'''return true if all characters in the string are
alphanumeric and thre is at least one character, false otherwise.
Alphanumeric does not include whitespacs''' 

print('abcd1234'.isalnum())
print('a b c d 1 2 3 4'.isalnum()) # has white space
print('abcd'.isalnum())
print(''.isalnum()) # no alphanumeric and all white space
print('1234'.isalnum())
print()

# isalpha() all alphabetic only
'''return true if all characters in the string are alphabtic
and there is at least one character, false otherwise'''

print('abcd'.isalpha())
print('abcd1234'.isalpha()) # false , has numbers and alphabetic
print('1234'.isalpha()) # false has numeric
print('a b c'.isalpha()) # false has white spase and alphabetic
print()

#isdigit()  , all numeric
'''return true if all characters in the string are digits
and there is at least one character, false otherwise'''

print('1234'.isdigit())
print('abcd1234'.isdigit())
print('abcd'.isdigit())
print('1 2 3 4'.isdigit())
print()


#islower() , lowercase
'''return true if all cased characters in the string are lowercase
and there is at least one character, false otherwise'''

print('abcd'.islower())
print('Abcd'.islower())
print('ABCD'.islower())
print()

#isupper() , all uppercase
'''return true if all characters in the string are uppercase
and there is at least one haracter, false otherwise'''

print('ABCD'.isupper())
print('Abcd'.isupper()) # false
print('abcd'.isupper())
print()

#isspace() only white space
'''return true if there are only whitespace charcters in the string
and there is at least one character, false otherwise'''

print(''.isspace()) # no whitespace
print(' '.isspace()) # True whitespace
print('a b'.isspace()) # false , alphabetic and space
print()

#istitle() all string starts with capital title
'''return true if the string is a titlecased string and there
is at least one character'''

print('This Is A String'.istitle())
print('This is A String'.istitle())
print('This is a string'.istitle())
print('this is a tring'.istitle())
print()

#join() join string by separator
'''return a string in which the parameter provided is
joined by a separator'''

print(sep = '')
sep = '-' # defined seperator by -
myTuple = ('a', 'b', 'c')
myList = ['d', 'e', 'f']
myString = "Hello World"

print(sep.join(myTuple))
print(sep.join(myList))
print(sep.join(myString))
print()

#lower() , make all lowercase
'''return a copy of the string converted to lowercase'''

print('Hello Python'.lower())
print('HELLO PYTHON'.lower())

#upper() , make all uppercase
'''return a copy of the string converted to uppercase'''

print('hello world'.upper())
print()

#replace(old, new[, count]) case-sensitive, replace()
'''return a copy of the string with all occurrences of substring
old replaced by new.  Count is optional. If given only first
count occurrences are replcaed'''

print('This is a string'.replace('s', 'p'))  # replace all occurences
print('This is a string'.replace('s', 'pp'))
print('This is a string'.replace('s', 'p', 2)) #replace first 2 occurences
print()


#split([sep[, maxsplit]]) case-sensitive
'''return a 'list' of the 'words' in the string, using 'sep' as the
delimiter. If sep is not given, at most maxsplit is used as the
delimiter. If maxsplit is given, at most maxsplit splits
are done'''
#split using comma as delimiter.
''' Notice there is a space before
the words 'is', 'a', and 'string' in the output''' 

print('This is a string'.split(',')) # one word in list
print('this, is, a, string'.split(','))
print()

#split using whitespace as delimiter
print('This is a string'.split())
print('This is a string'.split(' '))

#only do 2 splits
print('This, is, a, string'.split(',', 2))
print()








