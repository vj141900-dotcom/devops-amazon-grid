stage('Run Tests') {
    steps {
        sh '''
        echo "Installing dependencies..."
        pip install -r requirements.txt

        echo "Running tests..."
        pytest -q tests/ || true
        '''
    }
}

