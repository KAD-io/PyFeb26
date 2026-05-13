from logging import getLogger
import pytest
from source.bank_deposit import Bank


logger = getLogger(__name__)


@pytest.fixture
def bank():
    return Bank()


@pytest.fixture
def client_id():
    return "0000001"


@pytest.fixture
def client_name():
    return "John Smith"


@pytest.fixture
def non_existent_id():
    return "non_existent_id"


def test_register_client_success(bank, client_id, client_name):
    """Positive test: client registration"""
    logger.info("Running test: client registration")
    bank.register_client(client_id, client_name)
    assert client_id in bank.clients
    assert bank.clients[client_id]["name"] == client_name
    logger.info("Completing test: client registration")


def test_open_deposit_success(bank, client_id, client_name):
    """Positive test: opening deposit"""
    logger.info("Running test: opening deposit")
    bank.register_client(client_id, client_name)
    bank.open_deposit_account(client_id, 1000, 1)
    assert len(bank.clients[client_id]["deposits"]) == 1
    assert bank.clients[client_id]["deposits"][0]["start_balance"] == 1000
    logger.info("Completing test: opening deposit")


def test_calc_interest_rate_correctness(bank, client_id, client_name):
    """Positive test: rate calculation"""
    logger.info("Running test: rate calculation")
    bank.register_client(client_id, client_name)
    bank.open_deposit_account(client_id, 1000, 1, rate=0.1)
    expected_result = 1104.71
    result = bank.calc_interest_rate(client_id)
    assert result == expected_result
    logger.info("Completing test: rate calculation")


def test_close_deposit_success(bank, client_id, client_name):
    """Positive test: closing deposits"""
    logger.info("Running test: closing deposits")
    bank.register_client(client_id, client_name)
    bank.open_deposit_account(client_id, 1000, 1)
    assert bank.close_deposit(client_id) is True
    assert len(bank.clients[client_id]["deposits"]) == 0
    logger.info("Completing test: closing deposits")


def test_open_deposit_unregistered_client(bank, non_existent_id):
    """Negative tests: open deposit for non-existent ID should return False"""
    logger.info("Running test: open deposit unregistered client")
    assert bank.open_deposit_account(non_existent_id, 1000, 1) is False
    logger.info("Completing test: open deposit unregistered client")


def test_calc_interest_unregistered_client(bank, non_existent_id):
    """Negative tests: Interest calculation for non-existent customer should return None"""
    logger.info("Running test: calc interest unregistered client")
    assert bank.calc_interest_rate(non_existent_id) is None
    logger.info("Completing test: calc interest unregistered client")


def test_close_deposit_unregistered_client(bank, non_existent_id):
    """Negative tests: Closing the deposit of non-existent client should return False"""
    logger.info("Running test: close deposit unregistered client")
    assert bank.close_deposit(non_existent_id) is False
    logger.info("Completing test: close deposit unregistered client")
