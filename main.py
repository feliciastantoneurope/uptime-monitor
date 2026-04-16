import requests
import time

TARGET_URL = "https://google.com"

def check_status():
    try:
        response = requests.get(TARGET_URL, timeout=5)
        if response.status_code == 200:
            print(f"✅ SUCCESS: {TARGET_URL} is live!")
        else:
            print(f"⚠️ WARNING: {TARGET_URL} returned {response.status_code}")
    except Exception as e:
        print(f"❌ ERROR: Could not reach {TARGET_URL}. Details: {e}")

if __name__ == "__main__":
    print("--- Starting Uptime Monitor ---")
    while True:
        check_status()
        time.sleep(60)