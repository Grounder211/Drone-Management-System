pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Grounder211/Drone-Management-System.git'
		
            }
        }
	
	 stage('Run App in Container') {
            steps {
                sh '''
                docker run --rm -v "$PWD":/app -w /app python:3.11 \
                  "pip install -r requirements.txt && python app.py"
                '''
            }
        }

        
    }
}
