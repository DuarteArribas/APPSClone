import curses
from curses.textpad import Textbox,rectangle

class GUI:
  def __init__(self):
    # init
    self.stdscr = curses.initscr()
    curses.start_color()
    curses.cbreak()
    curses.echo(False)
    # colors
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_GREEN)
    # some color pairs
    self.white_red = curses.color_pair(1)
    self.red_black = curses.color_pair(2)
    self.black_yellow = curses.color_pair(3)
    self.white_green = curses.color_pair(4)

  def printTitle(self,title):
    self.stdscr.erase()
    self.stdscr.addstr(2,2,title,curses.A_BOLD | self.red_black)
    self.stdscr.refresh()

  def getInput(self,title):
    self.printTitle(title)
    newWindow = curses.newwin(10,40,4,3)
    self.stdscr.addstr(16,3,"CTRL+G to submit",curses.A_BOLD)
    box = Textbox(newWindow)
    rectangle(self.stdscr,3,2,14,43)
    rectangle(self.stdscr,15,2,17,19)
    self.stdscr.refresh()
    box.edit()
    return box.gather()

  def wait(self):
    self.stdscr.getch()

a = GUI()
a.getInput("Please choose the color:")
curses.nocbreak()
curses.echo()
curses.endwin()

