import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browsers",
        action="store",
        default="chrome,firefox,safari",
        help="Comma-separated list of browsers to test (chrome,firefox,safari)"
    )

@pytest.fixture
def browsers(request):
    browsers = request.config.getoption("--browsers")
    return browsers.split(",")

@pytest.fixture(params=["chrome", "firefox", "safari"])
def driver(request):
    browser = request.param

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=options
        )

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        driver = webdriver.Remote(
            command_executor="http://localhost:4445/wd/hub",
            options=options
        )

    elif browser == "safari":
        driver = webdriver.Safari()

    else:
        raise ValueError("Unsupported browser!")

    yield driver
    driver.quit()

