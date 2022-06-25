import unittest
import time
from appsclone_api.utils.logs import *

class TestLogs(unittest.TestCase):
  def test_format_message(self):
    print(Logs._setLogMsg(Logs.SEVERITY.DEBUG,"My message"))
    print(Logs._setLogMsg(Logs.SEVERITY.INFO,"My message2"))
    print(Logs._setLogMsg(Logs.SEVERITY.WARNING,"My message3"))
    print(Logs._setLogMsg(Logs.SEVERITY.ERROR,"My message4"))
    print(Logs._setLogMsg(Logs.SEVERITY.CRITICAL,"My message5"))

  def test_logging(self):
    logger = Logs("logs/logTest.log",1000)
    logger._Logs__writeLog(Logs.SEVERITY.DEBUG,"debug lol")
    logger._Logs__writeLog(Logs.SEVERITY.INFO,"info lol")
    logger._Logs__writeLog(Logs.SEVERITY.WARNING,"warning lol")
    logger._Logs__writeLog(Logs.SEVERITY.ERROR,"error lol")
    logger._Logs__writeLog(Logs.SEVERITY.CRITICAL,"critical lol")
    time.sleep(3)
    logger._Logs__writeLog(Logs.SEVERITY.INFO,"after 3 seconds")

  def test_log_regex(self):
    self.assertTrue(re.search("^(\d\d\d\d-\d\d-\d\d)","2022-06-14 19:20:43.448246 (INFO)     | An attempt to test the connection with APPS was made."))

  def test_log_regex2(self):
    self.assertFalse(re.search("^(\d\d\d\d-\d\d-\d\d)","Establishing client interface to https://pppx.gdgps.net//api/user"))

  def test_log_regex3(self):
    self.assertFalse(re.search("^(\d\d\d\d-\d\d-\d\d)","arrozEstablishing client interface to https://pppx.gdgps.net//api/user"))

  def test_get_log_msg(self):
    self.assertEqual(Logs._getLogMsg(Logs.LOG_TYPE.SUBROUTINE_START,"arroz"),"== arroz (START) ==")

  def test_write_routine(self):
    logger = Logs("logs/logTest.log",1000)
    logger.writeRoutineLog("infoRoutineStart",Logs.ROUTINE_STATUS.START)

  def test_write_routine2(self):
    logger = Logs("logs/logTest.log",1000)
    logger.writeRoutineLog("infoRoutineEnd",Logs.ROUTINE_STATUS.END)

  def test_write_subroutine(self):
    logger = Logs("logs/logTest.log",1000)
    logger.writeSubroutineLog("infoSubroutineStart",Logs.ROUTINE_STATUS.START)

  def test_write_subroutine2(self):
    logger = Logs("logs/logTest.log",1000)
    logger.writeSubroutineLog("infoSubroutineEnd",Logs.ROUTINE_STATUS.END)

  def test_write_subsubroutine(self):
    logger = Logs("logs/logTest.log",1000)
    logger.writeSubsubroutineLog("infoSubsubroutineStart",Logs.ROUTINE_STATUS.START)

  def test_write_subroutine2(self):
    logger = Logs("logs/logTest.log",1000)
    logger.writeSubsubroutineLog("infoSubsubroutineEnd",Logs.ROUTINE_STATUS.END)

  def test_write_regular_log(self):
    logger = Logs("logs/logTest.log",1000)
    logger.writeRegularLog(Logs.SEVERITY.INFO,"regularInfo")
if __name__ == '__main__':
  unittest.main()