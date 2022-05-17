class RinexHeader:
  """A rinex header

  Attributes
  ----------
  HEADER_START            : int
    rinex headers start at column 61 (python strings start counting at 0, so we subtract 1)
  HEADER_END              : int
    rinex headers end at column 80
  MANDATORY_RINEX_HEADERS : dict
    both rinex 2.11 and 3.02 must have these headers (their value is the respective format)
  """
  # == Attributes ==
  HEADER_START              = 60
  HEADER_END                = 80
  MANDATORY_RINEX_HEADERS   = {
    "RINEX VERSION / TYPE": "1F9.2,11X,1A1,19X,1A1,19X",
    "PGM / RUN BY / DATE" : "3A20",
    "MARKER NAME"         : "1A20",
    "OBSERVER / AGENCY"   : "1A20,1A60",
    "REC # / TYPE / VERS" : "3A20",
    "ANT # / TYPE"        : "2A20",
    "APPROX POSITION XYZ" : "3F14.4",
    "ANTENNA: DELTA H/E/N": "3F14.4",
    "TIME OF FIRST OBS"   : "5I6,1F13.7,5X,1A3"
  }
  # == Methods ==
  def __init__(self):
    """Initializes the header to the empty string, so that header lines can be appended and
    resets the number of headers to zero
    """
    self.header          = ""
    self.numberOfHeaders = 0
  def readHeader(self,rinexFile):
    """Reads a rinex file's header and counts the number of header it contains

    Parameters
    ----------
    rinexFile : str
      The rinex file to read the header from
    """
    with open(rinexFile,"r") as f:
      lines = f.readlines()
      for line in lines:
        if line[RinexHeader.HEADER_START:RinexHeader.HEADER_END].strip() == "END OF HEADER":
          self.numberOfHeaders += 1
          break
        elif line[RinexHeader.HEADER_START:RinexHeader.HEADER_END].strip() in list(RinexHeader.MANDATORY_RINEX_HEADERS.keys()):
          self.numberOfHeaders += 1
          self.header          += line[:RinexHeader.HEADER_START].strip()
          self.header          += "\n"

  def isValidHeader(self):
    pass
    