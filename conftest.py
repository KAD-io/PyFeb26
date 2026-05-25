import logging
import pytest
from playwright.sync_api import sync_playwright


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s.%(funcName)s: %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def pytest_addoption(parser):
    parser.addoption(
        "--log-lvl",
        action="store",
        default="INFO",
        help="Logging level for tests: DEBUG, INFO, WARNING, ERROR, CRITICAL",
    )


def pytest_configure(config):
    log_level_str = config.getoption("--log-lvl").upper()
    numeric_level = getattr(logging, log_level_str, logging.INFO)

    logging.getLogger().setLevel(numeric_level)

    config.option.log_cli_level = log_level_str
    config.option.log_cli_format = LOG_FORMAT
    config.option.log_cli_date_format = DATE_FORMAT

    config.option.log_format = LOG_FORMAT
    config.option.log_date_format = DATE_FORMAT


@pytest.fixture
def page():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()  # pylint: disable=redefined-outer-name
        page.goto("https://www.saucedemo.com/")
        yield page
        browser.close()
