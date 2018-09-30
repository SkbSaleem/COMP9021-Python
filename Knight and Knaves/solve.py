import re
import sys
import itertools



file_name=input("Which text file do you want to use for the puzzle?")

####GETTING THE NAMES####
with open(file_name) as file:
    text = file.read()
    text = re.sub('["!?.,:]', '', text)
    text = text.split()

names = []

for i in range(len(text)):
    if text[i] == 'Sir':      #assuming there will be only one name after 'Sir'.
        names.append(text[i + 1])
    if text[i] == 'Sirs':         #assuming there will be more than one name after 'Sirs'.
        j = 1
        while text[i + j] != 'and':         #while the next element is not 'and', append all names.
            names.append(text[i + j])
            j += 1
        else:
            names.append(text[i + j + 1])       #if the next element is 'and', append the name after 'and'.

names = sorted(set(names))
##print(names)
a = ''
for i in range(len(names)):
    a += ' ' + names[i]   
print('The Sirs are:{}'.format(a))



####FINDING WHO SAID WHAT####
with open(file_name) as file:
    lines = file.read().replace('\n', ' ').replace(',', '').replace(':', '')
    lines = re.sub('[.!?]', '#', lines)             #hash sign indicates a new line
    b = lines.replace('#', '')
    a = re.findall('"([^"]*)"', b)                   #'a' is the data between double quotes
    lines = lines.replace('"', '')
    lines = lines.split('#')

##print(a)
##print(lines)

quoted_lines = []                                   #those lines which contain quoted sayings
for i in a:
    for j in lines:
        if i in j:
            quoted_lines.append([i,j])
##print(quoted_lines)

who_said_what = []
for i in names:
    for j in quoted_lines:
        if i in j[1] and i not in j[0]:
            who_said_what.append([i, j[0]])
##print('who_said_what:', who_said_what)



####NO_SOLUTION####
for i in who_said_what:
    if i[1] == 'I am a Knave':
        print('There is no solution.')
        sys.exit()


##KNOWN_SOLUTIONS
b = [i for i in itertools.product([0,1], repeat=len(names))]    

known_solution = []
wide_potential_solutions = []

for i in who_said_what:
    if 'Sir ' in i[1] and ' I ' in i[1] and 'Knave' in i[1] and ' and ' in i[1] and ' one ' not in i[1]:       #someone says he and other people are knave, he will always 
        count = 0                                                                                                #be a knave and other will always be a knight if he talks about one other people only.
        a = None
        b = None
        for j in range(len(names)):
            if names[j] in i[1]:
                count += 1
                b = j
            if names[j] == i[0]:
                a = j
        if count ==1:
            known_solution.append((a, 0))
            known_solution.append((b, 1))


for i in who_said_what:
    if 'll of us are Knaves' in i[1]:                      #All/all of us are Knaves
        for j in range(len(names)):
            if names[j] == i[0]:
                known_solution.append((j, 0))


for i in who_said_what:
    if 't least one of ' in i[1] and ' I ' in i[1] and 'Knave' in i[1]:         #t least one of (I) is a (Knave).
        count = 0
        sayer = 0
        said = 0
        for j in range(len(names)):
            if names[j] in i[1]:
                said = j
                count += 1
            if names[j] == i[0]:
                sayer = j
        if count == 1:
            known_solution.append((sayer, 1))
            known_solution.append((said, 0))
        count = 0


for i in who_said_what:
    if ' and ' in i[1] and ' one ' not in i[1] and 'I ' not in i[1] and 'Knight' in i[1]:        #name in the saying#knight A==B==C
        sayer = None
        in_it = None
        for j in range(len(names)):
            if names[j] == i[0]:
                sayer = j
            if names[j] in i[1]:
                in_it = j
            if in_it != None and sayer != None:
                for (k,l) in known_solution:
                    if names[in_it] in i[1] and in_it == k and l == 1:
                        known_solution.append((sayer, 1))
                        for y in range(len(names)):
                            if names[y] in i[1] and y != in_it and y != sayer:
                                known_solution.append((y, 1))
                                
                    if names[in_it] in i[1] and in_it == k and l == 0:
                        known_solution.append((sayer, 0))
##                        for y in range(len(names)):
##                            if names[y] in i[1] and y != in_it and y != sayer:
##                                known_solution.append((y, 0))


