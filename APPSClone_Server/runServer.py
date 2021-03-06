from appsclone_server.appsCloneServer import *
from appsclone_server.utils.config    import *
from appsclone_server.utils.logs      import *
from appsclone_server.connection      import *

def main():
  # read configuration from config file
  cfg    = Config("config/appsclone.cfg")
  # initialize logs
  logger = Logs(cfg.getLogConfig("LOGS_FILE_SERVER"),int(cfg.getLogConfig("MAX_NUM_LOGS")))
  logger.writeNewRunLog("======= RUN ON APPSClone SERVER =======")
  # initialize connection object
  conn   = Connection_APPS(
    settingsFile      = cfg.getSettingsConfig("APPS_SETTINGS_FILE"),
    downloadDirectory = cfg.getOutConfig("RESULTS_DIR"),
    logger            = logger
  )
  # run server
  server = APPSCloneServer(
    cfg.getServerConfig("IP"),
    cfg.getServerConfig("PORT"),
    conn,
    cfg.getInConfig("TO_UPLOAD_REGULAR_DIR"),
    cfg.getQueuesConfig("APPS_IDS"),
    cfg.getQueuesConfig("APPSCLONE_IDS"),
    cfg.getQueuesConfig("REGULAR_USERS"),
    cfg.getOutConfig("RESULTS_REGULAR_DIR")
  )
  server.runServer()

if __name__ == '__main__':
  main()