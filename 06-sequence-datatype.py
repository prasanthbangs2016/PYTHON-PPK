'''
datatype:- sequence

a. str:- string can be single/double/triple quotes in python

'''


# str



name="PPK THOUGHTS"
print("string variable is",name)
print("knowing type of datatype",type(name))

#index positions for string in python

# PPK THOUGHTS
# 0123456789101112
# -13-12-11-10-9-8-7-6-5-4-3-2-1

'''
+---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

'''

#accessing string by array

print("accessing string by array")

#name="PPK THOUGHTS"
print("Institute Name is:",name[1:]) 

# find substring position from a string

print("find substring position from a string")

print(name.find('GH'))

# Substring is searched in 'eeks for geeks' 
#print(name.find('geeks ', 2))

# Substring is searched in 's for g'
#print(name.find('for ', 4, 11))
