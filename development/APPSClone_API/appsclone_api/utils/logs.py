import datetime
import logging
import re
from enum import Enum

class Logs:
  """A logging system, that formats logs according to their severity.

  Attributes
  ----------
  SEVERITY     : enum
    The logs severity in an easier to write way
  MIN_NUM_LOGS : int
    The minimum number of logs allowed
  MAX_NUM_LOGS : int
    The maximum number of logs allowed 
  """
  # == Attributes ==
  SEVERITY     = Enum(
    'SEVERITY', 'DEBUG INFO WARNING ERROR CRITICAL'
  )
  MIN_NUM_LOGS = 100
  MAX_NUM_LOGS = 100000
  # == Methods ==
  def __init__(self,loggingFile,maxLogs):
    """Set the default configuration of the logging tool to write to a specific file with a specific format.
    
    Parameters
    ----------
    loggingFile : str
      The file to log to
    maxLogs     : int
      The max quantity of allowed logs. Older logs will be deleted if this number is surpassed, so 
      that the number of logs will not be more than maxLogs
    """
    self.loggingFile = loggingFile
    if maxLogs > Logs.MAX_NUM_LOGS:
      self.maxLogs = Logs.MAX_NUM_LOGS
    elif maxLogs < Logs.MIN_NUM_LOGS:
      self.maxLogs = Logs.MIN_NUM_LOGS
    else:
      self.maxLogs = maxLogs
    logging.basicConfig(level = logging.INFO,filename = loggingFile,format = "%(message)s")

  def writeLog(self,severity,message):
    """Write a log to a file, according to its severity. Debug logs are not 
    written, but are the default if the parameter is misspelled.

    Parameters
    ----------
    severity : enum
      The severity of the log
    message  : str
      The log message
    """
    formattedMessage = self.__setLogMessage(severity,message)
    if severity   == Logs.SEVERITY.DEBUG:
      logging.debug(formattedMessage)
    elif severity == Logs.SEVERITY.INFO:
      logging.info(formattedMessage)
    elif severity == Logs.SEVERITY.WARNING:
      logging.warning(formattedMessage)
    elif severity == Logs.SEVERITY.ERROR:
      logging.error(formattedMessage)
    elif severity == Logs.SEVERITY.CRITICAL:
      logging.critical(formattedMessage)
    else:
      logging.debug(formattedMessage)
    self.__sanitizeLogs()

  def __setLogMessage(self,severity,message):
    """Format the logging message, so that it stays aligned. The date, severity and message are logged.

    Parameters
    ----------
    severity : enum
      The severity of the log
    message  : str
      The log message
    """
    severityString = str(severity).split(".")[1]
    return f"{datetime.datetime.now()} ({severityString}){' '*(8-len(severityString))} | {message}"

  def __sanitizeLogs(self):
    """Sanitize logs, so that logs from APPS don't appear and that the file 
    is truncated if it exceedes the maximum amount of allowed logs."""
    newLoggingFile = ""
    with open(self.loggingFile,"r+") as f:
      lines = f.readlines()
      for line in lines:
        if re.search("^(\d\d\d\d-\d\d-\d\d)",line):
          newLoggingFile += line
      logsList = newLoggingFile.split("\n")
      if len(logsList) > self.maxLogs:
        logsList = logsList[len(logsList)-self.maxLogs:]
      newLoggingFile = "\n".join(logsList)
    with open(self.loggingFile,"w") as f:
      f.write(newLoggingFile)

# ✓    unit tested
# ✓ feature tested