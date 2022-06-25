import gzip
import os

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

  @staticmethod
  def getUncompressedFile(filePath):
    """Uncompress and delete original file with gzip.

    Parameters
    ----------
    filePath : str
      The path of the file

    Returns
    ----------
    str
      The name of the uncompressed file or the given file if the file was already uncompressed
    """
    isCompressed = Helper._checkCompressedWithGzip(filePath)
    if isCompressed:
      uncompressedFile = Helper.compressUncompressGzip(filePath,False)
      os.remove(filePath)
      return uncompressedFile
    else:
      return filePath

  @staticmethod
  def _checkCompressedWithGzip(filePath):
    """Check if a file is compressed with gzip.

    Parameters
    ----------
    filePath : str
      The path of the file

    Returns
    ----------
    bool
      True if the file was compressed using gzip and False otherwise
    """
    with gzip.open(filePath,'r') as fGzip:
      try:
        fGzip.read(1)
        return True
      except gzip.BadGzipFile:
        return False

  @staticmethod
  def compressUncompressGzip(filePath,isCompress):
    """Compress or uncompress a file with gzip.

    Parameters
    ----------
    filePath   : str
      The path of the file
    isCompress : bool
      True to compress and False to uncompress

    Returns
    ----------
    str
      The name of the compressed or uncompressed file
    """
    if isCompress:
      fileToCompress = open(filePath,"rb")
      compressedFile = gzip.open(f"{filePath}.gz","wb")
      compressedFile.writelines(fileToCompress)
      fileToCompress.close()
      return f"{filePath}.gz"
    else:
      filenameNoExtension  = filePath.split(".")
      filenameNoExtension.pop()
      uncompressedFilename = "".join(filenameNoExtension)
      fileToCompress       = open(uncompressedFilename,"wb")
      compressedFile       = gzip.open(filePath,"rb")
      fileToCompress.write(compressedFile.read())
      fileToCompress.close()
      return uncompressedFilename

  @staticmethod
  def cleanEmptyFieldsInList(lst):
    """Clean the empty (stripped) fields in a list.

    Parameters
    ----------
    lst : list
      The list to cleanup

    Returns
    ----------
    list
      The list without any empty (stripped) fields
    """
    return [item for item in lst if item.strip()]

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
# ✓ feature tested