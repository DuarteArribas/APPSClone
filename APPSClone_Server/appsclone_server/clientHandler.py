from appsclone_server.connection import *
import os.path

class ClientHandler:
  """Handle clients' operations.
  
  Attributes
  ----------
  DEFAULT_UPLOAD_ARGS : dict
    Default upload arguments of APPS
  """
  DEFAULT_UPLOAD_ARGS = {
    "processing_mode"    : defines.GIPSYData.PROCESSING_MODE_DEFAULT,
    "product"            : defines.GIPSYData.PRODUCT_DEFAULT,
    "troposphere_model"  : defines.GIPSYData.TROP_GMF,
    "ocean_loading"      : True,
    "model_tides"        : True,
    "elev_dep_weighting" : defines.GIPSYData.ROOT_SINE,
    "elev_angle_cutoff"  : 7.5,
    "solution_period"    : 300
  }
  def __init__(self,conn,toUploadDir,appsIDQueue,idQueue,regularUsersIdQueue,resultsRegular):
    """Initalize handler.

    Parameters
    ----------
    conn                : Connection_APPS
      A connection to APPS object
    toUploadDir         : str
      The directory to upload to
    appsIDQueue         : str
      The queue of APPS ids
    idQueue             : str
      The queue of APPSClone ids
    regularUsersIdQueue : str
      The regular users id queue
    resultsRegular      : str
      The regular results directory
    """
    self.CLIENT_HANDLER_METHOD = {
      1: self.requestFileUpload,
      2: self.requestFileDownload,
    }
    self.conn                = conn
    self.toUploadDir         = toUploadDir
    self.appsIDQueue         = appsIDQueue
    self.idQueue             = idQueue
    self.regularUsersIdQueue = regularUsersIdQueue
    self.resultsRegular      = resultsRegular

  def process(self,option,args = None):
    """Process an option received by the client and call the appropriate client handler method.
    
    Parameters
    ----------
    option : int
      The chosen menu option
    args   : tuple
      The arguments sent by the client

    Return
    ----------
    dict
      The code to be treated by the client and the respective arguments
    """
    if args == None:
      return self.CLIENT_HANDLER_METHOD[option]()
    else:
      return self.CLIENT_HANDLER_METHOD[option](args)
  
  def requestFileUpload(self,args):
    """Called by the client to request a file upload.
    
    Parameters
    ----------
    args : list
      The list of upload arguments, where args[0] is the name of the file

    Returns
    ----------
    dict
      The code is either the new APPSClone id or -1 in case of error. The args defines the error that happened
    """
    rinexPath = Helper.joinPathFile(self.toUploadDir,args[0])
    if os.path.exists(rinexPath):
      if os.path.getsize(rinexPath) / (1024 * 1024.0) < self.conn.getQuotaLeft():
        error = self.conn.uploadFile(rinexPath,self.appsIDQueue,ClientHandler._getNewUploadArgs(args[1:]))
        os.remove(rinexPath)
        os.remove(rinexPath+".gz")
        if error == -1:
          return {"code":-1,"args":(f"Invalid file",)}
        newID = self.__increaseMaxID()
        self.__addToRegularUsersQueue(newID,error)
        return {"code":newID,"args":(f"OK",)}
      else:
        return {"code":-1,"args":(f"There isn't any quota available",)}
    else:
      return {"code":-1,"args":(f"An unknown error happened",)}

  @staticmethod
  def _getNewUploadArgs(args):
    """Transform the argument into correct ones.
    
    Parameters
    ----------
    args : list
      The list of upload arguments

    Returns
    ----------
    dict
      The corrected upload arguments
    """
    newDict = {}
    newDict["pressure"] = ""
    newDict["attitude"] = ""
    newDict["email"]    = ""
    newDict["access"]   = ""
    for arg in zip(args,ClientHandler.DEFAULT_UPLOAD_ARGS.keys(),ClientHandler.DEFAULT_UPLOAD_ARGS.values()):
      if arg[0] == None or not Connection_APPS._isValidArg(arg[1],arg[0]):
        newDict[arg[1]] = arg[2]
      else:
        newDict[arg[1]] = arg[0]
    newDict["generate_quaternions"] = ""
    return newDict

  def __increaseMaxID(self):
    """Increase the max id of APPSClone by one.
    
    Return
    ----------
    int
      The next max id
    """
    newID = 0
    with open(self.idQueue,"r") as f:
      lines = f.readlines()
      if len(lines) < 1:
        newID = 1
      else:
        newID = int(lines[0]) + 1
    with open(self.idQueue,"w") as f:
      f.write(f"{newID}")
    return newID

  def __addToRegularUsersQueue(self,newID,uuid):
    """Add the APPSClone id concatenated with the APPS id to the queue.
    
    Parameters
    ----------
    newID : int
      The APPSClone id of the user to add
    uuid  : string
      The id of the submission to APPS
    """
    with open(self.regularUsersIdQueue,"a") as f:
      uuid = self.conn.getFileData(uuid,self.appsIDQueue)["name"]
      f.write(f"{newID} {uuid}\n")

  def requestFileDownload(self,args):
    """Called by the client to request a file download.
    
    Parameters
    ----------
    args : list
      args[0] is the name of the file

    Returns
    ----------
    dict
      The code is either 0 on success or -1 in case of error. The args defines the error that happened
    """
    fileToDownload = ""
    with open(self.regularUsersIdQueue,"r") as f:
      lines = f.readlines()
      for line in lines:
        if line.split(" ")[0] == args[0]:
          fileToDownload = " ".join(line.split(" ")[1:]).split("\n")[0]
    if fileToDownload:
      for result in os.listdir(self.resultsRegular):
        if result.split("_results")[0] == fileToDownload:
          newLines = ""
          with open(self.regularUsersIdQueue,"r") as f:
            lines = f.readlines()
            for line in lines:
              if line.split(" ")[0] != args[0]:
                newLines += line
          with open(self.regularUsersIdQueue,"w") as f:
            f.writelines(newLines)
          return {"code":result,"args":(f"Results downloaded successfully",)}
      return {"code":-1,"args":(f"There isn't yet a result for that file",)}
    else:
      return {"code":-1,"args":(f"There isn't any uploaded file with that id!",)}