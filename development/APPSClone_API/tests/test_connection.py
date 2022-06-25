import unittest
import warnings
from appsclone_api.connection import *
from appsclone_api.utils.logs import *

class TestConnection(unittest.TestCase):
  def test_connection_ok(self):
    warnings.filterwarnings(action = "ignore",message = "unclosed",category = ResourceWarning)
    logger = Logs("logs/logTest.log",1000)
    conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
    self.assertTrue(conn.testConnection())

  def test_get_user_quota(self):
    warnings.filterwarnings(action = "ignore",message = "unclosed",category = ResourceWarning)
    logger = Logs("logs/logTest.log",1000)
    conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
    print(conn.getQuotaLeft())

  def test_file_validity(self):
    logger = Logs("logs/logTest.log",1000)
    conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
    self.assertFalse(conn._Connection_APPS__checkFileValidity("in/test/file"))

  def test_file_validity2(self):
    logger = Logs("logs/logTest.log",1000)
    conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
    self.assertTrue(conn._Connection_APPS__checkFileValidity("in/test/CVTY2720.21D"))

  def test_valid_arg_email(self):
    self.assertTrue(Connection_APPS._isValidArg("email",defines.Data.EMAIL_NOTIFY_DEFAULT))

  def test_valid_arg_email2(self):
    self.assertTrue(Connection_APPS._isValidArg("email",True))

  def test_valid_arg_email3(self):
    self.assertTrue(Connection_APPS._isValidArg("email",False))

  def test_valid_arg_email4(self):
    self.assertFalse(Connection_APPS._isValidArg("email","arroz"))

  def test_valid_arg_access(self):
    self.assertTrue(Connection_APPS._isValidArg("access",defines.Data.ACCESS_DEFAULT))

  def test_valid_arg_access2(self):
    self.assertTrue(Connection_APPS._isValidArg("access",defines.Data.PRIVATE))

  def test_valid_arg_access3(self):
    self.assertTrue(Connection_APPS._isValidArg("access",defines.Data.PUBLIC))

  def test_valid_arg_access4(self):
    self.assertFalse(Connection_APPS._isValidArg("access",True))

  def test_valid_arg_processing_mode(self):
    self.assertTrue(Connection_APPS._isValidArg("processing_mode",defines.GIPSYData.PROCESSING_MODE_DEFAULT))

  def test_valid_arg_processing_mode2(self):
    self.assertTrue(Connection_APPS._isValidArg("processing_mode",defines.GIPSYData.STATIC))

  def test_valid_arg_processing_mode3(self):
    self.assertTrue(Connection_APPS._isValidArg("processing_mode",defines.GIPSYData.KINEMATIC))

  def test_valid_arg_processing_mode4(self):
    self.assertFalse(Connection_APPS._isValidArg("processing_mode",True))

  def test_valid_arg_product(self):
    self.assertTrue(Connection_APPS._isValidArg("product",defines.GIPSYData.PRODUCT_DEFAULT))

  def test_valid_arg_product2(self):
    self.assertTrue(Connection_APPS._isValidArg("product",defines.OrbitClockProduct.REAL_TIME))

  def test_valid_arg_product3(self):
    self.assertTrue(Connection_APPS._isValidArg("product",defines.OrbitClockProduct.ULTRA))

  def test_valid_arg_product4(self):
    self.assertTrue(Connection_APPS._isValidArg("product",defines.OrbitClockProduct.RAPID))

  def test_valid_arg_product5(self):
    self.assertTrue(Connection_APPS._isValidArg("product",defines.OrbitClockProduct.FINAL))

  def test_valid_arg_product6(self):
    self.assertTrue(Connection_APPS._isValidArg("product",defines.GIPSYData.BEST))

  def test_valid_arg_product7(self):
    self.assertFalse(Connection_APPS._isValidArg("product",False))

  def test_valid_arg_troposphere_model(self):
    self.assertTrue(Connection_APPS._isValidArg("troposphere_model",defines.GIPSYData.TROP_GMF))

  def test_valid_arg_troposphere_model2(self):
    self.assertTrue(Connection_APPS._isValidArg("troposphere_model",defines.GIPSYData.TROP_OFF))

  def test_valid_arg_troposphere_model3(self):
    self.assertTrue(Connection_APPS._isValidArg("troposphere_model",defines.GIPSYData.TROP_PROVIDED))

  def test_valid_arg_troposphere_model4(self):
    self.assertTrue(Connection_APPS._isValidArg("troposphere_model",defines.GIPSYData.TROP_VMF1))

  def test_valid_arg_troposphere_model5(self):
    self.assertTrue(Connection_APPS._isValidArg("troposphere_model",defines.GIPSYData.TROP_GPT2))

  def test_valid_arg_troposphere_model6(self):
    self.assertFalse(Connection_APPS._isValidArg("troposphere_model",True))

  def test_valid_arg_ocean_loading(self):
    self.assertTrue(Connection_APPS._isValidArg("ocean_loading",True))

  def test_valid_arg_ocean_loading2(self):
    self.assertTrue(Connection_APPS._isValidArg("ocean_loading",False))

  def test_valid_arg_ocean_loading3(self):
    self.assertFalse(Connection_APPS._isValidArg("ocean_loading","arroz"))

  def test_valid_arg_model_tides(self):
    self.assertTrue(Connection_APPS._isValidArg("model_tides",True))

  def test_valid_arg_model_tides2(self):
    self.assertTrue(Connection_APPS._isValidArg("model_tides",False))

  def test_valid_arg_model_tides3(self):
    self.assertFalse(Connection_APPS._isValidArg("model_tides","arroz"))

  def test_valid_arg_elev_dep_weighting(self):
    self.assertTrue(Connection_APPS._isValidArg("elev_dep_weighting",defines.GIPSYData.ROOT_SINE))

  def test_valid_arg_elev_dep_weighting2(self):
    self.assertTrue(Connection_APPS._isValidArg("elev_dep_weighting",defines.GIPSYData.FLAT))

  def test_valid_arg_elev_dep_weighting3(self):
    self.assertTrue(Connection_APPS._isValidArg("elev_dep_weighting",defines.GIPSYData.SINE))

  def test_valid_arg_elev_angle_cutoff(self):
    self.assertTrue(Connection_APPS._isValidArg("elev_angle_cutoff",10))

  def test_valid_arg_elev_angle_cutoff2(self):
    self.assertTrue(Connection_APPS._isValidArg("elev_angle_cutoff",7.5))

  def test_valid_arg_elev_angle_cutoff3(self):
    self.assertTrue(Connection_APPS._isValidArg("elev_angle_cutoff",defines.GIPSYData.ELEV_ANGLE_CUTOFF_MIN+1))

  def test_valid_arg_elev_angle_cutoff4(self):
    self.assertFalse(Connection_APPS._isValidArg("elev_angle_cutoff",defines.GIPSYData.ELEV_ANGLE_CUTOFF_MIN))

  def test_valid_arg_elev_angle_cutoff5(self):
    self.assertFalse(Connection_APPS._isValidArg("elev_angle_cutoff",defines.GIPSYData.ELEV_ANGLE_CUTOFF_MIN-1))

  def test_valid_arg_elev_angle_cutoff6(self):
    self.assertFalse(Connection_APPS._isValidArg("elev_angle_cutoff",defines.GIPSYData.ELEV_ANGLE_CUTOFF_MAX+1))

  def test_valid_arg_elev_angle_cutoff7(self):
    self.assertFalse(Connection_APPS._isValidArg("elev_angle_cutoff",defines.GIPSYData.ELEV_ANGLE_CUTOFF_MAX))

  def test_valid_arg_elev_angle_cutoff8(self):
    self.assertTrue(Connection_APPS._isValidArg("elev_angle_cutoff",defines.GIPSYData.ELEV_ANGLE_CUTOFF_MAX-1))

  def test_valid_arg_solution_period(self):
    self.assertTrue(Connection_APPS._isValidArg("solution_period",300))

  def test_valid_arg_solution_period2(self):
    self.assertTrue(Connection_APPS._isValidArg("solution_period",10))

  def test_valid_arg_solution_period3(self):
    self.assertTrue(Connection_APPS._isValidArg("solution_period",-10))

  def test_valid_arg_solution_period3(self):
    self.assertTrue(Connection_APPS._isValidArg("solution_period",1000000))

  def test_valid_arg_solution_period4(self):
    self.assertFalse(Connection_APPS._isValidArg("solution_period",defines.GIPSYData.SOLUTION_PERIOD_MIN-1))

  def test_valid_arg_solution_period5(self):
    self.assertFalse(Connection_APPS._isValidArg("solution_period",defines.GIPSYData.SOLUTION_PERIOD_MIN))

  def test_valid_arg_solution_period6(self):
    self.assertTrue(Connection_APPS._isValidArg("solution_period",defines.GIPSYData.SOLUTION_PERIOD_MIN+1))

  def test_valid_arg_solution_period7(self):
    self.assertFalse(Connection_APPS._isValidArg("solution_period",-10000))

  def test_valid_arg_generate_quaternions(self):
    self.assertTrue(Connection_APPS._isValidArg("generate_quaternions",True))

  def test_valid_arg_generate_quaternions2(self):
    self.assertTrue(Connection_APPS._isValidArg("generate_quaternions",False))

  def test_valid_arg_generate_quaternions3(self):
    self.assertFalse(Connection_APPS._isValidArg("generate_quaternions","arroz"))

  def test_update_upload_args(self):
    logger = Logs("logs/logTest.log",1000)
    conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
    args   = {
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
    logger = Logs("logs/logTest.log",1000)
    conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
    args   = {
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
    logger = Logs("logs/logTest.log",1000)
    conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
    args   = {
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
    logger = Logs("logs/logTest.log",1000)
    conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
    args   = {
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
    logger = Logs("logs/logTest.log",1000)
    conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
    args   = {
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

  def test_add_to_apps_id_queue(self):
    logger = Logs("logs/logTest.log",1000)
    conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
    conn._Connection_APPS__addToIDQueue("00000000-0000-0000-0000-000000000000","arroz","queues/apps_id_queue_test")

  def test_remove_from_apps_id_queue(self):
    logger = Logs("logs/logTest.log",1000)
    conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
    conn._Connection_APPS__removeFromIDQueue("00000000-0000-0000-0000-000000000000","arroz","queues/apps_id_queue_test")

  # def test_upload_file(self):
  #   warnings.filterwarnings(action = "ignore",message = "unclosed",category = ResourceWarning)
  #   args = {
  #    "pressure"             : None,
  #    "attitude"             : None,
  #    "email"                : defines.Data.EMAIL_NOTIFY_DEFAULT,
  #    "access"               : defines.Data.ACCESS_DEFAULT,
  #    "processing_mode"      : defines.GIPSYData.PROCESSING_MODE_DEFAULT,
  #    "product"              : "arroz",
  #    "troposphere_model"    : defines.GIPSYData.TROP_GMF,
  #    "ocean_loading"        : True,
  #    "model_tides"          : True,
  #    "elev_dep_weighting"   : defines.GIPSYData.ROOT_SINE,
  #    "elev_angle_cutoff"    : 7.5,
  #    "solution_period"      : 300,
  #    "generate_quaternions" : False,
  #   }
  #   logger = Logs("logs/logTest.log",1000)
  #   conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
  #   conn.uploadFile("in/test/CVTY2720.21D","queues/apps_id_queue_test",args)

  # def test_get_file_data(self):
  #   warnings.filterwarnings(action = "ignore",message = "unclosed",category = ResourceWarning)
  #   logger = Logs("logs/logTest.log",1000)
  #   conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
  #   print(conn._Connection_APPS__getFileData("230f4eb0-f4f-11ec-8d6a-e0db55a1adf2","queues/apps_id_queue_test"))

  # def test_delete_file(self):
  #   warnings.filterwarnings(action = "ignore",message = "unclosed",category = ResourceWarning)
  #   logger = Logs("logs/logTest.log",1000)
  #   conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
  #   conn._Connection_APPS__removeData("230f4eb0-f40f-11ec-8d6a-e0db5501adf2","arroz","queues/apps_id_queue_test")

  # def test_approve_file(self):
  #   warnings.filterwarnings(action = "ignore",message = "unclosed",category = ResourceWarning)
  #   logger = Logs("logs/logTest.log",1000)
  #   conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
  #   conn._Connection_APPS__approveSubmission("230f4eb0-f40f-11ec-8d6a-e0db5501adf2","arroz","queues/apps_id_queue_test")

  # def test_retrieve_data(self):
  #   logger = Logs("logs/logTest.log",1000)
  #   conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
  #   conn._Connection_APPS__retrieveData(
  #     "b9d3abb0-f415-11ec-a201-e0db5501adf2","arroz","queues/apps_id_queue_test",
  #     "out/results_test"
  #   )

  # def test_handle_error(self):
  #   logger = Logs("logs/logTest.log",1000)
  #   conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
  #   conn._Connection_APPS__handleError("42307ec0-f416-11ec-9078-e0db5501adf2","arroz","queues/apps_id_queue_test")

  # def test_handle_file_state(self):
  #   logger = Logs("logs/logTest.log",1000)
  #   conn   = Connection_APPS(settingsFile = "config/apps_settings",downloadDirectory = "out/results_test",logger = logger)
  #   conn.handleFileState("5fa6743c-f416-11ec-92fe-e0db5501adf2","queues/apps_id_queue_test","out/results_test")
  
if __name__ == '__main__':
  unittest.main()