for i in who_said_what:
    if ' and ' in i[1] and ' one ' not in i[1] and 'I ' not in i[1] and 'Knave' in i[1]:        #name in the saying give lead#Knave A==B==C
        sayer = None
        in_it = None
        for j in range(len(names)):
            if names[j] == i[0]:
                sayer = j
            if names[j] in i[1]:
                in_it = j
            if in_it != None and sayer != None:
                for (k,l) in known_solution:
                    if names[in_it] in i[1] and in_it == k and l == 0:
                        known_solution.append((sayer, 1))
                        for y in range(len(names)):
                            if names[y] in i[1] and y != in_it and y != sayer:
                                known_solution.append((y, 1))
                                
                    if names[in_it] in i[1] and in_it == k and l == 1:
                        known_solution.append((sayer, 0))
##                        for y in range(len(names)):
##                            if names[y] in i[1] and y != in_it and y != sayer:
##                                known_solution.append((y, 0))



##for i in who_said_what:
##    if ' and ' in i[1] and ' one ' not in i[1] and 'I ' not in i[1] and 'Knight' in i[1]:        #name of the sayer gives lead#Knave A==B==C
##        for j in range(len(names)):
##            if names[j] == i[0]:
##                for (k,l) in known_solution:
##                    if j == k:
##                        for y in range(len(names)):
##                            if names[y] in i[1]:
##                                if 'Knight' in i[1]:
##                                    known_solution.append((y, 1))
##                                if 'Knaves' in i[1]:
##                                    known_solution.append((y, 0))
## 
##                                

          
##print('known_solution', known_solution)


b = [i for i in itertools.product([0,1], repeat=len(names))]    
for j in b:
    count = 0
    for (k,l) in known_solution:
        if j[k] == l:
            count += 1
    if count == len(known_solution):
        wide_potential_solutions.append(j)

for i in who_said_what:
    if 'll of us are Knaves' in i[1]:                      #All/all of us are Knaves
        for j in wide_potential_solutions:
            if sum(j) == 0:
                wide_potential_solutions.remove(j)
##print('wide_potential_solutions', wide_potential_solutions)            

####COMPLICATED_TRUTH_TABLE####
potential_solutions = []
#b = [i for i in itertools.product([0,1], repeat=len(names))]    
for i in who_said_what:

#--#All/all of us are Knaves--#
    temp_1 = []
    if 'll of us are Knaves' in i[1]:                      #All/all of us are Knaves
        quad = 0
        for j in range(len(names)):
            if names[j] == i[0]:
                quad = (j, 0)
        b = [i for i in itertools.product([0,1], repeat=len(names))]
        for a in b:
            if a[quad[0]] == quad[1]:
                temp_1.append(a)

##    print('temp_1:', temp_1)
    if len(temp_1) > 0:
        potential_solutions.append(temp_1)

    
#--I_AM_A_KNIGHT--#
    temp_3 = []
    if 'I am a Knight' in i[1]:                 
        for j in range(len(names)):         #sayer is knight
            if names[j] == i[0]:
                for a in b:
                    if a[j] == 1:
                        temp_3.append(a)

        for j in range(len(names)):         #sayer is a knave
            if names[j] == i[0]:
                for a in b:
                    if a[j] == 0:
                        temp_3.append(a)
##    print('temp_3',temp_3)                
    if len(temp_3) > 0:
        potential_solutions.append(temp_3)

