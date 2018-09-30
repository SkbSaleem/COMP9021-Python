from copy import deepcopy
import sys
from argparse import ArgumentParser

parser = ArgumentParser(allow_abbrev=False)
parser.add_argument('-print', dest = 'print', action='store_true', required = False)
parser.add_argument('--file', dest = 'txtfilename', required = True)
args = parser.parse_args()
filename = args.txtfilename


maze = []
with open (filename) as f:
    for lines in f:
        a = []
        for j in lines:
            if j.isdigit():
                a.append(j)
        if a == []:
            continue
        else:
            maze.append(a)
for i in range(len(maze)):
    for j in range(len(maze[i])):
        maze[i][j] = int(maze[i][j])
##print(maze)

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if maze[i][-1]==1 or maze[i][-1]==3 or maze[-1][j]==2 or maze[-1][j]==3:
            print('Incorrect input.')
            sys.exit()
        if maze[i][j]!=0 and maze[i][j]!=1 and maze[i][j]!=2 and maze[i][j]!=3:
            print('Incorrect input.')
            sys.exit()
        if (len(maze))<2 or (len(maze))>41 or (len(maze[0]))<2 or (len(maze[0]))>31:
            print('Incorrect input.')
            sys.exit()

for i in range(len(maze)-1):
    if len(maze[i]) != len(maze[i+1]):
        print('Incorrect input.')
        sys.exit()

######################################GATES############################################

gates = 0
cord_gates = []
#first row
for j in range(len(maze[0])):
    if maze[0][j] == 0:         #0 as a gate in first row
        if j == 0:      #0 as first element mean 2 gates
            gates += 2
            cord_gates.append((0,0))
            cord_gates.append((1,0))
            
        else:
            gates += 1
            cord_gates.append((0,j))

    if maze[0][j] == 2 and j != (len(maze[0]) - 1):        #2 as a gate in first row(excluding last element)
        gates += 1
        cord_gates.append((0,j))

    if maze[0][j] == 1 and j == 0:         #1 in first coloumn is a gate
        gates += 1
        cord_gates.append((0,j))
#last row
for j in range(len(maze[0])):
    if maze[-1][j] == 0 and j != (len(maze[0]) - 1):        #constraint for last element being 0
        gates += 1
        cord_gates.append((len(maze)-1,j))
#first coloumn (excluding first and last element)
for i in range(1, (len(maze) -1)):
    if maze[i][0] == 0:
        gates += 1
        cord_gates.append((i,0))
    if maze[i][0] == 1 and i != (len(maze) - 1):        #1 in last coloumn(excluding last row)
        gates += 1
        cord_gates.append((i,0))
#last coloumn(excluding first and last element)
for i in range(1, (len(maze) - 1)):
    if maze[i][-1] == 0:
        gates += 1
        cord_gates.append((i,len(maze[0])-1))

        
if gates == 0:
    print('The maze has no gate.')
if gates == 1:
    print('The maze has a single gate.')
if gates > 1:
    print('The maze has {} gates.'.format(gates))
##print('cord_gates', cord_gates)
######################################WALLS############################################
maze1=deepcopy(maze)
def walls(i,j):

    if maze1[i][j] == 1:
        maze1[i][j]=0
        if maze1[i][j+1]==1 or maze1[i][j+1]==2 or maze1[i][j+1]==3:        #forward
            walls(i,j+1)
        if maze1[i-1][j] == 2 or maze1[i-1][j]==3:         #upward
            walls(i-1,j)
        if maze1[i][j-1] == 1 or maze1[i][j-1] == 3:       #backward
            walls(i,j-1)
        if maze1[i-1][j+1]==2 or maze1[i-1][j+1]==3:       #upper right
            walls(i-1,j+1)

    if maze1[i][j] == 2:
        maze1[i][j]=0
        if maze1[i+1][j]==1 or maze1[i+1][j]==2 or maze1[i+1][j]==3:       #downward
            walls(i+1,j)
        if maze1[i][j-1]==1 or maze1[i][j-1]==3:        #backward
            walls(i,j-1)
        if maze1[i-1][j]==2 or maze1[i-1][j]==3:         #upward
            walls(i-1,j)
        if maze1[i+1][j-1] == 1 or maze1[i+1][j-1] == 3:      #lower left
            walls(i+1,j-1)
            
    if maze1[i][j]==3:
        maze1[i][j]=0
        if maze1[i][j+1] ==1 or maze1[i][j+1] ==2 or maze1[i][j+1] ==3:        #forward
            walls(i,j+1)
        if maze1[i][j-1] ==1 or maze1[i][j-1] ==3:        #backward
            walls(i,j-1)
        if maze1[i-1][j] ==2 or maze1[i-1][j] ==3:        #upward
            walls(i-1,j)
        if maze1[i+1][j] ==1 or maze1[i+1][j] ==2 or maze1[i+1][j] ==3:        #downward
            walls(i+1,j)
        if maze1[i-1][j+1]==2 or maze1[i-1][j+1]==3:      #upper right
            walls(i-1, j+1)
        if maze1[i+1][j-1] == 1 or maze1[i+1][j-1] == 3:      #lower left
            walls(i+1,j-1)
            
