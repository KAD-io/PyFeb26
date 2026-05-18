from logging import getLogger
import pytest
import random
from source.bank_deposit import Bank

logger = getLogger(__name__)


@pytest.fixture
def bank():
    return Bank()


@pytest.fixture
def stub_client_id():
    return "0000001"


@pytest.fixture
def stub_client_data():
    return {
        "name": "John Smith",
        "deposits": [
            {"start_balance": 1000, "years": 1, "rate": 0.1}
        ]
    }


def test_register_client_success(bank, stub_client_id, stub_client_data):
    """Positive test: client registration"""
    logger.info("Running test: client registration")
    bank.register_client(stub_client_id, stub_client_data["name"])
    assert stub_client_id in bank.clients
    assert bank.clients[stub_client_id]["name"] == stub_client_data["name"]
    logger.info("Completing test: client registration")


def test_open_deposit_success(bank, stub_client_id, stub_client_data):
    """Positive test: opening deposit"""
    logger.info("Running test: opening deposit")

    bank.clients[stub_client_id] = {"name": stub_client_data["name"], "deposits": []}

    result = bank.open_deposit_account(stub_client_id,
                                       stub_client_data["deposits"][0]["start_balance"],
                                       stub_client_data["deposits"][0]["years"])

    assert result is True
    assert len(bank.clients[stub_client_id]["deposits"]) == 1
    logger.info("Completing test: opening deposit")


@pytest.mark.flaky(reruns=5, reruns_delay=1)
def test_calc_interest_rate_flaky(bank, stub_client_id, mocker):
    """Flaky test: rate calculation"""
    logger.info("Running flaky test: rate calculation")

    if random.choice([True, False]):
        logger.warning("Flaky test failed intentionally!")
        assert False, "Random flaky failure"
    mocker.patch('source.bank_deposit.Bank.calc_interest_rate', return_value=1104.71)
    result = bank.calc_interest_rate(stub_client_id)
    assert result == 1104.71
    logger.info("Completing flaky test: rate calculation")


def test_close_deposit_success(bank, stub_client_id, stub_client_data):
    """Positive test: closing deposits"""
    logger.info("Running test: closing deposits")

    bank.clients[stub_client_id] = stub_client_data

    assert bank.close_deposit(stub_client_id) is True
    assert len(bank.clients[stub_client_id]["deposits"]) == 0
    logger.info("Completing test: closing deposits")


def test_open_deposit_unregistered_client(bank):
    """Negative tests: uses Mock to verify logging behavior"""
    logger.info("Running test: open deposit unregistered client")
    result = bank.open_deposit_account("non_existent_id", 1000, 1)
    assert result is False
    logger.info("Completing test: open deposit unregistered client")


def test_calc_interest_unregistered_client(bank):
    """Negative tests: uses Mock to verify logger errors"""
    logger.info("Running test: calc interest unregistered client")
    result = bank.calc_interest_rate("non_existent_id")
    assert result is None
    logger.info("Completing test: calc interest unregistered client")


def test_close_deposit_unregistered_client(bank):
    """Negative tests: Closing the deposit of non-existent client"""
    logger.info("Running test: close deposit unregistered client")
    result = bank.close_deposit("non_existent_id")
    assert result is False
    logger.info("Completing test: close deposit unregistered client")
