import unittest
from connection import *

class TestConnection(unittest.TestCase):
  # def test_connection_ok(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   self.assertTrue(conn.testConnection())

  # def test_gzip(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   self.assertTrue(conn._Connection_APPS__checkCompressedWithGzip("in/test/file.gz"))

  # def test_gzip2(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   self.assertFalse(conn._Connection_APPS__checkCompressedWithGzip("in/test/file"))

  # def test_getUncompressedFile(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   print(conn._Connection_APPS__getUncompressedFile("in/test/arroz.gz"))
  #   #self.assertFalse()

  # def test_gzip_compression(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   self.assertEqual(conn._Connection_APPS__compressUncompressGzip("in/test/arroz",True),"in/test/arroz.gz")

  # def test_gzip_uncompression(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   self.assertEqual(conn._Connection_APPS__compressUncompressGzip("in/test/arroz.gz",False),"in/test/arrozUncompressed")

  # def test_file_validity(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   self.assertFalse(conn._Connection_APPS__checkFileValidity("in/test/file"))

  # def test_file_validity2(self):
  #   conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
  #   self.assertTrue(conn._Connection_APPS__checkFileValidity("in/uploads_test/CVTY2720.21D"))

  def test_valid_arg_email(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("email",defines.Data.EMAIL_NOTIFY_DEFAULT))

  def test_valid_arg_email2(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("email",True))

  def test_valid_arg_email3(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("email",False))

  def test_valid_arg_email4(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__isValidArg("email","arroz"))

  def test_valid_arg_access(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("access",defines.Data.ACCESS_DEFAULT))

  def test_valid_arg_access2(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("access",defines.Data.PRIVATE))

  def test_valid_arg_access3(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("access",defines.Data.PUBLIC))

  def test_valid_arg_access4(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__isValidArg("access",True))

  def test_valid_arg_processing_mode(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("processing_mode",defines.GIPSYData.PROCESSING_MODE_DEFAULT))

  def test_valid_arg_processing_mode2(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("processing_mode",defines.GIPSYData.STATIC))

  def test_valid_arg_processing_mode3(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("processing_mode",defines.GIPSYData.KINEMATIC))

  def test_valid_arg_processing_mode4(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__isValidArg("processing_mode",True))

  def test_valid_arg_product(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("product",defines.GIPSYData.PRODUCT_DEFAULT))

  def test_valid_arg_product2(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("product",defines.OrbitClockProduct.REAL_TIME))

  def test_valid_arg_product3(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("product",defines.OrbitClockProduct.ULTRA))

  def test_valid_arg_product4(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("product",defines.OrbitClockProduct.RAPID))

  def test_valid_arg_product5(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("product",defines.OrbitClockProduct.FINAL))

  def test_valid_arg_product6(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("product",defines.GIPSYData.BEST))

  def test_valid_arg_product7(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__isValidArg("product",False))

  def test_valid_arg_troposphere_model(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("troposphere_model",defines.GIPSYData.TROP_GMF))

  def test_valid_arg_troposphere_model2(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("troposphere_model",defines.GIPSYData.TROP_OFF))

  def test_valid_arg_troposphere_model3(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("troposphere_model",defines.GIPSYData.TROP_PROVIDED))

  def test_valid_arg_troposphere_model4(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("troposphere_model",defines.GIPSYData.TROP_VMF1))

  def test_valid_arg_troposphere_model5(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("troposphere_model",defines.GIPSYData.TROP_GPT2))

  def test_valid_arg_troposphere_model6(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__isValidArg("troposphere_model",True))

  def test_valid_arg_ocean_loading(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("ocean_loading",True))

  def test_valid_arg_ocean_loading2(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("ocean_loading",False))

  def test_valid_arg_ocean_loading3(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__isValidArg("ocean_loading","arroz"))

  def test_valid_arg_model_tides(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("model_tides",True))

  def test_valid_arg_model_tides2(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("model_tides",False))

  def test_valid_arg_model_tides3(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__isValidArg("model_tides","arroz"))

  def test_valid_arg_elev_dep_weighting(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("elev_dep_weighting",defines.GIPSYData.ROOT_SINE))

  def test_valid_arg_elev_dep_weighting2(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("elev_dep_weighting",defines.GIPSYData.FLAT))

  def test_valid_arg_elev_dep_weighting3(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("elev_dep_weighting",defines.GIPSYData.SINE))

  def test_valid_arg_elev_angle_cutoff(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("elev_angle_cutoff",10))

  def test_valid_arg_elev_angle_cutoff2(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("elev_angle_cutoff",7.5))

  def test_valid_arg_elev_angle_cutoff3(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("elev_angle_cutoff",defines.GIPSYData.ELEV_ANGLE_CUTOFF_MIN+1))

  def test_valid_arg_elev_angle_cutoff4(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__isValidArg("elev_angle_cutoff",defines.GIPSYData.ELEV_ANGLE_CUTOFF_MIN))

  def test_valid_arg_elev_angle_cutoff5(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__isValidArg("elev_angle_cutoff",defines.GIPSYData.ELEV_ANGLE_CUTOFF_MIN-1))

  def test_valid_arg_elev_angle_cutoff6(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__isValidArg("elev_angle_cutoff",defines.GIPSYData.ELEV_ANGLE_CUTOFF_MAX+1))

  def test_valid_arg_elev_angle_cutoff7(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__isValidArg("elev_angle_cutoff",defines.GIPSYData.ELEV_ANGLE_CUTOFF_MAX))

  def test_valid_arg_elev_angle_cutoff8(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("elev_angle_cutoff",defines.GIPSYData.ELEV_ANGLE_CUTOFF_MAX-1))

  def test_valid_arg_solution_period(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("solution_period",300))

  def test_valid_arg_solution_period2(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("solution_period",10))

  def test_valid_arg_solution_period3(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("solution_period",-10))

  def test_valid_arg_solution_period3(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("solution_period",1000000))

  def test_valid_arg_solution_period4(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__isValidArg("solution_period",defines.GIPSYData.SOLUTION_PERIOD_MIN-1))

  def test_valid_arg_solution_period5(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__isValidArg("solution_period",defines.GIPSYData.SOLUTION_PERIOD_MIN))

  def test_valid_arg_solution_period6(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("solution_period",defines.GIPSYData.SOLUTION_PERIOD_MIN+1))

  def test_valid_arg_solution_period7(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__isValidArg("solution_period",-10000))

  def test_valid_arg_generate_quaternions(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("generate_quaternions",True))

  def test_valid_arg_generate_quaternions2(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertTrue(conn._Connection_APPS__isValidArg("generate_quaternions",False))

  def test_valid_arg_generate_quaternions3(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    self.assertFalse(conn._Connection_APPS__isValidArg("generate_quaternions","arroz"))

  def test_update_upload_args(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    args = {
      "pressure"             : None,
      "attitude"             : None,
      "email"                : defines.Data.EMAIL_NOTIFY_DEFAULT,
      "access"               : defines.Data.ACCESS_DEFAULT,
      "processing_mode"      : defines.GIPSYData.PROCESSING_MODE_DEFAULT,
      "product"              : defines.GIPSYData.PRODUCT_DEFAULT,
      "troposphere_model"    : defines.GIPSYData.TROP_GMF,
      "ocean_loading"        : True,
      "model_tides"          : True,
      "elev_dep_weighting"   : defines.GIPSYData.ROOT_SINE,
      "elev_angle_cutoff"    : 7.5,
      "solution_period"      : 300,
      "generate_quaternions" : False,
    }
    self.assertEqual(
      conn._Connection_APPS__updateUploadArgs(args),
      [
        None,
        None,
        defines.Data.EMAIL_NOTIFY_DEFAULT,
        defines.Data.ACCESS_DEFAULT,
        defines.GIPSYData.PROCESSING_MODE_DEFAULT,
        defines.GIPSYData.PRODUCT_DEFAULT,
        defines.GIPSYData.TROP_GMF,
        True,
        True,
        defines.GIPSYData.ROOT_SINE,
        7.5,
        300,
        False
      ]
    )

  def test_update_upload_args2(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    args = {
      "pressure"             : None,
      "attitude"             : None,
      "email"                : True,
      "access"               : defines.Data.ACCESS_DEFAULT,
      "processing_mode"      : defines.GIPSYData.PROCESSING_MODE_DEFAULT,
      "product"              : defines.GIPSYData.PRODUCT_DEFAULT,
      "troposphere_model"    : defines.GIPSYData.TROP_GMF,
      "ocean_loading"        : True,
      "model_tides"          : True,
      "elev_dep_weighting"   : defines.GIPSYData.ROOT_SINE,
      "elev_angle_cutoff"    : 7.5,
      "solution_period"      : 300,
      "generate_quaternions" : False,
    }
    self.assertEqual(
      conn._Connection_APPS__updateUploadArgs(args),
      [
        None,
        None,
        True,
        defines.Data.ACCESS_DEFAULT,
        defines.GIPSYData.PROCESSING_MODE_DEFAULT,
        defines.GIPSYData.PRODUCT_DEFAULT,
        defines.GIPSYData.TROP_GMF,
        True,
        True,
        defines.GIPSYData.ROOT_SINE,
        7.5,
        300,
        False
      ]
    )

  def test_update_upload_args3(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    args = {
      "pressure"             : None,
      "attitude"             : None,
      "email"                : True,
      "access"               : "arroz",
      "processing_mode"      : defines.GIPSYData.PROCESSING_MODE_DEFAULT,
      "product"              : defines.GIPSYData.PRODUCT_DEFAULT,
      "troposphere_model"    : defines.GIPSYData.TROP_GMF,
      "ocean_loading"        : True,
      "model_tides"          : True,
      "elev_dep_weighting"   : defines.GIPSYData.ROOT_SINE,
      "elev_angle_cutoff"    : 7.5,
      "solution_period"      : 300,
      "generate_quaternions" : False,
    }
    self.assertEqual(
      conn._Connection_APPS__updateUploadArgs(args),
      [
        None,
        None,
        True,
        defines.Data.ACCESS_DEFAULT,
        defines.GIPSYData.PROCESSING_MODE_DEFAULT,
        defines.GIPSYData.PRODUCT_DEFAULT,
        defines.GIPSYData.TROP_GMF,
        True,
        True,
        defines.GIPSYData.ROOT_SINE,
        7.5,
        300,
        False
      ]
    )

  def test_update_upload_args4(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    args = {
      "pressure"             : "",
      "attitude"             : "",
      "email"                : "",
      "access"               : "",
      "processing_mode"      : "",
      "product"              : "",
      "troposphere_model"    : "",
      "ocean_loading"        : "",
      "model_tides"          : "",
      "elev_dep_weighting"   : "",
      "elev_angle_cutoff"    : "",
      "solution_period"      : "",
      "generate_quaternions" : ""
    }
    self.assertEqual(
      conn._Connection_APPS__updateUploadArgs(args),
      [
        None,
        None,
        defines.Data.EMAIL_NOTIFY_DEFAULT,
        defines.Data.ACCESS_DEFAULT,
        defines.GIPSYData.PROCESSING_MODE_DEFAULT,
        defines.GIPSYData.PRODUCT_DEFAULT,
        defines.GIPSYData.TROP_GMF,
        True,
        True,
        defines.GIPSYData.ROOT_SINE,
        7.5,
        300,
        False
      ]
    )

  def test_update_upload_args5(self):
    conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    args = {
      "pressure"             : "",
      "attitude"             : "",
      "email"                : "",
      "access"               : "",
      "processing_mode"      : "",
      "product"              : "",
      "troposphere_model"    : defines.GIPSYData.TROP_PROVIDED,
      "ocean_loading"        : "",
      "model_tides"          : "",
      "elev_dep_weighting"   : "",
      "elev_angle_cutoff"    : "",
      "solution_period"      : "",
      "generate_quaternions" : ""
    }
    self.assertEqual(
      conn._Connection_APPS__updateUploadArgs(args),
      [
        None,
        None,
        defines.Data.EMAIL_NOTIFY_DEFAULT,
        defines.Data.ACCESS_DEFAULT,
        defines.GIPSYData.PROCESSING_MODE_DEFAULT,
        defines.GIPSYData.PRODUCT_DEFAULT,
        defines.GIPSYData.TROP_PROVIDED,
        True,
        True,
        defines.GIPSYData.ROOT_SINE,
        7.5,
        300,
        False
      ]
    )

  # def test_upload_file(self):
    # conn=Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/downloads",loggingFile = "logs/logTest.log")
    # conn.uploadFile("in/uploads_test/CVTY2720.21D","out/queue/queue")

if __name__ == '__main__':
  unittest.main()
