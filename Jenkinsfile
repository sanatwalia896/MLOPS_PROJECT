pipeline
{
    agent any 

    environment{
        VENV_DIR='venv'
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
    }
}