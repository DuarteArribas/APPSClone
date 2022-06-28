import appsclone_client
import unittest
from appsclone_client.uploadFileGenerator import *

class TestUploadFileGenerator(unittest.TestCase):
  def test_ask_inputs(self):
    uploadFile = UploadFileGenerator("arroz")
    uploadFile._UploadFileGenerator__askUploadFileInputs()
    self.assertTrue(uploadFile.downloadFromPath)
    self.assertTrue(uploadFile.uploadTopath)
    self.assertTrue(uploadFile.ip)

if __name__ == '__main__':
  unittest.main()