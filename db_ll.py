from peewee import *

db = None

class BaseModel(Model):
   class Meta:
      database = db

class Category(BaseModel):
   name = CharField()

class LedgerEntry(BaseModel):
   month = CharField()
   entry_type = CharField()
   category = ForeignKeyField(Category, related_name='categories')
   amount = DecimalField(decimal_places=2, auto_round=True)
   note = CharField()

def open_db(filename):
   global db
   db = SqliteDatabase(filename)
   db.connect()
   db.create_tables([Category, LedgerEntry], safe=True)

def close_db():
   global db
   db.close()


