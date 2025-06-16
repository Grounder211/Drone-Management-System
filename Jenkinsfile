pipeline {
    agent {
	docker {
            image 'python:3.9'
        }
	}

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Grounder211/Drone-Management-System.git'

            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}
