#! /usr/bin/env python3
# Echo Client
import sys
import socket
import time
import struct
#UCID - Pht7 Name: Peter Tran Section:003
# Get the server hostname, port and data length as command line arguments
host = sys.argv[1]
port = int(sys.argv[2])
countSeq = 1


print("Pinging " + host + ", " + str(port))

rttLength = []

# Create UDP client socket. Note the use of SOCK_DGRAM
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1)
# Send data to server

#print("Sending data to   " + host + ", " + str(port) + ": " + str(countSeq))
#clientsocket.sendto(countList.encode(),(host, port))

# Receive the server response
for x in range(10):
    timer = time.time()
    countSeq = countSeq + 1

    data = struct.pack('!ii', 1, countSeq)
    clientSocket.sendto(data, (host, port))
    try:
        data, _ = clientSocket.recvfrom(1024)
        timeChange = (time.time() - timer)
        rttLength.append(timeChange)
        print("Ping message number " + str(countSeq)+ ' RTT:' + str(timeChange) + 'secs')
    except socket.timeout:
        print("Ping message number " + str(countSeq) + " timed out")

mean = sum(rttLength,0.0) / len(rttLength)
print("10 packets transmitted, " + str(len(rttLength)) + "received, " + str((10-len(rttLength))*10) + "% packet loss")
print ('\n')
print ("Statistics:")
print ('Min/Max/Av RTT = '  + str(min(rttLength)) + '/' + str(max(rttLength)) + str(mean) + ' / '
 + 'secs')



#Close the client socket
clientSocket.close()
