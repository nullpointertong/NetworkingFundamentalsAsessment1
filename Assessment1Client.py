from socket import *
import socket as Socket


hostname = Socket.gethostname()
serverName = Socket.gethostbyname(hostname)  
filename = "HelloWorl.html"
serverPort = 80

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

serverPort = "80"



header = {
	"first_header" : "GET /%s HTTP/1.1" %(filename),
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	"Accept-Language": "en-us",
	"Host": serverName+ ":" + serverPort,
	}

serverPort = 80   

http_header = "\r\n".join("%s:%s" %(item,header[item]) for item in header)
print (http_header)

http =  http_header + "\r\n\r\n"

clientSocket.send(http.encode())


httpV = clientSocket.recv(1024)

print ('From Server : ',httpV.decode())
clientSocket.close()
print ("complete")