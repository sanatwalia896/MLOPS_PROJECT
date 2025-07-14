pipeline {
    agent any 

    environment {
        GCP_PROJECT = "second-core-462010-p4"
        GCLOUD_PATH = '/var/jenkins_home/google-cloud-sdk/bin'
    }

    stages {

        stage('Cloning Github Repo to Jenkins') {
            steps {
                script {
                    echo 'Cloning Github Repo to Jenkins ............'
                    checkout scmGit(
                        branches: [[name: '*/main']],
                        extensions: [],
                        userRemoteConfigs: [[
                            credentialsId: 'github-token',
                            url: 'https://github.com/sanatwalia896/MLOPS_PROJECT.git'
                        ]]
                    )
                }
            }
        }

        stage('Building and Pushing Docker image to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Building and pushing Docker image to GCR ......'
                        sh """
                        export PATH=$PATH:${GCLOUD_PATH}

                        echo "Authenticating with GCP"
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        echo "Setting GCP project"
                        gcloud config set project ${GCP_PROJECT}

                        echo "Configuring Docker to use GCR"
                        gcloud auth configure-docker --quiet

                        echo "Building Docker image for linux/amd64"
                        docker buildx create --use || true
                        docker buildx build --platform=linux/amd64 -t gcr.io/${GCP_PROJECT}/ml-project:latest --push .
                        """
                    }
                }
            }
        }

        stage('Deploying to Google Cloud Run') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo 'Deploying to Google Cloud Run ......'
                        sh """
                        export PATH=$PATH:${GCLOUD_PATH}

                        echo "Authenticating with GCP"
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        echo "Setting GCP project"
                        gcloud config set project ${GCP_PROJECT}

                        echo "Deploying to Cloud Run"
                        gcloud run deploy ml-project \
                            --image=gcr.io/${GCP_PROJECT}/ml-project:latest \
                            --platform=managed \
                            --region=us-central1 \
                            --allow-unauthenticated
                        """
                    }
                }
            }
        }
    }
}
