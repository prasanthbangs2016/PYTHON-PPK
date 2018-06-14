import os
os.system("cls")
fstvalue=int(input("enter the first value:"))
secvalue=int(input("enter the second value:"))

if (fstvalue==secvalue):
    print ("first and second values are same") 
else:
    print("both the numbers are not equal")	


if (fstvalue>secvalue):
    print ("first is big number than second value") 
else:
    print("secvalue is big number than second value:",secvalue)		