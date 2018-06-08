import os
os.system("cls")


total_sales=int(input("Please enter the sales values:"))
give_country=input("enter country name in ISO standard:")

if give_country == "IN":
    if total_sales <=50:
       print ("The total shipping cost is : 50rs")
elif total_sales <=100:
       print ("The total shipping cost is : 25rs")
elif total_sales <=150:
       print ("The total shipping cost is : 15rs")	  
else:
       print ("Shipping is free")
	   

if give_country == "US":
    if total_sales <=50:
       print ("The total shipping cost is : 5USD")
else:
       print ("Shipping is free")	   
	   
	   



# DURING SCRIPT RUN sales value and country format INDIA,USA, 	   
