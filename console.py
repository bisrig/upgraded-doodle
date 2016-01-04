import readline
import os
import db_access

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

def wrap_exception(fn):
   try:
      fn()
      return True
   except:
      return False

def main_menu():
   quit = False
   _ = os.system('clear')
   while not quit:
      print 'Budget Software Main Menu'
      print '-------------------------'
      print '1) Enter data'
      print '2) Review reports'
      print '3) Add new budget item'
      print '4) Set current budget item account value'
      print '5) Remove budget item'
      print '6) Monthly savings'
      print 'x/X/q/Q to quit'
      print 'Please enter selection'
      c = getch()
      if c == 'x' or c == 'X' or c == 'q' or c == 'Q':
         quit = True
      else:
         _ = os.system('clear')
         print 'Selection entered is ' + c
         print
         if c == '1':
            data_entry_opt()
         elif c == '2':
            review_menu_opt()
         elif c == '3':
            set_item_value_menu_opt()
         elif c == '4':
            add_item_opt()
         elif c == '5':
            remove_item_opt()
         else:
            pass

def data_entry_opt():
   completer_list = db_access.get_budget_item_list()

   def completer(text, state):
      options = [x for x in completer_list if x.startswith(text)]
      try:
         return options[state]
      except IndexError:
         return None

   readline.set_completer(completer)
   readline.parse_and_bind("tab: complete")
   
   item = None
   while not wrap_exception(lambda: db_access.validate_category(item)):
      item = raw_input('Enter budget item: ')
   
   completer_list = db_access.get_entry_type_list()
   entry_type = None
   while not wrap_exception(lambda: db_access.validate_entry_type(entry_type)):
      entry_type = raw_input('Entry for ' + item + ' is [' + ','.join(completer_list) + ']? ')
   
   completer_list = db_access.get_month_list()
   month = None
   while not wrap_exception(lambda: db_access.validate_month(month)):
      month = raw_input('Month for entry: ')

   readline.set_completer(None)
   amount = None
   while not wrap_exception(lambda: db_access.validate_amount(amount)):
      amount = raw_input('Amount of ' + entry_type + ' entry: ')
   
   note = None
   while not wrap_exception(lambda: db_access.validate_note(note)):
      note = raw_input('Note for entry: ')

   db_access.add_ledger_entry(month=month, category=item, entry_type=entry_type, amount=amount, note=note)
   #print item, entry_type, month, amount, note
   return

# TODO: Fill out this function
def review_menu_opt():
   return

# TODO: Fill out this function
def set_item_value_menu_opt():
   return

# TODO: Fill out this function
def add_item_opt():
   return

# TODO: Fill out this function
def remove_item_opt():
   return

