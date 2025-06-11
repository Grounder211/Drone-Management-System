pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Grounder211/Drone-Management-System.git'
            }
        }

        stage('Install & Run') {
            steps {
                sh '''
                    pip install --upgrade pip --user --no-cache-dir
                    pip install -r requirements.txt --user --no-cache-dir
                    python app.py
                '''
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
