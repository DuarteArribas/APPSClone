from appsclone_client.utils.argumentParser import *
from appsclone_client.appsCloneClient      import *
from appsclone_client.utils.config         import *
from appsclone_client.utils.logs           import *
import sys

def main():
  # read configuration from config file
  cfg       = Config("config/client.cfg")
  # initialize logs
  logger    = Logs(cfg.getLogConfig("LOGS_FILE"),int(cfg.getLogConfig("MAX_NUM_LOGS")))
  logger.writeNewRunLog("======= RUN ON APPSClone CLIENT =======")
  # initialize arguments
  ap        = ArgumentParser(logger)
  # get command-line arguments
  arguments = ap.getOptions(cfg.getLocalConfig("RINEX_DIR"))
  # if the file doesn't exist, exit; if it exists, proceed to the connection
  if not arguments[0]:
    print("The given option is invalid! Check logs to learn more.")
  else:
    if arguments[0] == "u" and not arguments[1]:
      print("Could not find the given RINEX file! Check logs to learn more.")
    else:
      client = APPSCloneClient(
        cfg.getConnectionConfig("APPS_IP"),
        cfg.getConnectionConfig("APPS_PORT"),
        cfg.getConnectionConfig("USERNAME"),
        cfg.getConnectionConfig("PASSWORD"),
        cfg.getConnectionConfig("TO_UPLOAD_DIR"),
        cfg.getLocalConfig("RINEX_DIR"),
        cfg.getLocalConfig("ID_QUEUE"),
        logger
      )
      client.runClient(arguments)

if __name__ == '__main__':
  main()