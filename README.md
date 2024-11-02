# Exfiltrating_Windows_Files
In this repo you'll find python written tools to help you exfiltrate data after encrypting it, to avoid detection. Here we'll use the libraries PyWin32.

- key_gen.py

This script generates the public and private key pair. After generating the public and private keys you can use the next script 'encrypt_decrupt.py' to start encrypting and decrypting data.

- encrypt_decrypt.py

After generating the public and private key pair with 'key_gen.py' you can start using this script to encrypt and decreypt data. 
