from flask import Flask, render_template, request
from datetime import datetime
from db_routines import DbRoutines
import math 

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

@app.route('/', methods=['GET', 'POST'])
def index():
    cursor = dbRoutines.mysql.connection.cursor()
    cursor.execute(f"use webapp_db;")
    cursor.execute('SELECT * from Food')
    food_data = cursor.fetchall()
    cursor.close()

  
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
        address = request.form['addressfield']
        cursor.execute(f"Insert INTO `Basket` (`BasketRef`, `PostalAddress` ) VALUES ('Basket','{address}');")
        dbRoutines.mysql.connection.commit()                                            
        cursor.close()

    

    # Join and select Food and Basket tables to provide data for page

    cursor = dbRoutines.mysql.connection.cursor()
    cursor.execute(f"use webapp_db;")
    cursor.execute('SELECT * FROM Food INNER JOIN Basket ON Food.FoodID = Basket.FoodID;')
    basket_data = cursor.fetchall()
    cursor.execute('SELECT PostalAddress FROM Basket WHERE PostalAddress IS NOT NULL;')
    address = cursor.fetchall()
    cursor.execute('SELECT SUM(FoodPrice) FROM Food INNER JOIN Basket ON Food.FoodID = Basket.FoodID WHERE Basket.FoodID IS NOT NULL;')
    total_cost_tuple = cursor.fetchall()
    cursor.close()
    total_cost_dict = total_cost_tuple[0]
    
    final_total_cost = math.floor(total_cost_dict['SUM(FoodPrice)'] * 100) / 100.0

    
   #CALCULATE TOTAL COST AND INSERT IT INTO RENDER TEMPLATE
    
    return render_template("basket.html", basket = basket_data, address = address, final_total_cost = final_total_cost)

@app.route('/orderreceived', methods=['GET', 'POST'])
def orderreceived():
    cursor = dbRoutines.mysql.connection.cursor()
    cursor.execute(f"use webapp_db;")
    cursor.execute('SELECT * FROM Food INNER JOIN Basket ON Food.FoodID = Basket.FoodID;')
    basket_data = cursor.fetchall()
    
    if request.form['addressfield'] != "":
        new_address = request.form['addressfield']
        cursor.execute(f"UPDATE Basket SET `PostalAddress` = '{new_address}' WHERE `BasketRef` = 'Basket';")
        dbRoutines.mysql.connection.commit()                                            
        

    cursor.execute('SELECT PostalAddress FROM Basket WHERE PostalAddress IS NOT NULL;')
    address = cursor.fetchall()
    cursor.execute('SELECT SUM(FoodPrice) FROM Food INNER JOIN Basket ON Food.FoodID = Basket.FoodID WHERE Basket.FoodID IS NOT NULL;')
    total_cost_tuple = cursor.fetchall()
    cursor.close()
    total_cost_dict = total_cost_tuple[0]
    
    final_total_cost = math.floor(total_cost_dict['SUM(FoodPrice)'] * 100) / 100.0
    
    timestamp = datetime.now(tz=None)

    #ADD DATA TO PASS TO ORDERS PAGE

    return render_template("orderreceived.html", timestamp = timestamp, basket = basket_data, final_total_cost = final_total_cost, address = address)

# IF address bar contains alternative address UPDATE Basket SET PostalAddress = {newenteredaddress} 

#   POST INSERT new order into ORDERS 

#GET INFO FROM BASKET AND PUBLISH TOTAL COST...?
  #ADD NAME AND ADDRESS ON MENU PAGE THEN UPDATE BEFORE YOU SUBMIT ON BASKET PAGE





@app.route('/orders', methods=['GET', 'POST'])
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








