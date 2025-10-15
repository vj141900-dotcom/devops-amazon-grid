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

                echo "Installing dependencies..."
                .venv/bin/python3 -m pip install --upgrade pip
                .venv/bin/python3 -m pip install -r requirements.txt

                echo "Running pytest using Python module..."
                .venv/bin/python3 -m pytest -v tests/ || true

                echo "Stopping Selenium Grid containers..."
                docker-compose down

                echo "===== Pipeline completed successfully ====="
                '''
            }
        }
    }
}

