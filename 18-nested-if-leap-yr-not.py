given_year=int(input("enter year in 4 digits:"))


if (given_year % 4) == 0:
   if (given_year % 100) == 0:
       if (givenyear % 400) == 0:
           print (given_year, " is A Leap Year")  #print if condition is true
       else:
           print (given_year, " is Not A Leap Year") # 3rd if else
   else:
       print (given_year, " is A Leap Year") # 2nd if else
else:
   print (given_year, "is Not A Leap Year") # 1st if else