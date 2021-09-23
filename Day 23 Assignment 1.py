from threading import Thread
import os,pickle,time

#---------------
t1 = time.time()
#---------------

class finder:
	
	dict1 = {}
	#To Store All File Indexes
	drive = ["/storage/emulated/0/Python"]
	#To Store All Drives/Folders To Traverse
	
	#Main Method To Traverse Through Dirs
	#Adding Files To dict1
	def walker(path1):
		
		for root,dirs,files in os.walk(path1):
			for file in files:
				finder.dict1.setdefault(file, []).append(root + "/" + file)
	
	#Creating Threads And With Each Thread,
	#Adding Files To dict1 Through walker
	def indexer(path):
		folders = list(os.walk(path))[0][1]
		#To Get The Dirs Present In This Drive
		#print(folders)
		
		threads = []
		#Storing Threads To join() All At End
		#For Blocking Further Progress
		
		#Each Thread "walk"s Through Each Dir
		for each in folders:
			dir = path + "/" + each
			th1 = Thread(target= finder.walker, args= (dir,))
			th1.start()
			threads.append(th1)
		
		#Joining All Threads To Run Remaining
		#Part Of Program After Indexing Done
		for th in threads:
			th.join()
	
	#Method To Add Drives Into Class Variable
	@classmethod
	def add_drive(cls,drive):
		cls.drive.append(drive)
	
	#Method To Run All Necessary Functions
	def main():
		#Indexing Through Each Drive
		for path in finder.drive:
			finder.indexer(path)
		
		#Storing All File Names With Indexes
		#As A Dict Into The The Given File
		with open("/storage/emulated/0/LetsUpgrade Python/Day 23 Assignment 1.pickle", "wb") as f:
			pickle.dump(finder.dict1,f)


#with open("/storage/emulated/0/LetsUpgrade Python/Day 23 Assignment 1.pickle", "rb") as f:
	#dict2 = pickle.load(f)
#print(len(dict2))

##To Prevent Using main() After Import
if __name__ == "__main__":
	finder.add_drive("/storage/emulated/0/LetsUpgrade Python")
	finder.main()
	#---------------
	t2 = time.time()
	#---------------
	print("Done In",(t2-t1),"seconds")
