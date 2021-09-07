#Hydra Assignment

#All Shield Members And Their Contacts Are Inserted Into A Dictionary For Reducing Time Complexity
shield = {
	'Nick Fury' : ('Tony Stark', 'Maria Hill', 'Norman Osborn'),
	
	'Hulk' : ('Tony Stark', 'HawkEye', 'Rogers'), 
	
	'Rogers' : ('Thor'),
	
	'Tony Stark' : ('Pepper Potts', 'Nick Fury'),
	
	'Agent 13' : ('Agent X', 'Nick Fury', 'Hitler'),
	
	'Thor' : ('HawkEye', 'BlackWidow'),
	
	'BlackWidow' : ('HawkEye'),
	
	'Maria Hill' : ('Hulk', 'Rogers', 'Nick Fury'),
	
	'Agent X' : ('Agent 13', 'Rogers'),
	
	'Norman Osborn' : ('Tony Stark', 'Thor')
	}
	

#We Know He Is Not Hydra
team = { 'Nick Fury' }


#We Know He Knows People Who Are Not Hydra
team.update(shield['Nick Fury'])


#Everyone Is Suspicious At First
#Hence All Shield Agents Are In Possible Hydra List
hydra = set()
for i in shield:
	if len(str(shield[i][0])) == 1:
		hydra.add(shield[i])
		continue
	hydra.update(shield[i])
	

#Updating Friendly Team By Checking Each Others Contacts
for i in shield:
	if i in team:
		if len(str(shield[i][0])) == 1:
			team.add(shield[i])
			continue
		team.update(shield[i])
		
		
#Updating Friendly Team Again To Add Remaining Contacts Missed At First Due To Unsortedness
for i in shield:
	if i in team:
		if len(str(shield[i][0])) == 1:
			team.add(shield[i])
			continue
		team.update(shield[i])
		

'''
The if-continue statement is added because for when there is no list in a key, both the set team and hydra would add the letters of the single string value.
If shield[i] is a string not a list, shield[i][0] is just a letter, it's len ==1,  it is added to the set
If shield[i] is a list, shield[i][0] is a string and it's len != 1, it is updated to the set
'''


#Removing Team From Hydra Suspects
for i in team:
	hydra.remove(i)
	
	
	
#Exposing All Hydra Agents
print(sorted(hydra))
#P.S. How Is Even Hitler There, Shouldn't He Have Possibly Died By Now??!