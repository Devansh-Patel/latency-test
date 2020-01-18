#!/bin/usr/python3

from pyDes import *
import socket
from datetime import datetime

port = 60000

key = "secret_k"
d = des(key)



s = socket.socket()
host = socket.gethostname()
s.bind((host, port))
s.listen(5)

print('Server listening...')

while True:
    conn, addr = s.accept()
    print ('Got connection from', addr)
    data = conn.recv(2048)
    print('Server received', repr(data))

    filename = 'mytext.txt'
    f = open(filename, 'rb')
    l = f.read(2048)

    
    while (l):
        cip = d.encrypt(l, pad=None, padmode=PAD_PKCS5)
        str11 = str(datetime.now())
        bb = bytes(str11, 'utf-8') 
        conn.send(bb)
        conn.send(cip)
        print('Sent', repr(l))
        l = f.read(2048)
    f.close()

    print('Done sending')
    #conn.send(b'Thank you for connecting')
    conn.close()
    