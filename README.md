# Exfiltrating_Windows_Files
In this repo you'll find python written tools to help you exfiltrate data after encrypting it, to avoid detection. Here we'll use the libraries PyWin32.

- key_gen.py

This script generates the public and private key pair. After generating the public and private keys you can use the next script 'encrypt_decrupt.py' to start encrypting and decrypting data.

- encrypt_decrypt.py

After generating the public and private key pair with 'key_gen.py' you can start using this script to encrypt and decreypt data. 

- email_exfil.py

This script exfiltres information you have encrypted with the scripts above. After you use email_exfil.py to send an encrypted file back to your Kali machine, you'll open the email client, select the message, and copy and paste it into a new file. You can then read from that file in order to decrypt it using the previous decrypt script.

- transmit_exfil.py

You can use this script to send your encrpypted data via file transfer. The script provides a function for windows as well with the 'win32file' library.

- paste_exfil.py

We can send our encrypted information by posting it on a web server. We will automate the process of posting the encrypted document to an account on https://pastebin.com. This will enables us to dead-drop the document and retrieve it when we want to without anyone else being able to decrypt it.

- exfil.py

Finally we tie everyting together. You can call to exfiltrate files by using any of the methods we have written. 
