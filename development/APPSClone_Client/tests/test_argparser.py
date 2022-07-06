import appsclone_client
import unittest
from appsclone_client.utils.argumentParser import *

class TestArgumentParser(unittest.TestCase):
  def testGetOptions(self):
    ap        = ArgumentParser()
    arguments = ap.getOptions()
    print(arguments)

if __name__ == '__main__':
  unittest.main()