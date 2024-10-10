pipeline {
  agent { label 'jenkins-worker' }

  environment {
    DOCKER_CREDENTIALS = 'docker-hub-credentials'
    IMAGE_NAME = 'my-nodejs-app'
  }

  stages {
    stage('Pull Code') {
      steps {
        git 'https://github.com/DmytroVashchuk/test-nodejs-app.git'
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
}

