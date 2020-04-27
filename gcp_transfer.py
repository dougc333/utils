import os
import sys


class Transfer:
    def __init__(self,fqdn_addr, user_name):
        print('current working dir:',os.getcwd())
        self.addr=fqdn_addr
        self.user = user_name
        self.os = self.darwin_linux()
        self.ssh = None #determines if .ssh exists 
        self.root = None #path of ssh
        self.ssh_key()
        self.ssh_path = None

    def darwin_linux(self):
        import platform
        sys = platform.system()
        if sys=='Darwin':
            print("mac")
        elif sys=='Linux':
            print('linux')
        else:
            print('not linux or mac not supported')
        return sys
        
    def ssh_key(self):
        '''
        make ssh key and copy to remote
        '''
        if self.os=='Darwin':
            if os.path.exists('/Users'+os.getlogin()+'.ssh'):
                print('mac .ssh exists')
                self.ssh=True
                self.ssh_path = '/Users'+os.getlogin()+'.ssh'
            else:
                print('mac .ssh not exist')
                self.ssh=False
        elif self.os=='Linux':
            if os.path.exists('/home/'+os.getlogin()+'.ssh'):
                print('linux .ssh exists')
                self.ssh=True
                self.ssh_path = '/home/'+os.getlogin()+'.ssh'
            else:
                print('linux .ssh no exist')
                self.ssh=False
        if os.path.exists('/root/.ssh'):
            print('ssh dir under root')
            self.root = True
            self.ssh_path = '/root/.ssh'

    def copy_remote(self):
        '''
        copy .pub to remote .ssh/authorized_keys
        assume remote is linux server only. 
        '''
        if self.ssh==False:
            os.system('cat /dev/zero | ssh-keygen -q -N ""')
            


