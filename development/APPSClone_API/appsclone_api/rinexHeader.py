from vars.receiversAndAntennas import *
from enum import Enum
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
  ALLOWED_VERSIONS        : list
    the allowed RINEX versions
  VALIDITY_ERRORS         : enum
    the error messages for when the file is not valid 
  """
  # == Attributes ==
  HEADER_START              = 60
  HEADER_END                = 80
  ALLOWED_VERSIONS          = ["ALL","2.11","3.02"]
  VALIDITY_ERRORS           = Enum(
    'VALIDITY_ERRORS', 'OK INVALID_NUMBER_OF_HEADERS INVALID_RECEIVER INVALID_ANTENNA INVALID_VERSION'
  )
  # == Methods ==
  def __init__(self):
    """Reset all mandatory header lines of the RINEX file being read and its version, so that new data can be appended"""
    self.mandatoryHeaders = {
      "RINEX VERSION / TYPE" : [RinexHeader.ALLOWED_VERSIONS[0],"F9.2,11X,A1,19X,A1,19X",[]],
      "PGM / RUN BY / DATE"  : [RinexHeader.ALLOWED_VERSIONS[0],"A20,A20,A20"           ,[]],
      "MARKER NAME"          : [RinexHeader.ALLOWED_VERSIONS[0],"A60"                   ,[]],
      "OBSERVER / AGENCY"    : [RinexHeader.ALLOWED_VERSIONS[0],"A20,A40"               ,[]],
      "REC # / TYPE / VERS"  : [RinexHeader.ALLOWED_VERSIONS[0],"3A20"                  ,[]],
      "ANT # / TYPE"         : [RinexHeader.ALLOWED_VERSIONS[0],"2A20"                  ,[]],
      "APPROX POSITION XYZ"  : [RinexHeader.ALLOWED_VERSIONS[0],"3F14.4"                ,[]],
      "ANTENNA: DELTA H/E/N" : [RinexHeader.ALLOWED_VERSIONS[0],"3F14.4"                ,[]],
      "TIME OF FIRST OBS"    : [RinexHeader.ALLOWED_VERSIONS[0],"5I6,F13.7,5X,A3"       ,[]],
      "END OF HEADER"        : [RinexHeader.ALLOWED_VERSIONS[0],"60X"                   ,[]]
    }
    self.version          = None

  def readMandatoryHeader(self,rinexFile):
    """Read a rinex file's mandatory header lines.

    Parameters
    ----------
    rinexFile : str
      The rinex file to read the header from
    """
    with open(rinexFile,"r") as f:
      lines = f.readlines()
      for line in lines:
        headerLabel = line[RinexHeader.HEADER_START:RinexHeader.HEADER_END].strip()
        #hasn't found the version yet-searching for it
        if not self.version:
          if headerLabel == "RINEX VERSION / TYPE":
            self.__fillHeaderData(headerLabel,line)
            if self.mandatoryHeaders[headerLabel][2][0] in RinexHeader.ALLOWED_VERSIONS:
              self.version = self.mandatoryHeaders[headerLabel][2][0]
        #has found the version, searching for mandatory header labels
        else:
          if headerLabel in list(self.mandatoryHeaders.keys()) and self.__isHeaderFromCurrentVersion(self.mandatoryHeaders[headerLabel][0]):
            self.__fillHeaderData(headerLabel,line)
            #header ends, data starts
            if headerLabel == "END OF HEADER":
              break
  
  def __fillHeaderData(self,headerLabel,line):
    """Fill the header's data with the parsed data from the current line."""
    self.mandatoryHeaders[headerLabel][2] = self.__parseFormat(
      line[:RinexHeader.HEADER_START],
      self.mandatoryHeaders[headerLabel][1]
    )

  def __isHeaderFromCurrentVersion(self,requiredVersion):
    """Check if the version required of the header that is currently being read is the version 
    of the file or a mandatory header for all RINEX versions

    Returns
    ----------
    bool
      True if the version required of the header is the version of the file or 
      a mandatory one for all RINEX versions and False otherwise
    """
    return requiredVersion == self.version or requiredVersion == "ALL"

  def isValidHeader(self):
    """Check if a RINEX header is valid.

    Returns
    ----------
    tuple(bool,enum)
      the bool is True if the header is valid and False otherwise. The enum 
      is the message, which indicates why the header is not valid
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
    """Check if the number of headers read is equal to the number of mandatory headers for the current version.

    Returns
    ----------
    bool
      True if the number of headers read is equal to the number of needed headers or False otherwise
    """
    # hasAllHeaders = True
    # for header in self.mandatoryHeaders:
    #   if self.mandatoryHeaders[header][0]
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
      three parts, as: `RTC`, where R is the number of times it should be repeated, T is the type of data it'll
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
    string : str
      the string to extract from

    Returns
    ----------
    tuple(integer,integer)
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

  @staticmethod
  def validityErrorToString(validityError):
    """Transform the validity error into a string error message.

    Parameters
    ----------
    validityError : enum
      The validity error

    Returns
    ----------
    string
      A validity error message
    """
    if validityError   == RinexHeader.VALIDITY_ERRORS.INVALID_NUMBER_OF_HEADERS:
      return "The rinex file doesn't contain the mandatory header lines!"
    elif validityError == RinexHeader.VALIDITY_ERRORS.INVALID_RECEIVER:
      return "The receiver of the rinex file is invalid!"
    elif validityError == RinexHeader.VALIDITY_ERRORS.INVALID_ANTENNA:
      return "The antenna of the rinex file is invalid!"
    elif validityError == RinexHeader.VALIDITY_ERRORS.INVALID_VERSION:
      supportedVersions = ", ".join([version for version in RinexHeader.ALLOWED_VERSIONS])
      return f"The version of the rinex file is invalid! (Supported versions are {supportedVersions})"
