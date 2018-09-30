#####input/output####
test_file=open("test.txt","wb") #to create as well as open a file
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("write me to the file\n", "UTF-8")) #write text to the screen or to the file.
                                                          #this is how you write in bytes in a file
test_file.close()

#Use "ab+" to read and Append to File. It also opens and creates the file.



test_file=open("test.txt", "r+")#to open file for reading and wrting
text_in_file=test_file.read()
print(text_in_file)

import os

os.remove("test.txt") #to delete the file as it is no longer needed. this module is iported from os
