import os
os.system("cls")

mypassword=""
while mypassword != "personal":
 mypassword =input("Enter paswword:")
 if mypassword == "personal":
    print("congrats your password matched,priviliged to enter")
 else:
    print("sorry!password doesnt matches,we cannot allow you")
	

#Enter paswword:prashanth
#sorry!password doesnt matches,we cannot allow you
#Enter paswword:"prashanth"
#sorry!password doesnt matches,we cannot allow you
#Enter paswword:"personal"
#sorry!password doesnt matches,we cannot allow you
#Enter paswword:personal
#congrats your password matched,priviliged to enter	

#taking variable and assigned with null value
#while mypassword is not equal to personal,so whenever condition get true,the while loop goes inside while loop and asked to enter password 
#untill it matches with personal keyword,it wont allow.