stage('Run Tests') {
    steps {
        sh '''
        echo "=== Checking Selenium Hub status ==="
        ATTEMPTS=0
        until curl -s http://localhost:4444/status | grep -q '"ready":true'; do
            ATTEMPTS=$((ATTEMPTS+1))
            echo "Waiting for Selenium Hub... attempt $ATTEMPTS"
            sleep 3
        done
        echo "✅ Selenium Hub is ready!"

        echo "=== Checking Node registration ==="
        ATTEMPTS=0
        while true; do
            NODE_COUNT=$(curl -s http://localhost:4444/status | grep -o '"uri"' | wc -l)
            if [ "$NODE_COUNT" -ge 2 ]; then
                echo "✅ Chrome & Firefox nodes registered!"
                break
            fi
            ATTEMPTS=$((ATTEMPTS+1))
            echo "Waiting for nodes... attempt $ATTEMPTS"
            sleep 5
            if [ $ATTEMPTS -gt 20 ]; then
                echo "❌ Timeout waiting for node registration"
                exit 1
            fi
        done

        echo "=== Testing if nodes can create sessions ==="
        BROWSERS=("chrome" "firefox")
        for browser in "${BROWSERS[@]}"; do
            echo "Testing $browser session..."
            for i in {1..6}; do
                STATUS=$(curl -s -X POST http://localhost:4444/wd/hub/session \
                    -H "Content-Type: application/json" \
                    -d '{"capabilities": {"alwaysMatch": {"browserName": "'$browser'"}}}' | grep -c "sessionId")
                if [ "$STATUS" -gt 0 ]; then
                    echo "✅ $browser session is alive!"
                    break
                fi
                echo "Retrying $browser session... ($i)"
                sleep 5
                if [ "$i" -eq 6 ]; then
                    echo "❌ $browser not ready after 30s"
                    exit 1
                fi
            done
        done

        echo "=== Final wait before pytest ==="
        sleep 5

        echo "=== Running tests ==="
        /Library/Frameworks/Python.framework/Versions/3.13/bin/python3 -m pytest -v tests/
        '''
    }
}

