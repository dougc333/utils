from __future__ import print_function
from pssh.clients import ParallelSSHClient
#from gevent import joinall

class ConfigCluster:
  def __init__(self):
    #test if file there
    self.filename='/Users/dougchang/Downloads/cuda-repo-ubuntu1804_10.1.105-1_amd64.deb'
    try:
      self.fh = open(self.filename)
      print("file found")
    except FileNotFoundError:
      print('file not found')
  def transfer(self):
    hosts = ['192.168.0.26','192.168.0.23']
    client = ParallelSSHClient(hosts)
    cmds = client.scp_send(self.filename,'/home/dc')
    joinall(cmds,raise_error=True)



c = ConfigCluster()
c.transfer()
