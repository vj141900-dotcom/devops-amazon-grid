pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/vj141900-dotcom/devops-amazon-grid.git'
            }
        }

        stage('Run Full Automation') {
            steps {
                sh '''
                echo "===== Starting Selenium Grid Automation ====="

                echo "Stopping old containers (if any)..."
                docker-compose down || true

                echo "Starting Selenium Grid containers..."
                docker-compose up -d

                echo "Setting up Python virtual environment..."
                python3 -m venv .venv
                source .venv/bin/activate

                echo "Installing dependencies..."
                pip install --upgrade pip
                pip install -r requirements.txt

                echo "Running pytest inside virtual environment..."
                pytest -v tests/ || true

                echo "Stopping Selenium Grid containers..."
                docker-compose down

                echo "===== Pipeline completed ====="
                '''
            }
        }
    }
}

