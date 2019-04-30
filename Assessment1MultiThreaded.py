
import http.server
from socket import *
import socket as Socket
import sys 
from threading import Thread
import os

CUR_DIR = os.path.dirname(os.path.realpath(__file__))

serverSocket = socket(AF_INET, SOCK_STREAM)

hostname = Socket.gethostname()

socketNum = 80 

serverSocket.bind((Socket.gethostbyname(hostname), socketNum))

serverSocket.listen(10)


#Fill in start
#Fill in end
def client_thread(connectionSocket, addr):
    connectionSocket = connectionSocket
    while True:    
        
        print('Ready to serve... IP = ' + Socket.gethostbyname(hostname))
        
        try:
            
            message = connectionSocket.recv(1024)  #Fill in start          #Fill in end        
            
            
            if not message:
                print('Client side attempting to Close Connection, continuing')
                connectionSocket.close()            
                continue   
            

            filename = message.split()[1]
            f = open(os.path.join(CUR_DIR, filename[1:].decode('unicode_escape')))                    
            outputdata = f.read() #Reads file                  
            
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            #Fill in start
            #Fill in end                
            
    
            for i in range(0, len(outputdata)):           
                connectionSocket.send(outputdata[i].encode())
                
            connectionSocket.send("\r\n".encode())
            #Send encoded data to socket.
            connectionSocket.close()

        except IOError as e:
            
            print("ERROR 404 TRY AGAIN")
    
            #Fill in start        
            #Fill in end
        
            connectionSocket.close()
            sys.exit(0)
            #Fill in start
            #Fill in end            
                                      
while True:
    connectionSocket, addr = serverSocket.accept()
    
    t = Thread(target=client_thread, args=(connectionSocket, addr))
    t.daemon = True
    t.start()
serverSocket.close()
sys.exit()

