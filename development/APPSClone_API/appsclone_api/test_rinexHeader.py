import unittest
from rinexHeader import *

class TestRinexheader(unittest.TestCase):
  # def test_rinex_validity1(self):
  #   header = RinexHeader()
  #   header.readMandatoryHeader("in/uploads/CVTY2720.21D")
  #   self.assertTrue(header.isValidHeader())

  # def test_rinex_validity2(self):
  #   header = RinexHeader()
  #   header.readMandatoryHeader("in/uploads/fileTest")
  #   self.assertFalse(header.isValidHeader())

  # def test_rinex_validity3(self):
  #   header = RinexHeader()
  #   header.readMandatoryHeader("in/uploads/fileTest2")
  #   self.assertFalse(header.isValidHeader())

  def test_string_extractor(self):
    header             = RinexHeader()
    number,numberCount = header._RinexHeader__extractIntUntilChar("1234abc321")
    self.assertEqual(number,1234)
    self.assertEqual(numberCount,4)

  def test_string_extractor2(self):
    header             = RinexHeader()
    number,numberCount = header._RinexHeader__extractIntUntilChar("1234")
    self.assertEqual(number,1234)
    self.assertEqual(numberCount,4)

  def test_string_extractor3(self):
    header             = RinexHeader()
    number,numberCount = header._RinexHeader__extractIntUntilChar("")
    self.assertEqual(number,0)
    self.assertEqual(numberCount,0)

  def test_string_extractor4(self):
    header             = RinexHeader()
    number,numberCount = header._RinexHeader__extractIntUntilChar("abc")
    self.assertEqual(number,1)
    self.assertEqual(numberCount,0)

  def test_string_extractor4(self):
    header             = RinexHeader()
    number,numberCount = header._RinexHeader__extractIntUntilChar("abc12345")
    self.assertEqual(number,1)
    self.assertEqual(numberCount,0)

  def test_string_extractor5(self):
    header             = RinexHeader()
    number,numberCount = header._RinexHeader__extractIntUntilChar("F9.2")
    self.assertEqual(number,1)
    self.assertEqual(numberCount,0)

  def test_string_extractor6(self):
    header             = RinexHeader()
    number,numberCount = header._RinexHeader__extractIntUntilChar("11X")
    self.assertEqual(number,11)
    self.assertEqual(numberCount,2)

  def test_rinex_format_version211(self):
    header = RinexHeader()
    self.assertEqual(header._RinexHeader__parseFormat("     2.11           OBSERVATION DATA    M (MIXED)           ","F9.2,11X,A20,A20"),["2.11","","OBSERVATION DATA","M (MIXED)"])

  def test_rinex_format_version302(self):
    header = RinexHeader()
    self.assertEqual(header._RinexHeader__parseFormat("     3.02           OBSERVATION DATA    G: GPS              ","F9.2,11X,A20,A20"),["3.02","","OBSERVATION DATA","G: GPS"])

  def test_rinex_format_version303(self):
    header = RinexHeader()
    self.assertEqual(header._RinexHeader__parseFormat("     3.03           OBSERVATION DATA    M (MIXED)           ","F9.2,11X,A20,A20"),["3.03","","OBSERVATION DATA","M (MIXED)"])
  
  def test_rinex_format_pgm(self):
    header = RinexHeader()
    self.assertEqual(header._RinexHeader__parseFormat("teqc  2019Feb25                         20211001 13:13:56UTC","A20,A20,A20"),["teqc  2019Feb25","","20211001 13:13:56UTC"])

  def test_rinex_format_markerName(self):
    header = RinexHeader()
    self.assertEqual(header._RinexHeader__parseFormat("CVTY                                                        ","A60"),["CVTY"])

  def test_rinex_format_observerAgency(self):
    header = RinexHeader()
    self.assertEqual(header._RinexHeader__parseFormat("RFGH                SEGAL                                   ","A20,A40"),["RFGH","SEGAL"])

  def test_rinex_format_receiver(self):
    header = RinexHeader()
    self.assertEqual(header._RinexHeader__parseFormat("3055025             SEPT POLARX5        5.3.2               ","3A20"),["3055025","SEPT POLARX5","5.3.2"])

  def test_rinex_format_antenna(self):
    header = RinexHeader()
    self.assertEqual(header._RinexHeader__parseFormat("1909270030          TWIVP6050_CONE  NONE                    ","2A20"),["1909270030","TWIVP6050_CONE  NONE"])

  def test_rinex_format_approxPosXYZ(self):
    header = RinexHeader()
    self.assertEqual(header._RinexHeader__parseFormat("  6378137.0000        0.0000        0.0000                  ","3F14.4"),["6378137.0000","0.0000","0.0000"])

  def test_rinex_format_antennaDeltaHEN(self):
    header = RinexHeader()
    self.assertEqual(header._RinexHeader__parseFormat("        0.9100        0.0000        0.0000                  ","3F14.4"),["0.9100","0.0000","0.0000"])

  def test_rinex_format_timeOfFirstObs(self):
    header = RinexHeader()
    self.assertEqual(header._RinexHeader__parseFormat("  2021     9    29     0     0    0.0000000     GPS         ","5I6,F13.7,5X,A3"),["2021","9","29","0","0","0.0000000","","GPS"])

  def test_rinex_format_endOfHeader(self):
    header = RinexHeader()
    self.assertEqual(header._RinexHeader__parseFormat("                                                            ","60X"),[""])

  def test_check_receiver(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/uploads/CVTY2720.21D")
    self.assertEqual(header._RinexHeader__isValidReceiver(),True)

  def test_check_antenna(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/uploads/CVTY2720.21D")
    self.assertEqual(header._RinexHeader__isValidAntenna(),True)
if __name__ == '__main__':
  unittest.main()
