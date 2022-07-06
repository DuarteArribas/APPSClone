import socket
import pickle
from appsclone_client.utils.sshConnection import *
from appsclone_client.utils.optionArgs    import *

class APPSCloneClient:
  """The APPSClone client for regular users, who wish to manually upload and retrieve to and from APPS.
  
  Attributes
  ----------
  MAX_TRIES               : int
    The maximum tries a client can fail to connect
  NUMBER_BYTES_TO_RECEIVE : int
    The max number of bytes to receive
  """
  # == Attributes ==
  NUMBER_BYTES_TO_RECEIVE = 16384
  def __init__(self,ip,port,username,password,toUploadDir,rinexDir,rinexFile):
    """The ip and port that the client will connect to."""
    self.ip                = ip
    self.port              = port
    self.username          = username
    self.password          = password
    self.toUploadDir       = toUploadDir
    self.rinexDir          = rinexDir
    self.rinexFile         = rinexFile

  def runClient(self,option,args):
    """Run the client."""
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
      self.socket = s
      s.connect((self.ip,self.port))
      self.__handleClientActions(option,args)

  def __handleClientActions(self,option,args):
    """Handle client actions."""
    if option == 1:
      # sshClient = SSHConnection(self.ip,self.port,self.username,self.password)
      # sshClient.putFile(Helper.joinPathFile(self.rinexDir,self.rinexFile),self.toUploadDir)
      self.socket.send(pickle.dumps(OptionArgs(option,(self.rinexFile,))))
      response = pickle.loads(self.socket.recv(APPSCloneClient.NUMBER_BYTES_TO_RECEIVE))
      response_code,response_args = response["code"],response["args"]
      print(response_code)
      print(response_args)
    elif option == 2:
      pass
    