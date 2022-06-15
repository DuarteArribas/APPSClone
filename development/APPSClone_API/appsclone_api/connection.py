import gzip
import os
import os.path
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
    self.apps              = APPS(settings_file = settingsFile,download_directory = downloadDirectory)
    self.logger            = Logs(loggingFile)
    self.uploadArgs        = {
      "pressure"             : None,
      "attitude"             : None,
      "email"                : defines.Data.EMAIL_NOTIFY_DEFAULT,
      "access"               : defines.Data.ACCESS_DEFAULT,
      "processing_mode"      : defines.GIPSYData.PROCESSING_MODE_DEFAULT,
      "product"              : defines.GIPSYData.PRODUCT_DEFAULT,
      "troposphere_model"    : defines.GIPSYData.TROP_GMF,
      "ocean_loading"        : True,
      "model_tides"          : True,
      "elev_dep_weighting"   : defines.GIPSYData.ROOT_SINE,
      "elev_angle_cutoff"    : 7.5,
      "solution_period"      : 300,
      "generate_quaternions" : False,
    }

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

  def uploadFile(self,file,uploadedFilesQueueFile,uploadArgs):
    """Upload file to APPS and add it to uploaded queue.

    Parameters
    ----------
    file                   : str
      The file to upload
    uploadedFilesQueueFile : str
      The file, which contains the uploaded files queue
    """
    self.logger.writeLog(Logs.SEVERITY.INFO,uploadStartLog.format(file = file))
    isValid = self.__checkFileValidity(file)
    if isValid:
      fileResponseObject = self.apps.upload_gipsyx(
        self.__compressUncompressGzip(file,True),
        **self.uploadArgs
      )
      self.logger.writeLog(Logs.SEVERITY.INFO,uploadSuccessLog.format(file = file))
      self.__addUploadToQueue(file,fileResponseObject["id"],uploadedFilesQueueFile)
    self.logger.writeLog(Logs.SEVERITY.INFO,uploadEndLog.format(file = file))

  def __checkFileValidity(self,file):
    """Check file validity and log it.

    Parameters
    ----------
    file       : str
      The file to check its validity

    Returns
    ----------
    bool
      True if the rinex file is valid and False otherwise
    """
    file   = self.__getUncompressedFile(file)
    header = RinexHeader()
    header.readMandatoryHeader(file)
    isValid,validity = header.isValidHeader()
    if isValid:
      self.logger.writeLog(Logs.SEVERITY.INFO,fileValidatedLog.format(file = file))
    else:
      validityErrorString = header.validityErrorToString(validity[0],validity[1])
      self.logger.writeLog(Logs.SEVERITY.ERROR,fileNotValidatedLog.format(file = file,validity = validityErrorString))
    return isValid

  def __getUncompressedFile(self,file):
    """Uncompress and delete original file with gzip.

    Parameters
    ----------
    file       : str
      The file to uncompress

    Returns
    ----------
    str
      The name of the uncompressed file or the given file if the file was already uncompressed
    """
    isCompressed = self.__checkCompressedWithGzip(file)
    if isCompressed:
      self.logger.writeLog(Logs.SEVERITY.WARNING,compressedLog.format(file = file))
      uncompressedFile = self.__compressUncompressGzip(file,False)
      os.remove(file)
      return uncompressedFile
    else:
      return file

  def __checkCompressedWithGzip(self,file):
    """Check if a file is compressed with gzip.

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
      filenameNoExtension  = file.split(".")
      filenameNoExtension.pop()
      uncompressedFilename = "".join(filenameNoExtension)
      fileToCompress       = open(f"{uncompressedFilename}Uncompressed","wb")
      compressedFile       = gzip.open(file,"rb")
      fileToCompress.write(compressedFile.read())
      return f"{uncompressedFilename}Uncompressed"

  def __addUploadToQueue(self,file,uuid,uploadedFilesQueueFile):
    """Add upload to the uploaded files queue.

    Parameters
    ----------
    file                   : str
      The uploaded file
    uuid                   : int
      The id of the uploaded file
    uploadedFilesQueueFile : str
      The file, which contains the uploaded files queue
    """
    with open(uploadedFilesQueueFile,"a") as f:
      f.write(f"{uuid}\n")
      self.logger.writeLog(Logs.SEVERITY.INFO,addedToQueueSuccessLog.format(file = file))

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
