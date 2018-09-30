####Looping####
'''looping allows us to perform an action a set number of times'''

'''for x in range (0, 10): #zero upto 10 but not including 10; as we did before.
    print (x,'',end='') #changing of space or ' or " doesnt make any difference.
                        
print (('\n')*3)

grocery_list = ['juice', 'tomatoes', 'potatoes', 'bananas']

for y in grocery_list:
    print(y)

for x in [2, 4, 6, 8, 10]:
    print (x)
'''
num_list = [[1,2, 3], [10, 20, 30], [100, 200, 300]]

for x in range (0,3): #it means x ranges are three subsets
    for y in range (0, 3): #as this loop is inside the first loop, thus y looks inside x. y ranges at elements in subsets.
        #for z in range (0,3): #more or less, I think it say how many times it gonna print x and y range
            print(num_list [x][y]) #if we include [z] in the print, it give error as int object is not subscriptable.




edibles = ["ham", "spam","eggs","nuts"]
for food in edibles:
    if food == "spam":
        print("No more spam please!")
        continue#break
    print("Great, delicious " + food)
else:
    print("I am so glad: No spam!")
print("Finally, I finished stuffing myself")



from math import sqrt
n = input("Maximum Number? ")
n = int(n)+1
for a in range(1,n):
    for b in range(a,n):
        c_square = a**2 + b**2
        c = int(sqrt(c_square))
        if ((c_square - c**2) == 0):
            print(a, b, c)




fibonacci = [0,1,1,2,3,5,8,13,21]
for i in range(len(fibonacci)):
    print(i,fibonacci[i])



colours = ["red"]
for i in colours[:]: #colours:  To avaoid this sid effect, it is best to work on a copy by using the slicing opertor.
    if i == "red":
        colours += ["black"]
    if i == "black":
        colours += ["white"]
print(colours)
