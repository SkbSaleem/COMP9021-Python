###FUNCTIONS####
'''functions help us to reuse and write more readable codes.'''

def addnumber(fnum, lnum):
    sumnum = fnum + lnum 
    return sumnum #if we dont do this return, the answer become 'None'
print (addnumber(1,4))
#string = addnumber(1, 4) #???????? what does it means here??

'''print(sumnum) we cant print this variable because it is created inside of functioan, we cant tak it outside
of the function because it doesnt eist outside. in such situation we say sumnum is out of scope. Thus it is very
important to understand that what happens in function stays there unless it is going to return to us.'''

import sys

print('what is your name')

name=sys.stdin.readline()
print('Fuck you',name)


print(('\n')*5)

long_string="i'll catch you if you fall- The floor" 
print(long_string[0:6]) #print first 6 chracters which means upto character 5 NOT 6

print(long_string[-8:]) #print last 8 characters

print(long_string[:-8])

print(long_string[:4]+" be there")

print("%c is my %s letter and my number %d is %.5f" %("X", "favorite",1,.14))

print(long_string.capitalize()) #if you want to capitalize the first letter of the string

print(long_string.find("floor")) #it shows the index of the work in the string. it is cae sensetive.

print(long_string.isalpha()) #if we want to know if all the string is alphabetic character. Give answer in true or false.

print(long_string.isalnum()) #if all string is number

print(len(long_string)) 

print(long_string.replace("floor", "ground"))

print(long_string.strip()) #if we want to strip the white space, well there is no white space here in the string.

quote_list=long_string.split(" ") #split a string into a list

print(quote_list)
