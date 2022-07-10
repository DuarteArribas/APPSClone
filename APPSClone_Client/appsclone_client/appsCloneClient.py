import socket
import pickle
import os
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
  def __init__(self,ip,port,username,password,toUploadDir,toDownloadDir,resultsDir,rinexDir,idQueue,logger):
    """Initialize a socket connection with the APPSClone server.

    Parameters
    ----------
    ip            : str
      The ip of the server
    port          : int
      The port of the server
    username      : str
      The username to connect to the server with
    password      : str
      The password of the user
    toUploadDir   : str
      The directory of the server to upload to
    toDownloadDir : str
      The directory of the server to download from
    resultsDir    : str
      The directory, which will contain the results of the post-processed files
    rinexDir      : str
      The directory where the rinex files must be put to be uploaded
    idQueue       : str
      The queue of the uploaded ids.
    logger        : Logs
      The log object to log to
    """
    self.ip            = ip
    self.port          = int(port)
    self.username      = username
    self.password      = password
    self.toUploadDir   = toUploadDir
    self.toDownloadDir = toDownloadDir
    self.resultsDir    = resultsDir
    self.rinexDir      = rinexDir
    self.idQueue       = idQueue
    self.logger        = logger

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
      sshClient = SSHConnection(self.ip,22,self.username,self.password,self.logger)
      sshClient.putFile(Helper.joinPathFile(self.rinexDir,args[0]),self.toUploadDir)
      self.socket.send(pickle.dumps(OptionArgs(1,(args))))
      self.logger.writeRegularLog(Logs.SEVERITY.INFO,uploadInfoSent.format(file = args[0]))
      response = pickle.loads(self.socket.recv(APPSCloneClient.NUMBER_BYTES_TO_RECEIVE))
      self.logger.writeRegularLog(Logs.SEVERITY.INFO,responseReceived)
      respondeCode,respondeArgs = response["code"],response["args"]
      if respondeCode == -1:
        self.logger.writeRegularLog(Logs.SEVERITY.ERROR,responseError.format(errorMsg = respondeArgs[0]))
        print("An error ocurred. Check logs to learn more.")
      else:
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,responseUploadSuccess.format(file = args[0]))
        self.__addIdToQueue(respondeCode)
        os.remove(Helper.joinPathFile(self.rinexDir,args[0]))
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,fileRemovedSuccess.format(file = args[0]))
    elif option == "d":
      numOfIds = len(self.__getAllIdsFromQueue())
      if numOfIds == 0:
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,noIds)
      else:
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,someIds.format(numIds = numOfIds))
      errorOcurred = False
      for rinexId in self.__getAllIdsFromQueue():
        self.socket.send(pickle.dumps(OptionArgs(2,(rinexId,))))
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,downloadInfoSent.format(id = rinexId))
        response = pickle.loads(self.socket.recv(APPSCloneClient.NUMBER_BYTES_TO_RECEIVE))
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,responseReceived)
        respondeCode,respondeArgs = response["code"],response["args"]
        if respondeCode == -1:
          self.logger.writeRegularLog(Logs.SEVERITY.ERROR,responseError.format(errorMsg = respondeArgs[0]))
          errorOcurred = True
        else:
          print(Helper.joinPathFile(self.toDownloadDir,respondeCode))
          sshClient = SSHConnection(self.ip,22,self.username,self.password,self.logger)
          sshClient.getFile(Helper.joinPathFile(self.toDownloadDir,respondeCode),self.resultsDir)
          self.__removeIdFromQueue(rinexId)
      if errorOcurred:
        print("An error ocurred. Check logs to learn more.")

  def __addIdToQueue(self,rinexId):
    """Add the id of the upload to the queue of uploaded ids.

    Parameters
    ----------
    rinexId : int
      The id to add to the queue
    """
    with open(self.idQueue,"a") as f:
      f.write(f"{rinexId}\n")
    self.logger.writeRegularLog(Logs.SEVERITY.INFO,addToQueueSuccess.format(id = rinexId))

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
    self.logger.writeRegularLog(Logs.SEVERITY.INFO,removeFromQueueSuccess.format(id = rinexId))

  def __getAllIdsFromQueue(self):
    """Get all ids from the queue of uploaded ids.

    Returns
    ----------
    list
      All ids of uploaded files in the queue
    """
    with open(self.idQueue,"r") as f:
      lines = f.readlines()
      return [line.split("\n")[0] for line in lines]
      
# ✓ feature tested