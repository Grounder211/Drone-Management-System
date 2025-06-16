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
                script {
                    def workspace = env.WORKSPACE
                    sh """
                        docker run --rm -v ${workspace}:/app -w /app python:3.11 \
                        /bin/bash -c "pip install -r requirements.txt"
                    """
                }
            }
        }

        stage('Run Python App') {
            steps {
                script {
                    def workspace = env.WORKSPACE
                    sh """
                        docker run --rm -v ${workspace}:/app -w /app python:3.11 \
                        /bin/bash -c "python app.py"
                    """
                }
            }
        }
    }
}
