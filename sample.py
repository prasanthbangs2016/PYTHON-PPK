totalsales = int(input("Please Enter The Sales Value : "))
givecountry = input("Please Enter The Country Name in ISO Standard : ")

if givecountry == "IN":
    if totalsales <= 50:
        print ("The Total Shipping Cost is  : 50INR")
elif totalsales <= 100:
        print ("The Total Shipping Cost is : 25INR")
elif totalsales <= 150:
	    print ("The Total Shipping Cost is : 5INR")
else:
        print ("The Shipping is Done FREE of Cost")