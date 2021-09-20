import os,re
from argparse import ArgumentParser as AP

version = 1.91

G = '\u001b[100;106m' #Green Background
Y = '\033[93m' #Yellow
R = '\033[91m' #Red
W = '\033[0m'  #Colour Reset Code, Here White
P = '\u001b[95m' #Pink
C = '\u001b[36m' #Cyan

#---------------------------------------------
##To Print Beautifully, Is Called By All Funcs
def Print(func,args):
	word = args[0]
	dir = args[1]
	
	print("\n" + "—"*65)
	print("The Word Searched For:",word)
	print("-"*40)
	found, not_working = func(word,dir)
	
	if found == 0:
		print(f"\nNo Files Containing {R}{word}{W} Found")
	else:
		print(f"\nTotal File(s) Found Containing {R}{word}{W}: {G} {found} {W}")
	
	if len(not_working) > 0:
		print("\n" + "*"*65 + "\n")
		print("File(s) Not Accessible:\n")
		for i in range(len(not_working)):
			print(f"{i+1}) {not_working[i]} Can Not Be Processed.")
		
	print("\n" + "—"*65)
	

#---------------------------------------------
#Word Search With Sensitive Case 
#Including Line Number

def func_m(word,dir):
	found = 0
	not_working = []
	
	for files in os.walk(dir):
		cwd = (files[0])
		
		#Prints Files Containing Word
		#And Increment Number Of Founds
		#While Collecting Non-Accessible Files
		for each in files[2]:
			try:
				f= open(f"{cwd}/{each}", 'r')
				data = f.read()
				f.close()
			except:
				not_working.append(each)
				continue
			#Collecting Non-Accessible Files
				
			#Searching For Word Inside File
			m = re.search(word, data)
			if m:
				found +=1
				line= data[:m.start()].count("\n") + 1
				#If Count=0, No Lines Before m And m.group() Will Be In Line 1
				print(f"{R}{m.group()}{W} Found In {C}{cwd}/{each}{W} In Line {P}{line}{W}")
				#os.getcwd() = files[0]
	
	#When All Files Are Accessed Or 
	#No Files Are Available,
	#Return The No. Of Found And
	#Non Accessible File Names
	return found, not_working
	
	
#---------------------------------------------
#Word Search With Sensitive Case 
#Without Line Number

def func_s(word,dir):
	not_working = []
	found = 0
	
	for files in os.walk(dir):
		cwd = (files[0])
		
		#Prints Files Containing Word
		#And Increment Number Of Founds
		#While Collecting Non-Accessible Files
		for each in files[2]:
			try:
				f= open(cwd+"/"+each, 'r')
				data = f.read()
				f.close()
			except:
				not_working.append(each)
				continue
			#Collecting Non-Accessible Files
				
			#Searching For Word Inside File
			m = re.search(word, data)
			if m:
				found += 1
				print(f"{R}{m.group()}{W} Found In {C}{cwd}/{each}{W}")
				#os.getcwd() = files[0]
	
	#When All Files Are Accessed Or 
	#No Files Are Available,
	#Return The No. Of Found And
	#Non Accessible File Names
	return found, not_working

#---------------------------------------------
#Recursively Searching Through Files 
#For Case Sensitive Word

def func_r(word,dir,found=0,not_working=[]):
	
	#To Get All Dirs Available
	dirs = [i for i in os.listdir(dir) if os.path.isdir(dir+"/"+i)]
	#To Get All Files Available
	files = [i for i in os.listdir(dir) if os.path.isfile(dir+"/"+i)]
	
	#Accessing The Deepest Folder First
	#Calls Itself And Prints Files Containing
	#Word And Increment Number Of Founds
	#While Collecting Non-Accessible Files
	if len(dirs) > 0:
		for i in dirs:
			path = (dir+"/"+i)
			found,not_working = func_r(word,path,found,not_working)
	
	#Printing The Accessible Files 
	#Containing Word
	#From The Bottom To The Top
	#Using Recursion
	for each in files:
		try:
			f= open(dir+"/"+each, 'r')
			data = f.read()
			f.close()
		except:
			#Collecting Non-Accessible Files
			not_working.append(each)
			continue
		
		#Searching For The Word Inside File
		m = re.search(word, data)
		if m:
			#When Word Is Found,
			#Increase Count
			found += 1
			#And Print
			lin=data[:m.start()].count('\n')+1
			print(f"{R}{m.group()}{W} Found In {C}{dir}/{each}{W} In Line {P}{lin}{W}")
			#os.getcwd() = files[0]
	
	#When All Files Are Accessed Or 
	#No Files Are Available,
	#Return The No. Of Found And
	#Non Accessible File Names
	return found, not_working
	
	
#---------------------------------------------
#Word Search With Insensitive Case & Line No.

