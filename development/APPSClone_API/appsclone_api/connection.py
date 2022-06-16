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
  DEFAULT_ARGS = {
    "pressure"             : None,
    "attitude"             : None,
    "email"                : (
      defines.Data.EMAIL_NOTIFY_DEFAULT,(
        defines.Data.EMAIL_NOTIFY_DEFAULT,
        True,
        False
      )
    ),
    "access"               : (
      defines.Data.ACCESS_DEFAULT,(
        defines.Data.ACCESS_DEFAULT,
        defines.Data.PRIVATE,
        defines.Data.PUBLIC
      )
    ),
    "processing_mode"      : (
      defines.GIPSYData.PROCESSING_MODE_DEFAULT,(
        defines.GIPSYData.PROCESSING_MODE_DEFAULT,
        defines.GIPSYData.STATIC,
        defines.GIPSYData.KINEMATIC
      )
    ),
    "product"              : (
      defines.GIPSYData.PRODUCT_DEFAULT,(
        defines.GIPSYData.PRODUCT_DEFAULT,
        defines.OrbitClockProduct.REAL_TIME,
        defines.OrbitClockProduct.ULTRA,
        defines.OrbitClockProduct.RAPID,
        defines.OrbitClockProduct.FINAL,
        defines.GIPSYData.BEST
      )
    ),
    "troposphere_model"    : (
      defines.GIPSYData.TROP_GMF,(
        defines.GIPSYData.TROP_OFF,
        defines.GIPSYData.TROP_PROVIDED,
        defines.GIPSYData.TROP_VMF1,
        defines.GIPSYData.TROP_GMF,
        defines.GIPSYData.TROP_GPT2
      )
    ),
    "ocean_loading"        : (
      True,(
        True,
        False
      )
    ),
    "model_tides"          : (
      True,(
        True,
        False
      )
    ),
    "elev_dep_weighting"   : (
      defines.GIPSYData.ROOT_SINE,(
        defines.GIPSYData.FLAT,
        defines.GIPSYData.SINE,
        defines.GIPSYData.ROOT_SINE
      )
    ),
    "elev_angle_cutoff"    : (
      7.5,(
        defines.GIPSYData.ELEV_ANGLE_CUTOFF_MIN,
        defines.GIPSYData.ELEV_ANGLE_CUTOFF_MAX
      )
    ),
    "solution_period"      : (
      300,(
        defines.GIPSYData.SOLUTION_PERIOD_MIN
      )
    ),
    "generate_quaternions" : (
      False,(
        True,
        False
      )
    ),
  }
  # == Methods ==
  def __init__(self,settingsFile,downloadDirectory,loggingFile):
    """Connects to APPS and initalizes the logger."""
    self.apps              = APPS(settings_file = settingsFile,download_directory = downloadDirectory)
    self.logger            = Logs(loggingFile)

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
    uploadArgs             : dict
      Contains pairs of argumentName->argument
    """
    self.logger.writeLog(Logs.SEVERITY.INFO,uploadStartLog.format(file = file))
    isValid = self.__checkFileValidity(file)
    if isValid:
      args               = self.__updateUploadArgs(uploadArgs)
      fileResponseObject = self.apps.upload_gipsyx(
        self.__compressUncompressGzip(file,True),
        *args
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

  def __updateUploadArgs(self,uploadArgs):
    """Update uploading args with the specified ones or with the defaults ones if no args
    are specified or if they're incorrect.

    Parameters
    ----------
    uploadArgs             : dict
      Contains pairs of argumentName->argument

    Returns
    ----------
    list
      The list of arguments
    """
    args = []
    for argName in uploadArgs:
      if uploadArgs[argName] != "" and self.__isValidArg(argName,uploadArgs[argName]):
        args.append(uploadArgs[argName])
      else:
        defaultValue = Connection_APPS.DEFAULT_ARGS[argName][0] if isinstance(Connection_APPS.DEFAULT_ARGS[argName],tuple) else Connection_APPS.DEFAULT_ARGS[argName]
        self.logger.writeLog(
          Logs.SEVERITY.WARNING,invalidArgLog.format(
            arg          = uploadArgs[argName],
            argName      = argName,
            defaultValue = defaultValue
          )
        )
        args.append(defaultValue)
    return args

  def __isValidArg(self,argName,arg):
    """Check if received argument is valid.

    Parameters
    ----------
    argName                : str
      The name of the argument
    arg                    : str
      The received argument

    Returns
    ----------
    bool
      True if the argument is valid and False otherwise
    """
    if argName   == "pressure" or argName == "attitude":
      return arg == None or os.path.isfile(arg)
    elif argName == "elev_angle_cutoff":
      return arg > Connection_APPS.DEFAULT_ARGS[argName][1][0] and arg < Connection_APPS.DEFAULT_ARGS[argName][1][1]
    elif argName == "solution_period":
      return arg > Connection_APPS.DEFAULT_ARGS[argName][1]
    else:
      return arg in Connection_APPS.DEFAULT_ARGS[argName][1]

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
