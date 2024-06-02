from pages.index_page import indexpage


def test_desktop_page(desktop_web):
    indexpage.open_browser()
    indexpage.desktop_btn_sign_in()
    indexpage.should_have_text()


def test_mobile_page(mobile_web):
    indexpage.open_browser()
    indexpage.mobile_btn_sign_in()
    indexpage.should_have_text()

