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
                // Checkout the latest code from the repoq
                git url: 'https://github.com/Grounder211/Drone-Management-System.git', branch: 'main'
            }
        }

        stage('Install Requirements') {
            steps {
                echo "Installing dependencies from requirements.txt"
                sh """
                    docker run --rm \
                    -v "${env.WORKSPACE}:${CONTAINER_WORKDIR}" \
                    -w ${CONTAINER_WORKDIR} \
                    ${DOCKER_IMAGE} \
                    /bin/bash -c "pip install -r requirements.txt"
                """
            }
        }

        stage('Run Python App') {
            steps {
                echo "Running the Python application"
                sh """
                    docker run --rm \
                    -v "${env.WORKSPACE}:${CONTAINER_WORKDIR}" \
                    -w ${CONTAINER_WORKDIR} \
                    ${DOCKER_IMAGE} \
                    /bin/bash -c "python app.py"
                """
            }
        }
    }
}
