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

# ✓    unit tested
# ✓ feature tested