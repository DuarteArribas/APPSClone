import configparser
class Config:
  """A config tool, which reads from the given configuration file."""
  # == Methods ==
  def __init__(self,configFile):
    """Set the default configuration of the config reading tool.
    
    Parameters
    ----------
    configFile : str
      The configuration file to read from
    """
    self.config = configparser.RawConfigParser()
    configList  = self.config.read(configFile)
    if len(configList) == 0:
      print("Could not read config file. Exiting...")
      exit(-1)

  def getFilePath(self,filePathKey):
    """Get a config from the FILE_PATHS section on the config file.

    Parameters
    ----------
    filePathKey : str
      The key corresponding to the wanted file path

    Returns
    ----------
    str
      The corresponding file path
    """
    return self.config.get("FILE_PATHS",filePathKey)

  def getLogConfig(self,logKey):
    """Get a config from the LOGS section on the config file.

    Parameters
    ----------
    logKey : str
      The key corresponding to the wanted configuration

    Returns
    ----------
    str
      The corresponding configuration
    """
    return self.config.get("LOGS",logKey)