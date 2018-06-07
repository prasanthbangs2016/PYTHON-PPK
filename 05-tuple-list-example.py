import os
os.system('cls')

a_tuple = (1,2,3,4,5,6,7,8,9,10)
b_list = [1,2,3,4,5]

print(tuple(b_list))
print(list(a_tuple))

fruits=['apple','mango','litchi']

print ("*** printing all values for list")
print (fruits)
print ("*** printing 1st list/array value from list")
print (fruits[0])
print ("*** printing 1 to 2 list/array value from list")
print (fruits[1:2])
print ("*** travel from 2nd  list/array value to end/everything list")
print (fruits[1:])

#output

#(1, 2, 3, 4, 5)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#*** printing all values for list
#['apple', 'mango', 'litchi']
#*** printing 1st list/array value from list
#apple
#*** printing 1 to 2 list/array value from list
#['mango']
#*** travel from 2nd  list/array value to end/everything list
#['mango', 'litchi']
