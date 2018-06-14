import os
os.system("cls")

print("Program to add natural numbers")
datainput=int(input("Enter number of values:"))

finalsum=0
loopindex=1

while loopindex <=datainput: 
   finalsum =finalsum + loopindex
   loopindex =loopindex+	1
print ("Sum of ",datainput,"Natural number is:",finalsum)
#print ("the current sum is:",finalsum)



#n=int(input("Enter a number: "))
#sum1 = 0
#while(n > 0):
#    sum1=sum1+n
#    n=n-1
#print("The sum of first n natural numbers is",sum1)


# loops are useful for data incremente