count=0               
for i in range(len(maze1)):
    for j in range(len(maze1[i])):
        if maze1[i][j] == 0:
            continue
        walls(i,j)
        count += 1
if count == 0:
    print('The maze has no wall.')
if count == 1:
    print('The maze has a single wall that are all connected.')
if count > 1:
    print('The maze has {} sets of walls that are all connected.'.format(count))
################################INACCESSABLE AREAS###############################################
maze2= deepcopy(maze)
def inac(i,j):
    if maze2[i][j]==0:
        if j+1<len(maze2[i]) and (maze2[i][j+1]==0 or maze2[i][j+1]==1):       #forward
            maze2[i][j]='X'
            inac(i,j+1)
        if j-1>=0 and (maze2[i][j-1]==0 or maze2[i][j-1]==1 or maze2[i][j-1]==2 or maze2[i][j-1]==3):      #backward
            maze2[i][j]='X'
            inac(i,j-1)
        if i-1>=0 and (maze2[i-1][j]==0 or maze2[i-1][j]==1 or maze2[i-1][j]==2 or maze2[i-1][j]==3):      #upward
            maze2[i][j]='X'
            inac(i-1,j)
        if i+1<len(maze2) and (maze2[i+1][j]==0 or maze2[i+1][j]==2):      #downward
            maze2[i][j]='X'
            inac(i+1,j)

    if maze2[i][j]==1:
        if j+1<len(maze2[i]) and (maze2[i][j+1]==0 or maze2[i][j+1]==1):       #forward
            maze2[i][j]='X'
            inac(i,j+1)
        if j-1>=0 and (maze2[i][j-1]==0 or maze2[i][j-1]==1 or maze2[i][j-1]==2 or maze2[i][j-1]==3):      #backward
            maze2[i][j]='X'
            inac(i,j-1)
        if i+1 < len(maze2) and (maze2[i+1][j]==0 or maze2[i+1][j]==2):      #downward
            maze2[i][j]='X'
            inac(i+1,j)


    if maze2[i][j]==2:
        if j+1<len(maze2[i]) and (maze2[i][j+1]==0 or maze2[i][j+1]==1):       #forward
            maze2[i][j]='X'
            inac(i,j+1)
        if i-1>=0 and (maze2[i-1][j]==0 or maze2[i-1][j]==1 or maze2[i-1][j]==2 or maze2[i-1][j]==3):      #upward
            maze2[i][j]='X'
            inac(i-1,j)
        if i+1<len(maze2) and (maze2[i+1][j]==0 or maze2[i+1][j]==2):      #downward
            maze2[i][j]='X'
            inac(i+1,j)
            
    if maze2[i][j]==3:
        if j+1<len(maze2[i]) and (maze2[i][j+1]==0 or maze2[i][j+1]==1):       #forward
            maze2[i][j]='X'
            inac(i,j+1)
        if i+1<len(maze2) and (maze2[i+1][j]==0 or maze2[i+1][j]==2):      #downward
            maze2[i][j]='X'
            inac(i+1,j)
    maze2[i][j]='X'

for(i,j) in cord_gates:
    inac(i,j)

a=0    
for i in range(len(maze2)-1):
    for j in range(len(maze2[i])-1):
        if maze2[i][j] != 'X':
            a += 1

if a == 0:
    print('The maze has no inaccessible inner point.')
if a == 1:
    print("The maze has a unique inaccessible inner point.")
if a > 1:
    print('The maze has {} inaccessible inner points.'.format(a))


