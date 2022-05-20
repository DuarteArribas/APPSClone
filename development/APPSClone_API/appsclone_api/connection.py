from gdgps_apps           import defines
from gdgps_apps.apps      import APPS
from rinexHeader          import *
from logs                 import *

class Connection_APPS:
  def __init__(self,settingsFile,downloadDirectory,loggingFile):
    self.apps = APPS(settings_file = settingsFile,download_directory = downloadDirectory)

  def testConnection(self):
    logging.info()
    return self.apps.ping()[0]

  def uploadFile(self,file):
    header = RinexHeader()
    header.readMandatoryHeader(file)
    if header.isValidHeader()[0]:
      if self.apps.testConnection():
        fileResponseObject = self.apps.upload_gipsyx(file)
        with open("")
      else:
        pass
    else:
      pass





