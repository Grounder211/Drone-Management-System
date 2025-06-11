pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.10'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Grounder211/Drone-Management-System.git'
            }
        }

        stage('Debug: List workspace') {
            steps {
                sh 'ls -l $WORKSPACE'
            }
        }

        stage('Run Python Script inside Docker') {
            steps {
                sh '''
                    docker run --rm \
                    -v "$WORKSPACE":/workspace \
                    -w /workspace \
                    $DOCKER_IMAGE /bin/bash -c "pip install -r requirements.txt && python app.py"
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
