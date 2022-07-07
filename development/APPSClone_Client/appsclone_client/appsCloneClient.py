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
  def __init__(self,ip,port,username,password,toUploadDir,rinexDir,idQueue):
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
    idQueue     : str
      The queue of the uploaded ids.
    """
    self.ip          = ip
    self.port        = int(port)
    self.username    = username
    self.password    = password
    self.toUploadDir = toUploadDir
    self.rinexDir    = rinexDir
    self.idQueue     = idQueue

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
      respondeCode,respondeArgs = response["code"],response["args"]
      if respondeCode == -1:
        print(respondeArgs[0])
      else:
        self.__addIdToQueue(respondeCode)
    elif option == "d":
      self.socket.send(pickle.dumps(OptionArgs(2,(args[0],))))
      response = pickle.loads(self.socket.recv(APPSCloneClient.NUMBER_BYTES_TO_RECEIVE))
      respondeCode,respondeArgs = response["code"],response["args"]
      if respondeCode == -1:
        print(respondeArgs[0])
      else:
        pass
        # sshClient = SSHConnection(self.ip,self.port,self.username,self.password)
        # sshClient.putFile(Helper.joinPathFile(self.rinexDir,self.rinexFile),self.toUploadDir)

  def __addIdToQueue(self,rinexId):
    """Add the id of the upload to the queue of uploaded ids.

    Parameters
    ----------
    rinexId : int
      The id to add to the queue
    """
    with open(self.idQueue,"a") as f:
      f.write(f"{rinexId}\n")

  def __removeIdFromQueue(self,rinexId):
    """Remove the id from the queue of uploaded ids.

    Parameters
    ----------
    rinexId : int
      The id to remove from the queue
    """
    newQueue = ""
    with open(self.idQueue,"r") as f:
      lines = f.readlines()
      for line in lines:
        if line.split("\n")[0] != str(rinexId):
          newQueue += line

    with open(self.idQueue,"w") as f:
      f.write(newQueue)