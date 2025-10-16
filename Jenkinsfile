stage('Test') {
    steps {
        sh '''
        echo "Waiting for Selenium Grid nodes to register..."
        for i in {1..15}; do
            READY=$(curl -s http://localhost:4444/status | grep -c '"ready":true')
            if [ "$READY" -gt 0 ]; then
                echo "✅ Selenium Grid is ready!"
                break
            fi
            echo "⏳ Waiting for Grid to be ready... ($i/15)"
            sleep 5
        done

        echo "🔍 Running tests now..."
        pytest -v --maxfail=1 --disable-warnings
        '''
    }
}

