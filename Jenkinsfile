pipeline{
    agent any

    environment {
    VENV_DIR = 'venv'
    DOCKER_IMAGE = "himanshu863/ml-project:latest"
    MINIO_ENDPOINT = "http://minio:9000"
}


    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins............'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/HimanshuB0810/HotelReservation_MLOPS-1.git']])
                }
            }
        }
        stage('Setting up our Virtual Environment and Installing dependancies'){
            steps{
                script{
                    echo 'Setting up our Virtual Environment and Installing dependancies'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
        stage('Build and Push Docker Image'){
            steps{
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-creds',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]){
                    sh '''
                    echo "Building Docker image..."
                    docker build -t $DOCKER_IMAGE .

                    echo "Logging into Docker Hub..."
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin

                    echo "Pushing image to Docker Hub..."
                    docker push $DOCKER_IMAGE
                    '''
                }
            }
        }

        
    }
}