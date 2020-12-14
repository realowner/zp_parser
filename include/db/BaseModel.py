from peewee import *
from .DbConnection import *

db_handle = DbConnection().db_handle


class BaseModel(Model):
    class Meta:
        database = db_handle
