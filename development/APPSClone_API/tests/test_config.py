import unittest
import appsclone_api
from appsclone_api.utils.config import *

class TestConfig(unittest.TestCase):
  def test_get_filePath(self):
    c = Config("config/appsclone.cfg")
    print(c.getFilePath("UPLOAD_INFO"))

if __name__ == '__main__':
  unittest.main()