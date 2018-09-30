from copy import deepcopy
import sys
import re
from itertools import chain
import re
import sys
import itertools
from copy import deepcopy
f1=input('which data file do you want to use? ')

##try:
f = open(f1)
data=[[]]
#make a dictionary which will have capital A-Z as keys and either of line enders as values.
line_ender=['!','.','?','"']
for line in f:
        data.append(line.strip())
del data[0]
##print(data)
data_char=[]
data_char1=[]
data_char2=[]
data_char3=[]
total_sirs=[]
final_sirs=[]
pos=[]
a=[]
data[0].split()
##create a list which has one word assigned to one index
for i in range(len(data)):
        a.append(data[i].split())
#split this list so that line enders are assigned with different index
p2=re.compile(r'(\W+)')
for i in range(len(a)):
       for j in range(len(a[i])):
                data_char.append((p2.split(a[i][j])))
for i in range(len(data_char)):
        for j in range(len(data_char[i])):
                if(data_char[i][j]!=''):
                        data_char1.append(data_char[i][j])
##check the closing 'double quotes' attached with the line enders->split it.
for i in range(len(data_char1)):
                if(data_char1[i]=='!"'):
                        data_char2.append(data_char1[i].partition('"'))
                        pos.append(i)
                elif(data_char1[i]=='."'):
                        data_char2.append(data_char1[i].partition('"'))
                        pos.append(i)
                elif(data_char1[i]=='?"'):
                        data_char2.append(data_char1[i].partition('"'))
                        pos.append(i)
                elif(data_char1[i]==',"'):
                        data_char2.append(data_char1[i].partition('"'))
                        pos.append(i)
                else :
                        data_char2.append(data_char1[i])

#remove the tuples generated in data_char2 due to partition
for i in range(len(data_char2)):
        count=0
        flag=0
        for j in range(len(pos)):
                if i == pos[j]:
                        if(data_char2[pos[j]][0]!=''):
                                data_char3.append(data_char2[i][0])
                        if data_char2[pos[j]][1]!= '':
                                data_char3.append(data_char2[i][1])
                        if data_char2[pos[j]][2]!= '':
                                data_char3.append(data_char2[i][2])
                        flag=1
        if count<1 and flag==0:
                        count+=1
                        data_char3.append(data_char2[i])

##find the Sirs and display in lexographic order                
for i in range(len(data_char3)):
    if data_char3[i]== 'Sir':
        total_sirs.append(data_char3[i+1])
    elif data_char3[i] == 'Sirs':
        total_sirs.append(data_char3[i+1])
        j = 1
        while(data_char3[i+j] != 'and'):
                if(data_char3!=','):
                        total_sirs.append(data_char3[i+j])
                        j += 1
        total_sirs.append(data_char3[i+j+1])
for i in total_sirs:
        if i==',':
                total_sirs.remove(',')
final_sirs=list(set(total_sirs))
final_sirs.sort(reverse=False)
print('The Sirs are:',end=' ')
for i in range(len(final_sirs)):
        print(final_sirs[i],end=' ')
totalsirs=len(final_sirs)

## form sentences in form of Sir1: " STATEMENTS"

with open(f1, 'r') as myfile:
    data=myfile.read().replace('\n', ' ').replace('!','.').replace(',','').replace('?','')
    test = data
    temp = data.split('.')
    
a = re.findall('"([^"]*)"', data)

b = ([s.strip('.') for s in a])


test = data.replace('"','')
temp1 = test.split('.')


quote = []
for i in range(len(temp1)):
    for j in range(len(b)):
        if b[j] in temp1[i]:
           quote.append(temp1[i]) 


name = deepcopy(final_sirs)

p = []
for i in range(len(quote)):
    for j in range(len(name)):
        if name[j] in quote[i] and name[j] not in b[i]:
            p.append(name[j])
            p.append(': ')
            p.append(b[i])


g=[]
l=[]

for i in range(0,len(p),3):
        try:
                l=p[i]+p[i+1]+p[i+2]
                g.append(l)
        except IndexError:
                break

##Derivation of solutions using a dictionary,truth table and checking upon the statements



