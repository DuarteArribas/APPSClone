import appsclone_api
import unittest
from appsclone_api.utils.config import *

class TestConfig(unittest.TestCase):
  def test_get_filePath(self):
    c = Config("config/appsclone.cfg")
    print(c.getLogConfig("LOGS_FILE_PATH"))

if __name__ == '__main__':
  unittest.main()