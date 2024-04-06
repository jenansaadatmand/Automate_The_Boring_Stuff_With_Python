#opening and reading text files by Buffer size so that we don't use much memory resources
# use read() to specify buffer we want, instead of readline()
inputFile = open('myfile.txt', 'r')
outputFile = open('myoutputfile.txt', 'w')
msg = inputFile.read(10) # read 10 bytes only
while len(msg):   # loop through file 10 bytes at a time, checks len variable msg, as long as value is not 0 the loop will run
    outputFile.write(msg + '\n')
    msg = inputFile.read(10) #writes message to output file, after writing the message, statement will read the next 10 bytes and keeps doing it until entire file is read
inputFile.close()
outputFile.close()

#opening, reading and writing binary files (non text, image or video)
# use 'rb' or 'wb' mode read binary, write binary
#inputFile = open('myimage.jpg', 'rb')
#outputFile = open('myoutputimage.jpg', 'wb')
#msg = inputFile.read(10) # read 10 bytes only
#while len(msg):   # loop through file 10 bytes at a time, checks len variable msg, as long as value is not 0 the oop will run
#    outputFile.write(msg) msg = inputFile.read(10) #writes message to output file, after writing the message, statement will read the next 10 bytes and keeps doing it until entire file is read
#inputFile.close()
#outputFile.close()

