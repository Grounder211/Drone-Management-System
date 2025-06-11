pipeline {
    agent {
        docker {
            image 'python:3.10'
            image 'paketobuildpacks/pip'
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
                    python -m pip install -r requirements.txt
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
            echo '❌ Script failed'§
        }
    }
}
