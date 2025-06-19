pipeline {
    agent any

    triggers {
        // Automatically trigger build on GitHub push
        githubPush()
    }

    environment {
        DOCKER_IMAGE = 'python:3.11'
        CONTAINER_WORKDIR = '/app'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the latest code from the repoqq
                git url: 'https://github.com/Grounder211/Drone-Management-System.git', branch: 'main'
            }
        }

        stage('Check Workspace') {
  steps {
    sh 'pwd'
    sh 'ls -la'
  }
}

        
        stage('Install Requirements') {
    steps {
        sh '''
          docker run --rm \
          -v "$PWD:/app" \
          -w /app \
          python:3.11 \
          pip install -r requirements.txt
        '''
    }
}



        stage('Run Python App') {
            steps {
                echo "Running the Python application"
                sh """
                    docker run --rm \
                    -v "${env.WORKSPACE}:${CONTAINER_WORKDIR}" \
                    -w ${CONTAINER_WORKDIR} \
                    ${DOCKER_IMAGE} \
                    /bin/bash -c "python app.py"
                """
            }
        }
    }
}
