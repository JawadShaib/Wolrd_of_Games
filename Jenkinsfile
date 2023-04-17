pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'https://github.com/JawadShaib/Wolrd_of_Games.git'
        DOCKER_IMAGE = 'wog_jawadshaib'
        DOCKERHUB_USERNAME = ''
        DOCKERHUB_PASSWORD = ''
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: env.GIT_REPO_URL
            }
        }

        stage('Build') {
            steps {
                bat "docker build -t ${env.DOCKER_IMAGE} ."
            }
        }

        stage('Run') {
            steps {
                bat "docker run -d -p 80:8777 --name app-container ${env.DOCKER_IMAGE}"
            }
        }

        stage('Test') {
            steps {
                bat "python e2e.py"
            }
        }

        stage('Terminate Container and Push Docker Image to Docker Hub') {
            steps {
                bat "docker rm -f app-container"
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKERHUB_PASSWORD', usernameVariable: 'DOCKERHUB_USERNAME')]) {
                    bat "docker login -u ${env.DOCKERHUB_USERNAME} -p ${env.DOCKERHUB_PASSWORD}"
                    bat "docker push ${env.DOCKER_IMAGE}"
                }
            }
        }
    }
}
