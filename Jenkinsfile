pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the latest code from the repo
                git url: 'https://github.com/Grounder211/Drone-Management-System.git', branch: 'main'
            }
        }

        
        stage('Install Requirements') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }
    

        stage('Run Python App') {
            steps {
                
                bat 'python app.py'
            }
        }
    }
}
