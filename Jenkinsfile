stage('Run Tests') {
    steps {
        sh '''
        echo "=== Waiting for Selenium Hub to be ready ==="
        ATTEMPTS=0
        until curl -s http://localhost:4444/status | grep -q '"ready":true'; do
            ATTEMPTS=$((ATTEMPTS+1))
            echo "Hub not ready... attempt $ATTEMPTS"
            sleep 2
        done

        echo "=== Waiting for Chrome & Firefox nodes to register ==="
        ATTEMPTS=0
        until [ "$(curl -s http://localhost:4444/se/grid/status | grep -c '"id"')" -ge 2 ]; do
            ATTEMPTS=$((ATTEMPTS+1))
            echo "Nodes not yet registered... attempt $ATTEMPTS"
            sleep 3
        done

        echo "=== Hub and Nodes are ready! Running pytest now ==="
        docker ps

        /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m pytest -v tests/
        '''
    }
}

