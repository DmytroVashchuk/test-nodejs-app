pipeline {
  agent any  // Використовуємо будь-яку доступну ноду

  environment {
    DOCKER_CREDENTIALS = 'docker-hub-credentials' // Ім'я ваших облікових даних Docker Hub у Jenkins
    IMAGE_NAME = 'dmytrovashchuk/test-nodejs-app' // Ваш репозиторій на Docker Hub
  }

  stages {
    stage('Pull Code') {
      steps {
        script {
          echo 'Pulling code from GitHub...'
          git url: 'https://github.com/DmytroVashchuk/test-nodejs-app.git', branch: 'main', credentialsId: 'your-jenkins-credentials-id'
        }
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          echo 'Building Docker Image...'
          docker.build(IMAGE_NAME)
        }
      }
    }

    stage('Run Tests') {
      steps {
        script {
          echo 'Running tests...'
          try {
            docker.image(IMAGE_NAME).inside {
              sh 'npm test'
            }
          } catch (Exception e) {
            currentBuild.result = 'FAILURE'
            throw e
          }
        }
      }
    }

    stage('Push to Docker Hub') {
      when {
        branch 'main'  // Виконується лише на гілці 'main'
      }
      steps {
        script {
          echo 'Pushing Docker image to Docker Hub...'
          docker.withRegistry('', DOCKER_CREDENTIALS) {
            docker.image(IMAGE_NAME).push()
          }
        }
      }
    }

    stage('Failure') {
      when {
        expression {
          return currentBuild.result == 'FAILURE'
        }
      }
      steps {
        echo 'Tests failed'
      }
    }
  }

  post {
    failure {
      echo "Pipeline failed!"
    }
  }
}
