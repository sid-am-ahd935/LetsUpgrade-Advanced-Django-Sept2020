#Program to sort all ip addresses based on the network id, that is, the last token


#input_ip = input ("Enter The IP Addresses Each Separated By A Space: ")
input_ip = "192.158.40.5 192.158.40.42 192.158.40.21 192.158.40.6 192.158.40.105 192.158.40.20 192.158.40.92 192.158.40.95"

#Creating A List Of IP Addresses
iplist = input_ip.split()

#Creating A List Of Individual List Of IP Tokens
iplists = [i.split(".") for i in iplist]

#Note: All elements in these lists are still strings. No effort is put to change them into int. Sorting is done via int in the function itself.

#Returns The Last Token As Int For Sorting
def lasttokenisint(x):
	return int (x[-1])

#Sorting With Last Token As Key
iplists.sort(key = lasttokenisint)

#Sorted Based On Last Token
print("Printing In Ascending Order Of The Network I.D.s:")
for i in range(len(iplists)):
	print(iplists[i])