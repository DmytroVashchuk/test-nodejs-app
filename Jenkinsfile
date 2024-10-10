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
                    // Замість 'your-jenkins-credentials-id' використовуйте ваш реальний ID облікових даних для доступу до репозиторію
                    git url: 'https://github.com/DmytroVashchuk/test-nodejs-app.git', branch: 'main', credentialsId: 'your-jenkins-credentials-id'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker Image...'
                    // Перевірка Docker
                    sh 'docker --version'

                    // Створення Docker образу
                    sh 'docker build -t ${IMAGE_NAME} .'
                }
            }
        }

        /* stage('Run Tests') {
            steps {
                script {
                    echo 'Running tests...'
                    try {
                        // Запуск тестів всередині контейнера Docker
                        docker.image(IMAGE_NAME).inside {
                            sh 'npm test'
                        }
                    } catch (Exception e) {
                        // Встановлюємо статус збірки як "FAILURE", якщо тести не пройшли
                        currentBuild.result = 'FAILURE'
                        // Викидаємо помилку, щоб зупинити пайплайн
                        throw e
                    }
                }
            }
        } */

        stage('Push to Docker Hub') {
    steps {
        script {
            def IMAGE_NAME = 'dmytrovashchuk/test-nodejs-app'
            def DOCKER_CREDENTIALS = 'docker-hub-credentials'
            
            echo 'Pushing Docker image to Docker Hub...'
            docker.withRegistry('', DOCKER_CREDENTIALS) {
                docker.image(IMAGE_NAME).push('latest')
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
            // Можна додати ще більше дій у разі помилки (наприклад, повідомлення в Slack або email)
        }
    }
}
