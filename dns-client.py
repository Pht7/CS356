#Peter Tran Pht7 003

import sys
import socket
import struct
import random

host = sys.argv[1]
port = int(sys.argv[2])
hostname = sys.argv[3]
messageID = random.randint(1,100)
questionLength = len(hostname.encode("utf-8"))
answerLength = 0
returnCode = 0
messageType = 1
questionName = hostname +' ' + 'A'+' '+ 'IN'



print("Message ID: " + str(messageID))
print("Question Length: " + str(questionLength))
print("Answer Length: "+str(answerLength))
print("Question: " + hostname +' ' + 'A'+' '+ 'IN')
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1)

counter = 0

for x in range(3):
    try:
        clientSocket.sendto(struct.pack(f'!hhihh{questionLength}s',messageType,returnCode,messageID,questionLength,answerLength,questionName.encode()),(host,port))
        data, address = clientSocket.recvfrom(1024)
        print("Sending request to " + host + ' ' + str(port) + ' ' + hostname)
    except:
        if(counter < 3):
         print('Request timed out')
         counter = counter+1
        else:
         print('Request timed out...closing program')
    else:
        messageType, returnCode, messageID, questionLength, answerLength = struct.unpack('!hhihh', data[:12])
        answerName = struct.unpack_from(f'!{questionLength}s', data[12:])
        answerName = answerName[0].decode()


        if (returnCode == 0):
            print("Received Response from " + host + ", " + str(port) + hostname)
            print("Return Code: " + str(returnCode) + " No error")
            print("Message ID: " + str(messageID))
            print("Question Length: " + str(questionLength))
            print("Answer Length: " + str(answerLength))
            print("Questions: " + answerName)
            print("Answer: " + questionName)
            break
        else:
            print("Received Response from " + host + ", " + str(port) + hostname)
            print("Return Code: " + str(returnCode) + " (Name does not exist)")
            print("Message ID: " + str(messageID))
            print("Question Length: " + str(questionLength))
            print("Answer Length: " + str(answerLength))
            print("Questions: " + questionName)
            break







clientSocket.close()