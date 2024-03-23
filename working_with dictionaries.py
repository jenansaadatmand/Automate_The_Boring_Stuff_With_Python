# Working with dictionaries
#clear(), marks the start of the output,
'''removes all elements in the dictionary and returns an empty dictionary'''

dic1 = {1: 'one', 2: 'two'}
print(dic1)
print()

dic1.clear()  # Returns empty dictionary
print(dic1)
print()

#del, delete entire dictionary, dictionary disappears
dic2 = {1: 'one', 2: 'two'}
del dic2
#print(dic2) # You will get NameError: name 'dic2' is not defined, because dic2 has been deleted
print()

# get() returns a value for the given key, if key not found will return None
# Alternatively, you can state the value to return if the key is not found
dic1a = {1: 'one', 2: 'two'}
a = dic1a.get(1)
print(a)
b = dic1a.get(2)
print(b)
c = dic1a.get(5) # Key 5 is not defined
print(c)
d = dic1a.get(5, "Not Found")
print(d)
if "4" in dic1a:
    dic1a["4"] = ["Four"]
else:
    dic1a["4"] = ["FOUR"]  # Trick to append if it is not in dictionary
    print(dic1a)
print()

if '4' in dic1a:
    dic1a["4"].append('CCC') # trick to appending two items in list as values for one key

# in , check if the item is in the dictionary
diccc = {1: 'one', 2: 'two' }

a = 1 in diccc # Check if item 1 in the dictionary
b = 2 in diccc
c = 3 in diccc
print(a, b, c) # print all three answers/variables
print()

print('one' in diccc.values())
print('three' in diccc.values())

#items()  , return a list of dictionary's pairs as tuples

dic1 = {1: 'one', 2: 'two'}
print(dic1.items()) # returns Tuples of list with dictionary pairs

#keys()  return list of the dictionary keys or dictionary values
dic1a = {1: 'one', 2: 'two'}
print(dic1a.keys())
print(dic1a.values())
print()

# values(),  returns list of the dictionary's values

dic1bb = {1: 'one', 2: 'two'}
dic1bb.values()


# len() , find the number of items in a dictionary
dic1T = {1: 'one', 2: 'two'}
print(len(dic1T))
print()

# update , adds/merges one dictionary key-value pair to another dictionary. Duplicates are removed
dictaa = {1: 'one', 2: 'two'}
dictcc = {1: 'one', 3: 'three'}

dictaa.update(dictcc)
print(dictaa)
print()
print(dictcc)  # no change
print()

# working with Tuples
# del  , deletes the entire Tuple

myTuple = ('a', 'b', 'c', 'd')
print(myTuple)
#del myTuple
#print(myTuple) # myTuple is not defined because it is deleted

# in  , check if an item is in Tuple

myTuple = ('a', 'b', 'c', 'd')
print('c' in myTuple)
print('e' in myTuple) 
print()
# len()   find the number of item in a tuple
myTuple = ('a', 'b', 'c', 'd')
print(len(myTuple))

# Addition Operator: +  concatenate Tuples

myTuple = ('a', 'b', 'c', 'd')
print(myTuple + ('e', 'f'))
print(myTuple) # unchanged
myTuple2 = myTuple + ('e', 'f')
print(myTuple2)
print()

# multiplication Operator: *  Duplicate a tuple and concatenate it to the end of the tuple
myTuple = ('a', 'b', 'c', 'd')
print(myTuple * 3) 
print(myTuple) # the + and * don't modify the tuple, the tuple stays the same


