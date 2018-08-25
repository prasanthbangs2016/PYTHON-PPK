'''

Data types:-

1. none : is equalent to null value in other language
2. nuemeric: int,float,complex,float,decimal and complex numbers
3.sequene: string,list,byte,byte array
4.sets : sets,frozen set
5.mapping: dictionary(key,value)

'''

'''
Description:- None examples
'''

'''
def add():
	a=10
	b=29
	c=a+b
result=add()
print(result)
'''

# if we execute above steps, we get "none" value as a result.

# below example tells obtaining null value and displaying in o/op in customized format words.

def add():
	a=10
	b=29
	c=a+b
result=add()

if(result=='None'):
	#print("result is nothing")
	print("result is",result)
else:
	print("result value is",result)

print(result)
