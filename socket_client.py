import sys
from socket import *
serverHost = 'localhost'
serverPort = 2009
msg  = [b'Hello network world']

if len(sys.argv) > 1:
	serverHost = sys.argv[1]
	if len(sys.argv) > 2:
		msg = (x.encode() for x in sys.argv[2:])

sokobj = socket(AF_INET,SOCK_STREAM)
sokobj.connect((serverHost,serverPort))

for line in msg:
	sokobj.send(line)
	data = sokobj.recv(1024)
	print('Client recvied: ', data)
sokobj.close()