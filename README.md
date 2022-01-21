# Final Project Report - QA DevOps Bootcamp

## James Anderson (DfECloud2)

https://github.com/jranderson100/FlaskCRUDApp 

Diagrams to illustrate this report can be found in the accompanying Project Documentation PDF in the repository.

My video demonstration of the app can be found here. ***


## Explanation of app and how it fulfils the brief

My web app is the beginning of a food ordering website. The landing page, a Menu Page displays a list of food options, allows the user to make a selection (or selections), enter their address and then proceed to a Basket page. In this Basket page, users can see the total cost of their order and a) empty their basket and start again b) confirm their order or c) update their address and then confirm their order. The next page confirms the details of their order and allows them to return to the Menu page, or to an Order History page which does not yet show information.  The web app achieves the brief’s required CRUD functionality as follows:

Create - Users can make selections and create a basket of their required food items and their address. This creates new records in the Basket SQL table.


Read - On the menu page, users can read data served from the Food SQL table in order to make their selection. On the Basket and Order Confirmed pages the user    can read data served from both the Food and Basket tables, joined with a JOIN statement.

 

Update - On the Basket page,  users can update their address (the PostalAddress field of the Basket SQL table).

Delete - On the Basket page, the user can empty their basket and return to the Menu page to begin a new order. This involves deleting all of the contents of the  Basket SQL table 


Additionally, the app meets the following requirements as laid out by the brief:

I have used Docker containers to build and host the application

I have built a a CI/CD pipeline using Jenkins to build and test my application, including a webhook to trigger Jenkins to build a new pipeline when I push code to my repository.

I am using a separate database service (MySQLContainer) which features two tables, Food and Basket (in addition to a fledgling Orders table) which have a relationship

I also tested the application using a unittest during the build stage of the Jenkins pipeline.

I have provided the following documentation:

Fig . 1 -  A diagram of the container architecture of my application

Fig. 2 - My MoSCoW chart used for planning my application

Fig. 3. -  A user journey board featuring user stories to help design the functionality of each page

Fig. 4 -  My Jira board used for planning my project timeline and sprints of development

Fig. 5  - An Entity Relationship Diagram (ERD) showing the relationship between rows in my two main tables 

Fig. 6 - An ERD for next steps showing how an Orders table would be integrated into the project. 

Fig. 7 and 8 - Reports for my unittest 
        
Fig. 9 and 10 - My webhook functionality



## Technical description of how the app works

	

### Setting up and creating the basket page

An instance of the Flask object (called “app”) is created and its relationship to my SQL database is configured.

The route (‘/’) is created for the landing/menu page.

This route’s index() function then makes a request to the SQL database selecting all data from the Food table and ensures that the Basket table is empty, using a DELETE statement. 

The data from the Food table is then passed into the render templates of the index.html page, the Menu page using dynamic paths for the images.

On the Menu page, the Food data passed into is deconstructed/unpackaged and passed into the appropriate HTML elements.

The user can make food selections and enter their address using a HTML form (checkboxes and a text input). They can then click the ‘Add to basket” button, which reroutes them to the Basket page (‘/basket’). This route’s basket() function inserts the user’s address and the FoodIDs of the selected food items (taken from the value of the checked HTML checkboxes) into the Basket table. The basket items are connected by a common “BasketRef” attribute.


### Creating the basket page 

The basket() function then makes a new request to the SQL database, getting data from both the Food and Basket page, and joining them on FoodID, in order to render the required information to provide the user with a basket. 

A new SQL request is made for the sum of all of the FoodPrice rows which are not NULL. This “total cost” data is passed, along with the other Food and Basket data, into the Basket page (basket.html) render template. 


### Revising or confirming the order on the basket page 

In the Basket page, the data retrieved from the SQL database is again deconstructed and used to populate the page, including a new total cost value.

The user can then either:

Click the “Empty basket” button, send a DELETE * statement to the database, emptying the Basket table, and return to the Menu page (‘/’ index.html) 

Re-enter their address, thus triggering upon submission an UPDATE call to the database and updating the Postal Address field in the Basket table with the new address

Click the “Confirm order” button which passes all the same data, as well as a new timestamp variable, into the render template of the next page ( ‘/orderreceived’) (“orderreceived.html)


The Order Confirmed page displays the order details (food, address and the new timestamp)


This is effectively the end of the app’s functionality. They can then click back through to the main page, again emptying the Basket table, or click through to an unfinished Orders page into which merely some placeholder data has been passed.




## A technical description of how the pipeline works

Through the Jenkinsfile in the main branch of my Github repository, Jenkins begins the build phase of the pipeline. 

Jenkins triggers docker-compose.yml which spins up my flask web app container (at localhost:5000), my sql database container(at localhost:3306) and my phpmyadmin container (at localhost:1001). 

The pipeline then proceeds to the Test phase, wherein the Jenkinsfile runs the test_images_test.py to check that the required food images are present in the webapp container. 

The pipeline moves over to the Deploy phase

I also set up a webhook with Github so that whenever I push new code to my repository it triggers Jenkins to build a new pipeline (see Fig. 9 and Fig. 10) 



## A report on the  tests run

At the test stage of the Jenkins pipeline, Jenkins runs a unit test to check that the image files are present in the working directory. See Fig. 7 for evidence of the passed test and also Fig. 8 for the test passing in Visual Studio Code.


## Risk assessment
The config details of my database are currently quite public in the main app.py page. By using Docker secrets or a similar tech, or placing these in a different file, it would significantly reduce the risk of the database admin details being accessed and used by unintended agents.

## Improvements to be made

More testing 

You may see from the “testing” branch of my github repository that I attempted to write unit tests to make a test call to the SQL database. 

Use of MVC/Flask data models

This would allow me to use effective object oriented models to interact with the database and save state locally rather than making so many calls to the SQL database. However, although slightly less efficient, I made the design choice to make more calls to the database and not create state locally, so as to avoid a whole class of bugs and keep things simple.

Use of SQL Alchemy 

We were advised during lectures, however, that we wouldn’t need to use this tech after all.

Use of Docker Swarm to deploy app

Through no fault of our instructor, our introduction to Docker Swarm was some time ago, and quite brief. With a little more time on this topic I would have been more comfortable with using Docker Swarm for the final project. 

Greater functionality

Then next step is to pass the basket data into a new Orders data, to capture instances of basket objects and provide further opportunity to join rows from different tables to render the data for the user. The "remove this item from the basket" checkboxes on the basket page do not work. A model-based architecture would give me greater flexility here, rather than tying all of my functions to routing.  

Style improvements

My app could be smarter stylistically, but in the short time frame I was focusing on functionality. My timestamp needs to be reformatted on the order page. 
