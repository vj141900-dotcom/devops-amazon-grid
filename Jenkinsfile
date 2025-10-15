pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/vj141900-dotcom/devops-amazon-grid.git'
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
                echo "Installing dependencies globally for Jenkins..."
                python3 -m pip install --upgrade pip
                python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                echo "Running pytest..."
                python3 -m pytest -v tests/ || true
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
