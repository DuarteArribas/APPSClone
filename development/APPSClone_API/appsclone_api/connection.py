from gdgps_apps      import defines
from gdgps_apps.apps import APPS

class Connection_APPS:
  def __init__(self,settingsFile,downloadDirectory):
    self.apps=APPS(settings_file=settingsFile,download_directory=downloadDirectory)

  def testConnection(self):
    return self.apps.ping()[0]
