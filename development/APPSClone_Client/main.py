from appsclone_client.appsCloneClient import *
from appsclone_client.argumentParser  import *
from appsclone_client.utils.config    import *
import sys

def main():
  # read configuration from config file
  cfg = Config("config/client.cfg")
  ap  = ArgumentParser()
  arguments = ap.getOptions()
  if not arguments[0]:
    print("The rinex file doesn't exist!")
  else:
    client = APPSCloneClient("localhost",12346,"arroz","massa","toUploadDir","rinexDir","rr1")
    client.runClient(1,None)


if __name__ == '__main__':
  main()