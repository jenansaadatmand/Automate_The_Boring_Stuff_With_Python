#Opening, reading and writing binary files (non text, image or video)
# Use 'rb' or 'wb' mode read binary, write binary
inputFile = open('myimage.jpeg', 'rb')
outputFile = open('myoutputimage.jpg', 'wb')
msg = inputFile.read(10) # read 10 bytes only
while len(msg):   # Loop through file 10 bytes at a time, checks len variable msg, as long as value is not 0 the oop will run
    outputFile.write(msg)
    msg = inputFile.read(10) #writes message to output file, after writing the message, statement will read the next 10 bytes and keeps doing it until entire file is read
inputFile.close()
outputFile.close()

