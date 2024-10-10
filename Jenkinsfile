pipeline {
  agent any  // Використовуємо будь-яку доступну ноду

  environment {
    DOCKER_CREDENTIALS = 'docker-hub-credentials' // Ім'я ваших облікових даних Docker Hub у Jenkins
    IMAGE_NAME = 'dmytrovashchuk/test-nodejs-app' // Ваш репозиторій на Docker Hub
  }

  stage('Pull Code') {
  steps {
    git url: 'https://github.com/DmytroVashchuk/test-nodejs-app.git', branch: 'main', credentialsId: 'your-jenkins-credentials-id'
  }
}

    stage('Build Docker Image') {
      steps {
        script {
          docker.build(IMAGE_NAME)
        }
      }
    }

    stage('Run Tests') {
      steps {
        script {
          docker.image(IMAGE_NAME).inside {
            sh 'npm test'
          }
        }
      }
    }

    stage('Push to Docker Hub') {
      when {
        branch 'main'
        expression {
          return currentBuild.result == null || currentBuild.result == 'SUCCESS'
        }
      }
      steps {
        script {
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
