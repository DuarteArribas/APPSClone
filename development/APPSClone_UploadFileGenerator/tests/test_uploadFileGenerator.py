import appsclone_uploadFileGenerator
import unittest
from appsclone_uploadFileGenerator.uploadFileGenerator import *

class TestUploadFileGenerator(unittest.TestCase):
  #def test_ask_inputs(self):
  #  uploadFile = UploadFileGenerator()
  #  uploadFile.askUploadFileInputs()
  #  self.assertTrue(uploadFile.downloadFromPath)
  #  self.assertTrue(uploadFile.uploadTopath)
  #  self.assertTrue(uploadFile.ip)
  #  for item in zip(uploadFile.__dict__.keys(),uploadFile.__dict__.values()):
  #    print(item)

  def test_generate_file(self):
    uploadFile = UploadFileGenerator()
    uploadFile.askUploadFileInputs("out/uploadFiles")
    uploadFile.generateUploadFile("out/uploadFiles")

if __name__ == '__main__':
  unittest.main()