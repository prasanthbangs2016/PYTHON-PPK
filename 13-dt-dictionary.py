'''
Data type: Dictionary

1. Data will be key,value
2.using key,we can access value
3.make sure key cannot be changed
4.denote {} parenthesis

'''

# Example

details={'name':'PRASHANTH','DOB':'31-03-1989'}

print(details)

print("type of data is:",type(details))


#appending data

details['job']='IT consultant'
print(details)

# accessing data using key

mydict = {
  'Apple': {'American':'16', 'Mexican':10, 'Chinese':5},
  'Grapes':{'Arabian':'25','Indian':'20'} }

print(mydict["Apple"])
print(mydict["Grapes"])


