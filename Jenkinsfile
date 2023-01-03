def img
def container_name = "add_house_prices"
pipeline {
    environment {
        registry = "axelmastroianni/${container_name}"
        registryCredential = "docker-hub-login"
        dockerImage = ''
    }
    agent any

    stages {
        stage("Build image") {
            steps {
                script {
                    img = registry + ":${env.BUILD_ID}"
                    println("${img}")
                    dockerImage = docker.build("${img}")
                }
            }
        }

        stage("Testing - running in Jenkins node") {
            steps {
                powershell "docker run --name ${container_name} ${img}"
            }
        }

        stage("Stopping running container") {
            steps {
                powershell "docker stop ${container_name}"
            }
        }

        stage("Removing the container") {
            steps {
                powershell "docker rm ${container_name}"
            }
        }
    }
}