################################################################################
##
##class Node:
##    def __init__(i,j,maze2[i][j])
##        self.i = i
##        self.j = j
##        self.value = maze2[i][j]
##
##    def up():
##        self = None
##    def down():
##        self = None
##    def left():
##        self= None
##    def right():
##        self=None
##
####2:recursion
##def move(i,j):
##    if maze2[i][j].up==True and i>=1:
##        move(i-1,j)
##    if maze2[i][j].down == True and i<(len(maze2)-1):
##        move[i+1][j]
##    if maze2[i][j].left == True and j>=1:
##        move[i][j-1]
##    if maze2[i][j].right ==True and j<(len(maze2)-1):
##        move[i][j+1]
##
##    
####3:find the directions of every coordinate
##for i in range(len(maze2)-1):
##    for j in range(len(maze2[i])-1):
##        if maze2[i][j].value == 0 or maze2[i][j].value==2:
##            maze2[i][j].up= True
##        else:
##            maze2[i][j].up = False
##
##for i in range(len(maze2)-1):
##    for j in range(len(maze2[i])-1):
##        if maze2[i][j].value == 0 or maze2[i][j].value==1:
##            maze2[i][j].left= True
##        else:
##            maze2[i][j].left = False
##
##for i in range(len(maze2)-1):
##    for j in range(len(maze2[i])-1):
##        if maze2[i][j].value == 0 or maze2[i][j].value==2:
##            maze2[i][j].down = True
##        else:
##            maze2[i][j].down = False
##
##for i in range(len(maze2)-1):
##    for j in range(len(maze2[i])-1):
##        if maze2[i][j].value == 0 or maze2[i][j].value==1:
##            maze2[i][j].right= True
##        else:
##            maze2[i][j].right = False
##
####4.def move(i,j):
##    
####if maze[][].up == True:
####    move([]-1,[])
####    listaa.append([][])
####5listaaa.append(listaa)
####len listaaa
##
##









##countt=0
##for i in range(len(maze2)):
##    for j in range(len(maze2[i])):
##        if maze2[i][j] != 'X' and maze2[i][j+1]!='X':
##            countt += 1
##print('The maze has {} sets connected.'.format(countt))

