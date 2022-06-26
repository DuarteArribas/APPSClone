import appsclone_api
import unittest
from appsclone_api.utils.config import *

class TestConfig(unittest.TestCase):
  def test_get_logs(self):
    c = Config("config/appsclone.cfg")
    self.assertEqual(c.getLogConfig("LOGS_FILE"),"logs/logs.log")

  def test_get_settings(self):
    c = Config("config/appsclone.cfg")
    self.assertEqual(c.getSettingsConfig("APPS_SETTINGS_FILE"),"config/apps_settings")

if __name__ == '__main__':
  unittest.main()