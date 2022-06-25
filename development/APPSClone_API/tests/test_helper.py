import appsclone_api
import unittest
from appsclone_api.utils.helper import *

class TestHelper(unittest.TestCase):
  def test_remove_duplicated_forward_slashes(self):
    self.assertEqual(Helper._removeDuplicatedForwardSlashes("//a/b/c/d/e//f/g/h/i/j//////k/l/m//"),"/a/b/c/d/e/f/g/h/i/j/k/l/m/")

  def test_remove_duplicated_forward_slashes2(self):
    self.assertEqual(Helper._removeDuplicatedForwardSlashes("//"),"/")

  def test_remove_duplicated_forward_slashes3(self):
    self.assertEqual(Helper._removeDuplicatedForwardSlashes(""),"")

  def test_remove_duplicated_forward_slashes4(self):
    self.assertEqual(Helper._removeDuplicatedForwardSlashes("ab"),"ab")

  def test_remove_duplicated_forward_slashes5(self):
    self.assertEqual(Helper._removeDuplicatedForwardSlashes("/"),"/")

  def test_join_path_to_file(self):
    self.assertEqual(Helper.joinPathFile("arroz/massa/feijao","grao"),"arroz/massa/feijao/grao")

  def test_join_path_to_file2(self):
    self.assertEqual(Helper.joinPathFile("arroz/massa/feijao","grao/vinagre"),"arroz/massa/feijao/grao/vinagre")

  def test_join_path_to_file3(self):
    self.assertEqual(Helper.joinPathFile("arroz/massa/feijao/","grao/vinagre"),"arroz/massa/feijao/grao/vinagre")

  def test_join_path_to_file4(self):
    self.assertEqual(Helper.joinPathFile("arroz/massa/feijao","/grao/vinagre"),"arroz/massa/feijao/grao/vinagre")

  def test_join_path_to_file5(self):
    self.assertEqual(Helper.joinPathFile("","grao"),"grao")

  def test_join_path_to_file6(self):
    self.assertEqual(Helper.joinPathFile("",""),"")

  def test_join_path_to_file7(self):
    self.assertEqual(Helper.joinPathFile("/","grao"),"/grao")

  def test_get_file_from_path(self):
    self.assertEqual(Helper.getFileFromPath("/"),"")

  def test_get_file_from_path2(self):
    self.assertEqual(Helper.getFileFromPath(""),"")

  def test_get_file_from_path3(self):
    self.assertEqual(Helper.getFileFromPath("/arroz/massa"),"massa")

  def test_get_file_from_path4(self):
    self.assertEqual(Helper.getFileFromPath("massa"),"massa")

  def test_get_file_from_path5(self):
    self.assertEqual(Helper.getFileFromPath("."),".")

  def test_convert_bytes_to_mb(self):
    self.assertEqual(Helper.bytesToMB(1000),0.001)

  def test_convert_bytes_to_mb2(self):
    self.assertEqual(Helper.bytesToMB(200),0.000)

  def test_convert_bytes_to_mb3(self):
    self.assertEqual(Helper.bytesToMB(10000),0.010)

  def test_is_gzip_compressed(self):
    self.assertTrue(Helper._checkCompressedWithGzip("in/test/file.gz"))

  def test_is_gzip_compressed2(self):
    self.assertFalse(Helper._checkCompressedWithGzip("in/test/file"))

  def test_gzip_compression(self):
    self.assertEqual(Helper.compressUncompressGzip("in/test/arroz",True),"in/test/arroz.gz")

  def test_gzip_uncompression(self):
    self.assertEqual(Helper.compressUncompressGzip("in/test/arroz.gz",False),"in/test/arroz")

  def test_get_uncompressed_file(self):
    self.assertEqual(Helper.getUncompressedFile("in/test/arroz.gz"),"in/test/arroz")

  def test_clean_empty_strs_from_list(self):
    self.assertEqual(Helper.cleanEmptyFieldsInList(["a","b","c"]),["a","b","c"])

  def test_clean_empty_strs_from_list2(self):
    self.assertEqual(Helper.cleanEmptyFieldsInList(["a","b"," "]),["a","b"])

  def test_clean_empty_strs_from_list3(self):
    self.assertEqual(Helper.cleanEmptyFieldsInList(["a","b"," ","c","   d","           "]),["a","b","c","   d"])

  def test_clean_empty_strs_from_list4(self):
    self.assertEqual(Helper.cleanEmptyFieldsInList([""]),[])

  def test_clean_empty_strs_from_list5(self):
    self.assertEqual(Helper.cleanEmptyFieldsInList([]),[])

  def test_is_valid_ipv4(self):
    self.assertFalse(Helper.isValidIpv4(""))

  def test_is_valid_ipv42(self):
    self.assertTrue(Helper.isValidIpv4("123.111.222.121"))

  def test_is_valid_ipv43(self):
    self.assertTrue(Helper.isValidIpv4("123.12.222.121"))

  def test_is_valid_ipv44(self):
    self.assertFalse(Helper.isValidIpv4("2.1.2.1.1"))

  def test_is_valid_ipv45(self):
    self.assertFalse(Helper.isValidIpv4("2.1.2.1."))

  def test_is_valid_ipv46(self):
    self.assertFalse(Helper.isValidIpv4("2.1.2"))

  def test_is_valid_ipv47(self):
    self.assertFalse(Helper.isValidIpv4("2.1.2."))

  def test_is_valid_ipv48(self):
    self.assertFalse(Helper.isValidIpv4("192.168.8.256"))

  def test_is_valid_ipv49(self):
    self.assertTrue(Helper.isValidIpv4("0.0.0.0"))

if __name__ == '__main__':
  unittest.main()