import os.path
import re
from appsclone_api.utils.sshConnection import *
from appsclone_api.utils.helper        import *
from appsclone_api.connection          import *
from appsclone_api.utils.logs          import *
from appsclone_api.constants           import *
from os                                import listdir

class APPSCloneServer:
  """TODOOOOOOOOOOO"""
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
    """Upload back results to the client who asked for them.

    Parameters
    ----------
    rinexQueue : str
      The file which contains the rinex queue
    resultsDir : str
      The directory to which the results should be downloaded to
    username   : str
      The username of the user to connect with
    password   : str
      The password of the user
    logger     : Logs
      The log object to log to
    """
    logger.writeRoutineLog(uploadBack,Logs.ROUTINE_STATUS.START)
    for result in os.listdir(resultsDir):
      queueLine = APPSCloneServer._getResultLineFromRinexQueue(rinexQueue,result)
      if queueLine:
        uploadDir = queueLine.split(" ")[1]
        ip        = queueLine.split(" ")[2]
        port      = queueLine.split(" ")[3]
        sshClient = SSHConnection(ip,port,username,password,logger)
        sshClient.putFile(Helper.joinPathFile(resultsDir,result),uploadDir)
        logger.writeRegularLog(Logs.SEVERITY.INFO,resultUploadedBack.format(file = result,uploadDir = uploadDir))
        APPSCloneServer._removeFileFromRinexQueue(rinexQueue,result,logger)
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
  def _removeFileFromRinexQueue(rinexQueue,result,logger):
    """Remove a line from the rinex queue.

    Parameters
    ----------
    rinexQueue : str
      The file which contains the rinex queue
    result     : str
      The name of the results file
    """
    newFileLines = ""
    queueChanged = False
    with open(rinexQueue,"r") as f:
      lines = f.readlines()
      for line in lines:
        if line.split(" ")[0] != result.split("_results")[0]:
          newFileLines += line
        else:
          queueChanged = True
    with open(rinexQueue,"w") as f: 
      f.write(newFileLines)
    if queueChanged:
      logger.writeRegularLog(Logs.SEVERITY.INFO,removedFromRinexQueue.format(file = result))

  @staticmethod
  def downloadRinexFiles(toDownloadDir,toUploadDir,rinexQueue,username,password,logger):
    """Download all files from the given upload files to the given directory.

    Parameters
    ----------
    toDownloadDir : str
      The directory to read the upload files from
    toUploadDir   : str
      The directory that contains the downloaded rinex file for upload 
    rinexQueue    : str
      The file which contains the rinex queue
    username      : str
      The username of the user to connect with
    password      : str
      The password of the user
    logger        : Logs
      The log object to log to
    """
    logger.writeRoutineLog(downloadRinex,Logs.ROUTINE_STATUS.START)
    alreadyUploadedFilenames = APPSCloneServer._getAlreadyUploadedFilenames(rinexQueue)
    for uploadFile in APPSCloneServer._getUploadFiles(toDownloadDir,logger):
      pathToDownloadFrom,dirToUploadTo,ip = APPSCloneServer._parseUploadFile(
        Helper.joinPathFile(toDownloadDir,uploadFile)
      )
      rinexFile = Helper.getFileFromPath(pathToDownloadFrom)
      if rinexFile not in alreadyUploadedFilenames:
        sshClient = SSHConnection(ip,22,username,password,logger)
        sshClient.getFile(pathToDownloadFrom,toUploadDir)
        alreadyUploadedFilenames.append(rinexFile)
        APPSCloneServer._addFileToRinexQueue(
          rinexQueue,
          rinexFile,
          dirToUploadTo,
          ip,
          22,
          logger
        )
      else:
        logger.writeRegularLog(Logs.SEVERITY.ERROR,alreadyUploaded.format(file = rinexFile))
      os.remove(Helper.joinPathFile(toDownloadDir,uploadFile))
      logger.writeRegularLog(Logs.SEVERITY.INFO,removedUploadFile.format(file = uploadFile))
    logger.writeRoutineLog(downloadRinex,Logs.ROUTINE_STATUS.END)

  @staticmethod
  def _getAlreadyUploadedFilenames(rinexQueue):
    """Get the filenames of already uploaded files to APPS.

    Parameters
    ----------
    rinexQueue : str
      The file which contains the rinex queue
    """
    alreadyUploadedFilenames = []
    with open(rinexQueue,"r") as f:
      lines = f.readlines()
      for line in lines:
       alreadyUploadedFilenames.append(line.split(" ")[0])
    return alreadyUploadedFilenames

  @staticmethod
  def _getUploadFiles(toDownloadDir,logger):
    """Get the list of upload files that are valid from the given directory.

    Parameters
    ----------
    toDownloadDir : str
      The directory to read the upload files from
    logger        : Logs
      The log object to log to

    Returns
    ----------
    list
      The valid upload files
    """
    logger.writeSubroutineLog(uploadFilesChecking,Logs.ROUTINE_STATUS.START)
    uploadFiles          = os.listdir(toDownloadDir)
    validatedUploadFiles = [
      uploadFile for uploadFile in uploadFiles if APPSCloneServer._isValidUploadFile(
        Helper.joinPathFile(toDownloadDir,uploadFile),
        logger
      )
    ]
    if len(validatedUploadFiles) > 0:
      logger.writeRegularLog(Logs.SEVERITY.INFO,uploadFilesExist.format(numOfUploadFiles = len(validatedUploadFiles)))
    else:
      logger.writeRegularLog(Logs.SEVERITY.INFO,noUploadFiles)
    logger.writeSubroutineLog(uploadFilesChecking,Logs.ROUTINE_STATUS.END)
    return validatedUploadFiles

  @staticmethod
  def _isValidUploadFile(uploadFile,logger):
    """Check if an upload file is valid. The first two lines must be file paths and the second line must
    be an ipv4 address. No more lines should be in the file.

    Parameters
    ----------
    uploadFile : str
      The upload file to check
    logger     : Logs
      The log object to log to

    Returns
    ----------
    bool
      True if the upload file is valid and False otherwise
    """
    filename = Helper.getFileFromPath(uploadFile)
    if os.path.isfile(uploadFile):
      with open(uploadFile,"r") as f:
        lines = f.readlines()
        lines = Helper.cleanEmptyFieldsInList(lines)
        if len(lines) == 3 and lines[0].strip() != "" and lines[1].strip() != "" and lines[2].strip() != "":
          validIpv4 = Helper.isValidIpv4(lines[2])
          if not validIpv4:
            logger.writeRegularLog(Logs.SEVERITY.ERROR,invalidUploadFileIP.format(file = filename,ip = lines[2]))
          else:
            logger.writeRegularLog(Logs.SEVERITY.INFO,validUploadFile.format(file = filename))
          return validIpv4
        else:
          logger.writeRegularLog(Logs.SEVERITY.ERROR,invalidUploadFileFields.format(file = filename))  
    else:
      logger.writeRegularLog(Logs.SEVERITY.ERROR,invalidUploadFileNotAFile.format(file = filename))
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
      The path of the rinex file to download
      The directory to upload the results of the processed rinex files to
      The IPV4 of the machine to donwload the rinex files from and upload the results to
    """
    with open(uploadFile,"r") as f:
      lines              = f.readlines()
      pathToDownloadFrom = lines[0].split("\n")[0]
      dirToUploadTo      = lines[1].split("\n")[0]
      ip                 = lines[2].split("\n")[0]
      return pathToDownloadFrom,dirToUploadTo,ip

  @staticmethod
  def _addFileToRinexQueue(rinexQueue,rinexFile,dirToUploadTo,ip,port,logger):
    """Add the rinex file, its upload path and its ip and port to the upload files queue file.

    Parameters
    ----------
    rinexQueue    : str
      The file which contains the rinex queue
    rinexFile     : str
      The rinex file to add to the queue
    dirToUploadTo : str
      The directory to upload the results to
    ip            : str
      The ip of the server to connect to
    port          : int
      The port of the server to connect to
    logger        : Logs
      The log object to log to
    """
    with open(rinexQueue,"a") as f:
      f.write(rinexFile + " " + dirToUploadTo + " " + ip + " " + str(port) + "\n")
    logger.writeRegularLog(Logs.SEVERITY.INFO,fileAddedToRinexQueue.format(file = rinexFile))

  @staticmethod
  def uploadAllRinexToApps(conn,downloadFolder,uploadedFilesQueue,args,logger):
    for rinex in os.listdir(downloadFolder):
      if os.path.getsize(APPSCloneServer._concatenateFileToPath(rinex,downloadFolder)) / (1024 * 1024.0) < conn.getQuotaLeft():
        conn.uploadFile(APPSCloneServer._concatenateFileToPath(rinex,downloadFolder),uploadedFilesQueue,args)
        os.remove(APPSCloneServer._concatenateFileToPath(rinex,downloadFolder))
        os.remove(APPSCloneServer._concatenateFileToPath(rinex,downloadFolder)+".gz")