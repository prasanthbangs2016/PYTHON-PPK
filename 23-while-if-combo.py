import os
os.system("cls")

sp=int(input("Enter start point:"))
if (sp <=0 or sp >10): # if zero or 10 then print cant proceed, if 1 to 10 then print from starting point of while condition
   print ("Sorry! start point is out of Boundary,cant proceed..")
else:
   while (sp <=10):
      print("The line no is:",sp)
      sp=sp+1
	  
	  
#o/p
#enter any integer:1
#The sequence no is: 1
#The sequence no is: 2
#The sequence no is: 3
#The sequence no is: 4
#The sequence no is: 5
#The sequence no is: 6
#The sequence no is: 7
#The sequence no is: 8
#The sequence no is: 9
#The sequence no is: 10	  