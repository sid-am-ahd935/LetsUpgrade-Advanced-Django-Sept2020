#Program To Store All IP Adresses From WebPage

def ip_extractor(ip:'Regex',page : str)->None:
	
	import re
	found_ip = re.finditer(ip,page)
	#All IPs Found In Page In One Iter Object
	
	c = 0 #For Counting All IP Addresses
	for each in found_ip:
		#each=<ipMatchObject> From Iter Object
		c += 1		
		print(f"{c})",each.group())
		#Printing The IP Addresses
		
	#Extras:
	lines = page.count("\n")
	print("\n\nTotal Lines:",lines)
	print("Total IPs Collected:",c)
	print("Average IPs Per Line:",(c/lines))


def main():
	
	import requests as req
	url = 'https://study-ccna.com/classes-of-ip-addresses//'
	req_ob = req.get(url)
	page = req_ob.text
	#Extracting URL Data Into A String
	
	ip1 = "[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+"
	ip_extractor(ip1,page)
	#This RegEx Is The Basic Structure Of An IP
	#[0-9]+ : any no. of digits of integer > 0
	#\.     : interpreted as 'ignore this dot'
	
	#ip2 = "[0-9]+\.[0-9]+\.[0-9]+"
	#ip3 = "[0-9]+\.[0-9]+"
	#ip_extractor(ip2)
	#ip_extractor(ip3)
	


if __name__ == "__main__":
	main()