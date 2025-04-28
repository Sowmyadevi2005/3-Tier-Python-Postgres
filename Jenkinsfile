pipeline {
    agent { label 'Agent-1' }
    environment {
        VENV_DIR = "myenv"
    }

    stages {
        stage('python install & venv setup') {
            steps {
                sh'''
                sudo apt update
                sudo apt install python3.12-venv -y python3-pip -y
                python3 -m venv $VENV_DIR
                . $VENV_DIR/bin/activate
                pip3 install -r requirements.txt
                '''
            }
        }
        stage('Install Postgres') {
            steps {
                sh'''
                sudo apt-get install -y postgresql postgresql-contrib
                sudo systemctl start postgresql
                sudo systemctl enable postgresql
                '''
            }
        }
stage('Configure PostgreSQL DB & User') {
    steps {
        sh '''
              sudo -u postgres psql -c "CREATE USER root WITH PASSWORD 'root';"
                sudo -u postgres psql -c "CREATE DATABASE my_database;"
                sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE my_database TO root;"
                sudo -u postgres psql -d my_database -c "GRANT ALL PRIVILEGES ON SCHEMA public TO root;"
                sudo -u postgres psql -c "GRANT CREATE ON DATABASE my_database TO root;"
        '''
    }
}

    }
}
