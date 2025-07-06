pipeline
{
    agent any 

    environment{
        VENV_DIR='venv'
        GCP_PROJECT="second-core-462010-p4"
        GCLOUD_PATH='var/jenkins_home/google-cloud-sdk/bin'
    }

    stages {
        stage('Cloning Github Repo to Jenkins'){
            steps{
                script{
                    echo'Cloning Github Repo to Jenkins ............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/sanatwalia896/MLOPS_PROJECT.git']])
                }
            }
        }
        stage('Setting up our vitual environment and Installing Dependencies'){
            steps{
                script{
                    echo'Setting up our vitual environment and Installing Dependencies ............'
                    
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip 
                    pip install -e .
                    '''
                }
            }
        }
        stage('Building and Pushing Docker image to GCR '){
            steps{
               withCredentials([file(credentialsId:'gcp-key',variable:'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'Building and pushing Docker image to GCR ......'
                        sh '''
                        export PATH=$PATH:$(GCLOUD_PATH)

                        gcloud auth activate-service-account --key-file=${GOOGLE_APPLICATION_CREDENTIALS}

                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/ml-project:latest .

                        docker push gcr.io/${GCP_PROJECT}/ml-project:latest 
                        '''

                    }
               }
            }
        }
    }
}