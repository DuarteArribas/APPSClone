import logging
import datetime
from enum import Enum

class Logs:
  SEVERITY = Enum(
    'SEVERITY', 'DEBUG INFO WARNING ERROR CRITICAL'
  )

  def __init__(self,loggingFile):
    logging.basicConfig(level = logging.INFO,filename = loggingFile,format = "%(message)s")

  def writeLog(self,severity,message):
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

  def __setLogMessage(self,severity,message):
    severityString = str(severity).split(".")[1]
    return f"{datetime.datetime.now()} ({severityString}){' '*(8-len(severityString))} | {message}"


