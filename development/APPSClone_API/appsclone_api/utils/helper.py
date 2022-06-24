class Helper:
  """Helper methods to other classes."""
  # == Methods ==
  @staticmethod
  def joinPathFile(path,file):
    """Concatenate a file to a filepath, separating them by /

    Parameters
    ----------
    path : str
      The path to concatenate the file to
    file : str
      The file to concatenate to the file path

    Returns
    ----------
    str
      The file path, with the file included
    """
    if path == "":
      return Helper._removeDuplicatedForwardSlashes(file)
    else:
      return Helper._removeDuplicatedForwardSlashes(path+"/"+file)

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
  def getFileFromPath(path):
    """Get a file, given its path.

    Parameters
    ----------
    path : str
      The path to gather the file from

    Returns
    ----------
    str
      The file from the file path
    """
    return path.split("/")[-1]

  @staticmethod
  def bytesToMB(by):
    """Convert bytes to mebibytes.
    
    Parameters
    ----------
    by : int
      The value in bytes to convert

    Returns
    ----------
    int
      The given value in mebibytes with five decimal places
    """
    return round(by / 1.049e+6,3)