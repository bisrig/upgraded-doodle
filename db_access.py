import db_ll
import decimal

# TODO fill this in for real
def get_budget_item_list():
   return [l.name for l in db_ll.Category.select()]

def get_entry_type_list():
   return ['Debit', 'Credit']

def get_month_list():
   return ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def validate_month(month):
   if month not in get_month_list():
      raise ValueError(month + ' not in month list')

def validate_entry_type(entry_type):
   if entry_type not in get_entry_type_list():
      raise ValueError(entry_type + ' not a valid entry type')

def validate_category(category):
   query = db_ll.Category.select().where(db_ll.Category.name == category)
   if query.count() == 0:
      raise ValueError(category + ' not a valid category')
   elif query.count() > 1:
      raise ValueError(category + ' matched multiple categories - there\'s a db problem')
   else:
      return query.get()

def validate_amount(amount):
   return decimal.Decimal(amount).quantize(decimal.Decimal('0.01'))  

def validate_note(note):
   if len(note) >= 255:
      raise ValueError('Note is too long')

def add_ledger_item(month, entry_type, category, amount, note):
   try:
      validate_month(month)
      validate_entry_type(entry_type)
      cat = validate_category(category)
      amt = validate_amount(amount)
      validate_note(note)

      le = db_ll.LedgerEntry(month=month, entry_type=entry_type, category=cat, amount=amt, note=note)
      le.save()
   except BaseException as e:
      print 'Error adding entry:', e

      

