#Opening and reading text files by Buffer size so that we don't use much memory resources
# Use read() to specify the buffer we want, instead of readline()
inputFile = open('myfile.txt', 'r')
outputFile = open('myoutputfile.txt', 'w')
msg = inputFile.read(10) # read 10 bytes only
while len(msg):   # Loop through file 10 bytes at a time, checks len variable msg, as long as the value is not 0 the loop will run
    outputFile.write(msg + '\n')
    msg = inputFile.read(10) #Writes a message to output file, after writing the message, a statement will read the next 10 bytes and keeps doing it until the entire file is read
inputFile.close()
outputFile.close()

#opening, reading and writing binary files (non text, image or video)
# Use 'rb' or 'wb' mode to read binary, write binary
#inputFile = open('myimage.jpg', 'rb')
#outputFile = open('myoutputimage.jpg', 'wb')
#msg = inputFile.read(10) # Read 10 bytes only
#while len(msg):   # Loop through file 10 bytes at a time, checks len variable msg, as long as the value is not 0 the oop will run
#    outputFile.write(msg) msg = inputFile.read(10) #Writes a message to the output file, after writing the message, the statement will read the next 10 bytes and keeps doing it until entire file is read
#inputFile.close()
#outputFile.close()
