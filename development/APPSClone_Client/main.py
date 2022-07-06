from appsclone_client.appsCloneClient import *
from appsclone_client.argumentParser  import *
from appsclone_client.utils.config    import *
import sys

def main():
  # read configuration from config file
  cfg = Config("config/client.cfg")
  ap  = ArgumentParser()
  print(ap.getOptions())
  #client = APPSCloneClient("localhost",12346,"arroz","massa","toUploadDir","rinexDir","rr1")
  #client.runClient(1,None)


if __name__ == '__main__':
  main()