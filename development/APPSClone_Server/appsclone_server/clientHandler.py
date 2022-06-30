from appsclone_server.connection import *
import os.path

class ClientHandler:
  """Handle clients' operations."""
  def __init__(self,conn):
    """Initalize handler."""
    self.CLIENT_HANDLER_METHOD = {
      1: self.requestFileUpload,
    }
    self.conn = conn

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
    rinexPath = Helper.joinPathFile("in/to_upload_regular",args[0])
    if os.path.exists(rinexPath):
      if os.path.getsize(rinexPath) / (1024 * 1024.0) < self.conn.getQuotaLeft():
        conn.uploadFile(rinexPath,appsIDQueue,APPSCloneServer.DEFAULT_UPLOAD_ARGS)
        os.remove(rinexPath)
        os.remove(rinexPath+".gz")