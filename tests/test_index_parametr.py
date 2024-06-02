from pages.index_page import indexpage
from tests.conftest import desktop, mobile


@desktop
def test_github_desktop(browser_setup):
    indexpage.open_browser()
    indexpage.desktop_btn_sign_in()
    indexpage.should_have_text()


@mobile
def test_github_mobile(browser_setup):
    indexpage.open_browser()
    indexpage.mobile_btn_sign_in()
    indexpage.should_have_text()
