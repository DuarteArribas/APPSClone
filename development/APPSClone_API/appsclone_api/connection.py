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

  def uploadFile(self,file):
    self.logger.writeLog(Logs.SEVERITY.INFO,f"Attempting to upload file {file} to APPS.")
    header = RinexHeader()
    header.readMandatoryHeader(file)
    isValid,validity = header.isValidHeader()
    if [0]:
      self.logger.writeLog(Logs.SEVERITY.INFO,"The file {file} was validated and is being considered a valid file for uploading.")
      if self.apps.testConnection():
        self.logger.writeLog(Logs.SEVERITY.INFO,"A connection to apps was established.")
        fileResponseObject = self.apps.upload_gipsyx(file)
        with open("")
      else:
        self.logger.writeLog(Logs.SEVERITY.ERROR,"A connection to APPS could not be established.")
    else:
      self.logger.writeLog(Logs.SEVERITY.ERROR,"The file {file} is invalid")





