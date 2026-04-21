import requests

BASE_URL = "http://127.0.0.1:8000"


def test_home():
    r = requests.get(BASE_URL)
    assert r.status_code == 200


def test_steps():
    r = requests.get(f"{BASE_URL}/steps")
    assert r.status_code == 200


def test_simulation():
    r = requests.post(f"{BASE_URL}/simulate?customer=ABC&material=MAT1&qty=10")
    assert r.status_code == 200
