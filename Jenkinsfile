pipeline {
    agent any
    stages {
        stage('Install') {
            steps {
                sh 'python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Run') {
            steps {
                sh 'source venv/bin/activate && python app.py'
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
