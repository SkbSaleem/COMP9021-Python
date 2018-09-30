import sys


filename = input('Which data file do you want to use? ')
try:
    
    file = open(filename)
    string_l = []
    l = []
    for line in file:
        string_l += line.split()
    for i in string_l:
        i = int(i)
        l.append(i)
    print(l)
    
except:
    print("Error: the file name you entered is not valid.")
    sys.exit()
water_enter = input('How many decilitres of water do you want to poor down?')
try:
    water_enter = int(water_enter)

    a = []
    b = []

    for i in l:
        if i not in a:
            a.append(i)
    a.sort()
    for i in a:
        b.append(l.count(i))


    total_capacity = 0 #the value of water can be stored.
    no_of_lands = b[0]
    height = a[0]
    used = 0                   #in the list, we can get the value by the index. But in the dictionary, we get the value by the key.
    for i in range(len(a)):  #to assign i the index in a and not the values of the list we use the range function with len of a.
        if i == 0: #if i is at the index 0 we do nothing as we dont have to add the previous land to the net land.
            pass
        else:
            no_of_lands += b[i]
        if i == len(a)-1:
            print('water is too much')
            height = a[-1]
            break
        else:
            total_capacity += (a[i+1]-a[i])*no_of_lands #differebce between two lands multiply by total of those kind of lands

        
        if water_enter < total_capacity:
            if i==0:
                height += water_enter/no_of_lands
                break
            else:
                used = total_capacity - no_of_lands * (a[i+1] - a[i])
                height = (water_enter - used) / no_of_lands + a[i]
                break
        elif water_enter == total_capacity:
            height = a[i+1]
            break
    print('{:.2f}'.format(height))
except:
    print("Error: The input doesn't make sense.")
    sys.exit()

