pipeline {
    agent any

    

    stages {
        stage('Pull Python Docker Image') {
            steps {
                sh 'docker pull $DOCKER_IMAGE'
            }
        }

        stage('Run Python Script inside Docker') {
            steps {
                sh '''
                      python app.py

                '''
            }
        }
    }
}
