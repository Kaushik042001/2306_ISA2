pipeline {
  agent any  // Use any available agent
  
  stages {
    stage('Clone GitHub Repository') {
      steps {
        script {
          // Clone the GitHub repository
          bat "git clone https://github.com/Kaushik042001/2306_ISA2.git"
        }
      }
    }
    
    stage('Build Docker Image') {
      steps {
        script {
          // Build the Docker image from the Dockerfile in the cloned repository
          bat "docker build -t 2306kaushik/2306"
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
    
    stage('Copy application.py and Clean Up') {
      steps {
        script {
          bat "docker cp my-app-container:/path/to/application.py ./application.py"
          bat "docker rm -f 2306 || exit 0"
        }
      }
    }
  }
}
