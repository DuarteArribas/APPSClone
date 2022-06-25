import unittest
import warnings
from appsclone_api.utils.sshConnection import *
from appsclone_api.utils.logs          import *

class TestSSHConnection(unittest.TestCase):
  def test_ssh_connect(self):
    warnings.filterwarnings(action = "ignore",message = "unclosed",category = ResourceWarning)
    logger = Logs("logs/logTest.log",1000)
    conn   = SSHConnection("138.68.128.182","22","root","Pr0j#to_Spr1ng",logger)

  def test_ssh_connect2(self):
    warnings.filterwarnings(action = "ignore",message = "unclosed",category = ResourceWarning)
    logger = Logs("logs/logTest.log",1000)
    conn   = SSHConnection("138.68.128.181","22","root","Pr0j#to_Spr1ng",logger)

  def test_ssh_connect3(self):
    warnings.filterwarnings(action = "ignore",message = "unclosed",category = ResourceWarning)
    logger = Logs("logs/logTest.log",1000)
    conn   = SSHConnection("138.68.128.182","21","root","Pr0j#to_Spr1ng",logger)

  def test_ssh_connect4(self):
    warnings.filterwarnings(action = "ignore",message = "unclosed",category = ResourceWarning)
    logger = Logs("logs/logTest.log",1000)
    conn   = SSHConnection("138.68.128.182","22","root2","Pr0j#to_Spr1ng",logger)

  def test_ssh_connect5(self):
    warnings.filterwarnings(action = "ignore",message = "unclosed",category = ResourceWarning)
    logger = Logs("logs/logTest.log",1000)
    conn   = SSHConnection("138.68.128.182","22","root","arroz",logger)

  def test_get_file(self):
    logger = Logs("logs/logTest.log",1000)
    conn   = SSHConnection("138.68.128.182","22","root","Pr0j#to_Spr1ng",logger)
    conn.getFile("~/arroz","in/to_upload_test")

  def test_get_file2(self):
    logger = Logs("logs/logTest.log",1000)
    conn   = SSHConnection("138.68.128.182","22","root","Pr0j#to_Spr1ng",logger)
    conn.getFile("~/arro","in/to_upload_test")
if __name__ == '__main__':
  unittest.main()