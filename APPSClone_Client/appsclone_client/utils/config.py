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

  def getConnectionConfig(self,key):
    """Get a config from the CONNECTION section on the config file.

    Parameters
    ----------
    key : str
      The key corresponding to the wanted configuration

    Returns
    ----------
    str
      The corresponding configuration
    """
    return self.config.get("CONNECTION",key)

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

  def getLocalConfig(self,key):
    """Get a config from the LOCAL section on the config file.

    Parameters
    ----------
    key : str
      The key corresponding to the wanted configuration

    Returns
    ----------
    str
      The corresponding configuration
    """
    return self.config.get("LOCAL",key)

# ✓    unit tested
# ✓ feature tested