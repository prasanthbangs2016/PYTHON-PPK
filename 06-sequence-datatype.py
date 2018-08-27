import os
os.system("cls")
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

print("accessing string by index")

#name="PPK THOUGHTS"
print("Institute Name is:",name[1:]) 

# find substring position from a string

print("find substring position from a string")

print(name.find('GH'))

# Substring is searched in 'eeks for geeks' 
#print(name.find('geeks ', 2))

# Substring is searched in 's for g'
#print(name.find('for ', 4, 11))


# slicing opetors

print("			# slicing opetors	#	")

print(name[0:5])
print(name[0:])

# increment index position by 2

print(" 		# increment index position by 2 in slicing operator	# 	")

print(name[0::2])
print(name[0:6:2])

# Realtime scenario

'''
i have filename: product_details_20180827.txt
i want only data of file
'''

filename="product_details_20180827.txt"

print("file processed date file",filename[16:24])

processed_dt=print(filename[16:24])


'''
Note: No char datatype is available in python ,every single/multi characters it is string.
'''