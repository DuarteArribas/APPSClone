import unittest
from rinexHeader import *

class TestRinexheader(unittest.TestCase):
  def test_rinex_read(self):
    header = RinexHeader()
    header.readHeader("in/uploads/CVTY2720.21D")
    print(header.header)

if __name__ == '__main__':
  unittest.main()
