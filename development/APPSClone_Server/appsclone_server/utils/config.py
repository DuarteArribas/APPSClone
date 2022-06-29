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

  def getInConfig(self,key):
    """Get a config from the IN section on the config file.

    Parameters
    ----------
    key : str
      The key corresponding to the wanted configuration

    Returns
    ----------
    str
      The corresponding configuration
    """
    return self.config.get("IN",key)

  def getOutConfig(self,key):
    """Get a config from the OUT section on the config file.

    Parameters
    ----------
    key : str
      The key corresponding to the wanted configuration

    Returns
    ----------
    str
      The corresponding configuration
    """
    return self.config.get("OUT",key)

  def getQueuesConfig(self,key):
    """Get a config from the QUEUES section on the config file.

    Parameters
    ----------
    key : str
      The key corresponding to the wanted configuration

    Returns
    ----------
    str
      The corresponding configuration
    """
    return self.config.get("QUEUES",key)

# ✓    unit tested
# ✓ feature tested