pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.10'
    }

    stages {
        stage('Debug: List workspace') {
            steps {
                sh 'ls -l /var/jenkins_home/workspace/jenkins_ci_demo'
            }
        }

        stage('Run Python Script in Docker') {
            steps {
                sh '''
                    docker run --rm \
                    -v /var/jenkins_home/workspace/jenkins_ci_demo:/workspace \
                    python:3.10 \
                    python /workspace/app.py
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
