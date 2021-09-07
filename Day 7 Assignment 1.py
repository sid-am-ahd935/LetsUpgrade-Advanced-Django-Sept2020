
#input_str = input("Enter The First List:\n")
#l1 = [int (i) for i in (input_str.split())]
#OR
#l1 = [int (i) for i in (input_str.split(","))]

#input_str = input("Enter The Second List:\n")
#l2 = [int (i) for i in (input_str.split())]
#OR
#l2 = [int (i) for i in (input_str.split(","))]

l1 = [5,15,25,35,45,55,65,75,85]
l2 = [10,20,30,40,50,60,70]



##First Approach 
#Good For Time Management
#O.K. For Space Management
def MergeSort1(l1,l2):
	l12 = []
	size = len(l1) + len(l2)
	ptr1 = 0
	ptr2 = 0
	#print("size=",size)
	for i in range (size-1):
		#For One List range(size) Is Ok
		#But For Two Lists It Will Show
		#List Index Out Of Range
		#print("i=",i)
		#print("ptr1=",ptr1)
		#print("ptr2=",ptr2,"\n\n")
		if ptr1 == len(l1):
			#List1 Has No More Values Left
			#Shown By Index Out Of Range
			#Inserting The Remaining Values
			#From List2 And Breaking The Loop
			l12.extend(l2)
			break
		if ptr2 == len(l2):
			#List2 Has No More Values Left
			#Shown By Index Out Of Range
			#Inserting The Remaining Values
			#From List1 And Breaking The Loop
			l12.extend(l1)
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
#As pop and insert Methods May Take O(N) Time
#Best For Space Management
def MergeSort2(l1,l2):
	l12 = []
	size = len(l1) + len(l2)
	l1.reverse()
	l2.reverse()
	#For Reducing Time Complexity Of
	#append And pop Functions
	#print("size=",size)
	
	for i in range (size-1):
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
		if l1[ptr1] == l2[ptr2]:
			l12.append(l1[ptr1])
			l12.append(l2[ptr2])
			continue
			
	return l12

print(MergeSort1(l1,l2))
#print(MergeSort2(l1,l2))