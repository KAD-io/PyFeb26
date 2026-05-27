from logging import getLogger

from playwright.sync_api import Page

from pages.base_page import BasePage

LOGGER = getLogger(__name__)


class Navbar(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.shopping_cart_button = page.locator("#shopping_cart_container")
        self.shopping_cart_badge = page.locator("[data-test='shopping-cart-badge']")
        self.burger_menu = page.locator("#react-burger-menu-btn")
        self.logout_sidebar = page.locator("#logout_sidebar_link")
        super().__init__(page)

    def logout(self):
        LOGGER.info("Click 'Burger menu'")
        self.burger_menu.click()
        LOGGER.info("Click 'Logout'")
        self.logout_sidebar.click()

    def go_to_cart(self):
        LOGGER.info("Click 'Shopping cart'")
        self.shopping_cart_button.click()
