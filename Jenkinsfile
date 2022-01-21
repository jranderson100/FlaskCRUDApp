pipeline {
	    agent any
	
	    stages {
	        stage ('build') {
	            steps{
	                echo 'Test stage executed.'
	                sh 'docker-compose -f /var/lib/jenkins/workspace/FlaskCRUDApp_main/webapp/docker-compose.yml up --build -d'
	            }
	        }
	
	        stage ('test') {
	            steps{
	                echo 'Test stage executed.'
			    	sh 'python3 webapp/webapp/test_images_test.py'
	            }
	        }
	
	        stage ('deploy') {
	            steps{
	                echo 'Deploy stage to be added.'
	            }
	        }
	    }
	}
