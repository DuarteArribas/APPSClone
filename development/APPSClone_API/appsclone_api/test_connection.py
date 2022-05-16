import unittest
from connection import *

class TestConnection(unittest.TestCase):
  def test_connection_ok(self):
    conn=Connection_APPS(settingsFile="config/apps_settings",downloadDirectory="out/downloads")
    self.assertTrue(conn.testConnection())

if __name__ == '__main__':
  unittest.main()
