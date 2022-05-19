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
    "PGM / RUN BY / DATE" : "A20,A20,A20",
    "MARKER NAME"         : "A60",
    "OBSERVER / AGENCY"   : "A20,A40",
    "REC # / TYPE / VERS" : "3A20",
    "ANT # / TYPE"        : "2A20",
    "APPROX POSITION XYZ" : "3F14.4",
    "ANTENNA: DELTA H/E/N": "3F14.4",
    "TIME OF FIRST OBS"   : "5I6,F13.7,5X,A3",
    "END OF HEADER"       : "60X"
  }
  RINEX_VERSION_HEADER_FULL = {
    "RINEX VERSION / TYPE": "F9.2,11X,A20,A20"
  }
  RINEX_VERSION_HEADER_ABBR = {
    "RINEX VERSION / TYPE": "F9.2,11X,A1,19X,A1,19X"
  }
  # == Methods ==
  def __init__(self):
    """
    Initializes the header to the empty string, so that header lines can be appended and
    resets the number of headers to zero.
    """
    self.header          = ""
    self.numberOfHeaders = 0
    self.version         = None

  def readMandatoryHeader(self,rinexFile):
    """Reads a rinex file's mandatory header lines and counts their number.

    Parameters
    ----------
    rinexFile : str
      The rinex file to read the header from
    """
    with open(rinexFile,"r") as f:
      lines = f.readlines()
      for line in lines:
        if "2.11" in line:
          version = "2.11"
        elif "3.02" in line:
          version = "3.02"
        if line[RinexHeader.HEADER_START:RinexHeader.HEADER_END].strip() == "END OF HEADER":
          self.numberOfHeaders += 1
          break
        elif line[RinexHeader.HEADER_START:RinexHeader.HEADER_END].strip() in list(RinexHeader.MANDATORY_RINEX_HEADERS.keys()):
          self.numberOfHeaders += 1
          self.header          += line.strip()
          self.header          += "\n"
        elif line[RinexHeader.HEADER_START:RinexHeader.HEADER_END].strip() == "RINEX VERSION / TYPE":
          self.numberOfHeaders += 1
          self.header          += line.strip()
          self.header          += "\n"
        

  def isValidHeader(self):
    """Checks if a RINEX header is valid.

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

  def __parseFormat(self,line,headerFormat):
    """Parses a RINEX header format to read the respective columns of the header line.

    Parameters
    ----------
    line         : str
      The header line to parse
    headerFormat : str
      The format to parse the header line

    Returns
    ----------
    list
      A list of each element of the header line as parsed from the header format
    """
    output          = []
    columnsRead     = 0
    numberOfColumns = 0
    formatString    = []
    #is multi format string?
    if "," in headerFormat:
      formatString  = headerFormat.split(",")
    else:
      formatString.append(headerFormat)
    #loop through format
    for f in formatString:
      timesToLoop,numberOfDigitsInBeggining = self.__extractIntUntilString(f)
      #loop through repetitions of format
      for i in range(timesToLoop):
        #string or integer
        if f[numberOfDigitsInBeggining] in "AI":
          numberOfColumns = 1 if not f[-1].isdigit() else int(f[numberOfDigitsInBeggining+1:])
        #spaces
        elif f[numberOfDigitsInBeggining] == "X":
          numberOfColumns = timesToLoop
          output.append(line[columnsRead:columnsRead+numberOfColumns].strip())
          columnsRead += numberOfColumns
          break
        #floats
        elif f[numberOfDigitsInBeggining] == "F":
          floatingSplit   = f[numberOfDigitsInBeggining+1:].split(".")
          numberOfColumns = int(floatingSplit[0])
        output.append(line[columnsRead:columnsRead+numberOfColumns].strip())
        columnsRead += numberOfColumns
    return output

  def __extractIntUntilString(self,string):
    if string == "":
      return 0,0
    elif not any(char.isdigit() for char in string):
      return 1,0
    numberString = ""
    for i in range(len(string)):
      if not string[i].isdigit():
        break
      else:
        numberString += string[i]
    return (int(numberString) if numberString != "" else 1),(len(numberString))