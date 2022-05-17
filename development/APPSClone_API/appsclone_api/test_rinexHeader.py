import unittest
from rinexHeader import *

class TestRinexheader(unittest.TestCase):
  def test_rinex_validity1(self):
    header = RinexHeader()
    header.readHeader("in/uploads/CVTY2720.21D")
    self.assertTrue(header.isValidHeader())

  def test_rinex_validity2(self):
    header = RinexHeader()
    header.readHeader("in/uploads/fileTest")
    self.assertFalse(header.isValidHeader())

  def test_rinex_validity3(self):
    header = RinexHeader()
    header.readHeader("in/uploads/fileTest2")
    self.assertFalse(header.isValidHeader())

if __name__ == '__main__':
  unittest.main()
