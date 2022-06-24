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

if __name__ == '__main__':
  unittest.main()