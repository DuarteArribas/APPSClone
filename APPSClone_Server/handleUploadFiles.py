from appsclone_server.appsCloneSpecialServer import *
from appsclone_server.utils.config           import *
from appsclone_server.utils.logs             import *
from appsclone_server.connection             import *

def main():
  # read configuration from config file
  cfg    = Config("config/appsclone.cfg")
  # initialize logs
  logger = Logs(cfg.getLogConfig("LOGS_FILE"),int(cfg.getLogConfig("MAX_NUM_LOGS")))
  logger.writeNewRunLog("======= RUN ON APPSClone SERVER TO HANDLE UPLOAD FILES =======")
  # initialize connection object
  conn   = Connection_APPS(
    settingsFile      = cfg.getSettingsConfig("APPS_SETTINGS_FILE"),
    downloadDirectory = cfg.getOutConfig("RESULTS_DIR"),
    logger            = logger
  )
  # check for state updates (if any) on APPS' uuid(s) of uploaded files (if any) and handle them
  APPSCloneSpecialServer.handleAllFileStates(
    conn,
    cfg.getQueuesConfig("APPS_IDS"),
    cfg.getOutConfig("RESULTS_DIR"),
    cfg.getOutConfig("RESULTS_REGULAR_DIR"),
    cfg.getQueuesConfig("RINEX"),
    logger
  )
  # upload results (if any) to the respective upload directory
  APPSCloneSpecialServer.uploadBackResults(cfg.getQueuesConfig("RINEX"),cfg.getOutConfig("RESULTS_DIR"),logger)
  # check for new upload files (if any)
  APPSCloneSpecialServer.downloadRinexFiles(
    cfg.getInConfig("TO_DOWNLOAD_DIR"),
    cfg.getInConfig("TO_UPLOAD_DIR"),
    cfg.getQueuesConfig("RINEX"),
    logger
  )
  # upload files (if any) to APPS
  APPSCloneSpecialServer.uploadAllRinexToApps(conn,cfg.getInConfig("TO_UPLOAD_DIR"),cfg.getQueuesConfig("APPS_IDS"),logger)

if __name__ == '__main__':
  main()