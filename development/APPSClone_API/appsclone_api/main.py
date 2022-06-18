from utils.config import *
from utils.logs   import *

if __name__ == '__main__':
  appsCloneConfig = Config("config/appsclone.cfg")
  logger          = Logs(
    appsCloneConfig.getLogConfig("LOGS_FILE_PATH"),
    appsCloneConfig.getLogConfig("MAX_NUM_LOGS")
  )