import gzip
from gdgps_apps           import defines
from gdgps_apps.apps      import APPS
from rinexHeader          import *
from logs                 import *

class Connection_APPS:
  def __init__(self,settingsFile,downloadDirectory,loggingFile):
    self.apps   = APPS(settings_file = settingsFile,download_directory = downloadDirectory)
    self.logger = Logs(loggingFile)

  def testConnection(self):
    return self.apps.ping()[0]

  def uploadFile(self,file,uploadedFiles):
    self.logger.writeLog(
      Logs.SEVERITY.INFO,
      f"Attempting to upload file {file} to APPS."
    )
    header = RinexHeader()
    if self.__checkCompressedWithGzip(file):
      pass
    else:
      header.readMandatoryHeader(file)
    
    isValid,validity = header.isValidHeader()
    if isValid:
      self.logger.writeLog(
        Logs.SEVERITY.INFO,
        f"The file {file} was validated and is being considered a valid file for uploading."
      )
      fileResponseObject = self.apps.upload_gipsyx(file)
      with open(uploadedFiles,"a") as f:
        f.write(f"{fileResponseObject}\n")
    else:
      self.logger.writeLog(
        Logs.SEVERITY.ERROR,
        f"The file {file} is invalid - {RinexHeader.validityErrorToString(validity)}"
      )

  def __checkCompressedWithGzip(self,file):
    with gzip.open(file,'r') as fGzip:
      try:
        fGzip.read(1)
        return True
      except gzip.BadGzipFile:
        return False

  def __compressUncompressGzip(self,file,isCompress):
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