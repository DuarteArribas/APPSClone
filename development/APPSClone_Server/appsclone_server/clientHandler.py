class ClientHandler:
  """Handle clients' operations."""
  def __init__(self,serverObject):
    """Initalize handler."""
    self.CLIENT_HANDLER_METHOD = {
      0: self.exitProgram,
      1: self.loginUser,
      2: self.registerUser,
      3: self.generateTickets,
      4: self.sendUserData,
      5: self.updateUserMoney
    }

  def process(self,option,args = None):
    """Process an option received by the client and calls the appropriate client handler method.
    
    Parameters
    ----------
    option : int
      The chosen menu option
    args   : tuple (default: None)
      The arguments sent by the client

    Return
    ----------
    dict
      A dictionary containing the code to be treated by the client and the respective arguments
    """
    if args == None:
      return self.CLIENT_HANDLER_METHOD[option]()
    else:
      return self.CLIENT_HANDLER_METHOD[option](args)
  
  def updateUserMoney(self, args):
    self.database.updateUserMoney(args[0],args[1])
    print(f"Money info updated for user:{args[0]} money:{args[1]}")
    return {"code":-1,"args":("Money updated!",)}