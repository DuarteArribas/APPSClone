from appsclone_client.utils.helper import *
from appsclone_client.gui          import *
from enum                          import Enum

class UploadFileGenerator:
  """"""
  # == Attributes ==
  
  INPUT_TYPES          = Enum(
    "INPUT_TYPES","TEXT_INPUT PICK_INPUT"
  )
  PICKUP_INPUT_OPTIONS = Enum(
    "PICKUP_INPUT_OPTIONS","PROCESSING_MODE PRODUCT TROPOSPHERE_MODEL OCEAN_LOADING MODEL_TIDES ELEV_DEP_WEIGHTING ELEV_ANGLE_CUTOFF SOLUTION_PERIOD GENERATE_QUATERNIONS"
  )
  # == Methods ==
  def __init__(self,generateToDir):
    self.downloadFromPath     = None
    self.uploadTopath         = None
    self.ip                   = None
    self.username             = None
    self.password             = None
    self.processing_mode      = None
    self.product              = None
    self.troposphere_model    = None
    self.ocean_loading        = None
    self.model_tides          = None
    self.elev_dep_weighting   = None
    self.elev_angle_cutoff    = None
    self.solution_period      = None
    self.generate_quaternions = None
    self.generateToDir = generateToDir

  def __askUploadFileInputs(self):
    currentInput       = UploadFileGenerator.INPUT_TYPES.TEXT_INPUT
    currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.PROCESSING_MODE
    gui = GUI()
    while True:
      if currentInput == UploadFileGenerator.INPUT_TYPES.TEXT_INPUT:
        self.downloadFromPath = ""
        self.uploadTopath     = ""
        self.ip               = ""
        self.downloadFromPath = gui.getInput("What is the absolute path of the rinex file that you want to upload?",None)
        while not Helper.isValidAbsolutePathToFile(self.downloadFromPath):
          self.downloadFromPath = gui.getInput(
            "What is the absolute path of the rinex file that you want to upload?",
            "The path you wrote is not a valid absolute path to a file!"
          )
        self.uploadTopath = gui.getInput("What is the absolute path of the directory where the results must be uploaded?",None)
        while not Helper.isValidAbsolutePathToDir(self.uploadTopath):
          self.uploadTopath = gui.getInput(
            "What is the absolute path of the directory where the results must be uploaded?",
            "The path you wrote is not a valid absolute path to a directory!"
          )
        self.ip = gui.getInput("What is the IP of your server?",None)
        while not Helper.isValidIpv4(self.ip):
          self.ip = gui.getInput(
            "What is the IP of your server?",
            "The IP you wrote is not a valid IPV4!"
          )
        self.username = gui.getInput("What is the username to connect to your server?",None)
        while not self.username:
          self.username = gui.getInput(
            "What is the username to connect to your server?",
            "The username must not be empty!"
          )
        self.password = gui.getInput("What is the password to connect to your server?",None)
        while not self.password:
          self.password = gui.getInput(
            "What is the password to connect to your server?",
            "The password must not be empty!"
          )
        currentInput = UploadFileGenerator.INPUT_TYPES.PICK_INPUT
      elif currentInput == UploadFileGenerator.INPUT_TYPES.PICK_INPUT:
        if currentPickupInput == UploadFileGenerator.PICKUP_INPUT_OPTIONS.PROCESSING_MODE:
          processingModes      = ["Default","Static","Kinematic","Back"]
          self.processing_mode = gui.getPickInput("What should be the processing mode of the rinex file?",processingModes)
          if self.processing_mode == "Default":
            self.processing_mode = "defines.GIPSYData.PROCESSING_MODE_DEFAULT"
          elif self.processing_mode == "Static":
            pass
          elif self.processing_mode == "Kinematic":
            pass
          elif self.processing_mode == "Back":
            pass