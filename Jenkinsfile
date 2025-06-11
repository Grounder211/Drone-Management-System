pipeline {
    agent any


    stages {
        stage('Check file') {
            steps {
                sh 'ls -l $WORKSPACE'
            }
        }
    }
    
    stages {
        stage('Pull Python Docker Image') {
            steps {
                sh 'docker pull python:latest'
            }
        }

        stage('Run Python Script inside Docker') {
            steps {
                sh '''
                    docker run --rm -v "$PWD":/workspace python:latest python /workspace/app.py



                '''
            }
        }
    }
}
