import datetime
import sys

#Due To Performance Issues,
#The Device Only Runs Upto 1 with 7 0's

def generated(main_list):
	t1 = datetime.datetime.now()
	list1 = (each**2 for each in main_list)
	for each in list1:
		each
	t2 = datetime.datetime.now()
	print ("\nTime Taken While Using Generator:", t2-t1)
	print ("Memory Taken By Generator:", sys.getsizeof(list1))

def listed(main_list):
	t1 = datetime.datetime.now()
	list1 = [each**2 for each in main_list]
	for each in list1:
		each
	t2 = datetime.datetime.now()
	print ("\nTime Taken While Using List", t2-t1)
	print ("Memory Taken By List:", sys.getsizeof(list1))


while True:
	num = input('\n\nEnter Size Of List: ')
	if not num.isnumeric(): break
	
	num = int(num)

	list1 = list(range(num))
	
	generated(list1)
	listed(list1)

print("Program Ended")
	