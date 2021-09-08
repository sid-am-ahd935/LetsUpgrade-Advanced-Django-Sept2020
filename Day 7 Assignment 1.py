#Dummy MergeSort Program For Two Sorted Lists

##First Approach 
#Good For Time Management
#O.K. For Space Management
#Stable Sort
def MergeSort1(l1,l2):
	l12 = []
	size = len(l1) + len(l2)
	ptr1 = 0
	ptr2 = 0
	#print("size=",size)
	for i in range (size):
		#Eg)len(l1) =10, len(l2) =10
		#Eg)len(l12)=20, but iteration=20-1=19
		#Hence range(size) Is OK
		#print("i=",i)
		#print("ptr1=",ptr1)
		#print("ptr2=",ptr2,"\n\n")
		if ptr1 == len(l1):
			#List1 Has No More Values Left
			#Shown By Index Out Of Range
			#Inserting The Remaining Values
			#From List2 And Breaking The Loop
			l12.extend(l2[ptr2:])
			break
		if ptr2 == len(l2):
			#List2 Has No More Values Left
			#Shown By Index Out Of Range
			#Inserting The Remaining Values
			#From List1 And Breaking The Loop
			l12.extend(l1[ptr1:])
			break
		if l1[ptr1] < l2[ptr2]:
			l12.append(l1[ptr1])
			ptr1 +=1
			continue
		if l2[ptr2] < l1[ptr1]:
			l12.append(l2[ptr2])
			ptr2 +=1
			continue
		if l1[ptr1] == l2[ptr2]:
			l12.append(l1[ptr1])
			l12.append(l2[ptr2])
			ptr1 +=1
			ptr2 +=1
			continue
			
	return l12

##Second Approach
#Worst For Time Management
#pop() & append() May Take O(N) Time If Worst
#Best For Space Management
#Unstable Sort
def MergeSort2(l1,l2):
	l12 = []
	size = len(l1) + len(l2)
	l1.reverse()
	l2.reverse()
	#For Reducing Time Complexity Of
	#append And pop Functions
	#print("size=",size)
	
	for i in range (size):
		if len(l1) == 0:
			#List1 Has No Elements Left
			#Since len = 0
			#Inserting The Remaining Values
			#From List2 And Breaking The Loop
			l2.reverse()
			l12.extend(l2)
			l2.clear()
			break
		if len(l2) == 0:
			#List2 Has No Elements Left
			#Since len = 0
			#Inserting The Remaining Values
			#From List1 And Breaking The Loop
			l1.reverse()
			l12.extend(l1)
			l1.clear()
			break
		
		ptr1 = l1.pop()
		ptr2 = l2.pop()
		#print("i=",i)
		#print("ptr1=",ptr1)
		#print("ptr2=",ptr2,"\n\n")
		
		if ptr1 < ptr2:
			l12.append(ptr1)
			l2.append(ptr2)
			continue
		if ptr2 < ptr1:
			l12.append(ptr2)
			l1.append(ptr1)
			continue
		if ptr1 == ptr2:
			l12.append(ptr1)
			l12.append(ptr2)
			continue
			
	return l12



#input_str = input("Enter The First List:\n")
#l1 = [int (i) for i in (input_str.split())]
#OR
#l1 = [int (i) for i in (input_str.split(","))]

#input_str = input("Enter The Second List:\n")
#l2 = [int (i) for i in (input_str.split())]
#OR
#l2 = [int (i) for i in (input_str.split(","))]

if __name__ != "__main__":
    exit()

while True:
	print("Press Enter To Repeat The Sorting")
	print("Enter Any Key To Exit")
	if input() != "": print("/Exit/"); break
	#Repeating Until User Enters Any Other Key

	from random import randint as r
	#For Random Inputs Of Random Sizes

	l1= sorted([r(0,100) for i in range(r(5,20))])
	l2= sorted([r(0,100) for i in range(r(5,20))])
	#Printing Beautifully
	print("First List:")
	print(l1)
	print("Length:",len(l1))
	
	print("\nSecond List:")
	print(l2)
	print("Length:",len(l2))
	
	print("\n\nMergeSorted List:")
	l12 = MergeSort1(l1,l2)
	print(l12)
	print("Length:",len(l12))
	
	#print("\n\nMergeSorted List:")
	#l21 = MergeSort2(l1,l2)
	#print(l21)
	#print("Length:",len(l12))
	
	print("_"*60,"\n")