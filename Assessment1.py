
import http.server
from socket import *
import socket as Socket
import sys 

serverSocket = socket(AF_INET, SOCK_STREAM)
hostname = Socket.gethostname()
socketNum = 80 
serverSocket.bind((Socket.gethostbyname(hostname), socketNum))

serverSocket.listen(1)

while True:    
    
    print('Ready to serve... IP = http://'+Socket.gethostbyname(hostname))
    connectionSocket, addr = serverSocket.accept()      
    try:
        message = connectionSocket.recv(1024)         
            
        if not message:

            print('Client side attempting to Close Connection, continuing')
            connectionSocket.close()     

            continue   

        filename = message.split()[1]                 
        f = open(filename[1:])             
        outputdata = f.read() #Fill in start       #Fill in end                   

        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        #Fill in start
        #Fill in end                

    
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:

        print("ERROR 404 TRY AGAIN")
        connectionSocket.send('Error 404: File not found'.encode())
        #Fill in start        
        #Fill in end

        connectionSocket.close()
        #Fill in start
        #Fill in end            
serverSocket.close()
sys.exit()                                
