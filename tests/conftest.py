import pytest
from selene import browser

@pytest.fixture
def desktop_web():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()

@pytest.fixture
def mobile_web():
    browser.config.window_width = 480
    browser.config.window_height = 800

    yield

    browser.quit()


@pytest.fixture(params=[("desktop", 1920, 1080), ("desktop", 1400, 1050), ("mobile", 480, 800), ("mobile", 540, 960)])
def browser_setup(request):
    browser.config.window_width = request.param[1]
    browser.config.window_height = request.param[2]

    yield request.param[0]


mobile = pytest.mark.parametrize("browser_setup", [("mobile", 480, 800), ("mobile", 540, 960)], indirect=True)
desktop = pytest.mark.parametrize("browser_setup", [("desktop", 1920, 1080), ("desktop", 1400, 1050)], indirect=True)
