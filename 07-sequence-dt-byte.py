import os
os.system("cls")
'''
Datatype:- byte

notes: To access byte data element we should use for loop

Iq:-
---
Once defined byte elements cannot be updated/modified.

[10,20,30,40,50] : this is list

'''
a=[10,20,30,40,50]

b=bytes(a)
print(b)
print(type(b))

'''
#accessing elements with loop
'''

for i in b:
		 print(i)
