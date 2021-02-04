#Peter Tran Pht7 003

import time
import sys
import random
import struct
import json
import socket
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
bulb = int(sys.argv[2])
getLightStatus = 0

newSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
newSocket.bind((serverIP,serverPort))
print("The server is ready to receive on port:  " + str(serverPort) + "\n")


while True:
    data, address = newSocket.recvfrom(1024)
    messageType,errorCode,status,color,receieveStat,messageID = struct.unpack('!hhhhhi',data[:14])
    print('Message ID: ' + str(messageID))
    if(status>2 or status < 0):
        errorCode = 1
    print('Light Status: ' + str(status))
    if(color>5 or color<0):
        errorCode = 2
    ##BAD COLOR
    print('Light Color: ' + str(color))
    print('Request Light Status/Color: ' + str(receieveStat))
    if(receieveStat>2):
        errorCode = 1
    print('Get Light Status: ' + str(getLightStatus))
    print('Error Code: ' + str(errorCode))
    if(receieveStat==0):
        print("Get Light Color: 5")
    else:
        print("Get Light Color: " + str(color))



