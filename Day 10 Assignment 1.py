import time as t

###Main Program
def read2ep(time_str): #Readable --> Epoch
	#Converting String Into 9tuple
	tupl9 = t.strptime(time_str,"%d-%m-%Y %H:%M:%S")
	#Converting 9tuple Into Epoch Time
	EpochTime = t.mktime(tupl9)
	del tupl9
	return EpochTime

#print("Enter Date And Time In dd-mm-yyyy HH:MM:SS Format:—")
#d_t = input("Enter: ")

##Extras
#For Creating Time Formattable Strings
def int2str(num):
	if num < 10:
		num = "0" + str(num)
	else:
		num = str(num)
	return num

#Printing Outputs Until User Breaks Loop
while True:
	print("Press Enter To Continue")
	print("Enter Any Key To Exit")
	if input() != "": break
	#Breaks Loop When User Enter Any Other Key
	
	from random import randint as rint
	#For Random Inputs

	yr = rint(1970,2037)
	mon = rint(1,12)
	
	'''
	Last Date Input Possible
	Date and Time: Tue Jan 19 08:44:07 2038
	Epoch Seconds: 2147483648.0
	'''
	
	if yr%4 == 0 and mon == 2:
		#Leap Year With February Month
		day = rint(1,29)
	elif mon == 2:
		#February Month
		day = rint(1,28)
	elif mon==4 or mon==6 or mon==9 or mon==11:
		#Months With 30 Days
		day = rint(1,30)
	else:
		#Months With 31 Days
		day = rint(1,31)
	
	
	sec = int2str(rint(0,59))
	min = int2str(rint(0,59))
	hr  = int2str(rint(0,23))
	day = int2str(day)
	mon = int2str(mon)
	yr  = int2str(yr)
	#All Time Variables Are Converted To str
	
	d_t = f"{day}-{mon}-{yr} {hr}:{min}:{sec}"
	print(d_t)
	#Converting Into Epoch
	epoch = read2ep(d_t)
	print("The Epoch Form Of Input Date-Time:",epoch)
	#For Rechecking:
	#print(t.ctime(epoch))
	print("-"*60,"\n")

print("//Exit//")