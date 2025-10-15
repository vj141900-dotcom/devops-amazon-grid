stage('Run Tests') {
    steps {
        sh '''
        echo "=== Waiting for Selenium Grid to initialize ==="
        sleep 15
        echo "=== Running tests using full interpreter path ==="
        /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m pytest -v tests/
        '''
    }
}

