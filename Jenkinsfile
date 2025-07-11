pipeline {
    agent any
    
    environment {
        SCANNER_HOME= tool 'sonar-scanner'
    }

    stages {
        stage('Git Checkout') {
            steps {
                git branch: 'main', credentialsId: 'git-cred', url: 'https://github.com/jaiswaladi246/Flask-postgresql.git'
            }
        }
        
        stage('Trivy FS Scan') {
            steps {
               sh 'trivy fs --format table -o fs.html .'
            }
        }
        
        stage('Sonarqube Analysis'){
            steps {
                withSonarQubeEnv('sonar'){
                        sh '$SCANNER_HOME/bin/sonar-scanner -Dsonar.projectName=multitier -Dsonar.projectKey=multitier'
                }
            }
        }
        
        stage('Docker Build & Tag') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker') {
                        sh 'docker build -t adijaiswal/flaskapp:latest .'
                        
                    }
                }
            }
        }
        
        stage('Trivy image Scan') {
            steps {
               sh 'trivy image --format table -o image.html adijaiswal/flaskapp:latest'
            }
        }
        
        stage('Docker Push') {
            steps {
                script {
                    withDockerRegistry(credentialsId: 'docker-cred', toolName: 'docker') {
                        sh 'docker push adijaiswal/flaskapp:latest'
                        
                    }
                }
            }
        }
        
        stage('Deploy To Kubernetes') {
            steps {
               withKubeConfig(caCertificate: '', clusterName: 'devopsshack-cluster', contextName: '', credentialsId: 'k8-token', namespace: 'webapps', restrictKubeConfigAccess: false, serverUrl: 'https://106B3EE2AEF1B9A1041B558B8FCC5D45.gr7.ap-south-1.eks.amazonaws.com') {
                        sh ' kubectl apply -f manifest.yml -n webapps'
                        sleep 30
                }
            }
        }
        
        stage('Verify the Deployment') {
            steps {
               withKubeConfig(caCertificate: '', clusterName: 'devopsshack-cluster', contextName: '', credentialsId: 'k8-token', namespace: 'webapps', restrictKubeConfigAccess: false, serverUrl: 'https://106B3EE2AEF1B9A1041B558B8FCC5D45.gr7.ap-south-1.eks.amazonaws.com') {
                        sh 'kubectl get pods -n webapps'
                        sh 'kubectl get svc -n webapps'
                       
                }
            }
        }
    }
}
