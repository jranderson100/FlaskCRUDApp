from flask import Flask
from flask_mysqldb import MySQL

from db_routines import DbRoutines

class DbRoutines():
    def __init__(self, app):
        self.mysql = MySQL()
        self.mysql.init_app(app)

    def user_credentials(self):
        return "Hello there..."