truthtable=[i for i in itertools.product([0,1],repeat=totalsirs)]
truth_dict={x:[] for x in final_sirs}
ans_truth_dict={x:[] for x in final_sirs}
fns=0
fls=0
fls1=0
for l in g:
        m = []
        spli=l.split(":")
        r=spli[0]
        m.append(spli[1])
        for k in m:
                
                n=k.split()
                saidnames=[]
                saidnamespos=[]
                names1=0
                name=0
                fls=0
                c=0
                
                ##Finding names of people in double quote
                for names in range(len(n)):
                        
                        if n[names]=='Sir':
                                names1=names+1
                                while names1<len(n):
                                        
                                        if n[names1]=='is' or n[names1]=='are':
                                                fls=1
                                                break
                                        if n[names]=='and' or n[names1]=='or' or n[names1]=='Sir':
                                                pass
                                        if n[names1]!='and' or n[names1]!='or' or n[names1]!='Sir':
                                                saidnames.append(n[names1])
                                        names1+=1
                                if fls==1:
                                        break
                        if fls==1:
                                break
                if fls!=1:
                        if n[0]=='All' or 'all':
                                for names12 in final_sirs:
                                        saidnames.append(names12)
                        names12=0
                        if n[0]=='Exactly' or n[0]=='exactly':
                                for names12 in final_sirs:
                                        saidnames.append(names12)
                        
                        names12=0
                        if n[0]=='At' or n[0]=='at':
                                for names12 in final_sirs:
                                        saidnames.append(names12)
                        names12=0
                        if n[0]=='I' :
                                saidnames.append('I')
                fls=0
                
                ##finding position of person who said the statement               
                for i in range(totalsirs):
                                if final_sirs[i]==r:
                                        c=i        

                
                ##finding positions of names so that it can be compared to positions in truth table
                for i in range(len(saidnames)):
                        for j in range(totalsirs):
                                if saidnames[i]==final_sirs[j]:
                                        saidnamespos.append(j)
                                        fls=1
                                if saidnames[i]=='I':
                                        saidnamespos.append(c)
                                        fls=1
                                else:
                                        pass

                ##In case the double quoted statement only had I and no Sirs
                if fls!=1:
                        saidnamespos.append(c)
                fls=0
                saidnamespos=list(set(saidnamespos))
                
                
                ##Deriving truth table according to statements
                i=0;j=0
                for j in range(len(truthtable)):
                        
                        ## I am a knave/knight
                        if n[0]=='I' :
                                if n[-1]=='Knave' :
                                        truth_dict[r].append(not truthtable[j][c])
                                if n[-1]=='Knight':
                                
                                        truth_dict[r].append(not not truthtable[j][c])

                        ##All of us are knights/knaves
                        t=0
                        fls=0
                        if n[0]=='All' or n[0]=='all':
                                for i in range(len(n)):
                                        if n[i]=='us':
                                                if(n[-1]=='Knaves'):
                                                        if truthtable[j]==(0)*len(totalsirs):
                                                                truth_dict[r].append(True)
                                                        else:
                                                                truth_dict[r].append(False)

                                                if n[-1]=='Knights':
                                                        if truthtable[j]==(1)*len(totalsirs):
                                                                truth_dict[r].append(True)
                                                        else:
                                                                truth_dict[r].append(False)
                                                                
                        ##Sir N1 is a knight/knave                                
                        t=0
                        fls=0
                        if n[0]=='Sir' and (n[2]!='or' or n[2]!='and' or n[3]!='or' or n[3]!='and'):
                                if n[-1]=='Knave' :
                                        truth_dict[r].append(not truthtable[j][saidposname[0]])
                                if n[-1]=='Knight' :
                                        truth_dict[r].append(not not truthtable[j][saidposname[0]])

                         ##Disjunction of Sirs is a knight/knave AND Exactly one of us is a knight/knave-->same               
                        t=0
                        fls=0
                        flag=[]
                        if (n[0]=='Exactly' or n[0]=='exactly') or (n[0]=='Sir') and (n[2]=='or' or n[3]=='or'):
                                
                                if n[-1]=='Knave' :
                                         for k in range(len(saidnamespos)):
                                                                if truthtable[j][saidnamespos[k]]==0:
                                                                        fls=1
                                                                        flag.append(0)
                                                                if truthtable[j][saidnamepos[k]]==1:
                                                                        flag.append(1)
                                         count=0
                                         for lmno in range (flag):
                                                 if flag[i]==0:
                                                         count+=1  
                                         if count==1:
                                                truth_dict[r].append(not 0)
                                         if count>1 or count<1:
                                                truth_dict[r].append(not 1)        
                                if n[-1]=='Knight' :
                                        for k in range(len(saidnamespos)):
                                                                if truthtable[j][saidnamespos[k]]==0:
                                                                        fls=1
                                                                        flag.append(0)
                                                                if truthtable[j][saidnamepos[k]]==1:
                                                                        flag.append(1)
                                        count=0
                                        for lmno in range (flag):
                                                if flag[i]==1:
                                                         count+=1  
                                        if count==1:
                                                truth_dict[r].append(not 0)
                                        if count>1 or count<1:
                                                truth_dict[r].append(not 1)        

                        ##Conjunction of Sirs is a knight/Knave
                        t=0
                        fls=0
                        if n[0]=='Sir' and (n[2]=='and' or n[3]=='and'):
                                
                                if n[-1]=='Knaves' :
                                        for k in range(len(saidnamespos)):
                                                                if truthtable[j][saidnamespos[k]]==0:
                                                                        
                                                                        fls+=1
                                                                        
                                        if fls==len(saidnamespos):
                                                
                                                truth_dict[r].append( not not 1)
                                        else:
                                                
                                                truth_dict[r].append(not 1)        
                                if n[-1]=='Knights' :
                                        for k in range(len(saidnamespos)):
                                                                if truthtable[j][saidnamespos[k]]==1:
                                                                        fls+=1
                                                                        break
                                        if fls==len(saidnamespos):
                                                truth_dict[r].append( not not 1)
                                        if fls==0:
                                                truth_dict[r].append(not 1)
                                        
                                        
                         ##Atleast one of conjunctions of Sirs/us is a knight/knave        
                        t=0
                        fls=0
                        fls1=0
                        count=0
                        if n[1]=='least' :
                                
                                for i in range(len(n)):
                                        if n[i]=='us':
                                                fls=1
                                                if n[-1]=='Knight':
                                                        for k in range(len(truthtable[j])):
                                                                if truthtable[j][k]==1:
                                                                        fls1=1
                                                                        break
                                                        if fls1==1:
                                                                 truth_dict[r].append(not not 1)
                                                        if fls1==0:
                                                                 truth_dict[r].append(not 1)
                                                
                                                if n[-1]=='Knave':
                                                        for k in range(len(truthtable[j])):
                                                                if truthtable[j][k]==0:
                                                                        fls1=1
                                                                        break
                                                        if fls1==1:
                                                                 truth_dict[r].append(not 0)
                                                        if fls1==0:
                                                                 truth_dict[r].append(not 1)
                                                         
                                if fls==0:
                                        if n[-1]=='Knight':
                                                        for k in range(len(saidnamespos)):
                                                                if truthtable[j][saidnamespos[k]]==1:
                                                                        fls1=1
                                                                        break
                                                        if fls1==1:
                                                                 truth_dict[r].append(not not 1)
                                                        if fls1==0:
                                                                 truth_dict[r].append(not 1)
                                                
                                        if n[-1]=='Knave':
                                                        for k in range(len(saidnamespos)):
                                                                if truthtable[j][saidnamespos[k]]==0:
                                                                        fls1=1
                                                                        break
                                                        if fls1==1:
                                                                 truth_dict[r].append(not 0)
                                                        if fls1==0:
                                                                 truth_dict[r].append(not 1)
                                                         

                        ##Atmost on of Conjuctions of Sirs is a Knight/Knave
                        t=0
                        fls=0
                        fls1=0
                        count=0
                        flag=[]
                        if n[1]=='most' :
                                if n[-1]=='Knave' :
                                         for k in range(len(saidnamespos)):
                                                                if truthtable[j][saidnamespos[k]]==0:
                                                                        fls=1
                                                                        flag.append(0)
                                                                if truthtable[j][saidnamepos[k]]==1:
                                                                        flag.append(1)
                                         count=0
                                         for lmno in range (flag):
                                                 if flag[i]==0:
                                                         count+=1  
                                         if count==1 or count==0:
                                                truth_dict[r].append(not 0)
                                         else:
                                                truth_dict[r].append(not 1)        
                                if n[-1]=='Knight' :
                                        for k in range(len(saidnamespos)):
                                                                if truthtable[j][saidnamespos[k]]==0:
                                                                        fls=1
                                                                        flag.append(0)
                                                                if truthtable[j][saidnamepos[k]]==1:
                                                                        flag.append(1)
                                        count=0
                                        for lmno in range (flag):
                                                if flag[i]==1:
                                                         count+=1  
                                        if count==1 or count==0:
                                                truth_dict[r].append(not 0)
                                        else:
                                                truth_dict[r].append(not 1)        
                   

                                 
