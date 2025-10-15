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

        echo "=== Waiting for Chrome & Firefox nodes to register ==="
        ATTEMPTS=0
        while true; do
            NODE_COUNT=$(curl -s http://localhost:4444/status | grep -o '"uri"' | wc -l)
            if [ "$NODE_COUNT" -ge 2 ]; then
                echo "✅ Chrome and Firefox nodes registered!"
                break
            fi
            ATTEMPTS=$((ATTEMPTS+1))
            echo "Nodes not ready yet... attempt $ATTEMPTS"
            sleep 5
            if [ $ATTEMPTS -gt 20 ]; then
                echo "❌ Timeout: Nodes did not register."
                docker ps
                exit 1
            fi
        done

        echo "=== Verifying Grid Session Creation (simple test) ==="
        for browser in chrome firefox; do
            echo "Checking $browser session..."
            curl -s -X POST http://localhost:4444/wd/hub/session \
                -H "Content-Type: application/json" \
                -d '{"capabilities": {"alwaysMatch": {"browserName": "'$browser'"}}}' | grep -q "sessionId"
            if [ $? -eq 0 ]; then
                echo "✅ $browser session successfully created"
            else
                echo "⚠️ $browser not ready yet, retrying..."
                sleep 5
            fi
        done

        echo "=== Giving final 10s for browser stabilization ==="
        sleep 10

        echo "=== Running pytest ==="
        /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m pytest -v tests/
        '''
    }
}

