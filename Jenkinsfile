pipeline
{
    agent any 

    stages {
        stage('Cloning Github Repo to Jenkins'){
            step{
                script{
                    echo'Cloning Github Repo to Jenkins ............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/sanatwalia896/MLOPS_PROJECT.git']])
                }
            }
        }
    }
}