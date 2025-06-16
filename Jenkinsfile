pipeline {
    agent {
        docker {
            image 'python:3.9'
		echo 'docker pulled python'
        }
    }

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Grounder211/Drone-Management-System.git'
		
            }
        }

        stage('Debug: List files') {
            steps {
                sh 'ls -R'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}
