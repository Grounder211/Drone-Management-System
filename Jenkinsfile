pipeline {
    agent any

    
    stages {
        stage('Pull Python Docker Image') {
            steps {
                sh 'docker pull python:latest'
            }
        }

        stage('Run Python Script inside Docker') {
            steps {
                sh '''
                     docker run python app.py

                '''
            }
        }
    }
}
