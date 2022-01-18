from flask import Flask, render_template, request
from datetime import datetime
from db_routines import DbRoutines
import json

########################################################
# TODO: Make server production grade using 'waitress'  #
########################################################

app = Flask(__name__)
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root_password'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

dbRoutines = DbRoutines(app)

is_registed_user = False

@app.route('/', methods=['GET', 'POST'])
def index():
    cursor = dbRoutines.mysql.connection.cursor()
    cursor.execute(f"use webapp_db;")
    cursor.execute('SELECT * from Food')
    food_data = cursor.fetchall()
    cursor.close()

    

    cursor = dbRoutines.mysql.connection.cursor()
    cursor.execute(f"use webapp_db;")
    cursor.execute('SELECT * from Orders')
    order_data = cursor.fetchall()
    cursor.close()
    
    if request.method == "POST":
        cursor = dbRoutines.mysql.connection.cursor()
        cursor.execute(f"use webapp_db;")
        cursor.execute('DELETE FROM Basket;')
        dbRoutines.mysql.connection.commit()
        cursor.close()
    
    

    return render_template("index.html", foods = food_data)



@app.route('/basket', methods=['GET', 'POST'])
def basket():

    #FOR EACH ITEM, MAKE A REQUEST BASED ON FOOD ITEMID to get all other info in order to render these items in baske
    

    if request.method == 'POST':
        basket_items = request.form.getlist('foodselector')
        cursor = dbRoutines.mysql.connection.cursor()
        cursor.execute(f"use webapp_db;")
        
        for item in basket_items:
            cursor.execute (f"INSERT INTO `Basket` (`BasketRef`, `FoodID`) VALUES ('Basket', '{item}');")
        
        dbRoutines.mysql.connection.commit()                                            
        cursor.close()

    # EDIT BELOW TO SELECT * from Basket 
    # cursor = dbRoutines.mysql.connection.cursor()
    # cursor.execute(f"use webapp_db;")
    # cursor.execute('SELECT * from Basket')
    # basket_data = cursor.fetchall()
    # cursor.close()

    # Join and select Food and Basket tables to provide data for page

    cursor = dbRoutines.mysql.connection.cursor()
    cursor.execute(f"use webapp_db;")
    cursor.execute('SELECT * FROM Food INNER JOIN Basket ON Food.FoodID = Basket.FoodID;')
    basket_data = cursor.fetchall()
    cursor.close()

    baskettype = type(basket)
    
   
    
    return render_template("basket.html", basket = basket_data, baskettype = baskettype)

@app.route('/orderreceived', methods=['GET', 'POST'])
def orderreceived():
  timestamp = datetime.now(tz=None)
  
  return render_template("orderreceived.html", timestamp = timestamp) 







@app.route('/confirmorder')
def confirmorder():
   pass
#  FOR EACH ITEM still in basket ITEMS, INSERT FOOD IDs INTO ORDERS TABLE

#     return render_template("orderreceived.html", orders = order_data)


@app.route('/orders')
def orders():
    cursor = dbRoutines.mysql.connection.cursor()
    cursor.execute(f"use webapp_db;")
    cursor.execute('SELECT * from Orders')
    order_data = cursor.fetchall()
    cursor.close()
    #RENDER ORDER HISTORY BY JOINING FOOD AND ORDER TABLES
    return render_template("orders.html", orders = order_data)




@app.route('/about')
def about():
    return render_template("about.html", company="Golden Dragon")


if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)








