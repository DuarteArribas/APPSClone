import unittest
from connection import *

class TestConnection(unittest.TestCase):
  # def test_connection_ok(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   self.assertTrue(conn.testConnection())

  # def test_gzip(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   self.assertTrue(conn._Connection_APPS__checkCompressedWithGzip("in/test/file.gz"))

  # def test_gzip2(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   self.assertFalse(conn._Connection_APPS__checkCompressedWithGzip("in/test/file"))

  # def test_getUncompressedFile(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   print(conn._Connection_APPS__getUncompressedFile("in/test/arroz.gz"))
  #   #self.assertFalse()

  # def test_gzip_compression(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   self.assertEqual(conn._Connection_APPS__compressUncompressGzip("in/test/arroz",True),"in/test/arroz.gz")

  # def test_gzip_uncompression(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   self.assertEqual(conn._Connection_APPS__compressUncompressGzip("in/test/arroz.gz",False),"in/test/arrozUncompressed")

  # def test_file_validity(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   self.assertFalse(conn._Connection_APPS__checkFileValidity("in/test/file"))

  # def test_file_validity2(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   self.assertTrue(conn._Connection_APPS__checkFileValidity("in/uploads_test/CVTY2720.21D"))

  def test_upload_file(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    conn.uploadFile("in/uploads_test/CVTY2720.21D","out/queue/queue")

if __name__ == '__main__':
  unittest.main()
