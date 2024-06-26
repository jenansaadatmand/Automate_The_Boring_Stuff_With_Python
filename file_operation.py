#Opening and reading Text files using readline() method, open(two parameters)
f = open('myfile.txt', 'r') #Open(filepath, mode r reading only)  
firstline = f.readline() # Reads the first line and assigns it to variable firstline
secondline = f.readline() #Reads the second line and assigns to the variable second line
thirdline = f.readline()
fourthline = f.readline()
fifthline = f.readline()
print(firstline)
print(secondline)
print(thirdline, end = '')
print(fourthline)
print(fifthline)
f.close() # Closes the file to free up system resources
# readline() function adds a new line '\n' after each line
#If you don't want the extra new line between each line of text
'''print(firstline, end = '')''' # Single line no space
print()

# For Loop to read text files efficient way
# for loop loops through text file line by line, read all file
f = open('myfile.txt', 'r')
for line in f:
     print(line, end = '') # end = '' prints no single line
f.close()

# Write to a file using a (append) mode
#or 'W' write mode but this will erase all previous content in the file if it exists
# Append two sentences to file
f = open('myfile.txt', 'a')
f.write('\nTHIS sentence will be appended.') # Escape character "\n" for new line
f.write('\nPython is Fun!')
print() # Will print all text in the file
f.close()
# If you keep running the program, it will append the same thing over and over
print()
