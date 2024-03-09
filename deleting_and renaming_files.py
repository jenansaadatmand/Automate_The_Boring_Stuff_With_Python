# Deleting and renaming files, remove(), rename()
# These two functions must be imported from the os module
# Remove('filename') deletes a file
# Rename('old name', 'new name') rename old file to new file
# os function directory operations, deleting, moving aroud, changing things
import os
import time
curDir = os.getcwd() # cwd current working directory
print(curDir) # displays /Users/jenansaadatmand/Documents
os.mkdir('newDir') # make new directory 
time.sleep(2) # so we can see the action happening
os.rename('newDir', 'newDir2') #rename directory





#time.sleep(2)
#os.rmdir('newDir2') # remove directory


#rename('myfile.txt', 'nfile.txt')
#file = open(nfile.text)
#print(file)
#file.close()
