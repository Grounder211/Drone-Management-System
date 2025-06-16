pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Grounder211/Drone-Management-System.git', branch: 'main'
            }
        }

        stage('Verify Files') {
            steps {
                sh 'ls -la'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh """
                    docker run --rm \
                    -v "${WORKSPACE}:/app" \
                    -w /app python:3.11 \
                    /bin/bash -c "ls -la && cat requirements.txt && pip install -r requirements.txt"
                """
            }
        }

        stage('Run Python App') {
            steps {
                sh """
                    docker run --rm \
                    -v "${WORKSPACE}:/app" \
                    -w /app python:3.11 \
                    /bin/bash -c "python app.py"
                """
            }
        }
    }
}
