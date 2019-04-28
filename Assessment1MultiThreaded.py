#import socket module
import http.server
from socket import *
import socket as Socket
import sys # In order to terminate the program
from threading import Thread
import os

CUR_DIR = os.path.dirname(os.path.realpath(__file__))

serverSocket = socket(AF_INET, SOCK_STREAM)
#Intilaizing The socket
hostname = Socket.gethostname()
#Calling the .gethostname() function to use the .gethostbyname function
socketNum = 80 
#Default socket
serverSocket.bind((Socket.gethostbyname(hostname), socketNum))
#Socket.gethostbyname(hostname) grabs the ip using the hostname grabed from previous function
serverSocket.listen(10)
#Enable a server to accept connections. it specifies the number of unaccepted connections that the system will allow before 
#refusing new connections. If not specified, a default reasonable value is chosen.


#Prepare a sever socket 
#Fill in start
#Fill in end
def client_thread(connectionSocket, addr):
    connectionSocket = connectionSocket
    while True:    
        #Establish the connection
        print('Ready to serve... IP = ' + Socket.gethostbyname(hostname))
        #Prints debug message + Ip address 
        # connectionSocket, addr = serverSocket.accept()      
        #Accepts the connection
        try:
            # print(connectionSocket.__dir__())
            message = connectionSocket.recv(1024)  #Fill in start          #Fill in end        
            #Recieves data from server with the max size of 1024 bytes
            
            if not message:
                print('Client side attempting to Close Connection, continuing')
                connectionSocket.close()            
                continue   
            #This runs to prevent an error when the Client is closing the connection sending a '' and there by breaking 
            #the code 

            filename = message.split()[1]
            f = open(os.path.join(CUR_DIR, filename[1:].decode('unicode_escape')))                    
            outputdata = f.read() #Reads file                  
            #Send one HTTP header line into socket
            connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
            #Fill in start
            #Fill in end                
            #Send the content of the requested file to the client
    
            for i in range(0, len(outputdata)):           
                connectionSocket.send(outputdata[i].encode())
                
            connectionSocket.send("\r\n".encode())
            #Send encoded data to socket.
            connectionSocket.close()

        except IOError as e:
            #Send response message for file not found
            print("ERROR 404 TRY AGAIN")
            #print(">>>>" +str(e) + "<<<")
            #connectionSocket.send('Error 404: File not found'.encode())
            #connectionSocket.send(str(e).encode())
            #Display it in a browser page
            #Fill in start        
            #Fill in end
            #Close client socket
            connectionSocket.close()
            sys.exit(0)
            #Fill in start
            #Fill in end            
                                      
while True:
    connectionSocket, addr = serverSocket.accept()
    # connectionSocket.recv(1024)
    t = Thread(target=client_thread, args=(connectionSocket, addr))
    t.daemon = True
    t.start()
serverSocket.close()
sys.exit()
    #Terminate the program after sending the corresponding data  
