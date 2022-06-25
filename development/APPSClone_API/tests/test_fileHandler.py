import unittest
import warnings
from appsclone_api.fileHandler import *
from appsclone_api.connection  import *
from appsclone_api.utils.logs  import *

class TestFileHandler(unittest.TestCase):
  def test_handle_states_of_ids(self):
    warnings.filterwarnings(action = "ignore",message = "unclosed",category = ResourceWarning)
    logger = Logs("logs/logTest.log",1000)
    conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
    FileHandler.handleAllFileStates(conn,"queues/apps_id_queue_test","out/results_test")

  # def test_concatenate_file_to_path(self):
  #   self.assertEqual(FileHandler._concatenateFileToPath("arroz","aa/bb/cc"),"aa/bb/cc/arroz")

  # def test_get_file_from_path(self):
  #   self.assertEqual(FileHandler._getFileFromPath("arroz/massa/feijao"),"feijao")

  # def test_get_file_from_path2(self):
  #   self.assertEqual(FileHandler._getFileFromPath("arroz"),"arroz")

  # def test_get_file_from_path3(self):
  #   self.assertEqual(FileHandler._getFileFromPath("arroz/"),"")

  # def test_get_file_from_path4(self):
  #   self.assertEqual(FileHandler._getFileFromPath(""),"")

  # def test_clean_empty_strs_from_list(self):
  #   self.assertEqual(FileHandler._cleanEmptyFieldsInList(["a","b","c"]),["a","b","c"])

  # def test_clean_empty_strs_from_list2(self):
  #   self.assertEqual(FileHandler._cleanEmptyFieldsInList(["a","b"," "]),["a","b"])

  # def test_clean_empty_strs_from_list3(self):
  #   self.assertEqual(FileHandler._cleanEmptyFieldsInList(["a","b"," ","c","   d","           "]),["a","b","c","   d"])

  # def test_clean_empty_strs_from_list4(self):
  #   self.assertEqual(FileHandler._cleanEmptyFieldsInList([""]),[])

  # def test_clean_empty_strs_from_list5(self):
  #   self.assertEqual(FileHandler._cleanEmptyFieldsInList([]),[])

  # def test_is_valid_ipv4(self):
  #   self.assertFalse(FileHandler._isValidIpv4(""))

  # def test_is_valid_ipv42(self):
  #   self.assertTrue(FileHandler._isValidIpv4("123.111.222.121"))

  # def test_is_valid_ipv43(self):
  #   self.assertTrue(FileHandler._isValidIpv4("123.12.222.121"))

  # def test_is_valid_ipv44(self):
  #   self.assertFalse(FileHandler._isValidIpv4("2.1.2.1.1"))

  # def test_is_valid_ipv45(self):
  #   self.assertFalse(FileHandler._isValidIpv4("2.1.2.1."))

  # def test_is_valid_ipv46(self):
  #   self.assertFalse(FileHandler._isValidIpv4("2.1.2"))

  # def test_is_valid_ipv47(self):
  #   self.assertFalse(FileHandler._isValidIpv4("2.1.2."))

  # def test_is_valid_ipv48(self):
  #   self.assertFalse(FileHandler._isValidIpv4("192.168.8.256"))

  # def test_is_valid_ipv49(self):
  #   self.assertTrue(FileHandler._isValidIpv4("0.0.0.0"))

  # def test_is_valid_upload_file(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertFalse(FileHandler._isValidUploadFile("in/test/arroz",logger))

  # def test_is_valid_upload_file2(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertFalse(FileHandler._isValidUploadFile("in/test/lol",logger))

  # def test_is_valid_upload_file3(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile",logger))

  # def test_is_valid_upload_file4(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile2",logger))

  # def test_is_valid_upload_file5(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile3",logger))

  # def test_is_valid_upload_file6(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile4",logger))

  # def test_is_valid_upload_file7(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile5",logger))

  # def test_is_valid_upload_file8(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile6",logger))

  # def test_is_valid_upload_file9(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile7",logger))

  # def test_is_valid_upload_file10(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertTrue(FileHandler._isValidUploadFile("in/test/uploadFile8",logger))

  # def test_is_valid_upload_file11(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile9",logger))

  # def test_is_valid_upload_file12(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile10",logger))

  # def test_is_valid_upload_file13(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertTrue(FileHandler._isValidUploadFile("in/test/uploadFile11",logger))

  # def test_is_valid_upload_file14(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertTrue(FileHandler._isValidUploadFile("in/test/uploadFile12",logger))

  # def test_is_valid_upload_file15(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertTrue(FileHandler._isValidUploadFile("in/test/uploadFile13",logger))

  # def test_is_valid_upload_file16(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile14",logger))

  # def test_is_valid_upload_file17(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertTrue(FileHandler._isValidUploadFile("in/uploadFilesTest/1/uploadFile1",logger))

  # def test_get_validated_list_of_uploadFiles(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertEqual(FileHandler._getUploadFiles("in/uploadFilesTest/1",logger),["uploadFile1","uploadFile2","uploadFile3","uploadFile4","uploadFile5"])

  # def test_get_validated_list_of_uploadFiles2(self):
  #   logger = Logs("logs/logTest2.log",1000)
  #   self.assertEqual(FileHandler._getUploadFiles("in/uploadFilesTest/2",logger),["uploadFile1","uploadFile4"])

  #def test_parse_upload_file(self):
  #  logger = Logs("logs/logTest2.log",1000)
  #  self.assertEqual(FileHandler._parseUploadFile("in/uploadFilesTest/1/uploadFile1"),("~/arroz","~","138.68.128.182"))

  #def test_parse_upload_file2(self):
  #  logger = Logs("logs/logTest2.log",1000)
  #  self.assertEqual(FileHandler._parseUploadFile("in/uploadFilesTest/2/uploadFile4"),("aaa","massa","192.168.8.1"))

  #def test_download_rinex_file(self):
  #  logger   = Logs("logs/logTest2.log",1000)
  #  password = input("Password:")
  #  user     = UserSSHClient("root",password)
  #  FileHandler._downloadRinexFile("~/arroz","out/results_test_test","138.68.128.182",22,user,logger)

  #def test_download_rinex_file2(self):
  #  logger = Logs("logs/logTest2.log",1000)
  #  password = input("Password:")
  #  user = UserSSHClient("root",password)
  #  FileHandler._downloadRinexFile("~/arroz","out/results_test_test","138.68.128.181",22,user,logger)

  #def test_download_rinex_file3(self):
  #  logger = Logs("logs/logTest2.log",1000)
  #  password = input("Password:")
  #  user = UserSSHClient("root",password)
  #  FileHandler._downloadRinexFile("~/arroz","out/results_test_test","138.68.128.182",21,user,logger)

  #def test_download_rinex_file4(self):
  #  logger = Logs("logs/logTest2.log",1000)
  #  password = input("Password:")
  #  user = UserSSHClient("roota",password)
  #  FileHandler._downloadRinexFile("~/arroz","out/results_test_test","138.68.128.182",22,user,logger)

  #def test_download_rinex_file5(self):
  #  logger = Logs("logs/logTest2.log",1000)
  #  password = input("Password (wrong):")
  #  user = UserSSHClient("root",password)
  #  FileHandler._downloadRinexFile("~/arroz","out/results_test_test","138.68.128.182",22,user,logger)

  #def test_download_rinex_file6(self):
  #  logger = Logs("logs/logTest2.log",1000)
  #  password = input("Password:")
  #  user = UserSSHClient("root",password)
  #  FileHandler._downloadRinexFile("~/arroza","out/results_test_test","138.68.128.182",22,user,logger)

  #def test_add_to_queue(self):
  #  logger = Logs("logs/logTest2.log",1000)
  #  FileHandler._addFileToQueueUploadFiles("out/queue/uploadFilesQueue","arroz","aa/bb/cc","192.168.8.2",22,logger)

  #def test_download_files(self):
  #  logger = Logs("logs/logTest2.log",1000)
  #  FileHandler.downloadRinexFiles("in/uploadFilesTest/1","out/results_test_test","out/queue/uploadFilesQueue",logger)

  #def test_get_line_from_queue(self):
  #  self.assertEqual(FileHandler._getFileLineFromQueueUploadFiles("out/queue/uploadFilesQueue","arroz_results.tar.gz"),"arroz ~ 138.68.128.181 22\n")

  #def test_get_line_from_queue2(self):
  #  self.assertEqual(FileHandler._getFileLineFromQueueUploadFiles("out/queue/uploadFilesQueue","aarroz_results.tar.gz"),None)

  #def test_remove_line_from_queue(self):
  #  FileHandler._removeFileFromQueueUploadFiles("out/queue/uploadFilesQueue","massaaaa")

  #def test_upload_results_file(self):
  #  password = input("Password:")
  #  user     = UserSSHClient("root",password)
  #  logger   = Logs("logs/logTest2.log",1000)
  #  FileHandler._uploadResultsFile("out/results_test_test/lol.tar.gz","~","138.68.128.182",22,user,logger)

  #def test_upload_all_results(self):
  #  logger   = Logs("logs/logTest2.log",1000)
  #  FileHandler.uploadBackResults("out/queue/uploadFilesQueue","out/resultsDir",logger)

  # def test_upload_all_rinex(self):
  #   logger   = Logs("logs/logTest2.log",1000)
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
  #   FileHandler.uploadAllRinexToApps(conn,"in/test2","out/queue/queue",args,logger)

if __name__ == '__main__':
  unittest.main()