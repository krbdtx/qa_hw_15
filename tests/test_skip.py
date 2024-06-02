import pytest
from selene import browser
from pages.index_page import indexpage


def test_for_desktop(browser_setup):
    if browser.config.window_width < 1000:
        pytest.skip('for mobile browsers')
    indexpage.open_browser()
    indexpage.desktop_btn_sign_in()
    indexpage.should_have_text()


def test_for_mobile(browser_setup):
    if browser.config.window_width > 1000:
        pytest.skip('for desktop browsers')
    indexpage.open_browser()
    indexpage.mobile_btn_sign_in()
    indexpage.should_have_text()
