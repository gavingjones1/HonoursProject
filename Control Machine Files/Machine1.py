#Machine one

import paramiko
import sys
import threading
from time import sleep

def timer():
    for i in range(5):
        sleep(1)
    output = 1
    return output



def connect1(data, func):

    print(data)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(data[0]["IP"],data[0]["port"],data[0]['username'], data[0]['password'])

    ssh.connect(data[0]["IP"],data[0]["port"],data[0]['username'], data[0]['password'])

    if ssh.get_transport().is_active():
        print('Connection established')



    if func == 'website':

        stdin, stdout, stderr = ssh.exec_command('python C:/CHECKER/websites_better.py')
        output = stdout.readlines()
        return output

    if func == 'file':
        stdin, stdout, stderr = ssh.exec_command('python C:/CHECKER/FileChecker3.py')
        output = stdout.readlines()
        return output

    if func == 'replace':
        stdin, stdout, stderr = ssh.exec_command('python C:/CHECKER/replace.py')
        output = stdout.readlines()
        return output

    if func == 'email':
        stdin, stdout, stderr = ssh.exec_command('python C:/CHECKER/Emails.py')
        output = stdout.readlines()
        return output
