stage('Run Tests') {
    steps {
        sh '''
        echo "=== Waiting for Selenium Hub to be ready ==="
        ATTEMPTS=0
        until curl -s http://localhost:4444/status | grep -q '"ready":true'; do
            ATTEMPTS=$((ATTEMPTS+1))
            echo "Waiting for Hub... attempt $ATTEMPTS"
            sleep 3
        done

        echo "=== Waiting for Chrome & Firefox node registration ==="
        ATTEMPTS=0
        while true; do
            NODE_COUNT=$(curl -s http://localhost:4444/status | grep -o '"uri"' | wc -l)
            if [ "$NODE_COUNT" -ge 2 ]; then
                echo "✅ Chrome and Firefox nodes registered successfully!"
                break
            fi
            ATTEMPTS=$((ATTEMPTS+1))
            echo "Nodes not ready yet... attempt $ATTEMPTS"
            sleep 5
            if [ $ATTEMPTS -gt 30 ]; then
                echo "❌ Timeout: Nodes did not register."
                docker ps
                exit 1
            fi
        done

        echo "=== Giving extra 15s for full browser startup ==="
        sleep 15

        echo "=== Running pytest ==="
        /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m pytest -v tests/
        '''
    }
}

