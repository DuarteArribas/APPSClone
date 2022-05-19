import unittest
from rinexHeader import *

class TestRinexheader(unittest.TestCase):
  def test_rinex_validity1(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/uploads/CVTY2720.21D")
    self.assertTrue(header.isValidHeader())

  def test_rinex_validity2(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/uploads/fileTest")
    self.assertFalse(header.isValidHeader())

  def test_rinex_validity3(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/uploads/fileTest2")
    self.assertFalse(header.isValidHeader())

  def test_string_extractor(self):
    header = RinexHeader()
    self.assertEqual(header.extractIntUntilString("1234abc123"),1234)

  def test_string_extractor2(self):
    header = RinexHeader()
    self.assertEqual(header.extractIntUntilString("1234"),1234)

  def test_string_extractor3(self):
    header = RinexHeader()
    self.assertEqual(header.extractIntUntilString(""),0)

  def test_string_extractor4(self):
    header = RinexHeader()
    self.assertEqual(header.extractIntUntilString("abc"),0)
  # def test_rinex_format_version(self):
  #   header = RinexHeader()
  #   self.assertEqual(header.parseFormat("     2.11           OBSERVATION DATA    M (MIXED)           ","1F9.2,11X,1A1,19X,1A1,19X"),["2.11",""])

  # def test_rinex_format_pgm(self):
  #   header = RinexHeader()
  #   self.assertEqual(header.parseFormat("teqc  2019Feb25                         20211001 13:13:56UTC","3A20"),["teqc  2019Feb25","","20211001 13:13:56UTC"])

  # def test_rinex_format_markerName(self):
  #   header = RinexHeader()
  #   self.assertEqual(header.parseFormat("CVTY                                                        ","1A20"),["CVTY"])

  # def test_rinex_format_observerAgency(self):
  #   header = RinexHeader()
  #   self.assertEqual(header.parseFormat("RFGH                SEGAL                                   ","1A20,1A60"),["RFGH","SEGAL"])

  # def test_rinex_format_receiver(self):
  #   header = RinexHeader()
  #   self.assertEqual(header.parseFormat("3055025             SEPT POLARX5        5.3.2               ","3A20"),["3055025","SEPT POLARX5","5.3.2"])

  # def test_rinex_format_antenna(self):
  #   header = RinexHeader()
  #   self.assertEqual(header.parseFormat("1909270030          TWIVP6050_CONE  NONE                    ","2A20"),["1909270030","TWIVP6050_CONE  NONE"])

  # def test_rinex_format_approxPosXYZ(self):
  #   header = RinexHeader()
  #   self.assertEqual(header.parseFormat("  6378137.0000        0.0000        0.0000                  ","3F14.4"),["6378137.0000","0.0000","0.0000"])

  # def test_rinex_format_antennaDeltaHEN(self):
  #   header = RinexHeader()
  #   self.assertEqual(header.parseFormat("        0.9100        0.0000        0.0000                  ","3F14.4"),["0.9100","0.0000","0.0000"])

  # def test_rinex_format_timeOfFirstObs(self):
  #   header = RinexHeader()
  #   self.assertEqual(header.parseFormat("  2021     9    29     0     0    0.0000000     GPS         ","5I6,1F13.7,5X,1A3"),["2021","0.0000","0.0000"])

  # def test_rinex_format_endOfHeader(self):
  #   header = RinexHeader()
  #   self.assertEqual(header.parseFormat("                                                            ","60X"),[""])

if __name__ == '__main__':
  unittest.main()
