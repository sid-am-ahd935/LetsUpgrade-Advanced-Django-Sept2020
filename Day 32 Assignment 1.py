import socket,time
from threading import Thread
G = "\u001b[32m"
R = "\u001b[31m"
W = "\033[0m"


def handle_client(c,addr):
	
	print(addr,R,"--->connected",W)
	
	data= c.recv(1024)
	data = int(data.decode())
	print(R,"Received From Client:",W,data)
	data = data ** 2
	
	print(R,"Sending Result To Client...",W)
	print(R,"Sent.",W)
	c.send(str(data).encode())
	
	print(R,"Closing Connection...",W)
	print(R,"Server Connection Closed.",W)
	c.close()


def server():
	
	#Creating Server Socket
	s = socket.socket()
	#Storing Server Details In Func Attributes
	server.host = "localhost"
	server.port = 12345
	host = server.host
	port = server.port
	server.started = False
	
	#For Finding Available Ports To Run Server
	while not server.started:
		try:
			#Allocating Server At (host,port) Address
			s.bind((host,port))
			#Starting Server
			s.listen(2)
			#Storing Server Socket In Func Attributes For Later
			server.socket = s
			server.started = True
			#Error When Port Already In Use
		except:
			#Change Server Port And Bind Again
			#Using The while Loop
			server.started = False
			port = port + 1
			server.port = port
	
	print(R,f"Server Socket Created Of {host= } & {port= }",W)
	print("-"*50)
	
	while server.started:
		c,addr = s.accept()
		th1 = Thread(target= handle_client,args= (c,addr), daemon= True)
		#Daemon Thread To Close Every Socket
		#Connection When MainThread Has Closed
		th1.start()
		

def client(nums : list,host,port):
	#nums -> Collection Of Data To Send
	
	for i in nums:
		print("*"*60)
		c = socket.socket()
		print(G,"Creating Client Socket",W)
		#Creating Client Socket
		c.connect((host,port))
		print(G,"Establishing Connection With The Server...",W)
		#Creating Connection To Server
		c.send(str(i).encode())
		print(G,"Sending Data To Server..",W)
		#Sending 'data'
		ans = int((c.recv(1024)).decode())
		print(G,"Received Result",W)
		#Receiving 'Answer'
		
		print(G,"Answer Received:",W,ans)
		c.close()
		print(G,"Closing Client Socket...",W)
		print(G,"Client Socket Closed",W)
		#Closing Client Socket
	
	return
		

def main():
	print("Enter Numbers With Spaces To Separate Each:")
	data = input().split()
	print("\n\n")
	#Server Is Not Running Currently
	server.started = False
	th = Thread(target= server, daemon= True)
	th.start()#Running Server Function
	
	#To Wait Until Server Has Started
	while not server.started:
		pass
	host = server.host
	port = server.port	
	client(data,host,port) #Running Client Function
	print("*"*60)
	server.socket.close()
	print(R,"\u001b[47mServer Socket Closed",W)
	#Closing Server Socket

if __name__ == "__main__":
	main()