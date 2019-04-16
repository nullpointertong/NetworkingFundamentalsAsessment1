#import socket module
import http.server
from socket import *
import socket as Socket
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
hostname = Socket.gethostname()
socketNum = 80 
serverSocket.bind((Socket.gethostbyname(hostname), socketNum))

serverSocket.listen(1)
#Prepare a sever socket
#Fill in start
#Fill in end

while True:    
    #Establish the connection
    print('Ready to serve... IP = ' + Socket.gethostbyname(hostname))
    connectionSocket, addr = serverSocket.accept()      
    try:
        message = connectionSocket.recv(1024)  #Fill in start          #Fill in end        
            
        if not message:
            print('Client side attempting to Close Connection, continuing')
            connectionSocket.close()            
            continue   

        filename = message.split()[1]                 
        f = open(filename[1:])                        
        outputdata = f.read() #Fill in start       #Fill in end                   
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        #Fill in start
        #Fill in end                
        #Send the content of the requested file to the client
    
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        print("ERROR 404 TRY AGAIN")
        connectionSocket.send('Error 404: File not found'.encode())
        #Fill in start        
        #Fill in end
        #Close client socket
        connectionSocket.close()
        #Fill in start
        #Fill in end            
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data                                    