'''

Desc: finding no of player

'''

n=int(input("enter no.of players\n"))

# dictionary has no key & values initially(making dictionary with empty as i give data in runtime)

player_details={}

#loop variable(initialize)

i=0

# Based no of players entered loop should start

# start

while(i<n):
	player_name=(input("enter player name\n"))
	player_score=int(input("enter player score\n"))

# updating empty dictionary by update function
	player_details.update({player_name:player_score})
	i+=1 #incrementing loop
print("player_details\n",player_details)

# checking player name existance

player=input("enter player name to search\n")
if(player in player_details.keys()):
	print("player found:",player_details)
else:
	print("player not found",player_details)

	