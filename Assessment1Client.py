from socket import *
import socket as Socket
import sys


hostname = Socket.gethostname()
serverName = Socket.gethostbyname(hostname)  
filename = "HelloWorld.html"
serverPort = 80

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

header = {
	"first_header" : "GET /%s HTTP/1.1" %(filename),
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language": "en-us",
	"Host": "{0}:{1}".format(serverName, serverPort)
	}
serverPort = 80   

http_header = "\r\n".join("%s:%s" %(item,header[item]) for item in header)


http =  http_header + "\r\n\r\n"

l_bytes = clientSocket.send(http.encode())


r_bytes = 0	
chunks = []
while r_bytes < 1024:
	httpV = clientSocket.recv(l_bytes)
	chunks += httpV.decode(),
	r_bytes = r_bytes + sys.getsizeof(l_bytes)


print ('From Server : ', ''.join(chunks))
clientSocket.close()
print ("complete")
