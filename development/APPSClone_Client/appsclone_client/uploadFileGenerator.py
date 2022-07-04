import os.path
from appsclone_client.utils.helper import *
from appsclone_client.gui          import *
from enum                          import Enum

class UploadFileGenerator:
  """Generator for upload files.

  Attributes
  ----------
  INPUT_TYPES          : enum
    The type of input that is being asked for
  PICKUP_INPUT_OPTIONS : enum
    The type of pick up input that is being asked for
  """
  # == Attributes ==
  INPUT_TYPES          = Enum(
    "INPUT_TYPES","TEXT_INPUT PICK_INPUT"
  )
  PICKUP_INPUT_OPTIONS = Enum(
    "PICKUP_INPUT_OPTIONS","PROCESSING_MODE PRODUCT TROPOSPHERE_MODEL OCEAN_LOADING MODEL_TIDES ELEV_DEP_WEIGHTING ELEV_ANGLE_CUTOFF SOLUTION_PERIOD"
  )
  # == Methods ==
  def __init__(self):
    """Assign default arguments for upload file."""
    self.uploadFileName     = None
    self.downloadFromPath   = None
    self.uploadTopath       = None
    self.ip                 = None
    self.username           = None
    self.password           = None
    self.processing_mode    = None
    self.product            = None
    self.troposphere_model  = None
    self.ocean_loading      = None
    self.model_tides        = None
    self.elev_dep_weighting = None
    self.elev_angle_cutoff  = None
    self.solution_period    = None

  def askUploadFileInputs(self,generateToDir):
    """Ask the arguments for the upload file, saving them to the instance variables of the class.

    Parameters
    ----------
    generateToDir : str
      The directory to generate the upload file to
    """
    currentInput       = UploadFileGenerator.INPUT_TYPES.TEXT_INPUT
    currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.PROCESSING_MODE
    gui = GUI()
    while True:
      if currentInput == UploadFileGenerator.INPUT_TYPES.TEXT_INPUT:
        self.uploadFileName   = ""
        self.downloadFromPath = ""
        self.uploadTopath     = ""
        self.ip               = ""
        self.username         = ""
        self.password         = ""
        self.uploadFileName = gui.getInput("What is the name of the upload file?",None)
        while os.path.isfile(Helper.joinPathFile(generateToDir,self.uploadFileName)):
          self.uploadFileName = gui.getInput(
            "What is the name of the upload file?",
            "A file with that name already exists!"
          )
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
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.PRODUCT
          elif self.processing_mode == "Static":
            self.processing_mode = "defines.GIPSYData.STATIC"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.PRODUCT
          elif self.processing_mode == "Kinematic":
            self.processing_mode = "defines.GIPSYData.KINEMATIC"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.PRODUCT
          elif self.processing_mode == "Back":
            currentInput = UploadFileGenerator.INPUT_TYPES.TEXT_INPUT
        elif currentPickupInput == UploadFileGenerator.PICKUP_INPUT_OPTIONS.PRODUCT:
          products     = ["Default","Real Time","Ultra","Rapid","Final","Best","Back"]
          self.product = gui.getPickInput("What should be the product to process the rinex file?",products)
          if self.product == "Default":
            self.product = "defines.GIPSYData.PRODUCT_DEFAULT"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.TROPOSPHERE_MODEL
          elif self.product == "Real Time":
            self.product = "defines.OrbitClockProduct.REAL_TIME"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.TROPOSPHERE_MODEL
          elif self.product == "Ultra":
            self.product = "defines.OrbitClockProduct.ULTRA"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.TROPOSPHERE_MODEL
          elif self.product == "Rapid":
            self.product = "defines.OrbitClockProduct.RAPID"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.TROPOSPHERE_MODEL
          elif self.product == "Final":
            self.product = "defines.OrbitClockProduct.FINAL"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.TROPOSPHERE_MODEL
          elif self.product == "Best":
            self.product = "defines.GIPSYData.BEST"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.TROPOSPHERE_MODEL
          elif self.product == "Back":
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.PROCESSING_MODE
        elif currentPickupInput == UploadFileGenerator.PICKUP_INPUT_OPTIONS.TROPOSPHERE_MODEL:
          troposphereModels      = ["Default","GMF","VMF1","GPT2","Back"]
          self.troposphere_model = gui.getPickInput("What should be the troposphere models to process the rinex file?",troposphereModels)
          if self.troposphere_model == "Default":
            self.troposphere_model = "defines.GIPSYData.TROP_GMF"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.OCEAN_LOADING
          elif self.troposphere_model == "GMF":
            self.troposphere_model = "defines.GIPSYData.TROP_GMF"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.OCEAN_LOADING
          elif self.troposphere_model == "VMF1":
            self.troposphere_model = "defines.GIPSYData.TROP_VMF1"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.OCEAN_LOADING
          elif self.troposphere_model == "GPT2":
            self.troposphere_model = "defines.GIPSYData.TROP_GPT2"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.OCEAN_LOADING
          elif self.troposphere_model == "Back":
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.PRODUCT
        elif currentPickupInput == UploadFileGenerator.PICKUP_INPUT_OPTIONS.OCEAN_LOADING:
          oceanLoadings      = ["Default","True","False","Back"]
          self.ocean_loading = gui.getPickInput("Ocean loading?",oceanLoadings)
          if self.ocean_loading == "Default":
            self.ocean_loading = True
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.MODEL_TIDES
          elif self.ocean_loading == "True":
            self.ocean_loading = True
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.MODEL_TIDES
          elif self.ocean_loading == "False":
            self.ocean_loading = False
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.MODEL_TIDES
          elif self.ocean_loading == "Back":
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.TROPOSPHERE_MODEL
        elif currentPickupInput == UploadFileGenerator.PICKUP_INPUT_OPTIONS.MODEL_TIDES:
          modelTides       = ["Default","True","False","Back"]
          self.model_tides = gui.getPickInput("Model tides?",modelTides)
          if self.model_tides == "Default":
            self.model_tides = True
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.ELEV_DEP_WEIGHTING
          elif self.model_tides == "True":
            self.model_tides = True
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.ELEV_DEP_WEIGHTING
          elif self.model_tides == "False":
            self.model_tides = False
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.ELEV_DEP_WEIGHTING
          elif self.model_tides == "Back":
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.OCEAN_LOADING
        elif currentPickupInput == UploadFileGenerator.PICKUP_INPUT_OPTIONS.ELEV_DEP_WEIGHTING:
          elevDepWeights       = ["Default","Flat","Sin","Sqrt Sin","Back"]
          self.elev_dep_weighting = gui.getPickInput("What is the elevation dependent weighting scheme?",elevDepWeights)
          if self.elev_dep_weighting == "Default":
            self.elev_dep_weighting = "defines.GIPSYData.ROOT_SINE"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.ELEV_ANGLE_CUTOFF
          elif self.elev_dep_weighting == "Flat":
            self.elev_dep_weighting = "defines.GIPSYData.FLAT"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.ELEV_ANGLE_CUTOFF
          elif self.elev_dep_weighting == "Sin":
            self.elev_dep_weighting = "defines.GIPSYData.SINE"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.ELEV_ANGLE_CUTOFF
          elif self.elev_dep_weighting == "Sqrt Sin":
            self.elev_dep_weighting = "defines.GIPSYData.ROOT_SINE"
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.ELEV_ANGLE_CUTOFF
          elif self.elev_dep_weighting == "Back":
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.MODEL_TIDES
        elif currentPickupInput == UploadFileGenerator.PICKUP_INPUT_OPTIONS.ELEV_ANGLE_CUTOFF:
          self.elev_angle_cutoff = gui.getInput("What is the elevation angle cutoff (Type default for default value and back to go to the previous option)?",None)
          if self.elev_angle_cutoff.lower() == "back":
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.ELEV_DEP_WEIGHTING
          elif not self.elev_angle_cutoff or not all([char.isdigit() or char == "." for char in self.elev_angle_cutoff]):
            self.elev_angle_cutoff = 7.5
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.SOLUTION_PERIOD
          else:
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.SOLUTION_PERIOD
        elif currentPickupInput == UploadFileGenerator.PICKUP_INPUT_OPTIONS.SOLUTION_PERIOD:
          self.solution_period = gui.getInput("What is the solution period (Type default for default value and back to go to the previous option)?",None)
          if self.solution_period.lower() == "back":
            currentPickupInput = UploadFileGenerator.PICKUP_INPUT_OPTIONS.ELEV_ANGLE_CUTOFF 
          elif not self.solution_period or not all([char.isdigit() or char == "." for char in self.solution_period]):
            self.solution_period = 300
            break
          else:
            break

  def generateUploadFile(self,generateToDir):
    """Generate an upload file from the asked input.

    Parameters
    ----------
    generateToDir : str
      The directory to generate the upload file to
    """
    with open(Helper.joinPathFile(generateToDir,self.uploadFileName),"w") as f:
      for arg in zip(self.__dict__.keys(),self.__dict__.values()):
        if arg[0] != "uploadFileName":
          f.write(f"{arg[1]}\n")

# ✓    unit tested
# ✓ feature tested