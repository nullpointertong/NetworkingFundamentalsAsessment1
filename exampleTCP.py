from socket import *
import socket as Socket

serverPort = 80
hostname = Socket.gethostname()    
adr = Socket.gethostbyname(hostname)
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((Socket.gethostbyname(hostname), serverPort))
print(adr)

serverSocket.listen(1)
print("The server is ready to receive")
while True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode()
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence.encode())
	connectionSocket.close()