'''

Description:- to print elements list in reverse order"

'''


import os
os.system("cls")

Days=['MON','TUE','WED','THURS','FRI','SAT','SUN']

i=len(Days)-1
print(i)


while(i>0):
	  print(Days[i])
	  i-=1
