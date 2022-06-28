from appsclone_api.appsCloneServer import *
from appsclone_api.utils.config    import *
from appsclone_api.utils.logs      import *
from appsclone_api.connection      import *

def main():
  # read configuration from config file
  cfg    = Config("config/appsclone.cfg")
  # initialize logs
  logger = Logs(cfg.getLogConfig("LOGS_FILE"),int(cfg.getLogConfig("MAX_NUM_LOGS")))
  # initialize connection object
  conn   = Connection_APPS(
    settingsFile      = cfg.getSettingsConfig("APPS_SETTINGS_FILE"),
    downloadDirectory = cfg.getOutConfig("RESULTS_DIR"),
    logger            = logger
  )
  # check for state updates (if any) on APPS' uuid(s) of uploaded files (if any) and handle them
  APPSCloneServer.handleAllFileStates(conn,cfg.getQueuesConfig("APPS_IDS"),cfg.getOutConfig("RESULTS_DIR"),logger)
  # upload results (if any) to the respective upload directory
  APPSCloneServer.uploadBackResults(cfg.getQueuesConfig("RINEX"),cfg.getOutConfig("RESULTS_DIR"),logger)
  # check for new upload files (if any)
  APPSCloneServer.downloadRinexFiles(
    cfg.getInConfig("TO_DOWNLOAD_DIR"),
    cfg.getInConfig("TO_UPLOAD_DIR"),
    cfg.getQueuesConfig("RINEX"),
    logger
  )
  # upload files to apps (if any)
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
    "generate_quaternions" : False
  }
  APPSCloneServer.uploadAllRinexToApps(conn,cfg.getInConfig("TO_UPLOAD_DIR"),cfg.getQueuesConfig("APPS_IDS"),args,logger)

if __name__ == '__main__':
  main()