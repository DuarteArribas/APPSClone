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

  def getLogConfig(self,key):
    """Get a config from the LOGS section on the config file.

    Parameters
    ----------
    key : str
      The key corresponding to the wanted configuration

    Returns
    ----------
    str
      The corresponding configuration
    """
    return self.config.get("LOGS",key)

  def getUploadFilesConfig(self,key):
    """Get a config from the UPLOAD_FILES section on the config file.

    Parameters
    ----------
    key : str
      The key corresponding to the wanted configuration

    Returns
    ----------
    str
      The corresponding configuration
    """
    return self.config.get("UPLOAD_FILES",key)

  def getAPPSUploadFilesConfig(self,key):
    """Get a config from the APPS_UPLOAD_FILES section on the config file.

    Parameters
    ----------
    key : str
      The key corresponding to the wanted configuration

    Returns
    ----------
    str
      The corresponding configuration
    """
    return self.config.get("APPS_UPLOAD_FILES",key)

  def getSettingsConfig(self,key):
    """Get a config from the SETTINGS section on the config file.

    Parameters
    ----------
    key : str
      The key corresponding to the wanted configuration

    Returns
    ----------
    str
      The corresponding configuration
    """
    return self.config.get("SETTINGS",key)

# ✓    unit tested