pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/Grounder211/Drone-Management-System.git'
      }
    }
    stage('List files') {
      steps {
        sh 'ls -l $PWD'
      }
    }
    stage('Run Python app') {
      steps {
        sh 'docker run --rm -v /var/jenkins_home/workspace/jenkins_ci_demo:/app -w /app python:3.11 /bin/bash -c "pip install -r requirements.txt && python app.py"'
      }
    }
  }
}
