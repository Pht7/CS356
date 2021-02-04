#! /usr/bin/env python3
# TCP Echo Client

import sys
import socket
import datetime
import time
import os

#PETER TRAN PHT7 CS 356
# Get the server hostname, port and data length as command line argumentshost = sys.argv[1]
##MAKES TIME PROGRESS HERE
t = time.gmtime()
currTime = time.strftime("%a, %d %b %Y %H:%M:%S GMT\r\n", t)
print("Current Time:",currTime)




url = (sys.argv[1])

splitMsg = url.split("/")



hostNameINC = splitMsg[0]
fileName = splitMsg[1]

splitSecond = hostNameINC.split(":")
#print(splitSecond) print out testing stguff lol
host = splitSecond[0]
port = (splitSecond[1])
#print(fileName,host,port) more ugly testing
# Create TCP client socket. Note the use of SOCK_STREAM for TCP packet
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




 #Create TCP connection to server

print("Connecting to " + host + ", " + str(port))
clientSocket.connect((host, int(port)))
print("FILENAME IS HERE: ")
print(fileName)

f = open("cache.txt","w")
f.write("filename.html")
f.close()
temp=[]
temp = "filename.html"
print(str(temp) + "toe")
conttype = str("Content-Type: text/html; charset=UTF-8\r\n\r\n")
getRequest = str("GET /" + fileName + " HTTP /1.1\r\n" + " Host: " + hostNameINC + "\r\n" + "\r\n")
if fileName not in temp:
    #IN FILE IDK WHY SO BROKEN :(
    #GET REQUEST HERE
    print("Sending data to server: " + getRequest)
    try:
        print("TRY ATTEMPT")
        h = open(fileName, "r")
        f = open("cache.txt", "w")
        f.write(fileName)
        f.write(getRequest)
        f.write("#")
        f.write(currTime)  ## Set date added
        f.write("#")
        f.write("\n")
        f.write(h.read())
        h.close()
        f.close()
        f = open("cache.txt", "r")
        print(f.read())
        clientSocket.send(getRequest.encode())
        temp.append(fileName)
    except:
        print("BROKEN BOY")
        brokenBoy = "1"
        clientSocket.send(brokenBoy.encode())

else:
    #conditionalRequest = ("HTTP/1.1 200 OK\r\n Date: " + str(currTime) + "\r\n" + str(modStr) + "Content-Length:" + str((len(fileName.encode("utf-8"))) + conttype))

    #ONLY CHECK IF CACHED!
    f = open("cache.txt", "r")
    timeCheck = f.read()
    tempArray2 = timeCheck.split("#")
    timeCheck = (tempArray2[1]) ## time check


    conditionalRequest = str("GET /" + fileName + " HTTP /1.1\r\n" + " Host: " + hostNameINC + "\r\n" + "If-Modified-Since: " + timeCheck)
    print("Sending CONDITIONAL REQUEST: " +conditionalRequest)

    h = open(fileName, "r")
    f = open("cache.txt", "w")
    f.write(fileName)
    f.write(conditionalRequest)
    f.write("#")
    f.write(currTime) ## Set date added
    f.write("#")
    f.write("\n")
    f.write(h.read())
    h.close()
    f.close()


    clientSocket.send(conditionalRequest.encode())


    h = open(fileName, "r")
    print(h.read())
    h.close()


    #conditionalRequest = ("HTTP/1.1 200 OK\r\nDate: " + str(currTime) + "\r\n" + "Last modified: "+ str(modStr) + "\n" +  "Content-Length:" + str((len(fileName.encode("utf-8")))) + "\n" + conttype +"\r\n" + "\r\n")
    #print(conditionalRequest + "Test MESSAGE REMOVE AFTER FOR CONDITIONAL REQUEST")

#return conditonla get

print(str(temp))

dataEcho = clientSocket.recv(8192)

# Display the decoded server response as an output
print("Receive data from server: " + dataEcho.decode())
print(dataEcho)



# Send encoded data through TCP connection
#print("Sending data to server:   " + data)
#clientSocket.send(data.encode())

#Receive the server response


# Close the client socket
clientSocket.close()
 




