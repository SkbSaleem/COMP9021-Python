
####ALGORATHIMATIC OPERATORS####
'''
their are seven different algorathimatic operators which are:
+ - * / % ** //
'''

print("5 + 2 =", 5+2)
print("5 - 2 =", 5-2)
print("5 * 2 =", 5*2)
print("5 / 2 =", 5/2)
print("5 ** 2 =", 5**2)     #** is called 'power of'
print("5 // 2 =", 5//2)     #// is called 'floor division'


####PRINT BY TAKING MULTIPLE STRINGS FROM DIFFERENT LINES####
quote = "Always remember you are unique"
multi_line_quotes = ''' just like
everyone else'''
print('\n')
join_above_two_strings_together = quote + multi_line_quotes
print(join_above_two_strings_together)

print('\n')
print("join_above_two_strings_together =", quote + multi_line_quotes)

print('\n')
print("%s %s %s" % ('I like the quote', quote, multi_line_quotes))

print ("\n" * 5)
print("I dont like ", end="")
print("newlines")

####LIST####
'''list allows to create a list of values and then to manipuate them. And each value is
going to have a index with the first value have index 0.An index is just like a label
to find the location/position of the vakue.'''

grocery_list = ['juice', 'tomatoes', 'potatoes',
                "bananas"]
print('First Item', grocery_list [0])

grocery_list[0]='green juice'
print('First Item', grocery_list [0])

print(grocery_list[0:3])        #I just noticed that it prefers the assign value to index 0 (that is green juice) instead of value alredy in the list (that is juice). 
                                #not included value at index 3

other_events = ['wash car', 'pick up kids', 'cash check']

overall_todo_list = [other_events, grocery_list]        #combining two list al together
print(overall_todo_list)


print(overall_todo_list[1][2])      #printing one elememt from the subset of a set.

'''different operations we can do in a list
.append, .insert, .remove, .sort, .reverse, del variable
'''
grocery_list.append('onions')       #add item at the end
print(overall_todo_list)

grocery_list.insert(1, 'pickle')        #add an item at some specific position
print(overall_todo_list)

#overall_todo_list.insert((1)(2), saqib)        #dont know how to do this??????????????????????

grocery_list.remove('bananas')

grocery_list.sort()
grocery_list.reverse()
del grocery_list[0]
print(overall_todo_list)

overall_todo_list_2 = overall_todo_list + other_events
print(overall_todo_list_2)

print(len(overall_todo_list_2))     #get the number of items in a list
#print(max(overall_todo_list_2))        #http://stackoverflow.com/questions/14886881/unorderable-types-int-str
print(max(grocery_list))        #maximum item or in this case what comes last alphateically
print(min(grocery_list))        #minimum item or in this case what comes first alphateically

####TUPLES####
'''Tuples are pretty much same as list but the only difference is tuples cant be change once created.
It is beingused normally to creat e a data that we know will remain the same.'''

pi_tuple = (3,1,4,5,3,7,3)      #list is inclosed in list brackets[] where as tuples are enclosed in parenthesis()
new_tuple = list(pi_tuple)      #convert tuple in to a list
new_tuple = tuple(new_tuple)    #convert list into a tuple
print(len(pi_tuple))
print(min(pi_tuple))
print(max(pi_tuple))
