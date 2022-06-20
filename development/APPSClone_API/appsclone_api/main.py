from utils.config import *
from utils.logs   import *
from fileHandler  import *
from connection   import *

if __name__ == '__main__':
  #read configuration from config file
  appsCloneConfig = Config("config/appsclone.cfg")
  #initialize logs
  logger          = Logs(
    appsCloneConfig.getLogConfig("LOGS_FILE_PATH"),
    appsCloneConfig.getLogConfig("MAX_NUM_LOGS")
  )
  #initialize connection object
  conn = Connection_APPS(
    settingsFile      = appsCloneConfig.getSettingsConfig("APPS_SETTINGS_FILE"),
    downloadDirectory = "out/downloads",
    logger            = logger
  )
  #check for state updates on APPS uploaded files

  #check for new upload files
  FileHandler.downloadRinexFiles(
    appsCloneConfig.getUploadFilesConfig("UPLOAD_FILES_DIR"),
    appsCloneConfig.getUploadFilesConfig("DOWNLOAD_RINEX_DIR"),
    appsCloneConfig.getUploadFilesConfig("RINEX_QUEUE"),
    logger
  )
  #upload files