#!/bin/bash/env python

import smtplib
import time
import win32com.client

smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_acct = 'user@example.com'
smtp_password = 'Password12345!'
tgt_acct = ['user@elsewhere.com']

# Function to fromat a message
def plain_email(subject, contents):
    message = f'Subject: {subject}\nFrom {smtp_acct}\n'
    message += f'To: {tgt_acct}\n\n{contents.decode()}'
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_acct, smtp_password)

    #server.set_debuglevel(1)    # Turn this line on to see the connection in your console
    server.sendemail(smtp_acct, tgt_acct, message)
    time.sleep(1)
    server.quit(1)

# Windows specifi function
# It performs the same technique
def outlook(subject, contents):
    outlook = win32com.client.Dispatch("Outlook.Application")
    message = outlook.CreateItem(0)
    message.DeleteAfterSubmit = True
    message.Subject = subject
    message.Body = contents.decode()
    message.To = tgt_acct[0]
    message.Send()

# Here you can call either fuction
if __name__ == '__main__':
    plain_email('test mesage 1', 'test message 2')