import unittest
from connection import *

class TestConnection(unittest.TestCase):
  def test_connection_ok(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn.testConnection())

  def test_gzip(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__checkCompressedWithGzip("in/test/file.gz"))

  def test_gzip2(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__checkCompressedWithGzip("in/test/file"))

  def test_gzip_compression(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertEqual(conn._Connection_APPS__compressUncompressGzip("in/test/arroz",True),"in/test/arroz.gz")

  def test_gzip_uncompression(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertEqual(conn._Connection_APPS__compressUncompressGzip("in/test/massa.gz",False),"in/test/massa.gzUncompressed")

  def test_upload_file(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    conn.uploadFile("in/uploads_test/fileTest","out/queue/queue")

if __name__ == '__main__':
  unittest.main()
