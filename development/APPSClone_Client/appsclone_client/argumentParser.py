import argparse
import os.path

class ArgumentParser:
  def __init__(self):
    self.parser = argparse.ArgumentParser(
      description="The APPSClone client. Upload RINEX files to the server and download back the results!"
    )
    self.parser.add_argument(
      "rinexFile",
      type = str,
      help = "The name of the RINEX file to upload."
    )
    self.parser.add_argument(
      "-m",
      type = int,
      help = "The processing mode. 1 means static, 2 means kinematic."
    )
    self.parser.add_argument(
      "-p",
      type = int,
      help = "The product. 1 means real time, 2 means ultra, 3 means rapid, 4 means final, 5 means best."
    )
    self.parser.add_argument(
      "-t",
      type = int,
      help = "The troposphere model. 1 means vmf1, 2 means gmf, 3 means gpt2."
    )
    self.parser.add_argument(
      "--ocean_loading",
      action = 'store_true',
      help   = "To load or not the ocean."
    )
    self.parser.add_argument(
      "--model_tides",
      action = 'store_true',
      help   = "To model or not the tides."
    )
    self.parser.add_argument(
      "-w",
      type = int,
      help = "The elevation dep weighting. 1 means flat, 2 means sine, 3 means root sine."
    )
    self.parser.add_argument(
      "-a",
      type = float,
      help = "The elevation angle cutoff. A floating-point number."
    )
    self.parser.add_argument(
      "-s",
      type = int,
      help = "The solution period. An integer."
    )
  
  def getOptions(self):
    args = self.parser.parse_args()
    toUploadArgs = []
    if os.path.exists(args.rinexFile):
      toUploadArgs.append(args.rinexFile)
    else:
      toUploadArgs.append(None)
    if args.m and args.m > 0 and args.m < 3:
      if args.m == 1:
        toUploadArgs.append("defines.GIPSYData.STATIC")
      elif args.m == 2:
        toUploadArgs.append("defines.GIPSYData.KINEMATIC")
    else:
      toUploadArgs.append(None)
    if args.p and args.p > 0 and args.p < 6:
      if args.p == 1:
        toUploadArgs.append("defines.OrbitClockProduct.REAL_TIME")
      elif args.p == 2:
        toUploadArgs.append("defines.OrbitClockProduct.ULTRA")
      elif args.p == 3:
        toUploadArgs.append("defines.OrbitClockProduct.RAPID")
      elif args.p == 4:
        toUploadArgs.append("defines.OrbitClockProduct.FINAL")
      elif args.p == 5:
        toUploadArgs.append("defines.GIPSYData.BEST")
    else:
      toUploadArgs.append(None)
    if args.t and args.t > 0 and args.t < 4:
      if args.t == 1:
        toUploadArgs.append("defines.GIPSYData.TROP_VMF1")
      elif args.t == 2:
        toUploadArgs.append("defines.GIPSYData.TROP_GMF")
      elif args.t == 3:
        toUploadArgs.append("defines.GIPSYData.TROP_GPT2")
    else:
      toUploadArgs.append(None)
    toUploadArgs.append(args.ocean_loading)
    toUploadArgs.append(args.model_tides)
    if args.w and args.w > 0 and args.w < 4:
      if args.w == 1:
        toUploadArgs.append("defines.GIPSYData.FLAT")
      elif args.w == 2:
        toUploadArgs.append("defines.GIPSYData.SINE")
      elif args.w == 3:
        toUploadArgs.append("defines.GIPSYData.ROOT_SINE")
    else:
      toUploadArgs.append(None)
    if args.a:
      toUploadArgs.append(args.a)
    else:
      toUploadArgs.append(None)
    if args.s:
      toUploadArgs.append(args.s)
    else:
      toUploadArgs.append(None)
    return toUploadArgs