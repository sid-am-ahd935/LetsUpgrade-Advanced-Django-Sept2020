#Dummy Finder Program Assignment

import os
from collections import defaultdict as ddict

#Creating Two Default Dicts
#Each For Files And Directories
file_dict = ddict(list)
dir_dict = ddict(list)

#Indexing All Available Folders And Files
i = 0 #For Counting Total Dir(s)
j = 0 #For Counting Total Files(s)
for r,d,f in os.walk("/storage/emulated/0"):
	for each in d:
		dir_dict[each].append(r)
		i += 1
	for each in f:
		file_dict[each].append(r)
		j += 1


print("\\"*4, "Indexing Done", "/"*4)
print("Dir(s) Indexed:",i)
print("File(s) Indexed:",j)


#User Input To Search
print("\nEnter The File Name, Initial Part Is Also Accepted If Full Name Not Available:-")
#name = input("Enter:")
name = " Assignment"
print("Enter: ",name)
i = 0 #For Counting Found Dir(s)
j = 0 #For Counting Found File(s)

print("\n"+"*"*15)
print("Dir(s) Found:")
print("*"*15,"\n")
#Searching Through Dir(s) And Printing Them
for k,v in dir_dict.items():
	if name.lower() in k.lower():
		for each in v:
			i += 1
			print("*"*60)
			print(f"\n{i})\n\n"+(each+"/"+k).replace(" ","_"),"\n")
			#Printing Full Path, " " As "_"
			
print("*"*60,"\n")


print("\n"+"*"*15)
print("File(s) Found:")
print("*"*15,"\n")
#Searching Through Files(s) And Printing Them
for k,v in file_dict.items():
	if name.lower() in k.lower():
		for each in v:
			j += 1
			print("*"*60)
			print(f"\n{j})\n\n"+(each+"/"+k).replace(" ","_"),"\n")
			#Printing Full Path With " " As "_"
			
print("*"*60,"\n\n")

#A Lot Of Print Statements Are 
#For Beautification Purposes Only
print("Total Dir(s) Found:",i)
print("Total File(s) Found:",j)

#And Along With The Printing, We Can Add
#TheIndexes Of The Found Files In A Dict
#With Their Path As Values
#To Use It For Easy Accessible
#Like Copy Paste Or Simply Opening It