pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Grounder211/Drone-Management-System.git', branch: 'main'
            }
        }

        stage('Show Workspace Files') {
            steps {
                echo "Jenkins Workspace Path: ${env.WORKSPACE}"
                sh "ls -la ${env.WORKSPACE}"
            }
        }

        stage('Install Requirements') {
            steps {
                echo "Installing dependencies from requirements.txt"
                sh """
                    docker run --rm \
                    -v "${env.WORKSPACE}:/app" \
                    -w /app \
                    python:3.11 \
                    /bin/bash -c "ls -la && cat requirements.txt && pip install -r requirements.txt"
                """
            }
        }

        stage('Run Python App') {
            steps {
                echo "Running the Python application"
                sh """
                    docker run --rm \
  -v /home/neeraj/jenkins_home/workspace/jenkins_ci_demo:/app \
  -w /app \
  python:3.11 \
  /bin/bash -c "pip install -r requirements.txt && python app.py"

                """
            }
        }
    }
}
