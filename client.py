#!/bin/usr/python3
from pyDes import *
import socket
from datetime import datetime

s = socket.socket()
host = socket.gethostname()
key = "secret_k"
d = des(key)
port = 60000

s.connect((host, port))
s.send(b"Hello server!")


with open ('received_file.txt', 'wb') as f:
    print ('file opened')
    while True:
        print('receiving data')
        data = s.recv(1024)
        print(data) 
        ls = data[26:]
        #print(ls)
        print(d.decrypt(ls, pad=None, padmode=PAD_PKCS5))
        print(datetime.now())
        #print('data=%s', (data))
        if not data:
            break
        f.write(data)
        #break
        
    
f.close()

'''filename = 'received_file.txt'
fi = open(filename, 'rb')
li = fi.read(2048)
#ls = li[26:]

print(d.decrypt(ls, pad=None, padmode=PAD_PKCS5))
print(datetime.now())
fi.close()
'''
print('Successfully got the file')
s.close()
print('connectionclosed')