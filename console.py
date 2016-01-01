import readline
import os

addrs = ['watermelon', 'rutabega', 'whatever']

def getch():
   import sys, tty, termios
   fd = sys.stdin.fileno()
   old_settings = termios.tcgetattr(fd)
   try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
   finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
   return ch

def completer(text, state):
   options = [x for x in addrs if x.startswith(text)]
   try:
      return options[state]
   except IndexError:
      return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")



def main_menu():
   quit = False
   _ = os.system('clear')
   while not quit:
      print 'Budget Software Main Menu'
      print '-------------------------'
      print '1) Add new budget item'
      print '2) Review reports'
      print '3) Add new budget item'
      print '4) Set current budget item account value'
      print '5) Remove budget item'
      print 'x/X/q/Q to quit'
      print 'Selection: '
      c = getch()
      if c == 'x' or c == 'X' or c == 'q' or c == 'Q':
         quit = True
      else:
         _ = os.system('clear')
         print 'Selection entered is ' + c
         print


