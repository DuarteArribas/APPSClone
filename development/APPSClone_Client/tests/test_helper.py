import appsclone_client
import unittest
from appsclone_client.utils.helper import *

class TestHelper(unittest.TestCase):
  def test_validate_file_path(self):
    self.assertFalse(Helper.isValidAbsolutePath("/"))

  def test_validate_file_path2(self):
    self.assertFalse(Helper.isValidAbsolutePath("/a/"))

  def test_validate_file_path3(self):
    self.assertFalse(Helper.isValidAbsolutePath("/a/b/c/d/e/f/"))

  def test_validate_file_path4(self):
    self.assertFalse(Helper.isValidAbsolutePath("/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/b/c/d/e/f/g"))
  
  def test_validate_file_path5(self):
    self.assertFalse(Helper.isValidAbsolutePath("arroz"))

  def test_validate_file_path6(self):
    self.assertFalse(Helper.isValidAbsolutePath("arroz/massa/feijao"))

  def test_validate_file_path7(self):
    self.assertTrue(Helper.isValidAbsolutePath("/arroz"))

  def test_validate_file_path8(self):
    self.assertTrue(Helper.isValidAbsolutePath("/arroz/massa/c"))

  def test_validate_file_path9(self):
    self.assertTrue(Helper.isValidAbsolutePath("/arroz/massa//c"))
    
if __name__ == '__main__':
  unittest.main()