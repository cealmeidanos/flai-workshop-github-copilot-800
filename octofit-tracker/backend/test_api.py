#!/usr/bin/env python
import requests
import json

base_url = 'http://localhost:8000'

print("=" * 60)
print("OCTOFIT TRACKER API TEST")
print("=" * 60)

# Test API root
print("\n1. Testing API Root (/):")
try:
    r = requests.get(f'{base_url}/')
    print(f"   Status: {r.status_code}")
    if r.status_code == 200:
        print(f"   Response: {json.dumps(r.json(), indent=2)[:200]}...")
except Exception as e:
    print(f"   Error: {e}")

# Test Users endpoint
print("\n2. Testing Users API (/api/users/):")
try:
    r = requests.get(f'{base_url}/api/users/')
    print(f"   Status: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        print(f"   Total users: {len(data)}")
        if data:
            print(f"   First user: {data[0]['name']} ({data[0]['email']})")
except Exception as e:
    print(f"   Error: {e}")

# Test Teams endpoint
print("\n3. Testing Teams API (/api/teams/):")
try:
    r = requests.get(f'{base_url}/api/teams/')
    print(f"   Status: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        print(f"   Total teams: {len(data)}")
        if data:
            print(f"   Teams: {', '.join([t['name'] for t in data])}")
except Exception as e:
    print(f"   Error: {e}")

# Test Activities endpoint
print("\n4. Testing Activities API (/api/activities/):")
try:
    r = requests.get(f'{base_url}/api/activities/')
    print(f"   Status: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        print(f"   Total activities: {len(data)}")
        if data:
            print(f"   Latest activity: {data[0]['user_name']} - {data[0]['activity_type']}")
except Exception as e:
    print(f"   Error: {e}")

# Test Leaderboard endpoint
print("\n5. Testing Leaderboard API (/api/leaderboard/):")
try:
    r = requests.get(f'{base_url}/api/leaderboard/')
    print(f"   Status: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        print(f"   Total entries: {len(data)}")
        if data:
            top3 = sorted(data, key=lambda x: x.get('rank', 999))[:3]
            for entry in top3:
                print(f"   Rank {entry['rank']}: {entry['user_name']} - {entry['total_calories']} calories")
except Exception as e:
    print(f"   Error: {e}")

# Test Workouts endpoint
print("\n6. Testing Workouts API (/api/workouts/):")
try:
    r = requests.get(f'{base_url}/api/workouts/')
    print(f"   Status: {r.status_code}")
    if r.status_code == 200:
        data = r.json()
        print(f"   Total workouts: {len(data)}")
        if data:
            print(f"   Sample workout: {data[0]['title']} ({data[0]['difficulty']})")
except Exception as e:
    print(f"   Error: {e}")

print("\n" + "=" * 60)
print("API TEST COMPLETE")
print("=" * 60)
