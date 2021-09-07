#Program to remove all 0s from left and add it to right in a sorted list

#input_str = input("Enter The Numbers Separated By Commas:\n")
input_str = "1,2,4,6,8,0,7,4,2,3,6,7,0,9,7,9,7,0,0,0,8,6,6,6,8,9,0,6,4,3,1,1,4,6,8,9,0,0,8,6,4,4,7,9,0"
l = input_str.split(",")
list1 = [int (i) for i in l]

list1.sort()

##Alternative Method (Inefficient)
#for i in range(len(list1)):
	#if list1[i] == 0:
	#	list1.remove(0) #removes from left
	#	list1.append(0) #adds to right

#Efficient Method
#for i in range(list1.count(0)):
#	list1.remove(0) #removes from left
#	list1.append(0) #adds to right


#More Efficient Method
c0 = list1.count(0)
for i in range(c0): list1.remove(0)
list1 = list1 + ([0] * c0)

print(list1)