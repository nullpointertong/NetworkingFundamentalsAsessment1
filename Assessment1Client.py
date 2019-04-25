from socket import *
import socket as Socket


hostname = Socket.gethostname()
serverName = Socket.gethostbyname(hostname)  
filename = "HelloWorl.html"
serverPort = 80

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

serverPort = "80"


try:
	clientSocket = socket(AF_INET, SOCK_STREAM)
	clientSocket.connect((hostname,int(serverName)))
	header = {
		"first_header" : "GET /%s HTTP/1.1" %(filename),
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Accept-Language": "en-us",
		"Host": serverName+ ":" + serverPort,
	}
	http_header = "\r\n".join("%s:%s" %(item,header[item]) for item in header)
	print (http_header)
	clientSocket.send("%s\r\n\r\n" %(http_header))

except IOError:
	sys.exit()

httpV = clientSocket.recv(1024)

print ('From Server : ',httpV.decode())
clientSocket.close()
print ("complete")