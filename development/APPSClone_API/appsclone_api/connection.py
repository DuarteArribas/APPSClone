import gzip
import os
from vars.loggingStrings.connectionLoggingStrings import *
from gdgps_apps.apps                              import APPS
from gdgps_apps                                   import defines
from rinexHeader                                  import *
from utils.logs                                   import *

class Connection_APPS:
  """A connection to APPS, which contains all functions to interact with its API."""
  # == Methods ==
  def __init__(self,settingsFile,downloadDirectory,loggingFile):
    """Connects to APPS and initalizes the logger."""
    self.apps   = APPS(settings_file = settingsFile,download_directory = downloadDirectory)
    self.logger = Logs(loggingFile)

  def testConnection(self):
    """Test the connection to apps.

    Returns
    ----------
    bool
      True if it was able to connect and False otherwise
    """
    connectionStatus = self.apps.ping()[0]
    if connectionStatus:
      self.logger.writeLog(Logs.SEVERITY.INFO,connectionSuccessLog)
    else:
      self.logger.writeLog(Logs.SEVERITY.INFO,connectionFailedLog)
    return connectionStatus

  def uploadFile(self,file,uploadedFiles):
    self.logger.writeLog(Logs.SEVERITY.INFO,uploadAttemptLog.format(file = file))
    file   = self.__uncompressFile(file)
    header = RinexHeader()
    header.readMandatoryHeader(file)
    isValid,validity = header.isValidHeader()
    if isValid:
      self.logger.writeLog(Logs.SEVERITY.INFO,fileValidatedLog.format(file = file))
      compressedFile     = self.__compressUncompressGzip(file,True)
      fileResponseObject = self.apps.upload_gipsyx(compressedFile)
      self.logger.writeLog(Logs.SEVERITY.INFO,uploadSuccessLog.format(file = file))
      with open(uploadedFiles,"a") as f:
        #f.write(f"{fileResponseObject["id"]}\n")
        self.logger.writeLog(Logs.SEVERITY.INFO,addedToQueueSuccessLog.format(file = file))
    else:
      validityErrorString = validityErrorToString(validity[0],validity[1])
      self.logger.writeLog(Logs.SEVERITY.ERROR,fileNotValidatedLog.format(file = file,validity = validityErrorString))

  def __uncompressFile(self,file):
    isCompressed = self.__checkCompressedWithGzip(file)
    if isCompressed:
      self.logger.writeLog(Logs.SEVERITY.WARNING,compressedLog.format(file = file))
      uncompressedFile = self.__compressUncompressGzip(file,False)
      os.remove(file)
      return uncompressedFile
    else:
      return file

  def __checkCompressedWithGzip(self,file):
    """Checks if a file was compressed using gzip

    Parameters
    ----------
    file : str
      The file to check

    Returns
    ----------
    bool
      True if the file was compressed using gzip and False otherwise
    """
    with gzip.open(file,'r') as fGzip:
      try:
        fGzip.read(1)
        return True
      except gzip.BadGzipFile:
        return False

  def __compressUncompressGzip(self,file,isCompress):
    """Compress or uncompress a file with gzip.

    Parameters
    ----------
    file       : str
      The file to compress or uncompress
    isCompress : bool
      True to compress and False to uncompress

    Returns
    ----------
    str
      The name of the compressed or uncompressed file
    """
    if isCompress:
      fileToCompress = open(file,"rb")
      compressedFile = gzip.open(f"{file}.gz","wb")
      compressedFile.writelines(fileToCompress)
      return f"{file}.gz"
    else:
      fileToCompress = open(f"{file}Uncompressed","wb")
      compressedFile = gzip.open(file,"rb")
      fileToCompress.write(compressedFile.read())
      return f"{file}Uncompressed"

  def getStateOfFile(self,uuid):
    state = self.apps.detail(uuid)["state"]
    if state == defines.Data.VERIFIED:
      self.apps.approve(uuid)
    elif state == defines.Data.AVAILABLE:
      self.apps.download_result(uuid)
      self.apps.delete_data(uuid)
      #remove from queue
      #log
    elif state == defines.Data.ERROR:
      self.apps.delete_data(uuid)
      #remove from queue
      #log
