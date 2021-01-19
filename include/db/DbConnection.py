from peewee import *


class DbConnection:

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DbConnection, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self.user = 'root'
        self.password = 'password'
        self.db_name = 'work'
        self.host = 'localhost'

        self.db_handle = MySQLDatabase(
            self.db_name, user=self.user,
            password=self.password,
            host=self.host,
            port=3306
        )

        self.db_handle.connect()
