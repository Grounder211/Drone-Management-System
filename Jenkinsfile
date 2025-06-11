pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.10'
    }

    stages {
        stage('Pull Python Docker Image') {
            steps {
                sh 'docker pull $DOCKER_IMAGE'
            }
        }

        stage('Run Python Script inside Docker') {
            steps {
                sh '''
                    docker run --rm \
    -v "$PWD":/workspace \
    $DOCKER_IMAGE \
    python app.py

                '''
            }
        }
    }
}
