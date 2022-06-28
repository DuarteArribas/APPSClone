from appsclone_client.gui import *
from enum                 import Enum

class UploadFileGenerator:
  """"""
  # == Attributes ==
  UPLOAD_FILE_OPTIONS = Enum(
    "UPLOAD_FILE_OPTIONS","DOWNLOAD_FROM_PATH UPLOAD_TO_PATH IP"
  )
  # == Methods ==
  def __init__(self,generateToDir):
    self.downloadFromPath = None
    self.uploadTopath     = None
    self.ip               = None
    self.generateToDir = generateToDir

  def __askUploadFileInputs(self):
    currentInput = UPLOAD_FILE_OPTIONS.DOWNLOAD_FROM_PATH
    gui = GUI()
    if currentInput == UPLOAD_FILE_OPTIONS.DOWNLOAD_FROM_PATH:
      self.downloadFromPath = gui.getInput("What is the absolute path of the rinex file that you want to upload?",None)
