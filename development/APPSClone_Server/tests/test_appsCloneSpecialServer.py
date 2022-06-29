import appsclone_server
import unittest
import warnings
from appsclone_server.appsCloneSpecialServer import *
from appsclone_server.connection             import *
from appsclone_server.utils.logs             import *

class TestAPPSCloneSpecialServer(unittest.TestCase):
  def test_handle_states_of_ids(self):
    warnings.filterwarnings(action = "ignore",message = "unclosed",category = ResourceWarning)
    logger = Logs("logs/logTest.log",1000)
    conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
    APPSCloneSpecialServer.handleAllFileStates(conn,"queues/apps_id_queue_test","out/results_test",logger)

  def test_get_line_from_queue(self):
    self.assertEqual(APPSCloneSpecialServer._getResultLineFromRinexQueue("queues/rinex_queue_test","arroz_results.tar.gz"),"arroz ~ 138.68.128.183 22 aa bb\n")

  def test_get_line_from_queue2(self):
    self.assertEqual(APPSCloneSpecialServer._getResultLineFromRinexQueue("queues/rinex_queue_test","aarroz_results.tar.gz"),None)

  # def test_remove_line_from_queue(self):
  #   logger = Logs("logs/logTest.log",1000)
  #   APPSCloneSpecialServer._removeFileFromRinexQueue("queues/rinex_queue_test","feijao_results.tar.gz",logger)

  # def test_upload_back_all_results(self):
  #   logger   = Logs("logs/logTest.log",1000)
  #   APPSCloneSpecialServer.uploadBackResults("queues/rinex_queue_test","out/results_test","root","Pr0j#to_Spr1ng",logger)

  def test_get_already_uploaded_files(self):
    self.assertEqual(APPSCloneSpecialServer._getAlreadyUploadedFilenames("queues/rinex_queue_test"),["arro","arroz"])

  def test_is_valid_upload_file(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertFalse(APPSCloneSpecialServer._isValidUploadFile("in/test/arroz",logger))

  def test_is_valid_upload_file2(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertFalse(APPSCloneSpecialServer._isValidUploadFile("in/test/lol",logger))

  def test_is_valid_upload_file3(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertFalse(APPSCloneSpecialServer._isValidUploadFile("in/test/uploadFile",logger))

  def test_is_valid_upload_file4(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertFalse(APPSCloneSpecialServer._isValidUploadFile("in/test/uploadFile2",logger))

  def test_is_valid_upload_file5(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertTrue(APPSCloneSpecialServer._isValidUploadFile("in/test/uploadFile3",logger))

  def test_is_valid_upload_file6(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertTrue(APPSCloneSpecialServer._isValidUploadFile("in/test/uploadFile4",logger))

  def test_is_valid_upload_file7(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertFalse(APPSCloneSpecialServer._isValidUploadFile("in/test/uploadFile5",logger))

  def test_is_valid_upload_file8(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertFalse(APPSCloneSpecialServer._isValidUploadFile("in/test/uploadFile6",logger))

  def test_is_valid_upload_file9(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertFalse(APPSCloneSpecialServer._isValidUploadFile("in/test/uploadFile7",logger))

  def test_is_valid_upload_file10(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertTrue(APPSCloneSpecialServer._isValidUploadFile("in/test/uploadFile8",logger))

  def test_is_valid_upload_file11(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertFalse(APPSCloneSpecialServer._isValidUploadFile("in/test/uploadFile9",logger))

  def test_is_valid_upload_file12(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertFalse(APPSCloneSpecialServer._isValidUploadFile("in/test/uploadFile10",logger))

  def test_is_valid_upload_file13(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertTrue(APPSCloneSpecialServer._isValidUploadFile("in/test/uploadFile11",logger))

  def test_is_valid_upload_file14(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertTrue(APPSCloneSpecialServer._isValidUploadFile("in/test/uploadFile12",logger))

  def test_is_valid_upload_file15(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertTrue(APPSCloneSpecialServer._isValidUploadFile("in/test/uploadFile13",logger))

  def test_is_valid_upload_file16(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertTrue(APPSCloneSpecialServer._isValidUploadFile("in/test/uploadFile14",logger))

  def test_get_validated_list_of_uploadFiles(self):
    logger = Logs("logs/logTest.log",1000)
    self.assertEqual(APPSCloneSpecialServer._getUploadFiles("in/to_download_test/1",logger),["uploadFile1","uploadFile2","uploadFile3","uploadFile4","uploadFile5"])

  def test_parse_upload_file(self):
   self.assertEqual(APPSCloneSpecialServer._parseUploadFile("in/test/uploadFile1"),("arroz","massa","192.168.8.255","root","Pr0j#to_Spr1ng"))

  def test_parse_upload_file2(self):
   self.assertEqual(APPSCloneSpecialServer._parseUploadFile("in/test/uploadFile4"),("aaa","massa","192.168.8.1","aa","bb"))

  # def test_add_to_queue(self):
  #   logger = Logs("logs/logTest.log",1000)
  #   APPSCloneSpecialServer._addFileToRinexQueue("queues/rinex_queue_test","arroz","aa/bb/cc","192.168.8.2",22,"aa","bb",logger)

  # def test_download_files(self):
  #   logger = Logs("logs/logTest.log",1000)
  #   APPSCloneSpecialServer.downloadRinexFiles(
  #     "in/to_download_test",
  #     "in/to_upload_test",
  #     "queues/rinex_queue_test",
  #     "root",
  #     "Pr0j#to_Spr1ng",
  #     logger
  #   )

  # def test_upload_all_rinex(self):
  #   logger   = Logs("logs/logTest.log",1000)
  #   args = {
  #     "pressure"             : None,
  #     "attitude"             : None,
  #     "email"                : defines.Data.EMAIL_NOTIFY_DEFAULT,
  #     "access"               : defines.Data.ACCESS_DEFAULT,
  #     "processing_mode"      : defines.GIPSYData.PROCESSING_MODE_DEFAULT,
  #     "product"              : "arroz",
  #     "troposphere_model"    : defines.GIPSYData.TROP_GMF,
  #     "ocean_loading"        : True,
  #     "model_tides"          : True,
  #     "elev_dep_weighting"   : defines.GIPSYData.ROOT_SINE,
  #     "elev_angle_cutoff"    : 7.5,
  #     "solution_period"      : 300,
  #     "generate_quaternions" : False,
  #   }
  #   conn = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
  #   APPSCloneSpecialServer.uploadAllRinexToApps(conn,"in/to_upload_test","queues/apps_id_queue_test",args,logger)

if __name__ == '__main__':
  unittest.main()