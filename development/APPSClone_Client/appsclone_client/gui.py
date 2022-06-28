import curses
from curses.textpad import Textbox,rectangle
from pick           import pick

class GUI:
  """GUI interface using curses."""
  # == Methods ==
  def __init__(self):
    """Initialize curses."""
    self.stdscr = curses.initscr()
    curses.start_color()
    curses.cbreak()
    curses.echo(False)
    curses.use_default_colors()
    curses.init_pair(1,curses.COLOR_GREEN,-1)
    curses.init_pair(2,curses.COLOR_WHITE,curses.COLOR_RED)
    self.greenBlack = curses.color_pair(1)   
    self.whiteRed = curses.color_pair(2)

  def __del__(self):
    """Return the terminal to a santizied state."""
    curses.nocbreak()
    curses.echo()
    curses.endwin()

  def getInput(self,title,errorMsg):
    """Get an input from the stdin.

    Parameters
    ----------
    title : str
      The title to show at the top of the input box

    Returns
    ----------
    str
      The input stripped and without any new line characters
    """
    self.stdscr.erase()
    self.__printTitle(title)
    self.__printCtrlG()
    if errorMsg:
      self.__printInputError(errorMsg)
    return self.__getInputBoxInput()

  def __printTitle(self,title):
    """Print the title to the specific coordinates to the stdout.

    Parameters
    ----------
    title : str
      The title to print
    """
    self.stdscr.addstr(2,3,title,curses.A_BOLD | self.greenBlack)
    self.stdscr.refresh()

  def __printCtrlG(self):
    """Print the CTRL + G confirmation at the specific coordinates, alongside its rectangle to the stdout."""
    self.stdscr.addstr(16,3,"CTRL+G to submit",curses.A_BOLD)
    rectangle(self.stdscr,15,2,17,19)
    self.stdscr.refresh()

  def __getInputBoxInput(self):
    """Get an input from the input box from the stdin.
    
    Returns
    ----------
    str
      The input stripped and without any new line characters
    """
    inputWindow = curses.newwin(10,40,4,3)
    box         = Textbox(inputWindow)
    rectangle(self.stdscr,3,2,14,43)
    self.stdscr.refresh()
    box.edit()
    return box.gather().strip().replace("\n","")

  def __printInputError(self,errorMsg):
    """Print an error message for the input.

    Parameters
    ----------
    errorMsg : str
      The error message to print
    """
    errorWindow = curses.newwin(3,22,15,21)
    errorWindow.addstr(errorMsg,curses.A_BOLD | self.whiteRed)
    errorWindow.refresh()

  def waitTest(self):
    """Wait for input. Only used for testing purposes."""
    self.stdscr.getch()

  def getPickInput(self,title,options):
    """Get an input from the given options list.

    Parameters
    ----------
    title   : str
      The title to show at the top of the input list
    options : list
      The list of possible input options

    Returns
    ----------
    str
      The input picked up
    """
    return pick(options,title,indicator = "->")[0]