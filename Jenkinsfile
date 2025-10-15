        stage('Install Dependencies') {
            steps {
                sh '''
                echo "Activating virtual environment and installing dependencies..."
                python3 -m venv .venv
                source .venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                echo "Running pytest inside virtual environment..."
                source .venv/bin/activate
                pytest -v tests/
                '''
            }
        }

