import appsclone_client
import unittest
from appsclone_client.utils.argumentParser import *
from appsclone_client.utils.config         import *

class TestArgumentParser(unittest.TestCase):
  def testGetOptions(self):
    # read configuration from config file
    cfg       = Config("config/client.cfg")
    # initialize logs
    logger    = Logs(cfg.getLogConfig("LOGS_FILE"),int(cfg.getLogConfig("MAX_NUM_LOGS")))
    ap        = ArgumentParser(logger)
    arguments = ap.getOptions(cfg.getLocalConfig("RINEX_DIR"))
    print(arguments)

if __name__ == '__main__':
  unittest.main()