import os
import requests

BASE_URL = os.getenv("BASE_URL", "http://localhost:8080")

def main():
    # 1) purchase
    purchase = {
        "event_type": "purchase",
        "user_id": "20031",
        "currency": "AED",
        "amount": 120
    }
    r1 = requests.post(f"{BASE_URL}/collect", json=purchase, timeout=5)
    print("purchase ->", r1.status_code, r1.json())

    # 2) install
    install = {
        "event_type": "install",
        "device_id": "device 2",
        "user_id": "20031",
        "app_version": "1.1",
        "ts": "2025-xx-xx@xx:xx:xx"
    }
    r2 = requests.post(f"{BASE_URL}/collect", json=install, timeout=5)
    print("install  ->", r2.status_code, r2.json())

    print("\nCheck ./output/stream_debug.json")

if __name__ == "__main__":
    main()