#!/bin/bash

# Test script for OctoFit Tracker API endpoints
# Tests both localhost and codespace URLs

echo "======================================"
echo "OctoFit Tracker API Endpoint Tests"
echo "======================================"
echo ""

# Set the codespace URL
if [ -n "$CODESPACE_NAME" ]; then
    CODESPACE_URL="https://${CODESPACE_NAME}-8000.app.github.dev"
    echo "Codespace URL: $CODESPACE_URL"
else
    CODESPACE_URL=""
    echo "Not running in GitHub Codespaces"
fi

LOCALHOST_URL="http://localhost:8000"
echo "Localhost URL: $LOCALHOST_URL"
echo ""

# Function to test an endpoint
test_endpoint() {
    local url=$1
    local endpoint=$2
    local description=$3
    
    echo "Testing: $description"
    echo "URL: ${url}${endpoint}"
    
    response=$(curl -s -w "\nHTTP_STATUS:%{http_code}" -X GET "${url}${endpoint}" -H "Accept: application/json")
    http_status=$(echo "$response" | grep "HTTP_STATUS" | cut -d':' -f2)
    body=$(echo "$response" | sed '/HTTP_STATUS/d')
    
    if [ "$http_status" = "200" ]; then
        echo "✓ Status: 200 OK"
        echo "Response preview: $(echo "$body" | head -c 150)..."
    else
        echo "✗ Status: $http_status"
        echo "Response: $body"
    fi
    echo ""
}

echo "======================================"
echo "Testing Localhost Endpoints"
echo "======================================"
echo ""

test_endpoint "$LOCALHOST_URL" "/api/users/" "Users API"
test_endpoint "$LOCALHOST_URL" "/api/teams/" "Teams API"
test_endpoint "$LOCALHOST_URL" "/api/activities/" "Activities API"
test_endpoint "$LOCALHOST_URL" "/api/leaderboard/" "Leaderboard API"
test_endpoint "$LOCALHOST_URL" "/api/workouts/" "Workouts API"

if [ -n "$CODESPACE_URL" ]; then
    echo "======================================"
    echo "Testing Codespace Endpoints"
    echo "======================================"
    echo ""
    
    test_endpoint "$CODESPACE_URL" "/api/users/" "Users API (Codespace)"
    test_endpoint "$CODESPACE_URL" "/api/teams/" "Teams API (Codespace)"
    test_endpoint "$CODESPACE_URL" "/api/activities/" "Activities API (Codespace)"
    test_endpoint "$CODESPACE_URL" "/api/leaderboard/" "Leaderboard API (Codespace)"
    test_endpoint "$CODESPACE_URL" "/api/workouts/" "Workouts API (Codespace)"
fi

echo "======================================"
echo "Test Complete"
echo "======================================"
