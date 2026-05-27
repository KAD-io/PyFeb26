import pytest
from playwright.sync_api import Page

from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage
from pages.navbar_page import Navbar


@pytest.fixture
def page(page: Page) -> Page:
    timeout = 10000
    page.set_default_navigation_timeout(timeout)
    page.set_default_timeout(timeout)
    page.goto('https://www.saucedemo.com/')
    return page


@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def navbar(page) -> Navbar:
    return Navbar(page)


@pytest.fixture
def inventory_page(page) -> InventoryPage:
    return InventoryPage(page)


@pytest.fixture
def checkout_page(page) -> CheckoutPage:
    return CheckoutPage(page)
