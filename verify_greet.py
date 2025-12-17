import requests
import time
import sys

def verify_greet():
    base_url = "http://127.0.0.1:5002"
    
    # Test 1: Index Page
    print(f"Testing Index {base_url}/...")
    try:
        resp = requests.get(f"{base_url}/")
        print(f"Index Status: {resp.status_code}")
        if resp.status_code != 200:
            print("FAILURE: Index page not reachable")
            return False
    except Exception as e:
        print(f"FAILURE: Could not reach index: {e}")
        return False

    # Test 2: API
    url = f"{base_url}/api/greet"
    payload = {"message": "hi"}
    
    print(f"Testing API {url} with payload {payload}...")
    
    try:
        response = requests.post(url, json=payload, timeout=30)
        print(f"Status Code: {response.status_code}")
        print(f"Response JSON: {response.json()}")
        
        if response.status_code == 200 and 'reply' in response.json():
            print("SUCCESS: Received valid reply.")
            return True
        else:
            print("FAILURE: Invalid response.")
            return False
            
    except requests.exceptions.ConnectionError:
        print("FAILURE: Could not connect to server. Is it running?")
        return False
    except Exception as e:
        print(f"FAILURE: Unexpected error: {e}")
        return False

if __name__ == "__main__":
    time.sleep(2)
    success = verify_greet()
    sys.exit(0 if success else 1)
