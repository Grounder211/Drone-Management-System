pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'python:3.10'
    }

    stages {
        stage('Verify workspace contents') {
            steps {
                sh 'ls -l $WORKSPACE'
            }
        }

        stage('Run Python Script inside Docker') {
            steps {
                sh '''
                    docker run --rm \
                    -v "$WORKSPACE":/workspace \
                    $DOCKER_IMAGE \
                    python /workspace/app.py
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Python script ran successfully!'
        }
        failure {
            echo '❌ Python script failed.'
        }
    }
}
