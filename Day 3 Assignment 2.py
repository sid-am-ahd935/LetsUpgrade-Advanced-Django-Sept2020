#Program to sort the list in ascending order according to the sum contained in individual tuple elements

#input_str = input("Enter The Tuples With Each Tuple Elements Separated By Spaces And Each Tuple Separated By A ',': \n")
input_str = "0 100, 7 15, 22 45, 19 45, 50 20, 19 21, 23 41"

tups = input_str.split(",")
list_of_tups = [tuple(i.split()) for i in tups]

def tuplesum(sublist):
	sum = 0
	for i in sublist:
		sum += int (i)
	#Sums All Items From Tuple If More Than Two
	#Also, Can Be Unpacked If Only Pairs Using
	#a,b = sublist
	#sum = a+b
	return sum

list_of_tups.sort(key = tuplesum)
for each in list_of_tups:
    print(each)