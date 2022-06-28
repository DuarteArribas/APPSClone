class Helper:
  """Helper methods to other classes."""
  # == Methods ==
  @staticmethod
  def isValidAbsolutePathToFile(path):
    """Validate an absolute path to a file.

    Parameters
    ----------
    path : str
      The path to validate

    Returns
    ----------
    bool
      True if the absolute path to a file is valid and False otherwise
    """
    if path:
      startWithSlash = True if path[0] == "/" else False
      endWithSlash   = True if path[-1] == "/" else False
      validLength    = all([True if len(file) <= 255 else False for file in path.split("/")]) and len(path) < 4096
      return startWithSlash and not endWithSlash and validLength
    else:
      return False

  @staticmethod
  def isValidAbsolutePathToDir(path):
    """Validate an absolute path to a directory.

    Parameters
    ----------
    path : str
      The path to validate

    Returns
    ----------
    bool
      True if the absolute path to a directory is valid and False otherwise
    """
    if path:
      startWithSlash = True if path[0] == "/" else False
      validLength    = all([True if len(file) <= 255 else False for file in path.split("/")]) and len(path) < 4096
      return startWithSlash and validLength
    else:
      return False

  @staticmethod
  def _removeDuplicatedForwardSlashes(string):
    """Removes duplicated '/' in a string

    Parameters
    ----------
    string : str
      The string to remove the duplicated '/'

    Returns
    ----------
    str
      The string without the duplicated '/'
    """
    formattedString = ""
    for i in range(len(string)):
      if i > 0:
        if formattedString[len(formattedString)-1] == "/":
          if string[i] != "/":
            formattedString += string[i]
        else:
          formattedString += string[i]
      else:
        formattedString += string[i] 
    return formattedString

  @staticmethod
  def isValidIpv4(address):
    """Check if an IPV4 address is valid.

    Parameters
    ----------
    address : str
      The ipv4 address to check

    Returns
    ----------
    bool
      True if the IPV4 address is valid and False otherwise
    """
    try:
      addressBytes      = address.split('.')
      validAddressBytes = [b for b in addressBytes if int(b) >= 0 and int(b) <= 255]
      return len(addressBytes) == 4 and len(validAddressBytes) == 4
    except:
      return False

# ✓    unit tested