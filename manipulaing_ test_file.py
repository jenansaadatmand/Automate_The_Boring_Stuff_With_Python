# To write into the file
file = open('testfile.txt', 'w')
file.write('Hello World''\n')
file.write('This is our new text file''\n')
file.write('and this is another line''\n')
file.write('Why? Because we can.')
file.close()

# To read the file, all content
#file = open('testfile.txt', 'r')
#for line in file:
#    print(line, end = '')
#file.close()

# To read a file, extract a string that contains all characters in the file
file = open('testfile.txt', 'r')
print(file.read())

# read a file and call a certain number of characters

file = open('testfile.txt', 'r')
print(file.read(5))
file.close()
print()
# readline() function: read a file line by line, as oppose to pulling the content of file at once
file = open('testfile.txt', 'r')
print(file.readline()) # returns the first line
print(file.readline(4)) # returns four characters of second line
file.close()
print()
# for loop, returns every line in file, properly seperated
file = open('testfile.txt', 'r')
for line in file:
    print(line, end = '')
file.close()
print()

# to append a file
file = open('testfile.txt', 'a')
file.write('\nWe Meet Again Wold')
file.close()

file = open('testfile.txt', 'r')
print(file.read())
file.close()
print()


#'with statement' for cleaner syntax and exceptions, any file opened will be closed automatically when you are done
with open('testfile.txt') as file: # with open('filename') as file:
    for line in file: #data = file.read()    
        print(line, end = '') # do something with data, no need to close file




