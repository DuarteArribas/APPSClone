import os.path
import gzip
import os
from appsclone_api.utils.helper import *
from appsclone_api.rinexHeader  import *
from appsclone_api.utils.logs   import *
from appsclone_api.constants    import *
from gdgps_apps.exceptions      import *
from gdgps_apps.apps            import APPS
from gdgps_apps                 import defines

class Connection_APPS:
  """A connection to APPS, which contains all functions to interact with its API.
  
  Attributes
  ----------
  DEFAULT_ARGS : dict
    Default upload arguments of APPS and the possible choices for them
  """
  # == Attributes ==
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
  def __init__(self,settingsFile,downloadDirectory,logger):
    """Connect to APPS and initalize the logger.
    
    Parameters
    ----------
    settingsFile      : str
      The APPS settings file to read the user's credentials from
    downloadDirectory : str
      The directory to download the processed results to
    logger            : Logs
      The logger object to log to
    """
    self.apps   = APPS(settings_file = settingsFile,download_directory = downloadDirectory)
    self.logger = logger

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

  def getQuotaLeft(self):
    """Check the amount of space left in the user's quota.

    Returns
    ----------
    int
      The amount of space left in the user's quota in mebibytes
    """
    profile = self.apps.profile()
    return self.__bytesToMB(profile["quota"] - profile["usage"])

  def uploadFile(self,file,appsIDQueue,uploadArgs):
    """Upload a file to APPS and add its id to the id queue.

    Parameters
    ----------
    file        : str
      The file to upload
    appsIDQueue : str
      The file which contains the ids of the files that were uploaded to APPS
    uploadArgs  : dict
      Contains pairs of argumentName->argument for the upload
    """
    self.logger.writeLog(
      Logs.SEVERITY.INFO,
      Logs.getLogMsg(
        Logs.LOG_TYPE.SUBROUTINE_START,
        rinexUpload.format(file = Helper.getFileFromPath(file))
      )
    )
    isValid = self.__checkFileValidity(file)
    if isValid:
      args               = self.__updateUploadArgs(uploadArgs)
      fileResponseObject = self.apps.upload_gipsyx(
        self.__compressUncompressGzip(file,True),
        pressure             = args[0],
        attitude             = args[1],
        email                = args[2],
        access               = args[3],
        processing_mode      = args[4],
        product              = args[5],
        troposphere_model    = args[6],
        ocean_loading        = args[7],
        model_tides          = args[8],
        elev_dep_weighting   = args[9],
        elev_angle_cutoff    = args[10],
        solution_period      = args[11],
        generate_quaternions = args[12]
      )
      self.logger.writeLog(Logs.SEVERITY.INFO,uploadSuccess.format(file = Helper.getFileFromPath(file)))
      self.__addUploadToQueue(fileResponseObject["id"],file,appsIDQueue)
    self.logger.writeLog(
      Logs.SEVERITY.INFO,
      Logs.getLogMsg(
        Logs.LOG_TYPE.SUBROUTINE_END,
        rinexUpload.format(file = file)
      )
    )

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

  def __addUploadToQueue(self,uuid,file,uploadedFilesQueueFile):
    """Add upload to the uploaded files queue.

    Parameters
    ----------
    uuid                   : str
      The id of the uploaded file
    file                   : str
      The uploaded file
    uploadedFilesQueueFile : str
      The file, which contains the uploaded files queue
    """
    with open(uploadedFilesQueueFile,"a") as f:
      f.write(f"{uuid}\n")
      self.logger.writeLog(Logs.SEVERITY.INFO,addedToQueueSuccessLog.format(file = file))

  def __removeFromUploadQueue(self,uuid,file,uploadedFilesQueueFile):
    """Remove upload from the uploaded files queue.

    Parameters
    ----------
    uuid                   : str
      The id of the uploaded file
    file                   : str
      The uploaded file
    uploadedFilesQueueFile : str
      The file, which contains the uploaded files queue
    """
    newQueue       = ""
    uuidNotInQueue = True
    with open(uploadedFilesQueueFile,"r") as f:
      lines = f.readlines()
      for line in lines:
        if not uuid == line.split("\n")[0]:
          newQueue += line
        else:
          uuidNotInQueue = False
    if uuidNotInQueue:
      self.logger.writeLog(Logs.SEVERITY.WARNING,uuidNotInQueueLog.format(file = file))
      return
    with open(uploadedFilesQueueFile,"w") as f:
      f.write(newQueue)
      self.logger.writeLog(Logs.SEVERITY.INFO,removedFromQueueSuccessLog.format(file = file))

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

  def handleFileState(self,uuid,uploadedFilesQueueFile,downloadFolder):
    """Handle what should be done, given the state of a file.

    Parameters
    ----------
    uuid                   : str
      The id of the file to handle
    uploadedFilesQueueFile : str
      The file, which contains the uploaded files queue
    downloadFolder         : str
      The file to which download the results into
    """
    self.logger.writeLog(Logs.SEVERITY.INFO,checkStateStartLog)
    fileDetails = self.__getFileData(uuid,uploadedFilesQueueFile)
    if fileDetails != None:
      fileState   = fileDetails["state"]
      file        = fileDetails["name"]
      self.logger.writeLog(Logs.SEVERITY.INFO,checkStateStartFileLog.format(file = file))
      if fileState   == defines.Data.NASCENT:
        self.logger.writeLog(Logs.SEVERITY.INFO,stateLog.format(file = file,state = "Nascent"))
      if fileState   == defines.Data.SUBMITTED:
        self.logger.writeLog(Logs.SEVERITY.INFO,stateLog.format(file = file,state = "Submitted"))
      elif fileState == defines.Data.VERIFIED:
        self.logger.writeLog(Logs.SEVERITY.INFO,stateLog.format(file = file,state = "Verified"))
        self.__approveSubmission(uuid,file,uploadedFilesQueueFile)
      elif fileState == defines.Data.APPROVED:
        self.logger.writeLog(Logs.SEVERITY.INFO,stateLog.format(file = file,state = "Approved"))
      elif fileState == defines.Data.WAITING:
        self.logger.writeLog(Logs.SEVERITY.INFO,stateLog.format(file = file,state = "Waiting"))
      elif fileState == defines.Data.QUEUED:
        self.logger.writeLog(Logs.SEVERITY.INFO,stateLog.format(file = file,state = "Queued"))
      elif fileState == defines.Data.PROCESSING:
        self.logger.writeLog(Logs.SEVERITY.INFO,stateLog.format(file = file,state = "Processing"))
      elif fileState == defines.Data.DONE:
        self.logger.writeLog(Logs.SEVERITY.INFO,stateLog.format(file = file,state = "Done"))
      elif fileState == defines.Data.AVAILABLE:
        self.logger.writeLog(Logs.SEVERITY.INFO,stateLog.format(file = file,state = "Available"))
        self.__retrieveData(uuid,file,uploadedFilesQueueFile,downloadFolder)
        self.__removeData(uuid,file,uploadedFilesQueueFile)
      elif fileState == defines.Data.ERROR:
        self.logger.writeLog(Logs.SEVERITY.INFO,stateLog.format(file = file,state = "Error"))
        self.__handleError(uuid,file,uploadedFilesQueueFile)
      self.logger.writeLog(Logs.SEVERITY.INFO,checkStateEndFileLog.format(file = file))
    else:
      self.logger.writeLog(Logs.SEVERITY.INFO,checkStateEndLog)

  def __getFileData(self,uuid,uploadedFilesQueueFile):
    """Get details from the file in APPS.

    Parameters
    ----------
    uuid                   : str
      The id of the submission
    uploadedFilesQueueFile : str
      The file, which contains the uploaded files queue

    Returns
    ----------
    dict | None
      Pairs of details from APPS. None is returned in case of error
    """
    fileData = None
    try:
      self.logger.writeLog(Logs.SEVERITY.INFO,fileDataStartLog.format(uuid = uuid))
      fileData = self.apps.detail(uuid)
    except DataNotFound:
      self.logger.writeLog(Logs.SEVERITY.ERROR,dataNotFoundLog.format(file = "Unknown"))
      self.__removeFromUploadQueue(uuid,"Unknown",uploadedFilesQueueFile)
      fileData = None
    except InvalidIdentifier:
      self.logger.writeLog(Logs.SEVERITY.ERROR,InvalidIdentifierLog.format(uuid = uuid))
      self.__removeFromUploadQueue(uuid,"Unknown",uploadedFilesQueueFile)
      fileData = None
    except:
      self.logger.writeLog(Logs.SEVERITY.CRITICAL,criticalExceptionLog.format(file = "Unknown"))
      fileData = None
    finally:
      self.logger.writeLog(Logs.SEVERITY.INFO,fileDataEndLog.format(uuid = uuid))
      return fileData

  def __approveSubmission(self,uuid,file,uploadedFilesQueueFile):
    """Approve the submission after it has been verified.

    Parameters
    ----------
    uuid                   : str
      The id of the submission
    file                   : str
      The name of the submission
    uploadedFilesQueueFile : str
      The file, which contains the uploaded files queue
    """
    try:
      self.logger.writeLog(Logs.SEVERITY.INFO,approveStartLog.format(file = file))
      self.apps.approve(uuid)
      self.logger.writeLog(Logs.SEVERITY.INFO,approvedSuccessfullLog.format(file = file))
    except DataNotFound:
      self.logger.writeLog(Logs.SEVERITY.ERROR,dataNotFoundLog.format(file = file))
      self.__removeFromUploadQueue(uuid,file,uploadedFilesQueueFile)
    except InvalidIdentifier:
      self.logger.writeLog(Logs.SEVERITY.ERROR,InvalidIdentifierLog.format(uuid = uuid))
      self.__removeFromUploadQueue(uuid,file,uploadedFilesQueueFile)
    except InvalidOperation:
      self.logger.writeLog(Logs.SEVERITY.ERROR,approvedUnsuccessfullLog.format(file = file))
      self.__removeData(uuid,file,uploadedFilesQueueFile)
      self.__removeFromUploadQueue(uuid,file,uploadedFilesQueueFile)
    except:
      self.logger.writeLog(Logs.SEVERITY.CRITICAL,criticalExceptionLog.format(file = file))
    finally:
      self.logger.writeLog(Logs.SEVERITY.INFO,approveEndLog.format(file = file))

  def __removeData(self,uuid,file,uploadedFilesQueueFile):
    """Remove both source and result data from APPS and from the uploaded queue.

    Parameters
    ----------
    uuid                   : str
      The id of the submission
    file                   : str
      The name of the submission
    uploadedFilesQueueFile : str
      The file, which contains the uploaded files queue
    """
    try:
      self.logger.writeLog(Logs.SEVERITY.INFO,removeDataStartLog.format(file = file))
      self.apps.delete_data(uuid)
      self.logger.writeLog(Logs.SEVERITY.INFO,dataDeletedSuccessfulLog.format(file = file))
    except DataNotFound:
      self.logger.writeLog(Logs.SEVERITY.ERROR,dataNotFoundLog.format(file = file))
    except InvalidIdentifier:
      self.logger.writeLog(Logs.SEVERITY.ERROR,InvalidIdentifierLog.format(uuid = uuid))
    except InvalidOperation:
      self.logger.writeLog(Logs.SEVERITY.ERROR,dataDeletedUnsuccessfulLog.format(file = file))
    except:
      self.logger.writeLog(Logs.SEVERITY.CRITICAL,criticalExceptionLog.format(file = file))
    finally:
      self.__removeFromUploadQueue(uuid,file,uploadedFilesQueueFile)
      self.logger.writeLog(Logs.SEVERITY.INFO,removeDataEndLog.format(file = file))

  def __retrieveData(self,uuid,file,uploadedFilesQueueFile,downloadFolder):
    """Retrieve results from APPS.

    Parameters
    ----------
    uuid                   : str
      The id of the submission
    file                   : str
      The name of the submission
    uploadedFilesQueueFile : str
      The file, which contains the uploaded files queue
    downloadFolder         : str
      The file to which download the results into
    """
    try:
      self.logger.writeLog(Logs.SEVERITY.INFO,retrieveDataStartLog.format(file = file))
      self.apps.download_result(uuid = uuid,dr = downloadFolder)
      self.logger.writeLog(Logs.SEVERITY.INFO,downloadSuccessfullLog.format(file = file))
    except DataNotFound:
      self.logger.writeLog(Logs.SEVERITY.ERROR,dataNotFoundLog.format(file = file))
      self.__removeFromUploadQueue(uuid,file,uploadedFilesQueueFile)
    except InvalidIdentifier:
      self.logger.writeLog(Logs.SEVERITY.ERROR,InvalidIdentifierLog.format(uuid = uuid))
      self.__removeFromUploadQueue(uuid,file,uploadedFilesQueueFile)
    except InvalidOperation:
      self.logger.writeLog(Logs.SEVERITY.ERROR,downloadUnsuccessfullLog.format(file = file))
      self.__removeFromUploadQueue(uuid,file,uploadedFilesQueueFile)
    except:
      self.logger.writeLog(Logs.SEVERITY.CRITICAL,criticalExceptionLog.format(file = file))
    finally:
      self.logger.writeLog(Logs.SEVERITY.INFO,retrieveDataEndLog.format(file = file))

  def __handleError(self,uuid,file,uploadedFilesQueueFile):
    """Handler error from APPS.

    Parameters
    ----------
    uuid                   : str
      The id of the submission
    file                   : str
      The name of the submission
    uploadedFilesQueueFile : str
      The file, which contains the uploaded files queue
    """
    self.logger.writeLog(Logs.SEVERITY.ERROR,errorFromAPPSLog.format(file = file))
    self.__removeData(uuid,file,uploadedFilesQueueFile)