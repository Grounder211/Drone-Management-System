pipeline {
  agent any

  environment {
    SERVER_SCRIPT = "C:\Users\ebalnee\OneDrive - Ericsson\Desktop\test\Drone-Management-System\start_server.bat"
  }

  stages {
    stage('Pull Repo') {
      steps {
        git 'https://github.com/Grounder211/Drone-Management-System.git'
      }
    }

    stage('Start Local Server') {
      steps {
        echo "Launching local HTTP server..."
        bat "${env.SERVER_SCRIPT}"
      }
    }

    stage('Wait/Health Check') {
      steps {
        echo "Checking if server is listening on port 8000..."
        bat 'curl http://localhost:8000'
      }
    }
  }

  post {
    success {
      echo "Server started and is listening. Jenkins job completed."
    }
    failure {
      echo "Failed to start server."
    }
  }
}
