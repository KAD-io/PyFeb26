from logging import getLogger

from playwright.sync_api import Page

from pages.base_page import BasePage

LOGGER = getLogger(__name__)


class InventoryPage(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.to_cart_backpack_button = page.locator("#add-to-cart-sauce-labs-backpack")
        self.remove_backpack_button = page.locator("#remove-sauce-labs-backpack")
        super().__init__(page)

    def add_item_to_cart(self):
        LOGGER.info("Click 'Add to cart': Sauce Labs Backpack")
        self.to_cart_backpack_button.click()
