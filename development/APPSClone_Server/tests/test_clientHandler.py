import appsclone_server
import unittest
from appsclone_server.clientHandler import *

class TestClientHandler(unittest.TestCase):
  def test_get_upload_dict(self):
    argsList          = [
      "defines.GIPSYData.STATIC",
      "defines.OrbitClockProduct.RAPID",
      "defines.GIPSYData.TROP_VMF1",
      True,
      False,
      "defines.GIPSYData.FLAT",
      1,
      "arroz"
    ]
    argsDictToConfirm = {
      "processing_mode"    : defines.GIPSYData.STATIC,
      "product"            : defines.OrbitClockProduct.RAPID,
      "troposphere_model"  : defines.GIPSYData.TROP_VMF1,
      "ocean_loading"      : True,
      "model_tides"        : False,
      "elev_dep_weighting" : defines.GIPSYData.FLAT,
      "elev_angle_cutoff"  : 1,
      "solution_period"    : 300
    }
    self.assertEqual(ClientHandler._getNewUploadArgs(argsList),argsDictToConfirm)

  def test_get_upload_dict_default(self):
    argsList          = [
      defines.GIPSYData.STATIC,
      defines.OrbitClockProduct.RAPID,
      defines.GIPSYData.TROP_VMF1,
      True,
      False,
      defines.GIPSYData.FLAT,
      1,
      "arroz"
    ]
    argsDictToConfirm = {
      "processing_mode"    : defines.GIPSYData.PROCESSING_MODE_DEFAULT,
      "product"            : defines.GIPSYData.PRODUCT_DEFAULT,
      "troposphere_model"  : defines.GIPSYData.TROP_GMF,
      "ocean_loading"      : True,
      "model_tides"        : True,
      "elev_dep_weighting" : defines.GIPSYData.ROOT_SINE,
      "elev_angle_cutoff"  : 7.5,
      "solution_period"    : 300
    }
    self.assertEqual(ClientHandler._getNewUploadArgs(argsList),argsDictToConfirm)

if __name__ == '__main__':
  unittest.main()