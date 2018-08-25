'''

Desc: command line arguments like unix scripting

command line arguments to work, we need to import sys module

sys	Access system-specific parameters and functions.
===================================================
This module provides access to some variables used or maintained by the interpreter and 
to functions that interact strongly with the interpreter. It is always available.

0	denotes script name
1	first parameter
etc

'''

import sys
#v1=sys.argv[1]
#v2=sys.argv[2]
#v3=v1+v2
#print("sum of 2 numbers is",v3)

v1=sys.argv[1]
v2=sys.argv[2]
v3=int(v1)+int(v2)
print("first argument is",sys.argv[1])
print("second argument is",sys.argv[2])
print("sum of 2 numbers is",v3)

# for the command line argument we have to explicitly tell the type of data it is so that sys module detects and gives results accordingly.

