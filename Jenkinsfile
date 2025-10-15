stage('Run Tests') {
    steps {
        sh '''
        echo "=== Waiting for Selenium Grid to be ready ==="
        ATTEMPTS=0
        until curl -s http://localhost:4444/status | grep -q '"ready":true'; do
            ATTEMPTS=$((ATTEMPTS+1))
            if [ $ATTEMPTS -gt 15 ]; then
                echo "Selenium Grid not ready after 30 seconds, exiting."
                docker ps
                exit 1
            fi
            echo "Waiting for Selenium Grid... attempt $ATTEMPTS"
            sleep 2
        done

        echo "=== Running tests using full interpreter path ==="
        /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m pytest -v tests/
        '''
    }
}

