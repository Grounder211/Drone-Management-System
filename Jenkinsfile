pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Grounder211/Drone-Management-System.git', branch: 'main'
            }
        }


        stage('Debug') {
    steps {
        bat 'echo %PATH%'
        bat 'where python'
        bat 'where pip'
    }
}


        stage('Install Requirements') {
            steps {
                echo "Installing dependencies from requirements.txt"
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Python App') {
            steps {
                echo "Running the Python application"
                bat 'python app.py'
            }
        }
    }
}
