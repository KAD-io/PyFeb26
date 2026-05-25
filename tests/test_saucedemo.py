import pytest
from logging import getLogger
from playwright.sync_api import expect


LOGGER = getLogger(__name__)


@pytest.fixture
def stub_user():
    return {
        "user": "standard_user",
        "password": "secret_sauce"
    }


@pytest.fixture
def stub_user_data():
    return {
        "first_name": "first_name",
        "last_name": "last_name",
        "postal_code": "postal_code"
    }


@pytest.fixture
def login_user(page, stub_user):
    page.locator("#user-name").fill(stub_user["user"])
    LOGGER.info("Entering username")
    page.locator("#password").fill(stub_user["password"])
    LOGGER.info("Entering password")
    page.locator("#login-button").click()
    LOGGER.info("Click 'Login'")
    yield page
    page.locator("#react-burger-menu-btn").click()
    LOGGER.info("Click 'Burger menu'")
    page.locator("#logout_sidebar_link").click()
    LOGGER.info("Click 'Logout'")


@pytest.fixture
def add_item_to_cart(login_user):
    page = login_user
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    LOGGER.info("Click 'Add to cart': Sauce Labs Backpack")
    page.locator("#shopping_cart_container").click()
    LOGGER.info("Click 'Shopping cart'")
    return page


def test_login(page, stub_user):
    LOGGER.info("Running test: login user")
    page.locator("#user-name").fill(stub_user["user"])
    LOGGER.info("Entering username")
    page.locator("#password").fill(stub_user["password"])
    LOGGER.info("Entering password")
    page.locator("#login-button").click()
    LOGGER.info("Click 'Login'")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    LOGGER.info("Completing test: login user")


def test_add_to_cart(login_user):
    LOGGER.info("Running test: add to cart")
    page = login_user
    page.locator("#add-to-cart-sauce-labs-backpack").click()
    LOGGER.info("Click 'Add to cart': Sauce Labs Backpack")
    expect(page.locator("#remove-sauce-labs-backpack")).to_be_visible()
    expect(page.locator("[data-test='shopping-cart-badge']")).to_be_visible()
    LOGGER.info("Completing test: add to cart")


def test_checkout_complete(add_item_to_cart, stub_user_data):
    LOGGER.info("Running test: checkout complete")
    page = add_item_to_cart
    page.locator("#checkout").click()
    LOGGER.info("Click 'Checkout'")
    page.locator("#first-name").fill(stub_user_data["first_name"])
    LOGGER.info("Entering first name")
    page.locator("#last-name").fill(stub_user_data["last_name"])
    LOGGER.info("Entering last name")
    page.locator("#postal-code").fill(stub_user_data["postal_code"])
    LOGGER.info("Entering ZIP/Postal Code")
    page.locator("#continue").click()
    LOGGER.info("Click 'Continue'")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-two.html")
    page.locator("#finish").click()
    LOGGER.info("Click 'Finish'")
    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    page.locator("#back-to-products").click()
    LOGGER.info("Click 'Back Home'")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    LOGGER.info("Completing test: checkout complete")
