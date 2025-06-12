pipeline {
    agent {
       any docker {
            image 'python:3.10'
        }
      
    }
    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Grounder211/Drone-Management-System.git'
		
            }
        }


        stage('Install') {
            steps {
		        sh 'pip install --upgrade pip'
			    sh 'python -m pip install -r requirements.txt'
                    
            }
        }
        stage('Run ') {
            steps {
                sh 'python app.py'
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
