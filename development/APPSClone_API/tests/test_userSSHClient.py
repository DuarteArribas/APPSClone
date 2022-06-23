import unittest
from userSSHClient import *

class TestUserSSHClient(unittest.TestCase):
  def test_username(self):
    user = UserSSHClient("arroz","massa")
    self.assertEqual(user.username,"arroz")

  def test_password(self):
    user = UserSSHClient("arroz","massa")
    self.assertEqual(user.password,"massa")

if __name__ == '__main__':
  unittest.main()