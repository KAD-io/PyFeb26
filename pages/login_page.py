from logging import getLogger

from playwright.sync_api import Page

from pages.base_page import BasePage

LOGGER = getLogger(__name__)


class LoginPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        super().__init__(page)

    def login_user(self, username: str, password: str):
        self.username_input.type(username)
        LOGGER.info("Entering password")
        self.password_input.type(password)
        LOGGER.info("Click 'Login'")
        self.login_button.click()
