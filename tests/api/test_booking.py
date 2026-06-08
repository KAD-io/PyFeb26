from logging import getLogger

import pytest
import requests
from jsonschema import validate

from test_data.user import Payload

LOGGER = getLogger(__name__)


@pytest.fixture(scope="module")
def auth_token(base_url, schemas):
    LOGGER.info("Create token")
    response = requests.post(f"{base_url}/auth", json=Payload.USER)
    return response.json()["token"]


@pytest.fixture()
def created_booking_id(base_url):
    LOGGER.info("Create booking")
    response = requests.post(f"{base_url}/booking", json=Payload.POST_PAYLOAD)
    assert response.status_code == 200
    booking_id = response.json()["bookingid"]
    yield booking_id
    LOGGER.info("Delete booking")
    requests.delete(
        f"{base_url}/booking/{booking_id}",
        headers={"Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="}
    )


@pytest.mark.positive_test
def test_auth_token(base_url, schemas):
    LOGGER.info("Running test: Create token")
    response = requests.post(f"{base_url}/auth", json=Payload.USER)
    assert response.status_code == 200
    data = response.json()
    validate(instance=data, schema=schemas["auth"])
    LOGGER.info("Completing test: Create token")


@pytest.mark.positive_test
def test_get_booking_ids(base_url):
    LOGGER.info("Running test: get booking")
    response = requests.get(f"{base_url}/booking")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    LOGGER.info("Completing test: get booking")


@pytest.mark.positive_test
def test_create_booking_success(base_url, schemas):
    LOGGER.info("Running test: create booking")
    response = requests.post(f"{base_url}/booking", json=Payload.POST_PAYLOAD)
    assert response.status_code == 200
    data = response.json()
    validate(instance=data, schema=schemas["create_booking_response"])
    LOGGER.info("Completing test: create booking")


@pytest.mark.positive_test
def test_update_booking_full_put(base_url, auth_token, created_booking_id, schemas, headers):
    LOGGER.info("Running test: update booking full")
    response = requests.put(f"{base_url}/booking/{created_booking_id}",
                            json=Payload.PUT_PAYLOAD,
                            headers=headers)
    assert response.status_code == 200
    data = response.json()
    validate(instance=data, schema=schemas["booking"])
    assert data == Payload.PUT_PAYLOAD
    LOGGER.info("Completing test: update booking full")


@pytest.mark.positive_test
def test_update_booking_partial_patch(base_url, auth_token, created_booking_id, schemas, headers):
    LOGGER.info("Running test: update booking partial")
    response = requests.patch(f"{base_url}/booking/{created_booking_id}",
                              json=Payload.PATCH_PAYLOAD,
                              headers=headers)
    assert response.status_code == 200
    data = response.json()
    validate(instance=data, schema=schemas["booking"])
    assert data["firstname"] == Payload.PATCH_PAYLOAD["firstname"]
    assert data["lastname"] == Payload.POST_PAYLOAD["lastname"]
    LOGGER.info("Completing test: update booking partial")


@pytest.mark.positive_test
def test_delete_booking_success(base_url, auth_token, created_booking_id, headers):
    LOGGER.info("Running test: delete booking")
    delete_response = requests.delete(f"{base_url}/booking/{created_booking_id}", headers=headers)
    assert delete_response.status_code == 201
    LOGGER.info("Completing test: delete booking")


@pytest.mark.negative_test
def test_update_booking_put_without_auth(base_url, created_booking_id):
    LOGGER.info("Running negative test: update booking without auth")
    response = requests.put(f"{base_url}/booking/{created_booking_id}", json=Payload.PUT_PAYLOAD)
    assert response.status_code == 403
    LOGGER.info("Completing negative test: update booking with invalid token")


@pytest.mark.negative_test
def test_update_booking_patch_invalid_token(base_url, created_booking_id):
    LOGGER.info("Running negative test: update booking with invalid token")
    headers = {"Cookie": "token=invalid_token_12345"}
    response = requests.patch(f"{base_url}/booking/{created_booking_id}",
                              json=Payload.PATCH_PAYLOAD,
                              headers=headers)
    assert response.status_code == 403
    LOGGER.info("Completing negative test: update booking with invalid token")


@pytest.mark.negative_test
def test_update_booking_put_missing_fields(base_url, auth_token, created_booking_id, headers):
    LOGGER.info("Running negative test: update booking with missing fields")
    incomplete_payload = {"firstname": "Semyon"}
    response = requests.put(f"{base_url}/booking/{created_booking_id}",
                            json=incomplete_payload,
                            headers=headers)
    assert response.status_code == 400
    LOGGER.info("Completing negative test: update booking with missing fields")