#--Conjunction_of_Sirs are Knights/Knaves--#
    temp_7 = []
    b = [i for i in itertools.product([0,1], repeat=len(names))]    
    
    if ' are ' in i[1] and ' and ' in i[1]:        
        quads = []
        if 'Knights' in i[1]:                #Sayer is a knight
            for j in range(len(names)):
                if names[j] in i[1]:
                    quads.append((j, 1))
                if names[j] == i[0]:
                    quads.append((j, 1))
            for a in b:
                count = 0
                for (k,l) in quads:
                    if a[k] == l:
                        count += 1
                if count == len(quads):
                    temp_7.append(a)
                count = 0
        if 'Knaves' in i[1]:                 #sayer is a knight
            if 'I' not in i[1]:
                for j in range(len(names)):
                    if names[j] in i[1]:
                        quads.append((j, 0))
                    if names[j] == i[0]:
                        quads.append((j, 1))
                for a in b:
                    count = 0
                    for (k,l) in quads:
                        if a[k] == l:
                            count += 1
                    if count == len(quads):
                        temp_7.append(a)
                    count = 0


        quads = []
        if 'Knights' in i[1]:                #Sayer is a knave
            say = 0
            for j in range(len(names)):
                if names[j] in i[1]:
                    quads.append((j, 0))
                if names[j] == i[0]:
                    say = j
            for a in b:
                count = 0
                for (k,l) in quads:
                    if a[k] == l:
                        count += 1
                if a[say] == 0 and count == len(quads) - 1:
                    temp_7.append(a)
                count = 0
        if 'Knaves' in i[1]:                 #sayer is a knave
            say = 0
            for j in range(len(names)):
                if names[j] in i[1]:
                    quads.append((j, 1))
                if names[j] == i[0]:
                    say = j
            for a in b:
                count = 0
                for (k,l) in quads:
                    if a[k] == l:
                        count += 1
                if a[say] == 0 and count == len(quads):
                    temp_7.append(a)
                count = 0
                
##    print('temp_7', temp_7)
    if len(temp_7) > 0:
        potential_solutions.append(temp_7)
        
#--Disjunction_of_Sirs are Knights/Knaves--#
    temp_8 = []
    b = [i for i in itertools.product([0,1], repeat=len(names))]    

    if ' is ' in i[1] and ' or ' in i[1]:        

        quads = []
        if 'Knight' in i[1]:                #Sayer is a knight
            say = 0
            for j in range(len(names)):
                if names[j] in i[1]:
                    quads.append((j, 1))
                if names[j] == i[1]:
                    say == j
            for a in b:
                count = 0
                for (k,l) in quads:
                    if a[k] == l:
                        count += 1
                if 'I' in i[1] and count == 0:
                    temp_8.append(a)
                if 'I' not in i[1] and count == 1 and a[say] == 1:
                    temp_8.append(a)
                count = 0
        if 'Knave' in i[1] and 'I' not in i[1]:                 #sayer is a knight

            say = 0
            for j in range(len(names)):
                if names[j] in i[1]:
                    quads.append((j, 0))
                if names[j] == i[0]:
                    say = j
            for a in b:
                count = 0
                for (k,l) in quads:
                    if a[k] == l:
                        count += 1
                if a[say] == 1 and count == len(quads) -1:
                    temp_8.append(a)
                count = 0

    
        quads = []
        if 'Knight' in i[1]:                #Sayer is a knave
            say = 0
            for j in range(len(names)):
                if names[j] in i[1]:
                    quads.append((j, 0))
                if names[j] == i[0]:
                    say = j
            for a in b:
                count = 0
                for (k,l) in quads:
                    if a[k] == l:
                        count += 1
                if a[say] == 0 and count == len(quads):
                    temp_8.append(a)
                count = 0
        if 'Knave' in i[1]:                 #sayer is a knave
            say = 0
            for j in range(len(names)):
                if names[j] in i[1]:
                    quads.append((j, 1))
                if names[j] == i[0]:
                    say = j
            for a in b:
                count = 0
                for (k,l) in quads:
                    if a[k] == l:
                        count += 1
                if a[say] == 0 and count == len(quads):
                    temp_8.append(a)
                count = 0
                
##    print('temp_8', temp_8)
    if len(temp_8) > 0:
        potential_solutions.append(temp_8)

#--ALL_OF_US_ARE_KNIGHTS--#
    temp_5 = []
    if 'll of us are Knights' in i[1]:          #sayer is knight  
        quads = []
        for j in range(len(names)):
            quads.append((j, 1))
        for a in b:
            count = 0
            for (k,l) in quads:
                if a[k] == l:
                    count += 1
            if count == len(quads):
                temp_5.append(a)
            count = 0

    if 'll of us are Knights' in i[1]:          #sayer is knave # atleast one of them should be knave
        quads = []
        say = 0
        for j in range(len(names)):
            if names[j] == i[0]:
                say = j
        for a in b:
            if a[say] == 0 and sum(a) < len(names)-1:
                temp_5.append(a)

       
##    print('temp_5', temp_5)
    if len(temp_5) > 0:
        potential_solutions.append(temp_5)

