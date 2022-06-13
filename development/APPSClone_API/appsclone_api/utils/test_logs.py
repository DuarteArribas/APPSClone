import unittest
import time
from logs import *

class TestLogs(unittest.TestCase):
  def test_format_message(self):
    logger = Logs("logs/logTest.log")
    print(logger._Logs__setLogMessage(Logs.SEVERITY.DEBUG,"My message"))
    print(logger._Logs__setLogMessage(Logs.SEVERITY.INFO,"My message2"))
    print(logger._Logs__setLogMessage(Logs.SEVERITY.WARNING,"My message3"))
    print(logger._Logs__setLogMessage(Logs.SEVERITY.ERROR,"My message4"))
    print(logger._Logs__setLogMessage(Logs.SEVERITY.CRITICAL,"My message5"))

  def test_logging(self):
    logger = Logs("logs/logTest.log")
    logger.writeLog(Logs.SEVERITY.DEBUG,"debug lol")
    logger.writeLog(Logs.SEVERITY.INFO,"info lol")
    logger.writeLog(Logs.SEVERITY.WARNING,"warning lol")
    logger.writeLog(Logs.SEVERITY.ERROR,"error lol")
    logger.writeLog(Logs.SEVERITY.CRITICAL,"critical lol")
    time.sleep(3)
    logger.writeLog(Logs.SEVERITY.INFO,"after 3 seconds")
if __name__ == '__main__':
  unittest.main()
