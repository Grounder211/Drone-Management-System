pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Grounder211/Drone-Management-System.git', branch: 'main'
            }
        }


             stage('Install Requirements') {
            steps {
                echo "Installing dependencies from requirements.txt"
                bat '"C:\\Users\\ebalnee\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" -m pip install -r requirements.txt'

            }
        }

        stage('Run Python App') {
            steps {
                echo "Running the Python application"
               bat '"C:\\Users\\ebalnee\\AppData\\Local\\Programs\\Python\\Python313\\python.exe" app.py'

            }
        }
    }
}
