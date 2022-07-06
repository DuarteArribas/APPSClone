import paramiko
import scp
from appsclone_client.utils.helper import *

class SSHConnection:
  """A client connection via ssh."""
  # == Methods ==
  def __init__(self,ip,port,username,password):
    """Set the initial connection parameters.

    Parameters
    ----------
    ip       : str
      The ip of the server to connect to
    port     : str
      The port of the server to connect to
    username : str
      The username of the user to connect with
    password : str
      The password of the user
    logger   : Logs
      The log object to log to
    """
    self.ip       = ip
    self.port     = int(port)
    self.username = username
    self.password = password
    self.client   = self.__connectViaSSH()

  def __connectViaSSH(self):
    """Connects to a server via ssh.

    Returns
    ----------
    SSHClient:
      An ssh client object
    """
    try:
      client = paramiko.SSHClient()
      client.load_system_host_keys()
      client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      client.connect(self.ip,self.port,self.username,self.password)
      return client
    except:
      pass
  
  def getFile(self,pathToDownloadFrom,downloadDir):
    """Download a file from the given path in the server to the given local path.

    Parameters
    ----------
    pathToDownloadFrom : str
      The path of the server to download the file from
    downloadDir        : str
      The local directory to download the file to
    """
    if self.client != None:
      try:
        filename = Helper.getFileFromPath(pathToDownloadFrom)
        scpClient = scp.SCPClient(self.client.get_transport())
        scpClient.get(pathToDownloadFrom,downloadDir)
      except:
        pass

  def putFile(self,pathToUpload,uploadDir):
    """Upload the given file to the given upload directory on the server.

    Parameters
    ----------
    pathToUpload : str
      The path of the file to upload
    uploadDir    : str
      The directory to upload the file to
    """
    if self.client != None:
      try:
        filename  = Helper.getFileFromPath(pathToUpload)
        scpClient = scp.SCPClient(self.client.get_transport())
        scpClient.put(pathToUpload,uploadDir)
      except:
        pass

# ✓    unit tested
# ✓ feature tested