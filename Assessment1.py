#import socket module
import http.server
from socket import *
import socket as Socket
import sys # In order to terminate the program
from _thread import *



serverSocket = socket(AF_INET, SOCK_STREAM)
#Intilaizing The socket
hostname = Socket.gethostname()
#Calling the .gethostname() function to use the .gethostbyname function
socketNum = 80 
#Default socket
serverSocket.bind((Socket.gethostbyname(hostname), socketNum))
#Socket.gethostbyname(hostname) grabs the ip using the hostname grabed from previous function
serverSocket.listen(1)
#Enable a server to accept connections. it specifies the number of unaccepted connections that the system will allow before 
#refusing new connections. If not specified, a default reasonable value is chosen.


#Prepare a sever socket 
#Fill in start
#Fill in end
def client_thread():
    while True:    
        #Establish the connection
        print('Ready to serve... IP = ' + Socket.gethostbyname(hostname))
        #Prints debug message + Ip address 
        connectionSocket, addr = serverSocket.accept()      
        #Accepts the connection
        try:
            message = connectionSocket.recv(1024)  #Fill in start          #Fill in end        
            #Recieves data from server with the max size of 1024 bytes
            
            if not message:
                print('Client side attempting to Close Connection, continuing')
                connectionSocket.close()            
                continue   
            #This runs to prevent an error when the Client is closing the connection sending a '' and there by breaking 
            #the code 

            filename = message.split()[1]                 
            f = open(filename[1:])                        
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

        except IOError:
            #Send response message for file not found
            print("ERROR 404 TRY AGAIN")
            connectionSocket.send('Error 404: File not found'.encode())
            #Display it in a browser page
            #Fill in start        
            #Fill in end
            #Close client socket
            connectionSocket.close()
            #Fill in start
            #Fill in end            

    serverSocket.close()
    sys.exit()#Terminate the program after sending the corresponding data                                    

while True:
    start_new_thread(client_thread())
    #client_thread()