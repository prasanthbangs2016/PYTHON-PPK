import os
os.system("cls")

'''

Data type: list

1. list is similar to array

array: deals data with similary data type

list: deals data with any data type


list slicing
------------
[start:stop:stepsize]

'''

list=['abcd',786,2.23,'john',70.2]

print(list)
print(list[0])
print(list[0:])
print(list[2:])


# concatination

print("				concatination		")

tiny=[123,'ppk']

print("concatenated list",list+tiny)
print(list)

print("repeatation of string",list*2)


# updating the elements in list
list[1]=786.2  #updating list 1st index position
print(list)

# appending to list

#syntax:-   list.append(item)
#--------

list.append('PrashanthK')
print(list)


#remove element from list
list.remove('PrashanthK')
print(list)

#clear all elements from list

list.clear()
print(list)

'''
Python List Methods
Methods that are available with list object in Python programming are tabulated below.

They are accessed as list.method(). Some of the methods have already been used above.

Python List Methods
append() - Add an element to the end of the list
extend() - Add all elements of a list to the another list
insert() - Insert an item at the defined index
remove() - Removes an item from the list
pop() - Removes and returns an element at the given index
clear() - Removes all items from the list
index() - Returns the index of the first matched item
count() - Returns the count of number of items passed as an argument
sort() - Sort items in a list in ascending order
reverse() - Reverse the order of items in the list
copy() - Returns a shallow copy of the list

'''


