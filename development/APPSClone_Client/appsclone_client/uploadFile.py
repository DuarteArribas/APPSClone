from appsclone_client.utils.helper import *
from appsclone_client.gui          import *
from enum                          import Enum

class UploadFileGenerator:
  """"""
  # == Attributes ==
  UPLOAD_FILE_OPTIONS = Enum(
    "UPLOAD_FILE_OPTIONS","TEXT_INPUT"
  )
  # == Methods ==
  def __init__(self,generateToDir):
    self.downloadFromPath = None
    self.uploadTopath     = None
    self.ip               = None
    self.generateToDir = generateToDir

  def __askUploadFileInputs(self):
    currentInput = UPLOAD_FILE_OPTIONS.TEXT_INPUT
    gui = GUI()
    if currentInput == UPLOAD_FILE_OPTIONS.TEXT_INPUT:
      self.downloadFromPath = ""
      self.uploadTopath     = ""
      self.ip               = ""
      self.downloadFromPath = gui.getInput("What is the absolute path of the rinex file that you want to upload?",None)
      while not Helper.isValidAbsolutePathToFile(self.downloadFromPath):
        self.downloadFromPath = gui.getInput(
          "What is the absolute path of the rinex file that you want to upload?",
          "The path you wrote is not a valid absolute path to a file! Please try again."
        )
      self.uploadTopath = gui.getInput("What is the absolute path of the directory where the results must be uploaded?",None)
      while not Helper.isValidAbsolutePathToDir(self.uploadTopath):
        self.uploadTopath = gui.getInput(
          "What is the absolute path of the directory where the results must be uploaded?",
          "The path you wrote is not a valid absolute path to a directory! Please try again."
        )
      self.ip = gui.getInput("What is the IP of your server?",None)
      while not Helper.isValidIpv4(self.ip):
        self.ip = gui.getInput(
          "What is the IP of your server?",
          "The IP you wrote is not a valid IPV4! Please try again."
        )
