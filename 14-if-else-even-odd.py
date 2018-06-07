# The script is to evaluate odd number or even number

var01 = int(input("enter any integer:"))

result = var01%2  #pulling up input value with modulus by 2

if (result ==0): #comparision operator with zero for input value to find even or odd
  print ("the given number is an even")
  print ("The entered number even value is:",var01)
else:
  print ("the give number is an odd")
  print ("the entered number odd value is:",var01)
