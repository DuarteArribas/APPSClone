from appsclone_client.utils.argumentParser import *
from appsclone_client.appsCloneClient      import *
from appsclone_client.utils.config         import *
import sys

def main():
  # read configuration from config file
  cfg       = Config("config/client.cfg")
  # initialize arguments
  ap        = ArgumentParser()
  # get command-line arguments
  arguments = ap.getOptions(cfg.getLocalConfig("RINEX_DIR"))
  # if the file doesn't exist, exit; if it exists, proceed to the connection
  if not arguments[0]:
    print("The given option is invalid")
  else:
    if not arguments[1]:
      print("Could not find the given RINEX file")
    else:
      client = APPSCloneClient(
        cfg.getConnectionConfig("APPS_IP"),
        cfg.getConnectionConfig("APPS_PORT"),
        cfg.getConnectionConfig("USERNAME"),
        cfg.getConnectionConfig("PASSWORD"),
        cfg.getConnectionConfig("TO_UPLOAD_DIR"),
        cfg.getLocalConfig("RINEX_DIR")
      )
      client.runClient(arguments)

if __name__ == '__main__':
  main()