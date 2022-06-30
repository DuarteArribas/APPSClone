import socket
import pickle
from appsclone_server.clientHandler import *
from appsclone_server.utils.logs    import *
from appsclone_server.constants     import *
from _thread                        import *

class APPSCloneServer:
  """The APPSClone server for regular users, who wish to manually upload and retrieve to and from APPS.
  
  Attributes
  ----------
  MAX_TRIES               : int
    The maximum tries a client can fail to connect
  NUMBER_BYTES_TO_RECEIVE : int
    The max number of bytes to receive
  """
  # == Attributes ==
  MAX_TRIES               = 5
  NUMBER_BYTES_TO_RECEIVE = 16384
  DEFAULT_UPLOAD_ARGS = {
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
    "generate_quaternions" : False
  }
  # == Methods ==
  def __init__(self,ip,port):
    """Server initialization.
    
    Parameters
    ----------
    ip   : int
      The ip of the server
    port : int
      The port to open the server on
    """
    self.ip            = ip
    self.port          = int(port)
    self.clientHandler = ClientHandler()

  def runServer(self):
    """Run the server."""
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
      s.bind((self.ip,self.port))
      s.listen(APPSCloneServer.MAX_TRIES)
      while True:
        client,clientAddress   = s.accept()
        start_new_thread(self.clientThread,(client,))

  def clientThread(self,client):
    """Thread to handle the clients' operations.

    Parameters
    ----------
    client : socketObject
      The client to handle
    """
    while True: 
      try:
        #receive data from client
        opt_args = pickle.loads(client.recv(APPSCloneServer.NUMBER_BYTES_TO_RECEIVE))
        #process client data
        response = self.clientHandler.process(opt_args.option,opt_args.args)
        #send data back to client
        client.send(pickle.dumps(response))
      except (ConnectionResetError,EOFError): #handle client disconnection gracefully
        pass