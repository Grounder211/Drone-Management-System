pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Grounder211/Drone-Management-System.git'
            }
        }

        stage('List files') {
            steps {
                sh 'ls -la'
            }
        }

        stage('Run Python app') {
            steps {
                sh '''
                    docker run --rm -v $PWD:/app -w /app python:3.11 /bin/bash -c "pip install -r requirements.txt && python app.py"
                '''
            }
        }
    }
}
