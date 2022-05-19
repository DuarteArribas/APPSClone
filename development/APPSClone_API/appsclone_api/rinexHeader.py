from receiversAndAntennas import *
from enum import Enum
class RinexHeader:
  """A rinex header. It's constituted by several mandatory header lines and several optional header lines.
  It's used to display metadata about a RINEX file.

  Attributes
  ----------
  HEADER_START              : int
    rinex headers start at column 61 (python strings start counting at 0, so we subtract 1)
  HEADER_END                : int
    rinex headers end at column 80
  MANDATORY_RINEX_HEADERS   : dict
    both rinex 2.11 and 3.02 must have these headers (their value is the respective format)
  ALLOWED_VERSIONS          : list
    the allowed RINEX versions
  VALIDITY_ERRORS           : enum
    the error messages for when the file is not valid 
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
  ALLOWED_VERSIONS          = ["2.11","3.02"]
  VALIDITY_ERRORS           = Enum(
    'VALIDITY_ERRORS', 'OK INVALID_NUMBER_OF_HEADERS INVALID_RECEIVER INVALID_ANTENNA INVALID_VERSION'
  )
  # == Methods ==
  def __init__(self):
    """
    Initialize the header to the empty string, so that header lines can be appended,
    resets the number of headers to zero and sets the version to None.
    """
    self.header          = ""
    self.numberOfHeaders = 0
    self.version         = None

  def readMandatoryHeader(self,rinexFile):
    """Read a rinex file's mandatory header lines and counts their number.

    Parameters
    ----------
    rinexFile : str
      The rinex file to read the header from
    """
    with open(rinexFile,"r") as f:
      lines = f.readlines()
      for line in lines:
        if "2.11" in line:
          self.version = "2.11"
        elif "3.02" in line:
          self.version = "3.02"
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
    """Check if a RINEX header is valid.

    Returns
    ----------
    bool
      True if the header is valid and False otherwise
    """
    if self.__isValidNumberOfHeaders(): #avoid checking receiver and antenna if at least one header is not there
      if self.__isValidReceiver():
        if self.__isValidAntenna():
          if self.version in RinexHeader.ALLOWED_VERSIONS:
            return True,RinexHeader.VALIDITY_ERRORS.OK
          else:
            return False,RinexHeader.VALIDITY_ERRORS.INVALID_VERSION
        else:
          return False,RinexHeader.VALIDITY_ERRORS.INVALID_ANTENNA
      else:
        return False,RinexHeader.VALIDITY_ERRORS.INVALID_RECEIVER
    else:
      return False,RinexHeader.VALIDITY_ERRORS.INVALID_NUMBER_OF_HEADERS

  def __isValidNumberOfHeaders(self):
    """Check if the number of headers read is equal to the number of needed headers.

    Returns
    ----------
    bool
      True if the number of headers read is equal to the number of needed headers or False otherwise
    """
    return self.numberOfHeaders == len(list(RinexHeader.MANDATORY_RINEX_HEADERS.keys())) + 1

  def __isValidReceiver(self):
    """Check if the receiver is valid.

    Returns
    ----------
    bool
      True if the receiver is in the valid receivers set or False otherwise
    """
    for line in self.header.split("\n"):
      if line[RinexHeader.HEADER_START:RinexHeader.HEADER_END] == "REC # / TYPE / VERS":
        receiver = self.__parseFormat(line[:RinexHeader.HEADER_START],RinexHeader.MANDATORY_RINEX_HEADERS["REC # / TYPE / VERS"])[1]
        return receiver in receivers
    return False

  def __isValidAntenna(self):
    """Check if the antenna is valid.

    Returns
    ----------
    bool
      True if the antenna is in the valid antennas set or False otherwise
    """
    for line in self.header.split("\n"):
      if line[RinexHeader.HEADER_START:RinexHeader.HEADER_END] == "ANT # / TYPE":
        antenna = self.__parseFormat(line[:RinexHeader.HEADER_START],RinexHeader.MANDATORY_RINEX_HEADERS["ANT # / TYPE"])[1]
        return antenna in antennas
    return False

  def __parseFormat(self,line,headerFormat):
    """Parse a RINEX header format to read the respective columns of the header line.

    Parameters
    ----------
    line         : str
      The header line to parse
    headerFormat : str
      The format to parse the header line. It's a string containing one format or mutiple formats separated
      by commas. If there are multiple formats, they should be applied in order. Each format is constituted by
      three parts, as: RTC, where R is the number of times it should be repeated, T is the type of data it'll
      contain (A -> String, I -> Integer, X -> Space, F -> Float) and C is the number of columns to read. E.G.:
      the format 3I10 will read 10 columns of integers 3 times.

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
      timesToLoop,numberOfDigitsInBeggining = self.__extractIntUntilChar(f)
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

  def __extractIntUntilChar(self,string):
    """Extract the number before a character appears.

    Parameters
    ----------
    string       : str
      the string to extract from

    Returns
    ----------
    integer, integer
      The number before the first char and the length of that number
    """
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