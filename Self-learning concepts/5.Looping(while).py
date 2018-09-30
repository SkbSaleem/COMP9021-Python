'''while loop used when we have no idea for how many times ahead we gonna use the loop again and again'''

import random
rand_num = random.randrange(0,100)

while(rand_num != 15):
    print (rand_num)
    rand_num = random.randrange(0,100) #it will continue printing random number untill random number appears 15.(it will not print 15)


i = 0;

while (i<=20): #create an iterator and its value is gonna change over and over again.
    if(i%2==0):
        print(i)
    elif(i==9):
        break   #it breaks while loop completely
    else:           #??????dont know its function here
        i+=1 #i=i+1
        continue #continue skips what all next in the while loop and jump back to the start of the while loop.
    i+=1 #this seems to be very important in while loop. It alots next value to iterator in while loop.
