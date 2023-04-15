pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'https://github.com/JawadShaib/Wolrd_of_Games.git'
        DOCKER_IMAGE = 'world-of-games_jawad_shaib'
        DOCKERHUB_USERNAME = 'personal_docker_username'
        DOCKERHUB_PASSWORD = 'personal _password'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: env.GIT_REPO_URL
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -d -p 80:8777 --name app-container ${DOCKER_IMAGE}'
            }
        }

        stage('Test') {
            steps {
                sh 'docker exec app-container python e2e.py'
            }
        }

        stage('Terminate Container and Push Docker Image to Docker Hub') {
            steps {
                sh 'docker rm -f app-container'
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'DOCKERHUB_PASS', usernameVariable: 'DOCKERHUB_USER')]) {
                    sh 'docker login -u ${DOCKERHUB_USER} -p ${DOCKERHUB_PASS}'
                    sh 'docker push ${DOCKER_IMAGE}'
                }
            }
        }
    }
}