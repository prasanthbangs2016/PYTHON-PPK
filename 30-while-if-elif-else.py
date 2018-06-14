import os
os.system("cls")
import random
samplevalue =20
values guessed = int(samplevalue * random.random())+1
yourguess=0
while yourguess !=valueguessed:
  youguess=int(input("pls enter your guessed number:"))
  
  if yourguess >0:
     if yourguess > value guessed:
	    print("The guessed number too big")
	 elif yourguess < valueguessed:
	    print('The guessed number too small")
  else:
      print ("sorry! you decide to leave game")
	  break
else:
  print("thats the spirit,finally guessed correctly")
	  