pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {

        stage('Install') {
        steps {
            git branch: 'main', url: 'https://github.com/Grounder211/Drone-Management-System.git'
            sh 'pip install --upgrade pip'
        }
    }
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Grounder211/Drone-Management-System.git'
            }
        }

        stage('Install & Run') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python app.py'
            }
        }
    }

    post {
        success {
            echo '✅ Done!'
        }
        failure {
            echo '❌ Something went wrong.'
        }
    }
}
