pipeline {

	    agent any 
	
	    stages {
	        stage ('build'){
	        steps{
	            // sh 'docker-compose -f /var/lib/jenkins/workspace/MultiBranchPipeline-Job_main/webapp/docker-compose.yml up --build -d'
	       		echo 'build stage executed'
		   
		    }}
	
	        stage ('test'){
	        steps{
	            echo 'Test stage executed.'
	        }}
	
	        stage ('Deploy'){
	        steps{
	            echo 'Deployment stage executed.'
	        }}
	
	        stage ('Post Check'){
	        steps{
	            echo 'Post Checks stage executed.'
	        }}
	
	    }
	}