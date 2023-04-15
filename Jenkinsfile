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
                bat 'docker build -t ${DOCKER_IMAGE} .'
            }
        }

        stage('Run') {
            steps {
                bat 'docker run -d -p 80:8777 --name app-container ${DOCKER_IMAGE}'
            }
        }

        stage('Test') {
            steps {
                bat 'docker exec app-container python e2e.py'
            }
        }

        stage('Terminate Container and Push Docker Image to Docker Hub') {
            steps {
                bat 'docker rm -f app-container'
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKERHUB_PASS', usernameVariable: 'DOCKERHUB_USER')]) {
                    bat 'docker login -u ${DOCKERHUB_USER} -p ${DOCKERHUB_PASS}'
                    bat 'docker push ${DOCKER_IMAGE}'
                }
            }
        }
    }
}