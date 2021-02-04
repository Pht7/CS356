#Peter Tran Pht7 003

#Peter Tran Pht7 003

import sys
import socket
import struct
import random

host = sys.argv[1]
port = int(sys.argv[2])
status = int(sys.argv[3])
color = int(sys.argv[4])
receieveStat = int(sys.argv[5])
messageID = random.randint(1,100)
messageType = 1
errorCode = 0
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1)
counter = 0
for x in range(3):
    try:
        clientSocket.sendto(struct.pack(f'!hhhhhi',messageType,errorCode,status,color,receieveStat, messageID),(host,port))
        print("Sending request to " + host + ' ' + str(port))
        print('Message ID: ' + str(messageID))
        print('Light Status: ' + str(status))
        print('Light Color: ' + str(color))
        print('Request Light Status/Color: ' + str(receieveStat))
        print('Error Code: ' + str(errorCode))
        break
    except:
        if (counter < 3):
            print('Request time out' + str(counter))
            counter = counter + 1
        else:
            print("Request timeout too many times exiting the program.")






clientSocket.close()