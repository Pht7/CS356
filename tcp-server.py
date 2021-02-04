#! /usr/bin/env python3
# TCP Echo Server

import sys
import socket
import os
import time
#PETER TRAN PHT7 CS 356
# Read server IP address and port from command-line arguments
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])
dataLen = 1000000
# Create a TCP "welcoming" socket. Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Assign IP address and port number to socket
serverSocket.bind((serverIP, serverPort))
# Listen for incoming connection requests
serverSocket.listen(1)




t = time.gmtime()
currTime = time.strftime("%a, %d %b %Y %H:%M:%S GMT", t)
print("Current Time:",currTime)


conttype = str("Content-Type: text/html; charset=UTF-8\r\n\r\n")

print('The server is ready to receive on port:  ' + str(serverPort) + '\n')

# loop forever listening for incoming connection requests on "welcoming" socket
while True:
    # Accept incoming connection requests; allocate a new socket for data communication
    connectionSocket, address = serverSocket.accept()
    print("Socket created for client " + address[0] + ", " + str(address[1]))

    # Receive and print the client data in bytes from "data" socket
    data = connectionSocket.recv(dataLen).decode()
    print("Data from client: " + data)

    f = open("cache.txt", "r")

    if(data=="1"):
        print("BROKEN")
        NM = ("HTTP/1.1 404 NOT FOUND\r\nDate: " + str(currTime) + "\r\n" + "Content-Length:" + "0\r\n" + "\n" + "\r\n")
        connectionSocket.send(NM.encode())
        sys.exit()
    else:
        if ("If-Modified-Since: " not in data):
            print("GET REQUEST")
            temp = data.split("/")
            fileName = temp[1].split(" ")
            fileName = fileName[0]
            print(fileName)
            modified = time.gmtime(os.path.getmtime(fileName))
            modStr = time.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n", modified)
            print(f"Last modified: ", modStr)
            getRequest = ("HTTP/1.1 200 OK\r\nDate: " + str(currTime) + "\r\n" + "Last modified: " + str(
                modStr) + "\n" + "Content-Length:" + str(
                (len(fileName.encode("utf-8")))) + "\n" + conttype + "\r\n" + "\r\n")

            connectionSocket.send(getRequest.encode())


        else:
            print("CONDITIONAL REQUEST")
            temp = data.split("/")
            print(temp[1])
            fileName = temp[1].split(" ")
            fileName = fileName[0]

            # MODIFY TIME CHECK
            modified = time.gmtime(os.path.getmtime(fileName))
            modStr = time.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n", modified)
            print(f"Last modified: ", modStr)

            f = open("cache.txt", "r")
            timeCheck = f.read()
            tempArray2 = timeCheck.split("#")
            # timeCheck = (tempArray2) ## time check

            t2 = time.strptime(modStr, "%a, %d %b %Y %H:%M:%S %Z\r\n")
            timeCheck = (tempArray2[1])
            t = time.strptime(timeCheck, "%a, %d %b %Y %H:%M:%S %Z\r\n")
            secs = time.mktime(t)
            secs2 = time.mktime(t2)

            print(secs)

            if (secs < secs2):
                print("NOT MODIFIED")
                conditionalRequest = ("HTTP/1.1 304 Not Modified \r\nDate: " + str(currTime) + "\r\n")
                connectionSocket.send(conditionalRequest.encode())

            else:
                print("MODIFIED")
                conditionalRequest = ("HTTP/1.1 Modified \r\nDate: " + str(currTime) + "\r\n")
                connectionSocket.send(conditionalRequest.encode())





        
