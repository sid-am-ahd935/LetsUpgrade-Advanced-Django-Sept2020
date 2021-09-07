#Program to return all indexes of all occurences of an element in a list

#input_str = input("Enter Elements For List With Commas To Separate Them:\n")
input_str = "1,2,3,5,1,1,4,4,2,5,6,6,5,4,21,3,5,7,9,7,6,5,3,1,1,3,4,2,1,1,2,3,4,5,4,2,1,1,2,4,4,1,2,3,4,2,1,1,3,4,4,5,5,2,1,1,4,5,6,6,5,7,8,8,4,2,1,1,4,5,5,6,6,0"
l= input_str.split(",")
list1 = [int (i) for i in l]

shift = 0
#A Variable Which Only Allows The index() To Start At An Index After Element's Previous Occurence 

#target = int (input("\nEnter The Element To Be Found: "))
target = 1

print(f"All indexes for '{target}':\n")
for i in range(list1.count(target)):
	if target in list1[shift:]:
		ans = list1.index(target,shift)
		print(ans)
		shift = ans +1