from utils.config import *
from utils.logs   import *
from fileHandler  import *

if __name__ == '__main__':
  #read configuration from config file
  appsCloneConfig = Config("config/appsclone.cfg")
  #initialize logs
  logger          = Logs(
    appsCloneConfig.getLogConfig("LOGS_FILE_PATH"),
    appsCloneConfig.getLogConfig("MAX_NUM_LOGS")
  )
  #check for state updates on APPS uploaded files

  #check for new upload files

  #upload files
  FileHandler.downloadRinexFiles()