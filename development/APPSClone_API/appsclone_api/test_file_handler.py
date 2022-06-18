import unittest
from fileHandler import *

class TestFileHandler(unittest.TestCase):
  def test_clean_empty_strs_from_list(self):
    self.assertEqual(FileHandler._cleanEmptyFieldsInList(["a","b","c"]),["a","b","c"])

  def test_clean_empty_strs_from_list2(self):
    self.assertEqual(FileHandler._cleanEmptyFieldsInList(["a","b"," "]),["a","b"])

  def test_clean_empty_strs_from_list3(self):
    self.assertEqual(FileHandler._cleanEmptyFieldsInList(["a","b"," ","c","   d","           "]),["a","b","c","   d"])

  def test_clean_empty_strs_from_list4(self):
    self.assertEqual(FileHandler._cleanEmptyFieldsInList([""]),[])

  def test_clean_empty_strs_from_list5(self):
    self.assertEqual(FileHandler._cleanEmptyFieldsInList([]),[])

  def test_is_valid_ipv4(self):
    self.assertFalse(FileHandler._isValidIpv4(""))

  def test_is_valid_ipv42(self):
    self.assertTrue(FileHandler._isValidIpv4("123.111.222.121"))

  def test_is_valid_ipv43(self):
    self.assertTrue(FileHandler._isValidIpv4("123.12.222.121"))

  def test_is_valid_ipv44(self):
    self.assertFalse(FileHandler._isValidIpv4("2.1.2.1.1"))

  def test_is_valid_ipv45(self):
    self.assertFalse(FileHandler._isValidIpv4("2.1.2.1."))

  def test_is_valid_ipv46(self):
    self.assertFalse(FileHandler._isValidIpv4("2.1.2"))

  def test_is_valid_ipv47(self):
    self.assertFalse(FileHandler._isValidIpv4("2.1.2."))

  def test_is_valid_ipv48(self):
    self.assertFalse(FileHandler._isValidIpv4("192.168.8.256"))

  def test_is_valid_ipv49(self):
    self.assertTrue(FileHandler._isValidIpv4("0.0.0.0"))

  def test_is_valid_upload_file(self):
    self.assertFalse(FileHandler._isValidUploadFile("in/test/arroz"))

  def test_is_valid_upload_file2(self):
    self.assertFalse(FileHandler._isValidUploadFile("in/test/lol"))

  def test_is_valid_upload_file3(self):
    self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile"))

  def test_is_valid_upload_file4(self):
    self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile2"))

  def test_is_valid_upload_file5(self):
    self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile3"))

  def test_is_valid_upload_file6(self):
    self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile4"))

  def test_is_valid_upload_file7(self):
    self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile5"))

  def test_is_valid_upload_file8(self):
    self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile6"))

  def test_is_valid_upload_file9(self):
    self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile7"))

  def test_is_valid_upload_file10(self):
    self.assertTrue(FileHandler._isValidUploadFile("in/test/uploadFile8"))

  def test_is_valid_upload_file11(self):
    self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile9"))

  def test_is_valid_upload_file12(self):
    self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile10"))

  def test_is_valid_upload_file13(self):
    self.assertTrue(FileHandler._isValidUploadFile("in/test/uploadFile11"))

  def test_is_valid_upload_file14(self):
    self.assertTrue(FileHandler._isValidUploadFile("in/test/uploadFile12"))

  def test_is_valid_upload_file15(self):
    self.assertTrue(FileHandler._isValidUploadFile("in/test/uploadFile13"))

  def test_is_valid_upload_file16(self):
    self.assertFalse(FileHandler._isValidUploadFile("in/test/uploadFile14"))

  def test_is_valid_upload_file17(self):
    self.assertTrue(FileHandler._isValidUploadFile("in/uploadFilesTest/1/uploadFile1"))

  def test_concatenate_file_to_path(self):
    self.assertEqual(FileHandler._concatenateFileToPath("arroz","aa/bb/cc"),"aa/bb/cc/arroz")

  def test_get_validated_list_of_uploadFiles(self):
    self.assertEqual(FileHandler.getUploadFiles("in/uploadFilesTest/1"),["uploadFile1","uploadFile2","uploadFile3","uploadFile4","uploadFile5"])

  def test_get_validated_list_of_uploadFiles2(self):
    self.assertEqual(FileHandler.getUploadFiles("in/uploadFilesTest/2"),["uploadFile1","uploadFile4"])

if __name__ == '__main__':
  unittest.main()