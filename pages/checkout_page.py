from logging import getLogger

from playwright.sync_api import Page

from pages.base_page import BasePage

LOGGER = getLogger(__name__)


class CheckoutPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator("#checkout")
        self.first_name_input = page.locator("#first-name")
        self.last_name_input = page.locator("#last-name")
        self.postal_code_input = page.locator("#postal-code")
        self.continue_button = page.locator("#continue")
        self.finish_button = page.locator("#finish")
        self.back_home_button = page.locator("#back-to-products")
        super().__init__(page)

    def go_to_checkout(self):
        LOGGER.info("Click 'Checkout'")
        self.checkout_button.click()

    def step_one(self, firstname: str, lastname: str, zipcode: str):
        LOGGER.info("Entering first name")
        self.first_name_input.type(firstname)
        LOGGER.info("Entering last name")
        self.last_name_input.type(lastname)
        LOGGER.info("Entering ZIP/Postal Code")
        self.postal_code_input.type(zipcode)
        LOGGER.info("Click 'Continue'")
        self.continue_button.click()

    def step_two(self):
        LOGGER.info("Click 'Finish'")
        self.finish_button.click()

    def complete(self):
        LOGGER.info("Click 'Back Home'")
        self.back_home_button.click()
