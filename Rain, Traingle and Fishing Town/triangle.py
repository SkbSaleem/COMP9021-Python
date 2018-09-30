import copy
import sys


filename = input('Which data file do you want to use? ')
try:
    
    file = open(filename)
    tri = []
    for line in file:
        line = line.split()
        if line:
            line = [int(i) for i in line]
            tri.append(line)
except:
    print("Error: the file name you entered is not valid.")
    sys.exit()

print(tri)

a = []
for i in range(len(tri) -2, -1, -1):  
    for j in range(len(tri[i])):

        if tri[i+1][j] > tri[i+1][j+1]:
            tri[i][j] = tri[i+1][j] + tri[i][j]
            a.append(tri[i+1][j])
        elif tri[i+1][j] < tri[i+1][j+1]:
            tri[i][j] = tri[i+1][j+1] + tri[i][j]
            a.append(tri[i+1][j])

        elif tri[i+1][j] == tri[i+1][j+1]:
            tri[i][j] = tri[i+1][j+1] + tri[i][j]
            a.append(tri[i+1][j])

print (tri[0][0])
