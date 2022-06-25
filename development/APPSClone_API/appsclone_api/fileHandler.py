import os.path
import re
from appsclone_api.utils.sshConnection import *
from appsclone_api.utils.helper        import *
from appsclone_api.connection          import *
from appsclone_api.utils.logs          import *
from appsclone_api.constants           import *
from os                                import listdir

class FileHandler:
  """
  """
  # == Attributes ==
  # == Methods ==
  @staticmethod
  def handleAllFileStates(conn,appsIDQueue,resultsDir,logger):
    """Handle the state of all files in the apps id queue.

    Parameters
    ----------
    conn        : Connection_APPS
      A connection to APPS object
    appsIDQueue : str
      The file which contains the ids of the files that were uploaded to APPS
    resultsDir  : str
      The directory to which the results should be downloaded to
    logger      : Logs
      The log object to log to
    """
    logger.writeRoutineLog(handleAllFilesState,Logs.ROUTINE_STATUS.START)
    with open(appsIDQueue,"r") as f:
      uuids = f.readlines()
      uuids = [uuid.split("\n")[0] for uuid in uuids]
      for uuid in uuids:
        conn.handleFileState(uuid,appsIDQueue,resultsDir)
    logger.writeRoutineLog(handleAllFilesState,Logs.ROUTINE_STATUS.END)

  @staticmethod
  def uploadBackResults(rinexQueue,resultsDir,username,password,logger):
    logger.writeRoutineLog(uploadBack,Logs.ROUTINE_STATUS.START)
    for result in os.listdir(resultsDir):
      queueLine = FileHandler._getResultLineFromRinexQueue(rinexQueue,result)
      if queueLine:
        uploadDir = queueLine.split(" ")[1]
        ip        = queueLine.split(" ")[2]
        port      = queueLine.split(" ")[3]
        sshClient = SSHConnection(ip,port,username,password)
        sshClient.putFile(Helper.joinPathFile(resultsDir,result),uploadDir)
        logger.writeRegularLog(Logs.SEVERITY.INFO,resultUploadedBack.format(file = result,uploadDir = uploadDir))
        FileHandler._removeFileFromQueueUploadFiles(rinexQueue,result)
      else:
        logger.writeRegularLog(Logs.SEVERITY.ERROR,resultNotInQueue.format(file = result))
      os.remove(Helper.joinPathFile(resultsDir,result))
    logger.writeRoutineLog(uploadBack,Logs.ROUTINE_STATUS.END)

  @staticmethod
  def _getResultLineFromRinexQueue(rinexQueue,result):
    """Get a line from the rinex queue.

    Parameters
    ----------
    rinexQueue : str
      The file which contains the rinex queue
    result     : str
      The name of the results file

    Returns
    ----------
    str or None
      The line, which contains the given result or None if no line contains the given result
    """
    with open(rinexQueue,"r") as f:
      lines = f.readlines()
      for line in lines:
        if line.split(" ")[0] == result.split("_results")[0]:
          return line
      return None

  @staticmethod
  def _removeFileFromRinexQueue(rinexQueue,result):
    """Remove a line from the rinex queue.

    Parameters
    ----------
    rinexQueue : str
      The file which contains the rinex queue
    result     : str
      The name of the results file
    """
    newFileLines = ""
    with open(rinexQueue,"r") as f:
      lines = f.readlines()
      for line in lines:
        if line.split(" ")[0] != result.split("_results")[0]:
          newFileLines += line
    with open(rinexQueue,"w") as f: 
      f.write(newFileLines)

  @staticmethod
  def downloadRinexFiles(uploadFilesDirectory,downloadFolder,uploadFilesQueueFile,logger):
    """Download all files from the given upload files to the given directory.

    Parameters
    ----------
    uploadFilesDirectory : str
      The directory to read the upload files from
    downloadFolder       : str
      The directory to download the files to 
    uploadFilesQueueFile : str
      The file, which contains the queue of the upload files
    logger               : Logs
      The Logs object that will be used to log several actions
    """
    logger.writeLog(Logs.SEVERITY.INFO,downloadRinexFilesRoutineStartLog)
    alreadyUploadedFileNames = []
    alreadyUploadedFileNames.append(FileHandler._getAlreadyUploadedFilenames(uploadFilesQueueFile))
    for uploadFile in FileHandler._getUploadFiles(uploadFilesDirectory,logger):
      pathToDownloadFrom,pathToUploadTo,ipToConnect = FileHandler._parseUploadFile(
        FileHandler._concatenateFileToPath(uploadFile,uploadFilesDirectory)
      )
      port = 22                                     #hardcode
      user = UserSSHClient("root","Pr0j#to_Spr1ng") #hardcode
      if FileHandler._getFileFromPath(pathToDownloadFrom) not in alreadyUploadedFileNames:
        FileHandler._downloadRinexFile(pathToDownloadFrom,downloadFolder,ipToConnect,port,user,logger)
        alreadyUploadedFileNames.append(FileHandler._getFileFromPath(pathToDownloadFrom))
        FileHandler._addFileToQueueUploadFiles(
          uploadFilesQueueFile,
          FileHandler._getFileFromPath(pathToDownloadFrom),
          pathToUploadTo,
          ipToConnect,
          port,
          logger
        )
      else:
        #TODO: log
        pass
      os.remove(FileHandler._concatenateFileToPath(uploadFile,uploadFilesDirectory))

    logger.writeLog(Logs.SEVERITY.INFO,downloadRinexFilesRoutineEndLog)

  @staticmethod
  def _getAlreadyUploadedFilenames(uploadFilesQueueFile):
    alreadyUploadedFileNames = []
    with open(uploadFilesQueueFile,"r") as f:
      lines = f.readlines()
      for line in lines:
       alreadyUploadedFileNames.append(line.split(" ")[0])
    return alreadyUploadedFileNames

  @staticmethod
  def _getUploadFiles(uploadFilesDirectory,logger):
    """Get the list of upload files that are valid from the given directory.

    Parameters
    ----------
    uploadFilesDirectory : str
      The directory to read the upload files from
    logger               : Logs
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
    logger     : Logs
      The Logs object that will be used to log several actions

    Returns
    ----------
    bool
      True if the upload file is valid and False otherwise
    """
    file = FileHandler._getFileFromPath(uploadFile)
    if os.path.isfile(uploadFile):
      with open(uploadFile,"r") as f:
        lines = f.readlines()
        lines = FileHandler._cleanEmptyFieldsInList(lines)
        if len(lines) == 3 and lines[0].strip() != "" and lines[1].strip() != "" and lines[2].strip() != "":
          validIpv4 = FileHandler._isValidIpv4(lines[2])
          if not validIpv4:
            logger.writeLog(Logs.SEVERITY.ERROR,invalidUploadFileLog.format(file = file,reason = "Invalid ip"))
          else:
            logger.writeLog(Logs.SEVERITY.INFO,validUploadFileLog.format(file = file))
          return validIpv4
        else:
          logger.writeLog(Logs.SEVERITY.ERROR,invalidUploadFileLog.format(file = file,reason = "Invalid fields in file"))  
    else:
      logger.writeLog(Logs.SEVERITY.ERROR,invalidUploadFileLog.format(file = file,reason = "Not a file"))
      return False

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
  def _downloadRinexFile(pathToDownloadFrom,downloadFolder,ipToConnect,port,user,logger):
    """Download a rinex file from the given server.

    Parameters
    ----------
    pathToDownloadFrom : str
      The path to the file on the server
    downloadFolder     : str
      The directory to download the files to 
    ipToConnect        : str
      The IP of the server
    port               : int
      The port to connect to the server on
    user               : UserSSHClient
      A user representation of the user that connects via ssh
    logger     : Logs
      The Logs object that will be used to log several actions
    """
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
      scpClient = scp.SCPClient(ssh.get_transport())
      scpClient.get(pathToDownloadFrom,downloadFolder)
      logger.writeLog(
        Logs.SEVERITY.INFO,
        scpSuccessful.format(file = FileHandler._getFileFromPath(pathToDownloadFrom),downloadFolder = downloadFolder)
      )
    except paramiko.ssh_exception.BadAuthenticationType:
      logger.writeLog(
        Logs.SEVERITY.ERROR,
        connectAttemptUnsuccessfulLog.format(reason = f"Could not connect to ip {ipToConnect}")
      )
      return
    except paramiko.ssh_exception.NoValidConnectionsError:
      logger.writeLog(
        Logs.SEVERITY.ERROR,
        connectAttemptUnsuccessfulLog.format(reason = f"The port {port} is not available")
      )
      return
    except paramiko.ssh_exception.AuthenticationException:
      logger.writeLog(
        Logs.SEVERITY.ERROR,
        connectAttemptUnsuccessfulLog.format(reason = "Could not authenticate user. The username or password may be invalid")
      )
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
  def _addFileToQueueUploadFiles(uploadFilesQueueFile,rinexFile,pathToUploadTo,ipToConnect,port,logger):
    """Add the rinex file, its upload path and its ip and port to the upload files queue file.

    Parameters
    ----------
    uploadFilesQueueFile : str
      The file, which contains the queue of the upload files
    rinexFile            : str
      The rinex file to add to the queue
    pathToUploadTo       : str
      The path to which the results must be uploaded to
    ipToConnect          : str
      The ip of the server to connect to
    port                 : int
      The port of the server to connect to
    logger     : Logs
      The Logs object that will be used to log several actions
    """
    with open(uploadFilesQueueFile,"a") as f:
      f.write(rinexFile + " " + pathToUploadTo + " " + ipToConnect + " " + str(port) + "\n")
    logger.writeLog(Logs.SEVERITY.INFO,fileAddedToQueueLog.format(file = rinexFile))

  @staticmethod
  def uploadAllRinexToApps(conn,downloadFolder,uploadedFilesQueue,args,logger):
    for rinex in os.listdir(downloadFolder):
      if os.path.getsize(FileHandler._concatenateFileToPath(rinex,downloadFolder)) / (1024 * 1024.0) < conn.getQuotaLeft():
        conn.uploadFile(FileHandler._concatenateFileToPath(rinex,downloadFolder),uploadedFilesQueue,args)
        os.remove(FileHandler._concatenateFileToPath(rinex,downloadFolder))
        os.remove(FileHandler._concatenateFileToPath(rinex,downloadFolder)+".gz")