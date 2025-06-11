pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.10'
    }

    stages {
        stage('Debug: List workspace') {
            steps {
                sh 'ls -l /var/jenkins_home/workspace/jenkins_ci_demo'
            }
        }
        stage('Installing Requirements') {
            steps {
                git branch:'main',url:'https://github.com/Grounder211/Drone-Management-System.git'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Python Script in Docker') {
            steps {
                git branch:'main',url:'https://github.com/Grounder211/Drone-Management-System.git'
                sh 'python3 app.py'
            }
        }
    }

    post {
        success {
            echo '✅ Script ran successfully'
        }
        failure {
            echo '❌ Script failed'
        }
    }
}
