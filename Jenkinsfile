pipeline {  
    stages{
        stage ('clone') {
            steps{
                git branch: 'master',
                    url:'https://github.com/Kavibalan1904/three-tier.git'
            }
        }
        stage ('Build Frontend') {
            steps{
                sh '''
                cd Frontend
                docker build -t kavidevops03/threetier-frontend:latest

                '''
            }
        }
        stage ('Build Backend') {
            steps{
                sh '''
                cd Backend
                docker build -t kavidevops03/threetier-backend:latest
                '''
            }
        }
        stage ('Docker Push') {
            steps{
                sh '''
                docker push kavidevops03/threetier-frontend:latest
                docker push kavidevops03/threetier-backend:latest
                '''
            }
        }
        stage('Deploy Kubernetes') {
            steps{
                sh '''
                kubectl apply -f K8s
                '''
            }
        }

    }
}
