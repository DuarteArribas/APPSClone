import os.path
import re
from os import listdir
from vars.loggingStrings.fileHandlerLoggingStrings import *
from userSSHClient import *
from utils.logs import *

class FileHandler:
  """
  """
  # == Attributes ==
  # == Methods ==
  @staticmethod
  def downloadRinexFiles(uploadFilesDirectory,downloadFolder,logger):
    logger.writeLog(Logs.SEVERITY.INFO,downloadRinexFilesRoutineStartLog)
    for uploadFile in _getUploadFiles(uploadFilesDirectory,logger):
      pathToDownloadFrom,pathToUploadTo,ipToConnect = _parseUploadFile(uploadFile)
      port = 22                           #hardcode
      user = UserSSHClient("root","root") #hardcode
      FileHandler._downloadRinexFile(pathToDownloadFrom,downloadFolder,ipToConnect,port,user)
    logger.writeLog(Logs.SEVERITY.INFO,downloadRinexFilesRoutineEndLog)

  @staticmethod
  def _getUploadFiles(uploadFilesDirectory,logger):
    """Get the list of upload files that are valid from the given directory.

    Parameters
    ----------
    uploadFilesDirectory : str
      The directory to read the upload files from
    logger : Logs
      The Logs object that will be used to log several actions

    Returns
    ----------
    list
      The valid upload files
    """
    logger.writeLog(Logs.SEVERITY.INFO,uploadFilesCheckingLog)
    uploadFiles          = os.listdir(uploadFilesDirectory)
    validatedUploadFiles = [uploadFile for uploadFile in uploadFiles if FileHandler._isValidUploadFile(FileHandler._concatenateFileToPath(uploadFile,uploadFilesDirectory),logger)]
    if len(validatedUploadFiles) > 0:
      logger.writeLog(Logs.SEVERITY.INFO,uploadFilesExistLog.format(numOfUploadFiles = len(validatedUploadFiles)))
    else:
      logger.writeLog(Logs.SEVERITY.INFO,noUploadFilesLog)
    return validatedUploadFiles

  @staticmethod
  def _concatenateFileToPath(file,path):
    """Concatenate a file to a filepath, separating them by /

    Parameters
    ----------
    file : str
      The file to concatenate to the file path
    path : str
      The path to concatenate the file to

    Returns
    ----------
    str
      The file path, with the file included
    """
    return path+"/"+file

  @staticmethod
  def _isValidUploadFile(uploadFile,logger):
    """Check if an upload file is valid. The first two lines must be file paths and the second line must
    be an ipv4 address. No more lines should be in the file.

    Parameters
    ----------
    uploadFile : str
      The upload file to check

    Returns
    ----------
    bool
      True if the upload file is valid and False otherwise
    """
    if os.path.isfile(uploadFile):
      with open(uploadFile,"r") as f:
        lines = f.readlines()
        lines = FileHandler._cleanEmptyFieldsInList(lines)
        if len(lines) == 3 and lines[0].strip() != "" and lines[1].strip() != "" and lines[2].strip() != "":
          validIpv4 = FileHandler._isValidIpv4(lines[2])
          if not validIpv4:
            logger.writeLog(Logs.SEVERITY.ERROR,invalidUploadFileLog.format(file = uploadFile,reason = "Invalid ip"))
          else:
            logger.writeLog(Logs.SEVERITY.INFO,validUploadFileLog.format(file = uploadFile))
          return validIpv4
        else:
          logger.writeLog(Logs.SEVERITY.ERROR,invalidUploadFileLog.format(file = uploadFile,reason = "Invalid fields in file"))  
    else:
      logger.writeLog(Logs.SEVERITY.ERROR,invalidUploadFileLog.format(file = uploadFile,reason = "Not a file"))
      return False

  @staticmethod
  def _cleanEmptyFieldsInList(lst):
    """Clean the empty (stripped) fields in a list.

    Parameters
    ----------
    lst : list
      The list to cleanup

    Returns
    ----------
    list
      The list without any empty (stripped) fields
    """
    return [item for item in lst if item.strip()]

  @staticmethod
  def _isValidIpv4(address):
    """Check if an IPV4 address is valid.

    Parameters
    ----------
    address : str
      The ipv4 address to check

    Returns
    ----------
    bool
      True if the IPV4 address is valid and False otherwise
    """
    try:
      addressBytes      = address.split('.')
      validAddressBytes = [b for b in addressBytes if int(b) >= 0 and int(b) <= 255]
      return len(addressBytes) == 4 and len(validAddressBytes) == 4
    except:
      return False

  @staticmethod
  def _parseUploadFile(uploadFile):
    """Parse an upload file to get its properties.

    Parameters
    ----------
    uploadFile : str
      The upload file to parse

    Returns
    ----------
    tuple(str,str,str)
      The path to download the rinex files from
      The path to upload the results of the processed rinex files to
      The IPV4 of the machine to donwload the rinex files from and upload the results to
    """
    with open(uploadFile,"r") as f:
      lines              = f.readlines()
      pathToDownloadFrom = lines[0].split("\n")[0]
      pathToUploadTo     = lines[1].split("\n")[0]
      ipToConnect        = lines[2].split("\n")[0]
      return pathToDownloadFrom,pathToUploadTo,ipToConnect

  @staticmethod
  def _downloadRinexFile(pathToDownloadFrom,downloadFolder,ipToConnect,port,user):
    logger.writeLog(
      Logs.SEVERITY.INFO,
      downloadRinexFileSubroutineStartLog.format(file = FileHandler._getFileFromPath(pathToDownloadFrom))
    )
    try:
      logger.writeLog(
        Logs.SEVERITY.INFO,
        sshConnectAttemptLog.format(ip = ipToConnect,port = port,username = user.username)
      )
      ssh = FileHandler._createSSHClient(ipToConnect,port,user.username,user.password)
      logger.writeLog(Logs.SEVERITY.INFO,connectAttemptSuccessfulLog)
      scp = SCPClient(ssh.get_transport())
      scp.get(pathToDownloadFrom,downloadFolder)
      logger.writeLog(
        Logs.SEVERITY.INFO,
        scpSuccessful.format(file = FileHandler._getFileFromPath(pathToDownloadFrom),downloadFolder = downloadFolder)
      )
    except paramiko.ssh_exception.BadAuthenticationType:
      logger.writeLog(Logs.SEVERITY.ERROR,connectAttemptUnsuccessfulLog.format(reason = "Could not connect to the given ip"))
      return
    except paramiko.ssh_exception.NoValidConnectionsError:
      logger.writeLog(Logs.SEVERITY.ERROR,connectAttemptUnsuccessfulLog.format(reason = "The given port is not available"))
      return
    except paramiko.ssh_exception.AuthenticationException:
      logger.writeLog(Logs.SEVERITY.ERROR,connectAttemptUnsuccessfulLog.format(reason = "Could not authenticate user"))
      return      
    except scp.SCPException:
      logger.writeLog(
        Logs.SEVERITY.ERROR,
        scpUnsuccessful.format(file = FileHandler._getFileFromPath(pathToDownloadFrom),downloadFolder = downloadFolder)
      )
      return
    except:
      logger.writeLog(Logs.SEVERITY.CRITICAL,unexpectedErrorLog)
      return
    finally:
      logger.writeLog(
        Logs.SEVERITY.INFO,
        downloadRinexFileSubroutineEndLog.format(file = FileHandler._getFileFromPath(pathToDownloadFrom))
      )

  @staticmethod
  def _createSSHClient(ip,port,user,password):
    """Create ssh client.

    Parameters
    ----------
    ip       : str
      The ip of the server to connect to
    port     : int
      The port of the server to connect to
    user     : str
      The user to connect to the server with
    password : str
      The password of the user

    Returns
    ----------
    SSHClient
      An ssh client object
    """
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip,port,user,password)
    return client

  @staticmethod
  def _getFileFromPath(path):
    """Get a file, given its path.

    Parameters
    ----------
    path : str
      The path to gather the file from

    Returns
    ----------
    str
      The file from the file path
    """
    return path.split("/")[-1]