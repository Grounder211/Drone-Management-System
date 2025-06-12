pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }
    stages {
        stage('Install') {
            steps {
                sh 'python -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }
        stage('Run') {
            steps {
                sh './venv/bin/python app.py'
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
