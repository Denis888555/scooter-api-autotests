import requests
import datetime as dt
from config import BASE_URL


def test_create_order_and_get_by_track():
    payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": (dt.date.today() + dt.timedelta(days=1)).isoformat(),
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }

    create_response = requests.post(
        f"{BASE_URL}/api/v1/orders",
        json=payload
    )

    track = create_response.json()["track"]

    get_response = requests.get(
        f"{BASE_URL}/api/v1/orders/track",
        params={"t": track}
    )

    assert get_response.status_code == 200
