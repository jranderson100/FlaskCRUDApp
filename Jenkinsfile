pipeline {
	    agent any
	
	    stages {
	        stage ('build') {
	            steps{
	                echo 'Build stage executed.'
	                sh 'docker-compose -f /var/lib/jenkins/workspace/FlaskCRUDApp_main/webapp/docker-compose.yml up --build -d'
			echo 'Build stage completed.'
	            }
	        }
	
	        stage ('test') {
	            steps{
	                echo 'Test stage executed.'
			sh 'docker run -i --rm --name test_fetch_food_data -v "$PWD":/home/jranderson100/Documents/Development/FlaskCRUDApp/webapp/webapp/tests/unit -w /home/jranderson100/Documents/Development/FlaskCRUDApp/webapp/webapp/tests/unit python:3 python3 test_fetch_food_data.py'
	            }
	        }
	
	        stage ('deploy') {
	            steps{
	                echo 'Deploy stage executed.'
	            }
	        }
	    }
	}
