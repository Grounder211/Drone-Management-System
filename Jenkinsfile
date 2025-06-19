pipeline {
    agent any

    triggers {
        // Automatically trigger build on GitHub push
        githubPush()
    }

    environment {
        DOCKER_IMAGE = 'python:3.11'
        CONTAINER_WORKDIR = '/app'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Grounder211/Drone-Management-System.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t drone-app .'
            }
        }

        stage('Run App in Docker') {
            steps {
                sh 'docker run --rm drone-app'
            }
        }
    }
}

}
