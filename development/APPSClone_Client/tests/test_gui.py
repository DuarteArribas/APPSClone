import appsclone_client
import unittest
from appsclone_client.gui import *

class TestGUI(unittest.TestCase):
  # def test_print_title(self):
  #   g = GUI()
  #   g._GUI__printTitle("arroz") 
  #   g.waitTest()

  # def test_print_ctrl_g(self):
  #   g = GUI()
  #   g._GUI__printCtrlG() 
  #   g.waitTest()

  # def test_print_input_box_rectangle(self):
  #   g = GUI()
  #   g._GUI__getInputBoxInput() 
  #   g.waitTest()

  # def test_showInputError(self):
  #   g = GUI()
  #   g._GUI__printInputError("arroz lol")

  # def test_get_input_no_error(self):
  #   g = GUI()
  #   self.assertEqual(g.getInput("What's your favorite color?",None),"green")

  # def test_get_input_error(self):
  #   g = GUI()
  #   self.assertEqual(g.getInput("What's your favorite color?","Please choose a real color!"),"green")

  # def test_get_pick_option(self):
  #   g   = GUI()
  #   lst = ["a","b","c"]
  #   self.assertEqual(g.getPickInput("What item do you want?",lst),"a")

if __name__ == '__main__':
  unittest.main()