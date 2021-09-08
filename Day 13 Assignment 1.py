#File Name Changer Through Config Input

import os
from configparser import ConfigParser as CP

#Assuming The Python File Is With The File Input.ini For Input
config = CP()
config.read("Day 13 Assignment 1 Input.ini")

#For Getting Full Path To File Directory
Folder = config.get("INPUT","current_path")

#To Get The File Extensions To Rename
ext1 = config.get("INPUT","From")

#To Rename The File Extensions Into
ext2 = config.get("INPUT","To")

#Changing Path Into The Given Directory
os.chdir(Folder)

#for each in os.listdir():
#	print(each)	
#print("\n")

#Iterating Through Every File
i = 0
for each in os.listdir():
	#Checking If Required To Change Extension
	if (each.rsplit(".",1)[1] == ext1):
		#Storing The New Name For Changing
		str1 = each.rsplit(".",1)[0] + "." + ext2
		print(f"Changed {each} to {str1}")
		#Changing Extension
		os.rename(each,str1)
		i += 1

print("\nTotal File(s) Renamed: %d,\nFrom [.%s] to [.%s]"%(i,ext1,ext2))

#for each in os.listdir():
#	print(each)