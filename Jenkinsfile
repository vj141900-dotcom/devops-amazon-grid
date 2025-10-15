stage('Run Tests') {
    steps {
        sh '''
        echo "=== Waiting for Selenium Hub to be ready ==="
        ATTEMPTS=0
        until curl -s http://localhost:4444/status | grep -q '"ready":true'; do
            ATTEMPTS=$((ATTEMPTS+1))
            echo "Waiting for Hub... attempt $ATTEMPTS"
            sleep 2
        done

        echo "=== Checking Chrome & Firefox Node registration ==="
        ATTEMPTS=0
        while true; do
            NODE_COUNT=$(curl -s http://localhost:4444/status | grep -o '"uri"' | wc -l)
            if [ "$NODE_COUNT" -ge 2 ]; then
                echo "✅ Chrome and Firefox nodes registered!"
                break
            fi
            ATTEMPTS=$((ATTEMPTS+1))
            echo "Waiting for nodes... attempt $ATTEMPTS"
            sleep 3
            if [ $ATTEMPTS -gt 20 ]; then
                echo "❌ Nodes did not register in time."
                docker ps
                exit 1
            fi
        done

        echo "=== Running pytest ==="
        /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m pytest -v tests/
        '''
    }
}

