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
  conn            = Connection_APPS(
    settingsFile      = appsCloneConfig.getSettingsConfig("APPS_SETTINGS_FILE"),
    downloadDirectory = appsCloneConfig.getAPPSUploadFilesConfig("RESULTS_DIR"),
    logger            = logger
  )
  #check for state updates (if any) on APPS uploaded files (if any) and handle them
  FileHandler.handleQueueFilesStates(
    conn,
    appsCloneConfig.getAPPSUploadFilesConfig("UPLOADED_FILES_QUEUE"),
    appsCloneConfig.getAPPSUploadFilesConfig("RESULTS_DIR")
  )
  #upload results (if any) to the respective upload directory
  FileHandler.uploadBackResults(
    appsCloneConfig.getUploadFilesConfig("RINEX_QUEUE"),
    appsCloneConfig.getAPPSUploadFilesConfig("RESULTS_DIR"),
    logger
  )
  #check for new upload files (if any)
  FileHandler.downloadRinexFiles(
    appsCloneConfig.getUploadFilesConfig("UPLOAD_FILES_DIR"),
    appsCloneConfig.getUploadFilesConfig("DOWNLOAD_RINEX_DIR"),
    appsCloneConfig.getUploadFilesConfig("RINEX_QUEUE"),
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
    appsCloneConfig.getUploadFilesConfig("DOWNLOAD_RINEX_DIR"),
    appsCloneConfig.getAPPSUploadFilesConfig("UPLOADED_FILES_QUEUE"),
    args,
    logger
  )