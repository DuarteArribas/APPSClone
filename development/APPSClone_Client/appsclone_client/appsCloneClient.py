import socket
import pickle
from appsclone_client.utils.sshConnection import *
from appsclone_client.utils.optionArgs    import *

class APPSCloneClient:
  """The APPSClone client for regular users, who wish to manually upload and retrieve to and from APPS.
  
  Attributes
  ----------
  NUMBER_BYTES_TO_RECEIVE : int
    The max number of bytes to receive
  """
  # == Attributes ==
  NUMBER_BYTES_TO_RECEIVE = 16384
  # == Methods ==
  def __init__(self,ip,port,username,password,toUploadDir,rinexDir):
    """Initialize a socket connection with the APPSClone server.

    Parameters
    ----------
    ip          : str
      The ip of the server
    port        : int
      The port of the server
    username    : str
      The username to connect to the server with
    password    : str
      The password of the user
    toUploadDir : str
      The directory of the server to upload with
    rinexDir    : str
      The directory where the rinex files must be put to be uploaded
    """
    self.ip          = ip
    self.port        = int(port)
    self.username    = username
    self.password    = password
    self.toUploadDir = toUploadDir
    self.rinexDir    = rinexDir

  def runClient(self,arguments):
    """Run the client.
    
    Parameters
    ----------
    arguments : list
      The list of command-line arguments. arguments[0] is the option
    """
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
      self.socket = s
      s.connect((self.ip,self.port))
      self.__handleClientActions(arguments[0],arguments[1:])

  def __handleClientActions(self,option,args):
    """Handle client actions.

    Parameters
    ----------
    option : str
      Upload | Download
    args   : list
      The upload arguments
    """
    if option == "u":
      # sshClient = SSHConnection(self.ip,self.port,self.username,self.password)
      # sshClient.putFile(Helper.joinPathFile(self.rinexDir,self.rinexFile),self.toUploadDir)
      self.socket.send(pickle.dumps(OptionArgs(1,(args))))
      response = pickle.loads(self.socket.recv(APPSCloneClient.NUMBER_BYTES_TO_RECEIVE))
      response_code,response_args = response["code"],response["args"]
      if response_code == -1:
        print(response_args[0])
    elif option == "d":
      self.socket.send(pickle.dumps(OptionArgs(2,(args[0],))))
      response = pickle.loads(self.socket.recv(APPSCloneClient.NUMBER_BYTES_TO_RECEIVE))
      response_code,response_args = response["code"],response["args"]
      if response_code == -1:
        print(response_args[0])
      else:
        # sshClient = SSHConnection(self.ip,self.port,self.username,self.password)
        # sshClient.putFile(Helper.joinPathFile(self.rinexDir,self.rinexFile),self.toUploadDir)