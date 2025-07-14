pipeline {
    agent any 

    environment {
        GCP_PROJECT = "second-core-462010-p4"
        GCLOUD_PATH = '/var/jenkins_home/google-cloud-sdk/bin'
    }

    stages {

        stage('Cloning GitHub Repo') {
            steps {
                script {
                    echo '📦 Cloning GitHub Repo to Jenkins...'
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

        stage('Build and Push Docker Image (linux/amd64)') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo '🐳 Building and pushing Docker image for linux/amd64...'
                        sh """
                        export PATH=$PATH:${GCLOUD_PATH}

                        echo "🔐 Authenticating with GCP"
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS} --quiet

                        echo "🔧 Setting GCP project"
                        gcloud config set project ${GCP_PROJECT} --quiet

                        echo "🔐 Configuring Docker to use GCR"
                        gcloud auth configure-docker --quiet

                        echo "🔨 Creating Docker buildx builder"
                        docker buildx create --use || true

                        echo "🐳 Building and pushing Docker image for amd64"
                        docker buildx build --platform=linux/amd64 -t gcr.io/${GCP_PROJECT}/ml-project:latest --push .
                        """
                    }
                }
            }
        }

        stage('Deploy to Google Cloud Run') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo '🚀 Deploying to Google Cloud Run...'
                        sh """
                        export PATH=$PATH:${GCLOUD_PATH}

                        echo "🔐 Authenticating with GCP"
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS} --quiet

                        echo "🔧 Setting GCP project"
                        gcloud config set project ${GCP_PROJECT} --quiet

                        gcloud run deploy ml-project \
                            --image=gcr.io/${GCP_PROJECT}/ml-project:latest \
                            --platform=managed \
                            --region=us-central1 \
                            --allow-unauthenticated \
                            --quiet

                        echo "✅ Cloud Run deployment complete!"
                        """
                    }
                }
            }
        }
    }
}
