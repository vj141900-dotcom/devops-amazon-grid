pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/<your-username>/devops-amazon-grid.git'
            }
        }

        stage('Start Selenium Grid') {
            steps {
                sh '''
                echo "Starting Docker containers for Selenium Grid..."
                docker-compose down || true
                docker-compose up -d
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                echo "Installing dependencies using system Python..."
                /usr/local/bin/python3 -m pip install --upgrade pip
                /usr/local/bin/python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                echo "Running pytest using system Python..."
                /usr/local/bin/python3 -m pytest -v tests/
                '''
            }
        }

        stage('Stop Selenium Grid') {
            steps {
                sh '''
                echo "Stopping Docker containers..."
                docker-compose down
                '''
            }
        }
    }
}

