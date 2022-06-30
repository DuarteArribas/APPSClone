import appsclone_server
import unittest
from appsclone_server.utils.config import *

class TestConfig(unittest.TestCase):
  def test_get_logs(self):
    c = Config("config/appsclone.cfg")
    self.assertEqual(c.getLogConfig("LOGS_FILE"),"logs/logs.log")

  def test_get_settings(self):
    c = Config("config/appsclone.cfg")
    self.assertEqual(c.getSettingsConfig("APPS_SETTINGS_FILE"),"config/apps_settings")

  def test_get_in(self):
    c = Config("config/appsclone.cfg")
    self.assertEqual(c.getInConfig("TO_UPLOAD_DIR"),"in/to_upload")

  def test_get_out(self):
    c = Config("config/appsclone.cfg")
    self.assertEqual(c.getOutConfig("RESULTS_DIR"),"out/results")

  def test_get_queues(self):
    c = Config("config/appsclone.cfg")
    self.assertEqual(c.getQueuesConfig("APPS_IDS"),"queues/apps_id_queue")

  def test_get_ip(self):
    c = Config("config/appsclone.cfg")
    self.assertEqual(c.getServerConfig("IP"),"localhost")

if __name__ == '__main__':
  unittest.main()