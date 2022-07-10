import argparse
import os.path
from appsclone_client.utils.helper import *
from appsclone_client.utils.logs   import *
from appsclone_client.constants    import *
from gdgps_apps                    import defines

class ArgumentParser:
  """The parser for the command line arguments."""
  # == Methods ==
  def __init__(self,logger):
    """Initalize the possible arguments.
    
    Parameters
    ----------
    logger   : Logs
      The log object to log to
    """
    self.logger = logger
    self.parser = argparse.ArgumentParser(
      description="The APPSClone client. Upload RINEX files to the server and download back the results!"
    )
    self.parser.add_argument(
      "option",
      type = str,
      help = "upload | download."
    )
    self.parser.add_argument(
      "-r",
      type = str,
      help = "The name of the RINEX file to upload."
    )
    self.parser.add_argument(
      "-m",
      type = int,
      help = "The processing mode. 1 means static, 2 means kinematic. Default is static."
    )
    self.parser.add_argument(
      "-p",
      type = int,
      help = "The product. 1 means real time, 2 means ultra, 3 means rapid, 4 means final, 5 means best. Default is best."
    )
    self.parser.add_argument(
      "-t",
      type = int,
      help = "The troposphere model. 1 means vmf1, 2 means gmf, 3 means gpt2. Default is gmf."
    )
    self.parser.add_argument(
      "--ocean_loading",
      action = 'store_true',
      help   = "To load or not the ocean model. Default is true."
    )
    self.parser.add_argument(
      "--model_tides",
      action = 'store_true',
      help   = "To model or not the tides. Default is true."
    )
    self.parser.add_argument(
      "-w",
      type = int,
      help = "The elevation dep weighting. 1 means flat, 2 means sine, 3 means root sine. Default is root sine."
    )
    self.parser.add_argument(
      "-a",
      type = float,
      help = "The elevation angle cutoff. A floating-point number. Default is 7.5."
    )
    self.parser.add_argument(
      "-s",
      type = int,
      help = "The solution period. An integer. Default is 300."
    )
    self.args = self.parser.parse_args()
  
  def getOptions(self,to_upload_rinex_dir):
    """Get the options for each argument.
    
    Parameters
    ----------
    to_upload_rinex_dir : str
      The directory where the rinex files must be put to be uploaded

    Returns
    ----------
    list
      The list of upload arguments for APPS. None means that the argument is not available
    """
    self.logger.writeRoutineLog(getOptions,Logs.ROUTINE_STATUS.START)
    toUploadArgs = []
    if self.args.option.lower() == "upload":
      self.logger.writeRegularLog(Logs.SEVERITY.INFO,uploadArg)
      toUploadArgs.append("u")
    elif self.args.option.lower() == "download":
      self.logger.writeRegularLog(Logs.SEVERITY.INFO,downloadArg)
      toUploadArgs.append("d")
    else:
      toUploadArgs.append(None)
      self.logger.writeRegularLog(Logs.SEVERITY.ERROR,unknownUploadOrDownloadArg.format(arg = self.args.option.lower()))
      self.logger.writeRoutineLog(getOptions,Logs.ROUTINE_STATUS.END)
      return toUploadArgs
    if self.args.option.lower() == "upload":
      if self.args.r:
        if os.path.exists(Helper.joinPathFile(to_upload_rinex_dir,self.args.r)):
          self.logger.writeRegularLog(Logs.SEVERITY.INFO,rinexArg.format(file = self.args.r))
          toUploadArgs.append(self.args.r)
        else:
          toUploadArgs.append(None)
          self.logger.writeRegularLog(Logs.SEVERITY.ERROR,unknownRinexArg.format(file = self.args.r))
          self.logger.writeRoutineLog(getOptions,Logs.ROUTINE_STATUS.END)
          return toUploadArgs
      else:
        toUploadArgs.append(None)
        self.logger.writeRegularLog(Logs.SEVERITY.ERROR,noRinexArg)
        self.logger.writeRoutineLog(getOptions,Logs.ROUTINE_STATUS.END)
        return toUploadArgs
    else:
      toUploadArgs.append(None)
    if self.args.m and self.args.m > 0 and self.args.m < 3:
      if self.args.m == 1:
        toUploadArgs.append(defines.GIPSYData.STATIC)
      elif self.args.m == 2:
        toUploadArgs.append(defines.GIPSYData.KINEMATIC)
    else:
      toUploadArgs.append(None)
    self.logger.writeRegularLog(
      Logs.SEVERITY.INFO,
      upArg.format(arg = "processing mode",argValue = toUploadArgs[-1] if self.args.m else "default")
    )
    if self.args.p and self.args.p > 0 and self.args.p < 6:
      if self.args.p == 1:
        toUploadArgs.append(defines.OrbitClockProduct.REAL_TIME)
      elif self.args.p == 2:
        toUploadArgs.append(defines.OrbitClockProduct.ULTRA)
      elif self.args.p == 3:
        toUploadArgs.append(defines.OrbitClockProduct.RAPID)
      elif self.args.p == 4:
        toUploadArgs.append(defines.OrbitClockProduct.FINAL)
      elif self.args.p == 5:
        toUploadArgs.append(defines.GIPSYData.BEST)
    else:
      toUploadArgs.append(None)
    self.logger.writeRegularLog(
      Logs.SEVERITY.INFO,
      upArg.format(arg = "product",argValue = toUploadArgs[-1] if self.args.p else "default")
    )
    if self.args.t and self.args.t > 0 and self.args.t < 4:
      if self.args.t == 1:
        toUploadArgs.append(defines.GIPSYData.TROP_VMF1)
      elif self.args.t == 2:
        toUploadArgs.append(defines.GIPSYData.TROP_GMF)
      elif self.args.t == 3:
        toUploadArgs.append(defines.GIPSYData.TROP_GPT2)
    else:
      toUploadArgs.append(None)
    self.logger.writeRegularLog(
      Logs.SEVERITY.INFO,
      upArg.format(arg = "troposphere model",argValue = toUploadArgs[-1] if self.args.t else "default")
    )
    toUploadArgs.append(self.args.ocean_loading)
    self.logger.writeRegularLog(
      Logs.SEVERITY.INFO,
      upArg.format(arg = "ocean loading",argValue = self.args.ocean_loading)
    )
    toUploadArgs.append(self.args.model_tides)
    self.logger.writeRegularLog(
      Logs.SEVERITY.INFO,
      upArg.format(arg = "model tides",argValue = self.args.model_tides)
    )
    if self.args.w and self.args.w > 0 and self.args.w < 4:
      if self.args.w == 1:
        toUploadArgs.append(defines.GIPSYData.FLAT)
      elif self.args.w == 2:
        toUploadArgs.append(defines.GIPSYData.SINE)
      elif self.args.w == 3:
        toUploadArgs.append(defines.GIPSYData.ROOT_SINE)
    else:
      toUploadArgs.append(None)
    self.logger.writeRegularLog(
      Logs.SEVERITY.INFO,
      upArg.format(arg = "elevation dep weighting",argValue = toUploadArgs[-1] if self.args.w else "default")
    )
    if self.args.a and (isinstance(self.args.a,int) or isinstance(self.args.a,float)):
      toUploadArgs.append(self.args.a)
    else:
      toUploadArgs.append(None)
    self.logger.writeRegularLog(
      Logs.SEVERITY.INFO,
      upArg.format(arg = "elevation angle cutoff",argValue = self.args.a)
    )
    if self.args.s and (isinstance(self.args.s,int)):
      toUploadArgs.append(self.args.s)
    else:
      toUploadArgs.append(None)
    self.logger.writeRegularLog(
      Logs.SEVERITY.INFO,
      upArg.format(arg = "solution period",argValue = self.args.s)
    )
    self.logger.writeRoutineLog(getOptions,Logs.ROUTINE_STATUS.END)
    return toUploadArgs

# ✓    unit tested
# ✓ feature tested