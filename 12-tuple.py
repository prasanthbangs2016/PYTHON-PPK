'''

Description: Tuple Data type

1. we cannot cange/update elements
2.append(),extend(),clear() doesnt work

'''

#To know tuple

#a=(10)
a=(10,) # with comma this is tuple for single elements
print(type(a))

b=(19,20,30)
print(type(b))


# converting range to tuple

c=tuple(range(0,10))

print("converting range to tuple c=tuple(range(0,10)):",c)

print(type(c))


# accessing tuple elements

tup=(50,60,70,80,90,100)

print(tup[0]) #slicing operator

print(tup[1]) #slicing operator

print(tup[5]) #slicing operator

print(tup[:]) #slicing operator


'''
what are the operations that we can do with tuple

Basic operators on tuple

1.finding length	2.concatenation	3.repetition	4.membership

'''

#length

student=(31,'PPK','31-03-1988')
print("no of elements is student=(31,'PPK','31-03-1988'):",len(student))

# Repetition

fees=(2500.00,)*4
print("repetion of value is fees=(2500.00,)*4:",fees)

# concatenation

student_1=student+fees
print("1st student details are student_1=student+fees:",student_1)