#--SIR_IS_A--##Sir Sir_Name is a Knight/Knave
    temp_6 = []
    if 'Sir ' in i[1] and ' is ' in i[1] and ' or ' not in i[1] and ' and ' not in i[1]:        
        quads = []
        if 'Knight' in i[1]:                #Sayer is a knight
            for j in range(len(names)):
                if names[j] in i[1]:
                    quads.append((j, 1))
                if names[j] == i[0]:
                    quads.append((j, 1))
            for a in b:
                count = 0
                for (k,l) in quads:
                    if a[k] == l:
                        count += 1
                if count == len(quads):
                    temp_6.append(a)
                count = 0
        if 'Knave' in i[1]:                 #sayer is a knight
            for j in range(len(names)):
                if names[j] in i[1]:
                    quads.append((j, 0))
                if names[j] == i[0]:
                    quads.append((j, 1))
            for a in b:
                count = 0
                for (k,l) in quads:
                    if a[k] == l:
                        count += 1
                if count == len(quads):
                    temp_6.append(a)
                count = 0


        quads = []
        if 'Knight' in i[1]:            #sayer is a knave
            for j in range(len(names)):
                if names[j] in i[1]:
                    quads.append((j, 0))
                if names[j] == i[0]:
                    quads.append((j, 0))
            for a in b:
                count = 0
                for (k,l) in quads:
                    if a[k] == l:
                        count += 1
                if count == len(quads):
                    temp_6.append(a)
                count = 0
        if 'Knave' in i[1]:             #sayer is a knave
            for j in range(len(names)):
                if names[j] in i[1]:
                    quads.append((j, 1))
                if names[j] == i[0]:
                    quads.append((j, 0))
            for a in b:
                count = 0
                for (k,l) in quads:
                    if a[k] == l:
                        count += 1
                if count == len(quads):
                    temp_6.append(a)
                count = 0
##    print('temp_6', temp_6)
    if len(temp_6) > 0:
        potential_solutions.append(temp_6)
#--AT_LEAST--##At/at least one of Conjunction_of_Sirs/us is a Knight/Knave
    temp_2 = []    
    b = [i for i in itertools.product([0,1], repeat=len(names))]    
    if 't least one of ' in i[1]:               #sayer is knight
        if 'Knight' in i[1]:
            if ' us ' in i[1]:
                for a in b:
                    if sum(a) > 0:
                        temp_2.append(a)
            else:
                quad = []
                for j in range(len(names)):
                    if names[j] in i[1]:
                        quad.append((j, 1))
                    if 'I' in i[1]:
                        if names[j] == i[0]:
                            quad.append((j, 1))
                for a in b:
                    count = 0
                    for (k,l) in quad:
                        if a[k] == l:
                            count += 1
                    if count > 0:
                        temp_2.append(a)
                        count = 0
                    count = 0
        if 'Knave' in i[1]:     #sayer is knight
            if ' us ' in i[1]:
                for a in b:
                    if sum(a) < len(names):
                        temp_2.append(a)
            if ' us ' not in i[1]:
                quad = []
                for j in range(len(names)):
                    if names[j] in i[1]:
                        quad.append((j, 0))

                            
                if 'I' in i[1]:
                    if len(quad) == 1:
                        for a in b:
                            for j in range(len(names)):
                                if names[j] == i[0]:
                                    if a[j] == 1:             #knight
                                        for (k,l) in quad:
                                            if a[k] == 0:       #knave
                                                temp_2.append(a)
                if len(quad) > 1:
                    for a in b:
                        count = 0
                        for (k, l) in quad:
                            if a[k] == l:
                                count += 1
                        if count > 0:
                            temp_2.append(a)
                            count = 0
                        count = 0                
##    print('temp_2', temp_2)
    if len(temp_2) > 0:
        potential_solutions.append(temp_2)
##    potential_solutions.append(temp_2)

