pipeline {
  agent any  // Use any available agent
  
  stages {
    stage('Build Docker Image') {
      steps {
        script {
          // Build the Docker image from the Dockerfile in the current directory
          bat "docker build -t 2306kaushik/dock ."
        }
      }
    }
    
    stage('Build and Run Docker Container') {
      steps {
        script {
          // Remove any existing container with the same name to avoid conflicts
          bat "docker rm -f my-app-container || exit 0"
          
          // Run the Docker container in detached mode
          bat "docker run -d --name my-app-container 2306kaushik/dock"
        }
      }
    }
  }
}
