import logging
import datetime
from enum import Enum
class Logs:
  """A logging system, that formats logs according to their severity.

  Attributes
  ----------
  SEVERITY : enum
    Represents the logs severity in an easier to write way
  """
  # == Attributes ==
  SEVERITY = Enum(
    'SEVERITY', 'DEBUG INFO WARNING ERROR CRITICAL'
  )
  # == Methods ==
  def __init__(self,loggingFile):
    """Set the default configuration of the logging tool to write to a specific file with a specific format."""
    logging.basicConfig(level = logging.INFO,filename = loggingFile,format = "%(message)s")

  def writeLog(self,severity,message):
    """Write a log to a file, according to its severity. Debug logs are not written, but are the default, if
       the parameter is misspelled.

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

  def __setLogMessage(self,severity,message):
    """Formats the logging message, so that it stays aligned and the date, severity and message are logged.

    Parameters
    ----------
    severity : enum
      The severity of the log
    message  : str
      The log message
    """
    severityString = str(severity).split(".")[1]
    return f"{datetime.datetime.now()} ({severityString}){' '*(8-len(severityString))} | {message}"