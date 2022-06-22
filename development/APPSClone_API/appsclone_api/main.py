from utils.config import *
from utils.logs   import *
from fileHandler  import *
from connection   import *

if __name__ == '__main__':
  #read configuration from config file
  appsCloneConfig = Config("config/appsclone.cfg")
  #initialize logs
  logger          = Logs(
    "logs/logTest.log",
    int(appsCloneConfig.getLogConfig("MAX_NUM_LOGS"))
  )
  #initialize connection object
  conn            = Connection_APPS(
    settingsFile      = "config/apps_settings",
    downloadDirectory = "out/downloads",
    logger            = logger
  )
  #check for state updates (if any) on APPS uploaded files (if any) and handle them
  FileHandler.handleQueueFilesStates(
    conn,
    "out/queue/queue",
    "out/downloads"
  )
  #upload results (if any) to the respective upload directory
  FileHandler.uploadBackResults(
    "out/queue/uploadFilesQueue",
    "out/downloads",
    logger
  )
  #check for new upload files (if any)
  FileHandler.downloadRinexFiles(
    "in/uploadFilesTest/1",
    "out/downloads_test",
    "out/queue/uploadFilesQueue",
    logger
  )
  #upload files to apps (if any)
  args = {
    "pressure"             : None,
    "attitude"             : None,
    "email"                : defines.Data.EMAIL_NOTIFY_DEFAULT,
    "access"               : defines.Data.ACCESS_DEFAULT,
    "processing_mode"      : defines.GIPSYData.PROCESSING_MODE_DEFAULT,
    "product"              : "arroz",
    "troposphere_model"    : defines.GIPSYData.TROP_GMF,
    "ocean_loading"        : True,
    "model_tides"          : True,
    "elev_dep_weighting"   : defines.GIPSYData.ROOT_SINE,
    "elev_angle_cutoff"    : 7.5,
    "solution_period"      : 300,
    "generate_quaternions" : False,
  }
  FileHandler.uploadAllRinexToApps(
    conn,
    "out/downloads_test",
    "out/queue/queue",
    args,
    logger
  )