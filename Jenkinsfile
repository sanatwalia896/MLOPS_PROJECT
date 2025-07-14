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

        stage('Building and Pushing Docker Image to GCR') {
            steps {
                withCredentials([file(credentialsId: 'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]) {
                    script {
                        echo '🐳 Building and pushing Docker image to GCR...'
                        sh """
                        export PATH=$PATH:${GCLOUD_PATH}

                        echo "🔐 Authenticating with GCP"
                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS} --quiet

                        echo "🔧 Setting GCP project"
                        gcloud config set project ${GCP_PROJECT} --quiet

                        echo "🔐 Configuring Docker to use GCR"
                        gcloud auth configure-docker --quiet

                        echo "🐳 Building Docker image (default linux/amd64)"
                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                        echo "📤 Pushing Docker image to GCR"
                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                        """
                    }
                }
            }
        }

        stage('Deploying to Google Cloud Run') {
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

                        echo "🚀 Deploying container to Cloud Run"
                        gcloud run deploy ml-project \
                            --image=gcr.io/${GCP_PROJECT}/ml-project:latest \
                            --platform=managed \
                            --region=us-central1 \
                            --allow-unauthenticated \
                            --quiet

                        echo "✅ Deployment to Cloud Run successful!"
                        """
                    }
                }
            }
        }
    }
}
