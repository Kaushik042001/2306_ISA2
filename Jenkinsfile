pipeline {
  agent any
  
  stages {
    stage('Build Docker Image') {
      steps {
        script {
          // Build the Docker image from the Dockerfile in the current directory
          bat "docker build -t 2306kaushik/2306 ."
        }
      }
    }
    
    stage('Build and Run Docker Container') {
      steps {
        script {
          // Remove any existing container with the same name to avoid conflicts
          bat "docker rm -f my-app-container || exit 0"
          
          // Run the Docker container in detached mode
          bat "docker run -d --name my-app-container 2306kaushik/2306"
        }
      }
    }
    
    stage('Copy application.py') {
      steps {
        script {
          // Copy the application.py file from the running container to the host
          bat "docker cp my-app-container:/opt/to/application.py ./application.py"
        }
      }
    }
    
    stage('Cleanup') {
      steps {
        script {
          // Stop and remove the container to clean up the environment
          bat "docker rm -f my-app-container || exit 0"
        }
      }
    }
  }
}
