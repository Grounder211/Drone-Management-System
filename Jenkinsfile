pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main', url: 'https://github.com/Grounder211/Drone-Management-System.git'

            }
        }

        stage('Set Up Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate

                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Python Script') {
            steps {
                sh '''
                    . venv/bin/activate

                    python3 app.py
                '''
            }
        }
    }
}
