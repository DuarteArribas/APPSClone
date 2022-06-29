import os.path
import os
from appsclone_server.utils.helper import *
from appsclone_server.rinexHeader  import *
from appsclone_server.utils.logs   import *
from appsclone_server.constants    import *
from gdgps_apps.exceptions         import *
from gdgps_apps.apps               import APPS
from gdgps_apps                    import defines

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
      The log object to log to
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
    self.logger.writeSubroutineLog(connectionTest,Logs.ROUTINE_STATUS.START)
    connectionStatus = self.apps.ping()[0]
    if connectionStatus:
      self.logger.writeRegularLog(Logs.SEVERITY.INFO,connectionSuccess)
    else:
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,connectionFailed)
    self.logger.writeSubroutineLog(connectionTest,Logs.ROUTINE_STATUS.END)
    return connectionStatus

  def getQuotaLeft(self):
    """Check the amount of space left in the user's quota.

    Returns
    ----------
    int
      The amount of space left in the user's quota in mebibytes
    """
    profile = self.apps.profile()
    return Helper.bytesToMB(profile["quota"] - profile["usage"])

  def uploadFile(self,filePath,appsIDQueue,uploadArgs):
    """Upload a file to APPS and add its id to the id queue.

    Parameters
    ----------
    filePath    : str
      The path of the file
    appsIDQueue : str
      The file which contains the ids of the files that were uploaded to APPS
    uploadArgs  : dict
      Pairs of argumentName->argument for the upload
    """
    filename = Helper.getFileFromPath(filePath)
    self.logger.writeSubroutineLog(rinexUpload.format(file = filename),Logs.ROUTINE_STATUS.START)
    isValid  = self.__checkFileValidity(filePath)
    if isValid:
      args               = self.__updateUploadArgs(uploadArgs)
      fileResponseObject = self.apps.upload_gipsyx(
        Helper.compressUncompressGzip(filePath,True),
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
      self.logger.writeRegularLog(Logs.SEVERITY.INFO,uploadSuccess.format(file = filename))
      self.__addToIDQueue(fileResponseObject["id"],filePath,appsIDQueue)
    self.logger.writeSubroutineLog(rinexUpload.format(file = filename),Logs.ROUTINE_STATUS.END)

  def __checkFileValidity(self,filePath):
    """Check file validity.

    Parameters
    ----------
    filePath : str
      The path of the file

    Returns
    ----------
    bool
      True if the rinex file is valid and False otherwise
    """
    file             = Helper.getUncompressedFile(filePath)
    filename         = Helper.getFileFromPath(file)
    header           = RinexHeader()
    header.readMandatoryHeader(file)
    isValid,validity = header.isValidHeader()
    if isValid:
      self.logger.writeRegularLog(Logs.SEVERITY.INFO,fileValidated.format(file = filename))
    else:
      validityErrorStr = RinexHeader.validityErrorToString(validity[0],validity[1])
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,fileNotValidated.format(file = filename,validity = validityErrorStr))
    return isValid

  def __updateUploadArgs(self,uploadArgs):
    """Update uploading args with the specified ones or with the defaults ones if no args
    are specified or if they're incorrect.

    Parameters
    ----------
    uploadArgs : dict
      Pairs of argumentName->argument for the upload

    Returns
    ----------
    list
      The arguments
    """
    args = []
    for argName in uploadArgs:
      if uploadArgs[argName] != "" and Connection_APPS._isValidArg(argName,uploadArgs[argName]):
        args.append(uploadArgs[argName])
      else:
        defaultValue = None
        if isinstance(Connection_APPS.DEFAULT_ARGS[argName],tuple):
          defaultValue = Connection_APPS.DEFAULT_ARGS[argName][0]
        else:
          defaultValue = Connection_APPS.DEFAULT_ARGS[argName]
        self.logger.writeRegularLog(
          Logs.SEVERITY.WARNING,invalidArg.format(
            arg          = uploadArgs[argName],
            argName      = argName,
            defaultValue = defaultValue
          )
        )
        args.append(defaultValue)
    return args

  @staticmethod
  def _isValidArg(argName,arg):
    """Check if received argument is valid.

    Parameters
    ----------
    argName : str
      The name of the argument
    arg     : str
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

  def __addToIDQueue(self,uuid,filename,appsIDQueue):
    """Add the upload's id to the apps ID queue.

    Parameters
    ----------
    uuid        : str
      The id of the uploaded file
    filename    : str
      The uploaded filename
    appsIDQueue : str
      The file which contains the ids of the files that were uploaded to APPS
    """
    with open(appsIDQueue,"a") as f:
      f.write(f"{uuid}\n")
      self.logger.writeRegularLog(Logs.SEVERITY.INFO,addedToQueueSuccess.format(file = filename))

  def __removeFromIDQueue(self,uuid,filename,appsIDQueue):
    """Remove upload's id from the apps ID queue.

    Parameters
    ----------
    uuid        : str
      The id of the uploaded file
    filename    : str
      The uploaded filename
    appsIDQueue : str
      The file which contains the ids of the files that were uploaded to APPS
    """
    newQueue       = ""
    uuidNotInQueue = True
    with open(appsIDQueue,"r") as f:
      lines = f.readlines()
      for line in lines:
        if not uuid == line.split("\n")[0]:
          newQueue += line
        else:
          uuidNotInQueue = False
    if uuidNotInQueue:
      self.logger.writeRegularLog(Logs.SEVERITY.WARNING,idNotInQueue.format(file = filename))
      return
    with open(appsIDQueue,"w") as f:
      f.write(newQueue)
      self.logger.writeRegularLog(Logs.SEVERITY.INFO,removedFromQueueSuccess.format(file = filename))

  def handleFileState(self,uuid,appsIDQueue,resultsDir):
    """Handle what should be done, given the state of a file.

    Parameters
    ----------
    uuid        : str
      The id of the submission
    appsIDQueue : str
      The file which contains the ids of the files that were uploaded to APPS
    resultsDir  : str
      The directory to which the results should be downloaded to
    """
    self.logger.writeSubroutineLog(checkState,Logs.ROUTINE_STATUS.START)
    fileDetails = self.__getFileData(uuid,appsIDQueue)
    if fileDetails != None:
      fileState = fileDetails["state"]
      filename  = fileDetails["name"]
      self.logger.writeRegularLog(Logs.SEVERITY.INFO,checkStateFile.format(file = filename))
      if fileState   == defines.Data.NASCENT:
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,state.format(file = filename,state = "Nascent"))
      if fileState   == defines.Data.SUBMITTED:
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,state.format(file = filename,state = "Submitted"))
      elif fileState == defines.Data.VERIFIED:
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,state.format(file = filename,state = "Verified"))
        self.__approveSubmission(uuid,filename,appsIDQueue)
      elif fileState == defines.Data.APPROVED:
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,state.format(file = filename,state = "Approved"))
      elif fileState == defines.Data.WAITING:
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,state.format(file = filename,state = "Waiting"))
      elif fileState == defines.Data.QUEUED:
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,state.format(file = filename,state = "Queued"))
      elif fileState == defines.Data.PROCESSING:
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,state.format(file = filename,state = "Processing"))
      elif fileState == defines.Data.DONE:
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,state.format(file = filename,state = "Done"))
      elif fileState == defines.Data.AVAILABLE:
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,state.format(file = filename,state = "Available"))
        self.__retrieveData(uuid,filename,appsIDQueue,resultsDir)
        self.__removeData(uuid,filename,appsIDQueue)
      elif fileState == defines.Data.ERROR:
        self.logger.writeRegularLog(Logs.SEVERITY.INFO,state.format(file = filename,state = "Error"))
        self.__handleError(uuid,filename,appsIDQueue)
    else:
      self.logger.writeSubroutineLog(checkState,Logs.ROUTINE_STATUS.END)

  def __getFileData(self,uuid,appsIDQueue):
    """Get details from the file in APPS.

    Parameters
    ----------
    uuid        : str
      The id of the submission
    appsIDQueue : str
      The file which contains the ids of the files that were uploaded to APPS

    Returns
    ----------
    dict | None
      Pairs of details from APPS. None is returned in case of error
    """
    fileData = None
    try:
      self.logger.writeSubsubroutineLog(fileDataGathering.format(uuid = uuid),Logs.ROUTINE_STATUS.START)
      fileData = self.apps.detail(uuid)
    except DataNotFound:
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,dataNotFound.format(uuid = uuid))
      self.__removeFromIDQueue(uuid,"Unknown",appsIDQueue)
      fileData = None
    except InvalidIdentifier:
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,invalidIdentifier.format(uuid = uuid))
      self.__removeFromIDQueue(uuid,"Unknown",appsIDQueue)
      fileData = None
    except:
      self.logger.writeRegularLog(Logs.SEVERITY.CRITICAL,criticalException.format(uuid = uuid))
      fileData = None
    finally:
      self.logger.writeSubsubroutineLog(fileDataGathering.format(uuid = uuid),Logs.ROUTINE_STATUS.END)
      return fileData

  def __approveSubmission(self,uuid,filename,appsIDQueue):
    """Approve the submission after it has been verified.

    Parameters
    ----------
    uuid        : str
      The id of the submission
    filename    : str
      The uploaded filename
    appsIDQueue : str
      The file which contains the ids of the files that were uploaded to APPS
    """
    try:
      self.logger.writeSubsubroutineLog(approveFile.format(file = filename),Logs.ROUTINE_STATUS.START)
      self.apps.approve(uuid)
      self.logger.writeRegularLog(Logs.SEVERITY.INFO,approveSuccessful.format(file = filename))
    except DataNotFound:
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,dataNotFound.format(uuid = uuid))
      self.__removeFromIDQueue(uuid,filename,appsIDQueue)
    except InvalidIdentifier:
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,invalidIdentifier.format(uuid = uuid))
      self.__removeFromIDQueue(uuid,filename,appsIDQueue)
    except InvalidOperation:
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,approveUnsuccessful.format(file = filename))
      self.__removeData(uuid,filename,appsIDQueue)
      self.__removeFromIDQueue(uuid,filename,appsIDQueue)
    except:
      self.logger.writeRegularLog(Logs.SEVERITY.CRITICAL,criticalException.format(uuid = uuid))
    finally:
      self.logger.writeSubsubroutineLog(approveFile.format(file = filename),Logs.ROUTINE_STATUS.END)

  def __removeData(self,uuid,filename,appsIDQueue):
    """Remove both source and result data from APPS and from apps ID queue.

    Parameters
    ----------
    uuid        : str
      The id of the submission
    filename    : str
      The uploaded filename
    appsIDQueue : str
      The file which contains the ids of the files that were uploaded to APPS
    """
    try:
      self.logger.writeSubsubroutineLog(removeData.format(file = filename),Logs.ROUTINE_STATUS.START)
      self.apps.delete_data(uuid)
      self.logger.writeRegularLog(Logs.SEVERITY.INFO,dataDeletedSuccessful.format(file = filename))
    except DataNotFound:
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,dataNotFound.format(uuid = uuid))
    except InvalidIdentifier:
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,invalidIdentifier.format(uuid = uuid))
    except InvalidOperation:
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,dataDeletedUnsuccessful.format(file = filename))
    except:
      self.logger.writeRegularLog(Logs.SEVERITY.CRITICAL,criticalException.format(uuid = uuid))
    finally:
      self.__removeFromIDQueue(uuid,filename,appsIDQueue)
      self.logger.writeSubsubroutineLog(removeData.format(file = filename),Logs.ROUTINE_STATUS.END)

  def __retrieveData(self,uuid,filename,appsIDQueue,resultsDir):
    """Retrieve results from APPS.

    Parameters
    ----------
    uuid        : str
      The id of the submission
    filename    : str
      The uploaded filename
    appsIDQueue : str
      The file which contains the ids of the files that were uploaded to APPS
    resultsDir  : str
      The directory to which the results should be downloaded to
    """
    try:
      self.logger.writeSubsubroutineLog(retrieveData.format(file = filename),Logs.ROUTINE_STATUS.START)
      self.apps.download_result(uuid = uuid,dr = resultsDir)
      self.logger.writeRegularLog(Logs.SEVERITY.INFO,dataDownloadedSuccessful.format(file = filename))
    except DataNotFound:
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,dataNotFound.format(uuid = uuid))
      self.__removeFromIDQueue(uuid,filename,appsIDQueue)
    except InvalidIdentifier:
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,invalidIdentifier.format(uuid = uuid))
      self.__removeFromIDQueue(uuid,filename,appsIDQueue)
    except InvalidOperation:
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,dataDownloadedUnsuccessful.format(file = filename))
      self.__removeData(uuid,filename,appsIDQueue)
      self.__removeFromIDQueue(uuid,filename,appsIDQueue)
    except:
      self.logger.writeRegularLog(Logs.SEVERITY.CRITICAL,criticalExceptionLog.format(file = filename))
    finally:
      self.logger.writeSubsubroutineLog(retrieveData.format(file = filename),Logs.ROUTINE_STATUS.END)

  def __handleError(self,uuid,filename,appsIDQueue):
    """Handler error from APPS.

    Parameters
    ----------
    uuid        : str
      The id of the submission
    filename    : str
      The uploaded filename
    appsIDQueue : str
      The file which contains the ids of the files that were uploaded to APPS
    """
    self.logger.writeRegularLog(Logs.SEVERITY.ERROR,errorFromAPPS.format(file = filename))
    self.__removeData(uuid,filename,appsIDQueue)

# ✓    unit tested
# ✓ feature tested