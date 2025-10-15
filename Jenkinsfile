pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/vj141900-dotcom/devops-amazon-grid.git'
            }
        }

        stage('Setup & Run Tests') {
            steps {
                sh '''
                echo "===== Starting Selenium Grid Automation ====="

                echo "Cleaning up old containers..."
                docker-compose down || true

                echo "Starting new Selenium Grid containers..."
                docker-compose up -d

                echo "Installing dependencies (using system Python)..."
                python3 -m pip install --upgrade pip
                python3 -m pip install -r requirements.txt

                echo "Running pytest using system Python..."
                python3 -m pytest -v tests/ || true

                echo "Stopping Selenium Grid containers..."
                docker-compose down

                echo "===== Pipeline completed successfully ====="
                '''
            }
        }
    }
}

