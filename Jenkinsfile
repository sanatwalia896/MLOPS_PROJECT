pipeline {
    agent any 

    environment {
        VENV_DIR = 'venv'
        GCP_PROJECT = "second-core-462010-p4"
        GCLOUD_PATH = '/var/jenkins_home/google-cloud-sdk/bin'  // Added missing slash at the start
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

        stage('Setting up Virtual Environment and Installing Dependencies') {
            steps {
                script {
                    echo 'Setting up virtual environment and installing dependencies ............'

                    sh """
                    python3 -m venv \$VENV_DIR
                    . \$VENV_DIR/bin/activate
                    pip install --upgrade pip 
                    pip install -e .
                    """
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

                        echo "Building Docker image"
                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                        echo "Pushing Docker image to GCR"
                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest
                        """
                    }
                }
            }
        }
    }
}
