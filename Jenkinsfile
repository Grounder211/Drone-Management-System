pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }
    stages {
        stage('Run Python Script') {
            steps {
                sh 'python main.py'
            }
        }
    }

    
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run script') {
            steps {
                sh 'python app.py'
            }
        }
    }


