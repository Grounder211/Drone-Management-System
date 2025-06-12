pipeline {
    agent {
        any
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Grounder211/Drone-Management-System.git'
            }
        }
        stage('Install') {
            steps {
                sh 'docker inspect -f . python:latest'
                sh 'docker pull python:latest'

                sh 'pip install --upgrade pip'
                echo 'successfully installed pip- '
                sh 'python -m pip install -r requirements.txt'
            }
        }
        stage('Run') {
            steps {
                sh 'python app.py'
            }
        }
    }
    post {
        success {
            echo '✅ Script ran successfully'
        }
        failure {
            echo '❌ Script failed'
            // Print workspace contents to debug
            sh 'ls -l'
            // Print last few lines of logs or relevant files if needed
        }
    }
}
