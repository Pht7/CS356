import socket
import time
import sys
import random
import struct
seq = 0
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

newSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dsfxcxdszzdswexzczsaxzxzawzxwqsdaxc cvfdrefdcv cxdsaxzd nbvc

newSocket.bind((serverIP,serverPort))

print("The server is ready to receive on port:  " + str(serverPort) + "\n")

while True:
    randomNumber = random.randint(0,10)
    # Receive and print the client data from "data" socket
    data, address = newSocket.recvfrom(1024)
    one, seq = struct.unpack("!ii", data)
    print("Responding to ping request with sequence number " + str(seq+1))

    if randomNumber < 4:
        print('Message with sequence number ' + str(seq+1) + ' dropped')
        continue

    # Echo back to client
    # Echo back to client
    newSocket.sendto(data,address)
