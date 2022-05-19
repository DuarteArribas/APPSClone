class RinexHeader:
  """A rinex header. It's constituted by several mandatory header lines and several optional header lines.
  It's used to display metadata about a RINEX file.

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
    "TIME OF FIRST OBS"   : "5I6,1F13.7,5X,1A3",
    "END OF HEADER"       : "60X"
  }
  # == Methods ==
  def __init__(self):
    """Initializes the header to the empty string, so that header lines can be appended and
    resets the number of headers to zero
    """
    self.header          = ""
    self.numberOfHeaders = 0
    self.receiver        = (None,None,None)
  def readMandatoryHeader(self,rinexFile):
    """Reads a rinex file's mandatory header lines and counts their number

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
          self.header          += line.strip()
          self.header          += "\n"

  def isValidHeader(self):
    """Checks if a RINEX header is valid

    Returns
    ----------
    bool
      True if the header is valid and False otherwise
    """
    if self.__isValidNumberOfHeaders(): #avoid checking receiver and antenna if at least one header is not there
      return self.__isValidReceiver() and self.__isValidAntenna()

  def __isValidNumberOfHeaders(self):
    return self.numberOfHeaders == len(list(RinexHeader.MANDATORY_RINEX_HEADERS.keys()))

  def __isValidReceiver(self):
    
    # for line in self.header.split("\n"):
    #   if line
    # givenReceiver
    pass

  def __isValidAntenna(self):
    pass

  def parseFormat(self,line,format):
    output = []
    if "," in format:
      for f in format.split(","):
        for i in range(int(f[0])):
          if f[1] in "AIX":
            numberOfColumns = int(f[2:])
          elif f[1] == "F":
            floatingSplit   = f[2:].split(".")
            numberOfColumns = int(floatingSplit[0])
          output.append(line[i*numberOfColumns:i*numberOfColumns+numberOfColumns].strip())
    else:
      for i in range(int(format[0])):
          if format[1] in "AIX":
            numberOfColumns = int(format[2:])
          elif format[1] == "F":
            floatingSplit   = format[2:].split(".")
            numberOfColumns = int(floatingSplit[0])
          output.append(line[i*numberOfColumns:i*numberOfColumns+numberOfColumns].strip())
    return output
    