stage('Run Tests') {
    steps {
        sh '''
        echo "=== Checking Selenium Hub readiness ==="
        ATTEMPTS=0
        until curl -s http://localhost:4444/status | grep -q '"ready":true'; do
            ATTEMPTS=$((ATTEMPTS+1))
            echo "Waiting for Hub... attempt $ATTEMPTS"
            sleep 2
        done

        echo "=== Checking Chrome & Firefox nodes ==="
        ATTEMPTS=0
        while true; do
            NODE_COUNT=$(curl -s http://localhost:4444/status | grep -o '"uri"' | wc -l)
            if [ "$NODE_COUNT" -ge 2 ]; then
                echo "✅ Chrome and Firefox nodes registered successfully!"
                break
            fi
            ATTEMPTS=$((ATTEMPTS+1))
            echo "Waiting for nodes... attempt $ATTEMPTS"
            sleep 5
            if [ $ATTEMPTS -gt 15 ]; then
                echo "❌ Nodes not registered within timeout."
                docker ps
                exit 1
            fi
        done

        echo "=== All nodes ready. Running tests ==="
        /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m pytest -v tests/
        '''
    }
}

