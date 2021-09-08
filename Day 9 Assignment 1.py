from random import sample as ch, shuffle as mix

#All Alphabets Into A List
chars = [chr (i) for i in range(97,123)] + [chr (i) for i in range(65,91)]
#All Numbers Inti A List
nums = ['1','2','3','4','5','6','7','8','9','0']
#All Symbols Inti A List
symbols = ["#", "@", "$", "%", "!", "?"]

#Infinite Loop Which User Can Break At Will
while True:
	loop = input("Enter To Continue and Enter Any Key To Exit: ")
	if loop != "": break
	
	#Password Contains 6 Characters
	password =  ch(chars, k=6)
	#Password Contains 4 Numbers
	password += ch(nums, k=4)
	#Password Contains 2 Symbols
	password += ch(symbols, k=2)
	#Password Is Given A Good Shuffle
	mix(password)
	#Password Converted Into A String From List
	password = "".join(password)
	#Printing Password
	print("Password: ",password,"\n")
	#print(symbols)
	
print("/Exit/")