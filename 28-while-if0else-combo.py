#inputvalue=True
inputvalue=int(input("input number within 10 and 20:"))
while inputvalue:
  print(inputvalue)
  inputvalue=inputvalue+1
  if (inputvalue >=10 and inputvalue<=20):
      print(inputvalue)
	  #inputvalue=False
  else:
      print("Sorry! Number shoulb be in btwn 10 and 20 only")
	  
	  
#print ("finally you entered correct values")
print ("Terminating the process as valid input is found:",inputvalue)