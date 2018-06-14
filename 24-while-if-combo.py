import os
os.system("cls")

fv=int(input("Enter first value:"))
sv=int(input("Enter second value:"))

if (fv <=0 or sv >10):
   print("The first and second values were out boundary,cant proceed")
else:
   while(fv<=sv):
     print ("line no is:",sv)
     sv=sv+1
	 #sv=sv+1 (without this update statement loop will be infinie loop)
	 

#o/p
#Enter first value:1
#Enter second value:3
#line no is: 3
#line no is: 4
#line no is: 5
#line no is: 6
#line no is: 7
#line no is: 8
#line no is: 9
#line no is: 10
#line no is: 11
#line no is: 12
#line no is: 13
#line no is: 14
#line no is: 15
#line no is: 16
#line no is: 17
#line no is: 18
#line no is: 19
#line no is: 20
#line no is: 21
#line no is: 22
#line no is: 23
#line no is: 24
#line no is: 25
#line no is: 26
#line no is: 27
#line no is: 28
#line no is: 29
#line no is: 30
#line no is: 31
#line no is: 32	 