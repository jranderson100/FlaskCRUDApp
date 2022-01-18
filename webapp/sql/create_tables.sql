START TRANSACTION;

-- Use (swtich to) webapp_db 
USE webapp_db;

-- Drop the Persons table if it exists


DROP TABLE IF EXISTS Food;
DROP TABLE IF EXISTS Basket;
DROP TABLE IF EXISTS Orders;

-- Create Food table


CREATE TABLE Food (
    FoodID int NOT NULL AUTO_INCREMENT,
    FoodName varchar(255) NOT NULL,
    FoodPrice float NOT NULL,
    FoodCalories int NOT NULL,
    FoodImage varchar(255),

    PRIMARY KEY (FoodID)
);


INSERT into Food (FoodName, FoodPrice, FoodCalories, FoodImage) VALUES ("Special Fried Rice", 6.99, 600, "specialfriedrice");
INSERT into Food (FoodName, FoodPrice, FoodCalories, FoodImage) VALUES ("Kung Po Chicken", 7.99, 781, "kungpochicken");
INSERT into Food (FoodName, FoodPrice, FoodCalories, FoodImage) VALUES ("Crispy Wontons", 7.99, 500, "crispywontons");
INSERT into Food (FoodName, FoodPrice, FoodCalories, FoodImage) VALUES ("Hoisin Duck and Pancakes", 7.99, 500, "duckandpancakes");

CREATE TABLE Basket (
    RowID int NOT NULL AUTO_INCREMENT,
    BasketRef varchar(255),
    FoodID int,
    OrderTime varchar(255), 
    Cost float,
    PostalAddress varchar(1000),

    PRIMARY KEY (RowID),
    FOREIGN KEY(FoodID) REFERENCES Food(FoodID)
);




CREATE TABLE Orders (
    OrderID int NOT NULL AUTO_INCREMENT,
    ItemOneFoodID int NOT NULL, 
    ItemTwoFoodID int,
    ItemThreeFoodID int,
    ItemFourFoodID int,
    TotalCost float NOT NULL,

    PRIMARY KEY (OrderID)
);


INSERT into Orders (ItemOneFoodID, ItemTwoFoodID, TotalCost) VALUES (10, 20, 30.99);