#--EXACTLY--#

    temp_4 = []
    b = [i for i in itertools.product([0,1], repeat=len(names))]
    if 'xactly one of ' in i[1]:        #Exactly/exactly one of Conjunction_of_Sirs/us is a Knight/Knave
        if 'Knight' in i[1]:                        
            if ' us ' in i[1]:
                for a in b:
                    for j in range(len(names)):
                        if names[j] == i[0]:
                            if sum(a) == 1 and a[j] == 1:       #sayer is knight
                                temp_4.append(a)
            else:
                quad = []
                for j in range(len(names)):
                    if names[j] in i[1]:
                        quad.append((j, 1))
                    if 'I' in i[1]:
                        if names[j] == i[0]:
                            quad.append((j, 1))
                for a in b:
                    count = 0
                    for (k,l) in quad:
                        if a[k] == l:
                            count += 1
                    if count == 1:
                        temp_4.append(a)
                        count = 0
                    count = 0
        if 'Knave' in i[1]:
            if ' us ' in i[1]:
                for a in b:
                    if sum(a) == len(names)-1:
                        temp_4.append(a)
            else:
                quad = []
                for j in range(len(names)):
                    if names[j] in i[1]:
                        quad.append((j, 0))
                    if 'I' in i[1]:
                        if names[j] == i[0]:
                            quad.append((j, 0))
                count = 0
                for a in b:
                    for (k, l) in quad:
                        if a[k] == l:
                            count += 1
                    if count == len(quad) - (len(quad) - 1):
                        temp_4.append(a)
                    count = 0
                            
##    print('temp_4:',temp_4)
    if len(temp_4) > 0:
        potential_solutions.append(temp_4)
    
#--AT_MOST--#
    temp = []
    b = [i for i in itertools.product([0,1], repeat=len(names))]
    if 't most' in i[1]:        #Exactly/exactly one of Conjunction_of_Sirs/us is a Knight/Knave
        if 'Knight' in i[1]:                        #At/at most one of Conjunction_of_Sirs/us is a Knight/Knave
            if ' us ' in i[1]:
                for a in b:
                    if sum(a) < 2:
                        temp.append(a)
            else:
                quad = []
                for j in range(len(names)):
                    if names[j] in i[1]:
                        quad.append((j, 1))
                    if 'I' in i[1]:
                        if names[j] == i[0]:
                            quad.append((j, 1))
                for a in b:
                    count = 0
                    for (k,l) in quad:
                        if a[k] == l:
                            count += 1
                    if count < 2:
                        temp.append(a)
                        count = 0
                    count = 0
        if 'Knave' in i[1]:
            if ' us ' in i[1]:
                for a in b:
                    if sum(a) == len(names)-1:
                        temp.append(a)
            else:
                quad = []
                for j in range(len(names)):
                    if names[j] in i[1]:
                        quad.append((j, 0))
                    if 'I' in i[1]:
                        if names[j] == i[0]:
                            quad.append((j, 0))
                for a in b:
                    count = 0
                    for (k, l) in quad:
                        if a[k] == l:
                            count += 1
                    if count < 2:
                        temp.append(a)
                        count = 0
                    count = 0
                            
                    
##    print('temp:',temp)
    if len(temp) > 0:
        potential_solutions.append(temp)
for i in who_said_what:       
    if len(wide_potential_solutions) == 3:
        if 'xactly one of us is a Knigh' in i[1]:
            for (k,l) in known_solution:
                if l == 0:
                    for j in range(len(names)):
                        if names[j] == i[0]:
                            for k in wide_potential_solutions:
                                if k[j] != 1:
                                    known_solution.append((j, 1))






for i in who_said_what:       
    for (k,l) in known_solution:
        if names[k] == i[0] and 'xactly one of us i' in i[1] and l == 1:
            if 'Knight' in i[1]:
                for j in wide_potential_solutions:
                    if sum(j) != 1:
                        wide_potential_solutions.remove(j)
                    if j[k] != 1:
                        wide_potential_solutions.remove(j)

                        



                    
##print('potential_solutions',wide_potential_solutions)
final = []
for i in potential_solutions:
    for j in i:
        final.append(j)
for i in who_said_what:
    if 'll of us are Knaves' in i[1]: 
        for a in final:
            if sum(a) == 0:
                final.remove(a)


final = set(final)

##print('final', final)
##print(len(final))






    

if len(wide_potential_solutions) == 1:
    print('There is a unique solution:')
    for i in range(len(wide_potential_solutions[0])):
        if wide_potential_solutions[0][i] == 0:
            print('Sir {} is a {}.'.format(names[i], 'Knave'))
        if wide_potential_solutions[0][i] == 1:
            print('Sir {} is a {}.'.format(names[i], 'Knight'))
   
else:
    print('There are {} solutions.'.format(len(wide_potential_solutions)))

