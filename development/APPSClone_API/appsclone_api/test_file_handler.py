import unittest
from fileHandler import *

class TestFileHandler(unittest.TestCase):
  def test_clean_empty_strs_from_list(self):
    self.assertEqual(FileHandler.cleanEmptyFieldsInList(["a","b","c"]),["a","b","c"])

  def test_clean_empty_strs_from_list2(self):
    self.assertEqual(FileHandler.cleanEmptyFieldsInList(["a","b"," "]),["a","b"])

  def test_clean_empty_strs_from_list3(self):
    self.assertEqual(FileHandler.cleanEmptyFieldsInList(["a","b"," ","c","   d","           "]),["a","b","c","   d"])

  def test_clean_empty_strs_from_list4(self):
    self.assertEqual(FileHandler.cleanEmptyFieldsInList([""]),[])

  def test_clean_empty_strs_from_list5(self):
    self.assertEqual(FileHandler.cleanEmptyFieldsInList([]),[])

if __name__ == '__main__':
  unittest.main()