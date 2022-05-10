import logging
import random

from playwright.sync_api import sync_playwright


def open_browser() -> None:
    playwright = sync_playwright().start()
    browaer = playwright.webkit.launch(headless=False)
    page = browaer.new_page()

    page.goto('http://www.cdfgsanya.com/index.html')
    page.wait_for_timeout(random.randint(200, 500))
    logging.debug('page title: %s' % page.title())


def search():


open_browser()