#########################Converting the statements to information depending on whether the person who said it is a knight/knave###############################

##start a new loop
## go through my truth dictionary and see if that key in the truth table is a knight or a knave, hence the statement changes.

c=0
for l in g:
        r,m=l.split(":")
        flag=0
        for j in range(totalsirs):
                if final_sirs[j]==r:
                        c=j    
        
        for keys,values in truth_dict.items():
                for j in range(len(truthtable)): 
                        if keys==r:
                                try:
                                        if truthtable[j][c]==0:
                                                if values[j]==True:
                                                        ans_truth_dict[r].append(0)
                                                if values[j]==False:
                                                        ans_truth_dict[r].append(1)
                                        if truthtable[j][c]==1:
                                                if values[j]==True:
                                                        ans_truth_dict[r].append(1)
                                                if values[j]==False:
                                                        ans_truth_dict[r].append(0)
                                except IndexError:
                                        pass

##Comparison for keys in ans_truth_dict and DEDUCING the answer               
flag=0
last_answer=[]

for i in range(len(truthtable)):
        flag=0
        for keys,values in ans_truth_dict.items():
                try:
                        if values[i]==0:
                                flag=1
                except IndexError:
                        pass
        
        if flag==0:
                last_answer.append(i)

print()                                              
if len(last_answer)>1:
        print('There are {} solutions.'.format(len(last_answer)))
if len(last_answer)==0:
        print('There is no solution.')
answer=[]
if len(last_answer)==1:
        print('There is a unique solution:')
        for i in range(len(last_answer)):
                for j in range(len(truthtable[i])):
                        if truthtable[last_answer[0]][j]==1:
                                answer.append('Knight')
                        if truthtable[last_answer[0]][j]==0:
                                answer.append('Knave')
        for k in range(len(final_sirs)):
                print('Sir {} is a {}.'.format(final_sirs[k],answer[k]))
                                               
               
