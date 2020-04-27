#moving files 

import os
#os.system('pip install pexpect')
from pexpect import pxssh
import getpass

dest="192.168.0.26"
dest_path = ':/home/dc'
filename = 'testfile.txt'

print("current cwd:",os.getcwd())
hostname='nlpdl.ddns.net'
username='dc'
filename='testfile.txt'
try:
    s = pxssh.pxssh()
    hostname = input('hostname: ')
    username = input('username: ')
    password = getpass.getpass('password: ')
    s.login(hostname, username, password,sync_multiplier=5)
    s.sendline('uptime')   # run a command
    s.prompt()             # match the prompt
    print(s.before)        # print everything before the prompt.
    #s.sendline('scp testfile.txt dc@nlpdl.ddns.net:/home/dc')
    #s.prompt()
    #print(s.before)
    #s.sendline('ls -l')
    #s.prompt()
    #print(s.before)
    #s.sendline('df')
    #s.prompt()
    #print(s.before)
    s.logout()
except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)