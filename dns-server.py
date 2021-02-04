import socket
#Peter Tran Pht7 003

import time
import sys
import random
import struct
import json
serverIP = sys.argv[1]
serverPort = int(sys.argv[2])

newSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
newSocket.bind((serverIP,serverPort))
print("The server is ready to receive on port:  " + str(serverPort) + "\n")
DNSList = []
fileOpen = open('dns-master.txt')


while True:
    sepLine = fileOpen.readline()
    if not sepLine:
        break
    DNSList.append(sepLine.strip())


print(DNSList)



while True:
    data, address = newSocket.recvfrom(1024)
    print("Ping")
    messageType,returnCode,messageID,questionLength,answerLength = struct.unpack('!hhihh',data[:14])
    questionName = struct.unpack(f'!{questionLength}s',data[12:])
    questionName = questionName[0].decode()
    print("Question name " + questionName)
    for dnsTYPE in DNSList:
        # Test if in the array
        if questionName not in dnsTYPE:
        #If not return 1, aka not good
            returnCode = 1
            newSocket.sendto(struct.pack(f'!hhihh{questionLength}s', messageType, returnCode, messageID, questionLength,answerLength, questionName.encode()), address)
            print("Not in")
        else:
        #else assume good
            print("In")
            answerLength = len(questionName.encode("utf-8"))
            answerName = questionName
            returnCode = 0
            newSocket.sendto(struct.pack(f'!hhihh{questionLength}s{answerLength}s', messageType, returnCode, messageID,questionLength, answerLength, questionName.encode(), answerName.encode()),address)











