from appsclone_server.connection import *
import os.path

class ClientHandler:
  """Handle clients' operations."""
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
  def __init__(self,conn,toUploadDir,appsIDQueue,idQueue,regularUsersIdQueue):
    """Initalize handler."""
    self.CLIENT_HANDLER_METHOD = {
      1: self.requestFileUpload,
      2: self.requestFileDownload,
    }
    self.conn                = conn
    self.toUploadDir         = toUploadDir
    self.appsIDQueue         = appsIDQueue
    self.idQueue             = idQueue
    self.regularUsersIdQueue = regularUsersIdQueue

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
    """
    rinexPath = Helper.joinPathFile(self.toUploadDir,args[0])
    if os.path.exists(rinexPath):
      if os.path.getsize(rinexPath) / (1024 * 1024.0) < self.conn.getQuotaLeft():
        error = self.conn.uploadFile(rinexPath,self.appsIDQueue,ClientHandler.DEFAULT_UPLOAD_ARGS)
        os.remove(rinexPath)
        os.remove(rinexPath+".gz")
        if error == -1:
          return {"code":-1,"args":(f"Invalid file",)}
        newID = self.__increaseMaxID()
        self.addToRegularUsersQueue(newID)
        return {"code":newID,"args":(f"OK",)}
      else:
        return {"code":-1,"args":(f"There isn't any quota available",)}
    else:
      return {"code":-1,"args":(f"An unknown error happened",)}

  @staticmethod
  def _getNewUploadArgs(args):
    newDict = {}
    for arg in zip(args,ClientHandler.DEFAULT_UPLOAD_ARGS.keys(),ClientHandler.DEFAULT_UPLOAD_ARGS.values()):
      if not arg[0] or not Connection_APPS._isValidArg(arg[1],arg[0]):
        newDict[arg[1]] = arg[2]
      else:
        newDict[arg[1]] = arg[0]
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

  def __addToRegularUsersQueue(self,newID):
    """Add the APPSClone id concatenated with the APPS id to the queue.
    
    Parameters
    ----------
    newID : int
      The APPSClone id of the user to add
    """
    with open(self.regularUsersIdQueue,"a") as f:
      uuid = self.conn.getFileData(error,self.appsIDQueue)["name"]
      f.write(f"{newID} {uuid}\n")

  def requestFileDownload(self,args):
    fileToDownload = ""
    with open("queues/regularUsersIDQueue","r") as f:
      lines = f.readlines()
      for line in lines:
        if line.split(" ")[0] == args[0]:
          fileToDownload = " ".join(line.split(" ")[1:]).split("\n")[0]
    if fileToDownload:
      for result in os.listdir("out/results_regular"):
        if result.split("_results")[0] == fileToDownload:
          newLines = ""
          with open("queues/regularUsersIDQueue","r") as f:
            lines = f.readlines()
            for line in lines:
              if line.split(" ")[0] != args[0]:
                newLines += line
          with open("queues/regularUsersIDQueue","w") as f:
            f.writelines(newLines)
          return {"code":0,"args":(f"Results downloaded successfully",)}
      return {"code":-1,"args":(f"There isn't yet a result for that file",)}
    else:
      return {"code":-1,"args":(f"There isn't any uploaded file with that id!",)}