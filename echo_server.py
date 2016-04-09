from socket import *
import sys
myHost = ''
myPort = sys.argv[1]

com ='''
if myPort == len(sys.argv[1]):
	myPort = 2009
else: 
	myPort = int(sys.argv[1])
'''
sockobj = socket(AF_INET,SOCK_STREAM)
sockobj.bind((myHost,int(myPort)))
sockobj.listen(5)

while True:
		connection, address = sockobj.accept()
		print('Server connect by',address)
		while True:
			data = connection.recv(1024)
			if not data: break
			connection.send(b'Echo=>' + data)
		connection.close()