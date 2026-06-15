from logging import getLogger

import pytest

from test_data.booking_schemas import Schema

LOGGER = getLogger(__name__)


@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getini("base_url")


@pytest.fixture(scope="session")
def schemas():
    return {
        "auth": Schema.AUTH,
        "booking": Schema.BOOKING,
        "create_booking_response": Schema.CREATE_BOOKING_RESPONSE
    }


@pytest.fixture()
def headers(auth_token):
    return {"Cookie": f"token={auth_token}", "Accept": "application/json"}
