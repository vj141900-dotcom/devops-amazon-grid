import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox", "safari"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        drv = webdriver.Remote(
            command_executor="http://selenium-hub:4444/wd/hub",
            options=options
        )

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        drv = webdriver.Remote(
            command_executor="http://selenium-hub:4444/wd/hub",
            options=options
        )

    elif browser == "safari":
        drv = webdriver.Safari()

    else:
        raise ValueError("Unsupported browser")

    yield drv
    drv.quit()

