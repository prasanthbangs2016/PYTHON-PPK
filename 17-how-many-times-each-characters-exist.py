'''

Desc: How many times each character exist

'''

letters={}  # empty dictionary
x="Book"


# To access keys letter.get(i,0)

# letter.get(i,0)+1 with this addition


for i in x:
	letters[i]=letters.get(i,0)+1
print(letters)


# k,v variables

for k,v in letters.items():
	print("{} is found {} times".format(k,v))

	
	
'''

output

{'B': 1, 'o': 2, 'k': 1}
B is found 1 times
o is found 2 times
k is found 1 times	

'''