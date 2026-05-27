import time
from logging import getLogger
import pytest
from playwright.sync_api import expect
from test_data.users import UserData, UserLoginData

LOGGER = getLogger(__name__)


@pytest.fixture
def login_user(login_page, navbar):
    login_page.login_user(UserLoginData.USERNAME, UserLoginData.PASSWORD)
    yield
    navbar.logout()


@pytest.fixture
def add_to_cart(login_user, inventory_page, navbar):
    inventory_page.add_item_to_cart()
    navbar.go_to_cart()
    return


@pytest.mark.login
def test_login(login_page):
    LOGGER.info("Running test: login user")
    login_page.login_user(UserLoginData.USERNAME, UserLoginData.PASSWORD)
    expect(login_page.page).to_have_url("https://www.saucedemo.com/inventory.html")
    LOGGER.info("Completing test: login user")


@pytest.mark.adding_to_cart
def test_add_to_cart(login_user, inventory_page, navbar):
    LOGGER.info("Running test: add to cart")
    inventory_page.add_item_to_cart()
    navbar.go_to_cart()
    expect(inventory_page.remove_backpack_button).to_be_visible()
    expect(navbar.shopping_cart_badge).to_be_visible()
    LOGGER.info("Completing test: add to cart")


@pytest.mark.checkout
def test_checkout_complete(add_to_cart, checkout_page):
    LOGGER.info("Running test: checkout complete")

    checkout_page.go_to_checkout()
    checkout_page.step_one(UserData.FIRSTNAME, UserData.LASTNAME, UserData.ZIP)
    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    checkout_page.step_two()
    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    checkout_page.complete()
    expect(checkout_page.page).to_have_url("https://www.saucedemo.com/inventory.html")

    LOGGER.info("Completing test: checkout complete")
