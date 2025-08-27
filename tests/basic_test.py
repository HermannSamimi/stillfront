from fastapi.testclient import TestClient
from service.app import app
from kit.events import AppInstall, PurchaseTxn

c = TestClient(app)

def test_health():
    assert c.get("/status").status_code == 200

def test_install_flow():
    evt = AppInstall(device_id="d1", user_id="u1", app_version="1.01").to_dict()
    r = c.post("/collect", json=evt)
    assert r.status_code == 201
    assert r.json()["status"] == "ok"

def test_purchase_validation(): #timestamp removed
    bad = {
        "event_type":"purchase",
        "currency": "AED",
        "amount": 120,
        "user_id":"20031"
    }
    r = c.post("/collect", json=bad)
    assert r.status_code == 422


def test_purchase_ok():
    evt = {
        "event_type":"purchase",
        "user_id":"20031",
        "currency": "AED",
        "amount": 120
    }
    r = c.post("/collect", json=evt)
    assert r.status_code == 201