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
                echo "=== Cleaning old containers ==="
                docker-compose down || true
                echo "=== Starting new Selenium Grid ==="
                docker-compose up -d
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                echo "=== Installing dependencies ==="
                /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m pip install --upgrade pip
                /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                echo "=== Running tests using full interpreter path ==="
                /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m pytest -v tests/ || true
                '''
            }
        }

        stage('Stop Selenium Grid') {
            steps {
                sh '''
                echo "=== Stopping Selenium Grid ==="
                docker-compose down
                '''
            }
        }
    }
}

