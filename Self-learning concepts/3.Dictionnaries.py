
####DICTIONARIES####
'''Adistiinary is made up of the values with the unique key for each value you are gonna
store. And it is very similar to list but the biggeset difference is you cant
join dictionarries together as you can do with the list'''

super_villains = {'Fiddler' : 'Isaac',
                'weather' : 'mark',
                'Mirror' : 'Sam Scudder',
                'Pied Piper' : 'Thomas Peterson'}   # we use dict curely braces in the dictionnary

print(super_villains['Fiddler'])

del super_villains['Mirror']
super_villains['Pied Piper'] = 'Hartley'

print(super_villains)

print(len(super_villains))

print(super_villains.get('Pied Piper')) #we can also get the VALUE

print (super_villains.keys()) #keys means the names of values (according to my understanding)

print (super_villains.values())
