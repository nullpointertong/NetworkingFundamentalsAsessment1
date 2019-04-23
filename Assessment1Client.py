from socket import *
import socket as Socket


hostname = Socket.gethostname()
serverName = Socket.gethostbyname(hostname)
filename = "HelloWorld.html"
serverPort = 80

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

string = "HTTP/1.1/" + filename + " 200 OK\r\n\r\n"

clientSocket.send(string.encode())
httpV = clientSocket.recv(1024)


print ('From Server : ',httpV.decode())
clientSocket.close()
print ("complete")