import unittest
from appsclone_api.rinexHeader import *

class TestRinexheader(unittest.TestCase):
  def test_rinex_header_reading(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/CVTY2720.21D")
    for h in header.mandatoryHeaders:
      print(header.mandatoryHeaders[h])

  def test_header_required(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/CVTY2720.21D")
    self.assertTrue(header._RinexHeader__isHeaderFromCurrentVersion("2.11"))

  def test_header_required2(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/CVTY2720.21D")
    self.assertTrue(header._RinexHeader__isHeaderFromCurrentVersion("ALL"))

  def test_header_required3(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/CVTY2720.21D")
    self.assertFalse(header._RinexHeader__isHeaderFromCurrentVersion("3.02"))

  def test_string_extractor(self):
    number,numberCount = RinexHeader._extractIntUntilChar("1234abc321")
    self.assertEqual(number,1234)
    self.assertEqual(numberCount,4)

  def test_string_extractor2(self):
    number,numberCount = RinexHeader._extractIntUntilChar("1234")
    self.assertEqual(number,1234)
    self.assertEqual(numberCount,4)

  def test_string_extractor3(self):
    number,numberCount = RinexHeader._extractIntUntilChar("")
    self.assertEqual(number,0)
    self.assertEqual(numberCount,0)

  def test_string_extractor4(self):
    number,numberCount = RinexHeader._extractIntUntilChar("abc")
    self.assertEqual(number,1)
    self.assertEqual(numberCount,0)

  def test_string_extractor5(self):
    number,numberCount = RinexHeader._extractIntUntilChar("abc12345")
    self.assertEqual(number,1)
    self.assertEqual(numberCount,0)

  def test_string_extractor6(self):
    number,numberCount = RinexHeader._extractIntUntilChar("F9.2")
    self.assertEqual(number,1)
    self.assertEqual(numberCount,0)

  def test_string_extractor7(self):
    number,numberCount = RinexHeader._extractIntUntilChar("11X")
    self.assertEqual(number,11)
    self.assertEqual(numberCount,2)

  def test_rinex_format_version211(self):
    self.assertEqual(
      RinexHeader._parseFormat("     2.11           OBSERVATION DATA    M (MIXED)           ","F9.2,11X,A20,A20"),
      ["2.11","","OBSERVATION DATA","M (MIXED)"]
    )

  def test_rinex_format_version302(self):
    self.assertEqual(
      RinexHeader._parseFormat("     3.02           OBSERVATION DATA    G: GPS              ","F9.2,11X,A20,A20"),
      ["3.02","","OBSERVATION DATA","G: GPS"]
    )

  def test_rinex_format_version303(self):
    self.assertEqual(
      RinexHeader._parseFormat("     3.03           OBSERVATION DATA    M (MIXED)           ","F9.2,11X,A20,A20"),
      ["3.03","","OBSERVATION DATA","M (MIXED)"]
    )
  
  def test_rinex_format_pgm(self):
    self.assertEqual(
      RinexHeader._parseFormat("teqc  2019Feb25                         20211001 13:13:56UTC","A20,A20,A20"),
      ["teqc  2019Feb25","","20211001 13:13:56UTC"]
    )

  def test_rinex_format_markerName(self):
    self.assertEqual(
      RinexHeader._parseFormat("CVTY                                                        ","A60"),
      ["CVTY"]
    )

  def test_rinex_format_observerAgency(self):
    self.assertEqual(
      RinexHeader._parseFormat("RFGH                SEGAL                                   ","A20,A40"),
      ["RFGH","SEGAL"]
    )

  def test_rinex_format_receiver(self):
    self.assertEqual(
      RinexHeader._parseFormat("3055025             SEPT POLARX5        5.3.2               ","3A20"),
      ["3055025","SEPT POLARX5","5.3.2"]
    )

  def test_rinex_format_antenna(self):
    self.assertEqual(
      RinexHeader._parseFormat("1909270030          TWIVP6050_CONE  NONE                    ","2A20"),
      ["1909270030","TWIVP6050_CONE  NONE"]
    )

  def test_rinex_format_approxPosXYZ(self):
    self.assertEqual(
      RinexHeader._parseFormat("  6378137.0000        0.0000        0.0000                  ","3F14.4"),
      ["6378137.0000","0.0000","0.0000"]
    )

  def test_rinex_format_antennaDeltaHEN(self):
    self.assertEqual(
      RinexHeader._parseFormat("        0.9100        0.0000        0.0000                  ","3F14.4"),
      ["0.9100","0.0000","0.0000"]
    )

  def test_rinex_format_timeOfFirstObs(self):
    self.assertEqual(
      RinexHeader._parseFormat("  2021     9    29     0     0    0.0000000     GPS         ","5I6,F13.7,5X,A3"),
      ["2021","9","29","0","0","0.0000000","","GPS"]
    )

  def test_rinex_format_endOfHeader(self):
    self.assertEqual(
      RinexHeader._parseFormat("                                                            ","60X"),
      [""]
    )

  def test_rinex_validity_number_headers(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/CVTY2720.21D")
    isValid,validity = header._RinexHeader__isValidNumberOfHeaders()
    self.assertTrue(isValid)

  def test_rinex_validity_number_header2(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/fileTest")
    isValid,validity = header._RinexHeader__isValidNumberOfHeaders()
    self.assertFalse(isValid)

  def test_rinex_validity_number_header3(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/fileTest2")
    isValid,validity = header._RinexHeader__isValidNumberOfHeaders()
    self.assertFalse(isValid)

  def test_rinex_validity_number_header4(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/fileTest3")
    isValid,validity = header._RinexHeader__isValidNumberOfHeaders()
    self.assertFalse(isValid)

  def test_rinex_validity_number_header5(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/CVTY2720.21D")
    isValid,validity = header._RinexHeader__isValidNumberOfHeaders()
    self.assertTrue(isValid)

  def test_check_receiver(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/CVTY2720.21D")
    isValid,receiver = header._RinexHeader__isValidReceiver()
    self.assertTrue(isValid)
    #print(receiver)

  def test_check_receiver2(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/fileTest")
    isValid,receiver = header._RinexHeader__isValidReceiver()
    self.assertFalse(isValid)
    #print(receiver)

  def test_check_receiver3(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/fileTest4")
    isValid,receiver = header._RinexHeader__isValidReceiver()
    self.assertFalse(isValid)
    #print(receiver)

  def test_check_antenna(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/CVTY2720.21D")
    isValid,antenna = header._RinexHeader__isValidAntenna()
    self.assertTrue(isValid)
    #print(antenna)

  def test_check_antenna2(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/fileTest")
    isValid,antenna = header._RinexHeader__isValidAntenna()
    self.assertFalse(isValid)
    #print(antenna)

  def test_check_antenna3(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/fileTest4")
    isValid,antenna = header._RinexHeader__isValidAntenna()
    self.assertTrue(isValid)
    #print(antenna)

  def test_check_antenna4(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/fileTest5")
    isValid,antenna = header._RinexHeader__isValidAntenna()
    self.assertFalse(isValid)
    #print(antenna)

  def test_rinex_validity1(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/CVTY2720.21D")
    validity,validityError = header.isValidHeader()
    print("1",validityError)
    self.assertTrue(validity)

  def test_rinex_validity2(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/fileTest")
    validity,validityError = header.isValidHeader()
    print("2",validityError)
    self.assertFalse(validity)

  def test_rinex_validity3(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/fileTest2")
    validity,validityError = header.isValidHeader()
    print("3",validityError)
    self.assertFalse(validity)

  def test_rinex_validity4(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/fileTest3")
    validity,validityError = header.isValidHeader()
    print("4",validityError)
    self.assertFalse(validity)

  def test_rinex_validity5(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/fileTest6")
    validity,validityError = header.isValidHeader()
    print("5",validityError)
    self.assertFalse(validity)

  def test_rinex_validity6(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/fileTest7")
    validity,validityError = header.isValidHeader()
    print("6",validityError)
    self.assertFalse(validity)

  def test_rinex_validity7(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/fileTest8")
    validity,validityError = header.isValidHeader()
    print("7",validityError)
    self.assertFalse(validity)

  def test_rinex_validity8(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/fileTest9")
    validity,validityError = header.isValidHeader()
    print("8",validityError)
    self.assertFalse(validity)

  def test_rinex_validity9(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/DUTH0630.22O")
    validity,validityError = header.isValidHeader()
    self.assertTrue(validity)

  def test_rinex_validity10(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/LARM0630.22O")
    validity,validityError = header.isValidHeader()
    self.assertTrue(validity)

  def test_rinex_validity11(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/NOA10630.22O")
    validity,validityError = header.isValidHeader()
    self.assertTrue(validity)

  def test_rinex_validity12(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/rovn0010.21o")
    validity,validityError = header.isValidHeader()
    self.assertTrue(validity)

  def test_rinex_validity13(self):
    header = RinexHeader()
    header.readMandatoryHeader("in/test/VLNS0630.22O")
    validity,validityError = header.isValidHeader()
    self.assertTrue(validity)

  def test_validity_error_no_of_headers_toString(self):
    header = RinexHeader()
    self.assertEqual(
      RinexHeader.validityErrorToString(RinexHeader.VALIDITY_ERRORS.INVALID_NUMBER_OF_HEADERS,"PGM / RUN BY / DATE"),
      "The rinex file doesn't contain the mandatory header lines. Missing, at least, header 'PGM / RUN BY / DATE'"
    )

  def test_validity_error_version_toString(self):
    header = RinexHeader()
    self.assertEqual(
      RinexHeader.validityErrorToString(RinexHeader.VALIDITY_ERRORS.INVALID_VERSION,"2.12"),
      "The version '2.12' of the rinex file is invalid (Supported versions are 2.11, 3.02)"
    )

if __name__ == '__main__':
  unittest.main()