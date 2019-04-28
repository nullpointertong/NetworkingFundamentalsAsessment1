from socket import *
import socket as Socket


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
print (http_header)

http =  http_header + "\r\n\r\n"

l_bytes = clientSocket.send(http.encode())
print(l_bytes)

r_bytes = 0
chunks = []
while r_bytes < 400:
	httpV = clientSocket.recv(l_bytes)
	chunks += httpV.decode(),
	r_bytes = r_bytes + len(httpV)
	#print(r_bytes)
	r_bytes+=1

print ('From Server : ', ''.join(chunks))
clientSocket.close()
print ("complete")



#  while bytes_recd < MSGLEN:
#             chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
#             if chunk == b'':
#                 raise RuntimeError("socket connection broken")
#             chunks.append(chunk)
#             bytes_recd = bytes_recd + len(chunk)
#         return b''.join(chunks)