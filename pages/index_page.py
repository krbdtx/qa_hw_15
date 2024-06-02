from selene import browser, have


class IndexPage:

    def open_browser(self):
        browser.open("https://github.com")
        return self

    def desktop_btn_sign_in(self):
        browser.element(".HeaderMenu-link--sign-in").click()

    def mobile_btn_sign_in(self):
        browser.element(".Button--link").click()
        browser.element(".HeaderMenu-link--sign-in").click()

    def should_have_text(self):
        browser.element(".auth-form-header").element("h1").should(have.text("Sign in to GitHub"))


indexpage = IndexPage()
