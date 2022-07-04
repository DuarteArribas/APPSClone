import appsclone_uploadFileGenerator
import unittest
from appsclone_uploadFileGenerator.utils.helper import *

class TestHelper(unittest.TestCase):
  def test_validate_file_path(self):
    self.assertFalse(Helper.isValidAbsolutePathToFile(""))

  def test_validate_file_path2(self):
    self.assertFalse(Helper.isValidAbsolutePathToFile("/"))

  def test_validate_file_path3(self):
    self.assertFalse(Helper.isValidAbsolutePathToFile("/a/"))

  def test_validate_file_path4(self):
    self.assertFalse(Helper.isValidAbsolutePathToFile("/a/b/c/d/e/f/"))

  def test_validate_file_path5(self):
    self.assertFalse(Helper.isValidAbsolutePathToFile("/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/b/c/d/e/f/g"))
  
  def test_validate_file_path6(self):
    self.assertFalse(Helper.isValidAbsolutePathToFile("arroz"))

  def test_validate_file_path7(self):
    self.assertFalse(Helper.isValidAbsolutePathToFile("arroz/massa/feijao"))

  def test_validate_file_path8(self):
    self.assertTrue(Helper.isValidAbsolutePathToFile("/arroz"))

  def test_validate_file_path9(self):
    self.assertTrue(Helper.isValidAbsolutePathToFile("/arroz/massa/c"))

  def test_validate_file_path10(self):
    self.assertTrue(Helper.isValidAbsolutePathToFile("/arroz/massa//c"))

  def test_validate_file_path11(self):
    self.assertTrue(Helper.isValidAbsolutePathToFile("~/arroz/massa//c"))

  def test_validate_file_path_to_dir_(self):
    self.assertFalse(Helper.isValidAbsolutePathToDir(""))

  def test_validate_file_path_to_dir_2(self):
    self.assertTrue(Helper.isValidAbsolutePathToDir("/"))

  def test_validate_file_path_to_dir_3(self):
    self.assertTrue(Helper.isValidAbsolutePathToDir("/a/"))

  def test_validate_file_path_to_dir_4(self):
    self.assertTrue(Helper.isValidAbsolutePathToDir("/a/b/c/d/e/f/"))

  def test_validate_file_path_to_dir_5(self):
    self.assertFalse(Helper.isValidAbsolutePathToDir("/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/b/c/d/e/f/g"))
  
  def test_validate_file_path_to_dir_6(self):
    self.assertFalse(Helper.isValidAbsolutePathToDir("arroz"))

  def test_validate_file_path_to_dir_7(self):
    self.assertFalse(Helper.isValidAbsolutePathToDir("arroz/massa/feijao"))

  def test_validate_file_path_to_dir_8(self):
    self.assertTrue(Helper.isValidAbsolutePathToDir("/arroz"))

  def test_validate_file_path_to_dir_9(self):
    self.assertTrue(Helper.isValidAbsolutePathToDir("/arroz/massa/c"))

  def test_validate_file_path_to_dir_10(self):
    self.assertTrue(Helper.isValidAbsolutePathToDir("/arroz/massa//c"))

  def test_validate_file_path_to_dir_11(self):
    self.assertTrue(Helper.isValidAbsolutePathToDir("~/arroz/massa//c"))

if __name__ == '__main__':
  unittest.main()