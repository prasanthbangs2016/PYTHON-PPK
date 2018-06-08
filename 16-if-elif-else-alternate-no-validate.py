var01=int(input("Enter first int value:"))
var02=int(input("Enter second int value:"))

if(var01 < var02):
  print ("first value is less than second value")
  print ("first value is:",var01,"second value is:",var02)
elif(var01 > var02):
  print ("first value is greater than second value")
  print ("the first value is:",var02,"second value is:",var02)
elif var01==var02:
  print ("first and second values are same")
  print ("the first value is:",var02,"second value is:",var02)  
else:
  print ("None of the values were matching hence terminating")

waitforinput=input("Enter any key to terminate")