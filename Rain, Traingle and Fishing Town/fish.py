import sys
filename = input('Which data file do you want to use?')



try:
    
    file = open(filename)
    string_l = []
    l = []
    for line in file:
        string_l += line.split()
    for i in string_l:
        i = int(i)
        l.append(i)
    #print(l)
except:
    print("Error: the file name you entered is not valid.")
    sys.exit()   


N = len(l)
dist = []
for n in range(0, N+1, 2):
    try:
        dist.append(l[n])
    except:
        continue
#print (dist)

quan_fish = []
for n in range (1, N+1, 2):
    try:
        quan_fish.append(l[n])
    except:
        continue
#print(quan_fish)


diff_dist = []
temp = 0
dist.sort(reverse=True)
for i in range(len(dist)):
    try:
        
        temp = dist[i] - dist[(i+1)]
        diff_dist.append(temp)
    except:
        continue


fish_lost = sum(diff_dist)
#print(fish_lost)

sum_quan_fish = sum(quan_fish)
#print(sum_quan_fish)

avg_sum_quan_fish = int(sum_quan_fish/len(quan_fish))
#print(avg_sum_quan_fish)

avg_fish_lost = int(fish_lost/len(dist))
#print(avg_fish_lost)

Yes_i_did = avg_sum_quan_fish - avg_fish_lost
if Yes_i_did < 0: 
    Yes_i_did = min(quan_fish)



print ("The maximum quantity of fish that each town can have is ", Yes_i_did)
