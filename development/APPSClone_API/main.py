from appsclone_api.appsCloneServer import *
from appsclone_api.utils.config    import *
from appsclone_api.utils.logs      import *
from appsclone_api.connection      import *

def main():
  # read configuration from config file
  cfg    = Config("config/appsclone.cfg")
  # initialize logs
  logger = Logs(
    cfg.getLogConfig("LOGS_FILE"),
    int(cfg.getLogConfig("MAX_NUM_LOGS"))
  )
  #initialize connection object
  conn   = Connection_APPS(
    settingsFile      = cfg.getSettingsConfig("APPS_SETTINGS_FILE"),
    downloadDirectory = cfg.getSettingsConfig("APPS_SETTINGS_FILE"),
    logger            = logger
  )
  # #check for state updates (if any) on APPS uploaded files (if any) and handle them
  # FileHandler.handleQueueFilesStates(
  #   conn,
  #   "out/queue/queue",
  #   "out/downloads"
  # )
  # #upload results (if any) to the respective upload directory
  # FileHandler.uploadBackResults(
  #   "out/queue/uploadFilesQueue",
  #   "out/downloads",
  #   logger
  # )
  # #check for new upload files (if any)
  # FileHandler.downloadRinexFiles(
  #   "in/uploadFilesTest/1",
  #   "out/downloads_test",
  #   "out/queue/uploadFilesQueue",
  #   logger
  # )
  # #upload files to apps (if any)
  # args = {
  #   "pressure"             : None,
  #   "attitude"             : None,
  #   "email"                : defines.Data.EMAIL_NOTIFY_DEFAULT,
  #   "access"               : defines.Data.ACCESS_DEFAULT,
  #   "processing_mode"      : defines.GIPSYData.PROCESSING_MODE_DEFAULT,
  #   "product"              : "arroz",
  #   "troposphere_model"    : defines.GIPSYData.TROP_GMF,
  #   "ocean_loading"        : True,
  #   "model_tides"          : True,
  #   "elev_dep_weighting"   : defines.GIPSYData.ROOT_SINE,
  #   "elev_angle_cutoff"    : 7.5,
  #   "solution_period"      : 300,
  #   "generate_quaternions" : False,
  # }
  # FileHandler.uploadAllRinexToApps(
  #   conn,
  #   "out/downloads_test",
  #   "out/queue/queue",
  #   args,
  #   logger
  # )

if __name__ == '__main__':
  main()