def func_mi(word,dir):
	found = 0
	not_working = []
	
	for files in os.walk(dir):
		cwd = (files[0])
		
		#Prints Files Containing Word
		#And Increment Number Of Founds
		#While Collecting Non-Accessible Files
		for each in files[2]:
			try:
				f= open(f"{cwd}/{each}", 'r')
				data = f.read()
				f.close()
			except:
				not_working.append(each)
				continue
			#Collecting Non-Accessible Files
				
			#Searching For Word Inside File
			m = re.search(word, data, re.I)
			if m:
				found +=1
				line= data[:m.start()].count("\n") + 1
				#If Count=0, No Lines Before m And m.group() Will Be In Line 1
				print(f"{R}{m.group()}{W} Found In {C}{cwd}/{each}{W} In Line {P}{line}{W}")
				#os.getcwd() = files[0]
	
	#When All Files Are Accessed Or 
	#No Files Are Available,
	#Return The No. Of Found And
	#Non Accessible File Names
	return found, not_working
	
	
#---------------------------------------------
#Search With Insensitive Case Without Line No.

def func_si(word,dir):
	not_working = []
	found = 0
	
	for files in os.walk(dir):
		cwd = (files[0])
		
		#Prints Files Containing Word
		#And Increment Number Of Founds
		#While Collecting Non-Accessible Files
		for each in files[2]:
			try:
				f= open(cwd+"/"+each, 'r')
				data = f.read()
				f.close()
			except:
				not_working.append(each)
				continue
			#Collecting Non-Accessible Files
				
			#Searching For Word Inside File
			m = re.search(word, data, re.I)
			if m:
				found += 1
				print(f"{R}{m.group()}{W} Found In {C}{cwd}/{each}{W}")
				#os.getcwd() = files[0]
	
	#When All Files Are Accessed Or 
	#No Files Are Available,
	#Return The No. Of Found And
	#Non Accessible File Names
	return found, not_working

#---------------------------------------------
#Seaching Word Through Files Recursively
#For Finding Case Insensitive Word

def func_ri(word,dir,found=0,not_working=[]):
	
	#To Get All Dirs Available
	dirs = [i for i in os.listdir(dir) if os.path.isdir(dir+"/"+i)]
	#To Get All Files Available
	files = [i for i in os.listdir(dir) if os.path.isfile(dir+"/"+i)]
	
	#Accessing The Deepest Folder First
	#Calls Itself And Prints Files Containing
	#Word And Increment Number Of Founds
	#While Collecting Non-Accessible Files
	if len(dirs) > 0:
		for i in dirs:
			path = (dir+"/"+i)
			found,not_working = func_ri(word,path,found,not_working)
	
	#Printing The Accessible Files 
	#Containing Word
	#From The Bottom To The Top
	#Using Recursion
	for each in files:
		try:
			f= open(dir+"/"+each, 'r')
			data = f.read()
			f.close()
		except:
			#Collecting Non-Accessible Files
			not_working.append(each)
			continue
		
		#Searching For The Word Inside File
		m = re.search(word, data, re.I)
		if m:
			#When Word Is Found,
			#Increase Count
			found += 1
			#And Print
			lin=data[:m.start()].count('\n')+1
			print(f"{R}{m.group()}{W} Found In {C}{dir}/{each}{W} In Line {P}{lin}{W}")
			#os.getcwd() = files[0]
	
	#When All Files Are Accessed Or 
	#No Files Are Available,
	#Return The No. Of Found And
	#Non Accessible File Names
	return found, not_working
	
	
#---------------------------------------------
##Main Function To Run The Whole Program

def main():
	a = AP(description= "Finds First Occurence Of The Searched [str] Word In Text Files Provided By [DIR] (RegEx Available) (Current Directory= '.')")
	
	
	a.add_argument("-v", dest= "version", default= None, action= 'store_true', help= 'Print Current Version Number Of This Program')
	a.add_argument("-m", nargs= 2, metavar= ('[str]', '[DIR]'), help = 'To Get Files With Line Number Containing str')
	a.add_argument("-s", nargs= 2, metavar= ('[str]', '[DIR]'), help = 'To Get Only The Files Containing str')
	a.add_argument("-r", nargs= 2, metavar= ('[str]', '[DIR]'), help = 'To Search Like -m Option In Recursive Order')
	a.add_argument("-mi", nargs= 2, metavar= ('[str]', '[DIR]'), help = '-m Option With Case Insensitive')
	a.add_argument("-si", nargs= 2, metavar= ('[str]', '[DIR]'), help = '-s Option With Case Insensitive')
	a.add_argument("-ri", nargs= 2, metavar= ('[str]', '[DIR]'), help = '-r Option With Case Insensitive')
	
	#a.print_help()
	args = a.parse_args()
	#"-mi Import /storage/emulated/0/Python".split())
	if args.version:
		print("—"*65)
		print("\nCurrent Version: %.3f\n"%version)
		print("—"*65)
	
	if args.m: 	Print(func_m,args.m)
	
	if args.s: 	Print(func_s,args.s)
		
	if args.r: 	Print(func_r,args.r)
		
	if args.mi:	Print(func_mi,args.mi)
	
	if args.si:	Print(func_si,args.si)
		
	if args.ri:	Print(func_ri,args.ri)
	
#---------------------------------------------
#Running The Program
if __name__ == "__main__":
	main()