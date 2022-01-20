

from flask import Flask, request
from flask_mysqldb import MySQL

class DbRoutines():
    def __init__(self, app):
        self.mysql = MySQL()
        self.mysql.init_app(app)

    def user_credentials(self):
        return "Hello there..."



app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root_password'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

dbRoutines = DbRoutines(app)

def fetch_food_data():
    cursor = dbRoutines.mysql.connection.cursor()
    cursor.execute(f"use webapp_db;")
    cursor.execute('SELECT * from Food')
    food_data = cursor.fetchall()
    cursor.close()

    if food_data != None:
        return False
