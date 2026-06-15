class Payload:
    USER = {"username": "admin", "password": "password123"}
    PUT_PAYLOAD = {
        "firstname": "Ivan",
        "lastname": "Ivanov",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-06-10", "checkout": "2026-06-15"},
        "additionalneeds": "Breakfast"
    }
    POST_PAYLOAD = {
        "firstname": "Petr",
        "lastname": "Petrov",
        "totalprice": 300,
        "depositpaid": False,
        "bookingdates": {"checkin": "2026-08-01", "checkout": "2026-08-10"},
        "additionalneeds": "Dinner"
    }
    PATCH_PAYLOAD = {"firstname": "Alex", "totalprice": 500}