##
##def walls(i,j):
##
##    if maze2[i][j] == 1:
##        maze2[i][j]=0
##        if maze2[i][j+1]==1 or maze2[i][j+1]==2 or maze2[i][j+1]==3:        #forward
##            walls(i,j+1)
##        if maze2[i-1][j] == 2 or maze2[i-1][j]==3:         #upward
##            walls(i-1,j)
##        if maze2[i][j-1] == 1 or maze2[i][j-1] == 3:       #backward
##            walls(i,j-1)
##        if maze2[i-1][j+1]==2 or maze2[i-1][j+1]==3:       #upper right
##            walls(i-1,j+1)
##
##    if maze2[i][j] == 2:
##        maze2[i][j]=0
##        if maze2[i+1][j]==1 or maze2[i+1][j]==2 or maze2[i+1][j]==3:       #downward
##            walls(i+1,j)
##        if maze2[i][j-1]==1 or maze2[i][j-1]==3:        #backward
##            walls(i,j-1)
##        if maze2[i-1][j]==2 or maze2[i-1][j]==3:         #upward
##            walls(i-1,j)
##        if maze2[i+1][j-1] == 1 or maze2[i+1][j-1] == 3:      #lower left
##            walls(i+1,j-1)
##            
##    if maze2[i][j]==3:
##        maze2[i][j]=0
##        if maze2[i][j+1] ==1 or maze2[i][j+1] ==2 or maze2[i][j+1] ==3:        #forward
##            walls(i,j+1)
##        if maze2[i][j-1] ==1 or maze2[i][j-1] ==3:        #backward
##            walls(i,j-1)
##        if maze2[i-1][j] ==2 or maze2[i-1][j] ==3:        #upward
##            walls(i-1,j)
##        if maze2[i+1][j] ==1 or maze2[i+1][j] ==2 or maze2[i+1][j] ==3:        #downward
##            walls(i+1,j)
##        if maze2[i-1][j+1]==2 or maze2[i-1][j+1]==3:      #upper right
##            walls(i-1, j+1)
##        if maze2[i+1][j-1] == 1 or maze2[i+1][j-1] == 3:      #lower left
##            walls(i+1,j-1)
##            
##countt=0               
##for i in range(len(maze2)):
##    for j in range(len(maze2[i])):
##        if maze2[i][j] == 'X':
##            continue
##        walls(i,j)
##        countt += 1
##print('The maze has {} sets connected.'.format(countt))
##
##
##
##a=0
##for i in range(len(maze2)):
##    for j in range(len(maze2[i])):
##        try:
##            if maze2[i][j]!='X' and maze2[i][j+1]!='X' and j+1<(len(maze2[i])-1):
##                a+=1
####            if maze[i][j]==3 and (maze[i][j+1]==2 or maze[i][j+1]==3) and (maze[i+1][j]==1 or maze[i+1][j]==3):
####                a+=1
##        except:
##            pass
##print(a)
##def i_i_p(i,j):
##    try:
##        if (maze2[i][j+1]==0 or maze2[i][j+1]==1):        #forward
####            if j+1<len(maze2[0]):
##            maze2[i][j]='X'
####            j+=1
##            i_i_p(i,j)
##
##        if maze2[i][j]==2 or maze2[i][j]==0:       #upward
####            if i-1 > -1:
##            maze2[i][j]='X'
####            i-=1
##            i_i_p(i,j)
##
##        if maze2[i][j]==0 or maze2[i][j]==1:      #backward
####            if j-1 > -1:
##            maze2[i][j]='X'
####            j-=1
##            i_i_p(i,j)
##
##        if maze2[i+1][j]==0 or maze2[i+1][j]==2:      #downward
####            if i+1 < len(maze2):
##            maze2[i][j]='X'
####            i+=1
##            i_i_p(i,j)
##    except:
##        pass
##    
##for (i,j) in cord_gates:
##    i_i_p(i,j)
##
##i_i_p_cords=[]
##for i in range(len(maze2)):
##    for j in range(len(maze2[0])):
##        if maze2[i][j]!='X':
##            i_i_p_cords.append((i,j))
##
##print()
##print(i_i_p_cords)
##print()
##print(maze2)
##
##
##
#####################################################################################
##def path(i,j):
##    try:
##        
##        if (maze[i][j+1]==0 or maze[i][j+1]==1):        #forward
##            if j+1<len(maze[0]):
##                j+=1
##                print(i,j, maze[i][j])
##                maze[i][j] = 'o'
##                path(i,j)
####                maze[i][j] = 'X'
##    
##        if maze[i][j]==2 or maze[i][j]==0:       #upward
##            if i-1 > -1:
##                i-=1
##                print(i,j,maze[i][j])
##                maze[i][j] = 'o'
##                path(i,j)
####                maze[i][j] = 'X'
##    
##        if maze[i][j]==0 or maze[i][j]==1:      #backward
##            if j-1 > -1:
##                j-=1
##                print(i,j,maze[i][j])
##                maze[i][j] = 'o'
##                path(i,j)
####                maze[i][j] = 'X'
##        
##        if maze[i+1][j]==0 or maze[i+1][j]==2:      #downward
##            if i+1 < len(maze):
##                i+=1
##                print(i,j,maze[i][j])
##                maze[i][j] = 'o'
##                path(i,j)
####                maze[i][j] = 'X'
##        flag
##       
##            
##            
##    except:
##        pass
##
##
##
####for (i,j) in cord_gates:
##path(7,0)
##print(maze, end='\n')
##
##
##
##
##
##
##
##
##
##
##
##
##maze1 = []
##for i in range(len(maze)):
##    for j in range(len(maze[0])):
##        if maze[i][j] == 0:
##            a = ' '
##            maze1.append(a)
##        if maze[i][j] == 1:
##            a = '‾'
##            maze1.append(a)
##        if maze[i][j] == 2:
##            a = '|'
##            maze1.append(a)
##        if maze[i][j] == 3:
##            a = '|‾'
##            maze1.append(a)
##
#### print(maze1)
##ascii_maze = ''
##count=0
##for i in range(0,len(maze1)):
##    ascii_maze += (maze1[i])#,end='')
##    count+=1
##    if count==len(maze[0]):
##        ascii_maze += '\n'
##        count=0
##print(ascii_maze)
##
##
##PATH, START, EXIT, VISITED, SOLUTION = ' SE.o'
##
##class Maze():
##    def __init__ (self, ascii_maze):
##        self.maze = ascii_maze.splitlines()         #split the strings of the maze as each element to a new line.
##
##    def __repr__(self):         #representation of the maze for the viewrs. Put it back as it was before.
##        return "\n".join(self.maze)
##
##
##if __name__ == "__main__":
##    maze = Maze(ascii_maze)
##    #print(maze)
##    
##
##
##
##class Node:
##    def __init__(i,j,maze[i][j])
##        self.i = i
##        self.j = j
##        self.value = maze[i][j]
##
##        def up():
##            self = None
##
##
##2:recursion
##3:find the directions of every coordinate
##maze[1][2].up
##.down
##.left
##.right
##4.def move(i,j)
##if maze[][].up == True:
##    move([]-1,[])
##    listaa.append([][])
##5listaaa.append(listaa)
##len listaaa 
