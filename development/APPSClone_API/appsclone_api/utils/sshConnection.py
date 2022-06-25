import paramiko
from appsclone_api.utils.logs import *
from appsclone_api.constants  import *

class SSHConnection:
  """A client connection via ssh."""
  # == Methods ==
  def __init__(self,ip,port,username,password,logger):
    """Set the initial connection parameters.

    Parameters
    ----------
    ip       : str
      The ip of the server to connect to
    port     : str
      The port of the server to connect to
    username : str
      The username of the user to connect with
    password : str
      The password of the user
    logger   : Logs
      The log object to log to
    """
    self.ip       = ip
    self.port     = int(port)
    self.username = username
    self.password = password
    self.logger   = logger
    self.client   = self.__connectViaSSH()

  def __connectViaSSH(self):
    """Connects to a server via ssh.

    Returns
    ----------
    SSHClient:
      An ssh client object
    """
    self.logger.writeRoutineLog(
      sshConnect.format(ip = self.ip,port = self.port,username = self.username),Logs.ROUTINE_STATUS.START
    )
    try:
      client = paramiko.SSHClient()
      client.load_system_host_keys()
      client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      client.connect(self.ip,self.port,self.username,self.password)
      self.logger.writeRegularLog(Logs.SEVERITY.INFO,sshConnectSuccessful)
      return client
    except paramiko.ssh_exception.BadAuthenticationType:
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,sshConnectUnsuccessfulBadIP.format(ip = self.ip))
      return None
    except paramiko.ssh_exception.NoValidConnectionsError:
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,sshConnectUnsuccessfulBadPort.format(port = self.port))
      return None
    except paramiko.ssh_exception.AuthenticationException:
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,sshConnectUnsuccessfulBadUser.format(username = self.username))
      return None
    except:
      self.logger.writeRegularLog(Logs.SEVERITY.CRITICAL,criticalSSHException)
    finally:
      self.logger.writeRoutineLog(
        sshConnect.format(ip = self.ip,port = self.port,username = self.username),Logs.ROUTINE_STATUS.END
      )
  
  def getFile(self,)