#This test ensures, before the app is launched, that the SQL database returns the data from the Food table as intended
#Command to run python3 -m unittest discover
#From unit folder


import unittest



from flask import Flask, request
from db_routines import DbRoutines

from tests.unit.fetch_food_data import fetch_food_data

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root_password'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

dbRoutines = DbRoutines(app)

# def fetch_food_data():
#     cursor = dbRoutines.mysql.connection.cursor()
#     cursor.execute(f"use webapp_db;")
#     cursor.execute('SELECT * from Food')
#     food_data = cursor.fetchall()
#     cursor.close()

#     if food_data != None:
#         return True



class FoodTestClass(unittest.TestCase):
    def test_fetch_food_data(self):
        self.assertTrue(fetch_food_data(True))

if __name__ == '__main__':
    unittest.main()