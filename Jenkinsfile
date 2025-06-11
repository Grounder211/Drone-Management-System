pipeline {
    agent any  // Runs on any available Jenkins agent

    environment {
        DOCKER_IMAGE = 'python:3.10'
    }

    stages {
        stage('Pull Python Docker Image') {
            steps {
                echo 'Pulling Docker image...'
                sh 'docker pull $DOCKER_IMAGE'
            }
        }

        stage('Run Python Script inside Docker') {
            steps {
                echo 'Running main.py in Docker container...'
                sh '''
                    docker run --rm \
                    -v "$PWD":/app \
                    -w /app \
                    $DOCKER_IMAGE \
                    python app.py
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
