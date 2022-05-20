import gzip
import os
from gdgps_apps           import defines
from gdgps_apps.apps      import APPS
from rinexHeader          import *
from logs                 import *

class Connection_APPS:
  """A connection to APPS, which contains all functions to interact with its API."""
  # == Methods ==
  def __init__(self,settingsFile,downloadDirectory,loggingFile):
    """
    Connects to APPS and initalizes the logger.
    """
    self.apps   = APPS(settings_file = settingsFile,download_directory = downloadDirectory)
    self.logger = Logs(loggingFile)

  def testConnection(self):
    """Test the connection to apps

    Returns
    ----------
    bool
      True if it was able to connect and False otherwise
    """
    return self.apps.ping()[0]

  def uploadFile(self,file,uploadedFiles):
    self.logger.writeLog(
      Logs.SEVERITY.INFO,
      f"Attempting to upload file {file} to APPS."
    )
    header = RinexHeader()
    isCompressed = self.__checkCompressedWithGzip(file)
    if isCompressed:
      uncompressedFile = self.__compressUncompressGzip(file,False)
      header.readMandatoryHeader(uncompressedFile)
      os.remove(uncompressedFile)
    else:
      header.readMandatoryHeader(file)
    isValid,validity = header.isValidHeader()
    if isValid:
      self.logger.writeLog(
        Logs.SEVERITY.INFO,
        f"The file {file} was validated and is being considered a valid file for uploading."
      )
      if not isCompressed:
        self.logger.writeLog(
          Logs.SEVERITY.WARNING,
          f"File {file} was not compressed. Compressing it for uploading..."
        )
        compressedFile = self.__compressUncompressGzip(file,True)
        fileResponseObject = self.apps.upload_gipsyx(compressedFile)
      else:
        fileResponseObject = self.apps.upload_gipsyx(file)
      self.logger.writeLog(
        Logs.SEVERITY.INFO,
        f"Successfuly uploaded file {file} to APPS."
      )
      with open(uploadedFiles,"a") as f:
        f.write(f"{fileResponseObject}\n")
        self.logger.writeLog(
          Logs.SEVERITY.INFO,
          f"Successfuly added file {file} to the uploaded queue."
        )
    else:
      self.logger.writeLog(
        Logs.SEVERITY.ERROR,
        f"The file {file} is invalid - {RinexHeader.validityErrorToString(validity)}"
      )

  def __checkCompressedWithGzip(self,file):
    """Checks if a file was compressed using gzip

    Parameters
    ----------
    file : str
      The file to check

    Returns
    ----------
    bool
      True if the file was compressed using gzip and False otherwise
    """
    with gzip.open(file,'r') as fGzip:
      try:
        fGzip.read(1)
        return True
      except gzip.BadGzipFile:
        return False

  def __compressUncompressGzip(self,file,isCompress):
    """Compress or uncompress a file with gzip.

    Parameters
    ----------
    file       : str
      The file to compress or uncompress
    isCompress : bool
      True to compress and False to uncompress

    Returns
    ----------
    str
      The name of the compressed or uncompressed file
    """
    if isCompress:
      fileToCompress = open(file,"rb")
      compressedFile = gzip.open(f"{file}.gz","wb")
      compressedFile.writelines(fileToCompress)
      return f"{file}.gz"
    else:
      fileToCompress = open(f"{file}Uncompressed","wb")
      compressedFile = gzip.open(file,"rb")
      fileToCompress.write(compressedFile.read())
      return f"{file}Uncompressed"