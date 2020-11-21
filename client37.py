import socket               # Import socket module
import threading
import os
from tqdm import tqdm

def see():   #Deamon Thread to Keep listening
   while True:
    ro1=(s.recv(5000).decode())
    print(ro1)
    if ro1=="stop":
     s.close

    
    


     
def encrypt(a): #A function to encode the data using custom made encrytion
   a1=a.encode('unicode_escape')
   a2=len(a1)
    
  
        
   
s = socket.socket(socket.AF_INET)         # Create a socket object
host = '80.78.219.189'  # Get local machine name
port = 12345               # Reserve a port for your recieving.

buff=4096
kk=0

s.connect((host, port))
print(s.recv(5000))
print(host)
print("Enter what you want the other person want to know bakayaro!, \nType stop to stop. Enjoy\n")
see1=threading.Thread(target=see)
see1.daemon=True
see1.start()
while True:
     in1=input()
     if in1=="stop":
         s.close
         break

            

     in1=bytes(in1,'UTF-8')
     s.send(in1)




     
s.close()

                    # Close the socket when done
