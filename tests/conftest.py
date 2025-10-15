import os
import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome", "firefox", "safari"])
def driver(request):
    browser = request.param

    # ✅ Detect if we are inside Jenkins Docker or local host
    grid_host = "selenium-hub" if os.environ.get("JENKINS_URL") else "localhost"
    grid_url = f"http://{grid_host}:4444/wd/hub"

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        drv = webdriver.Remote(command_executor=grid_url, options=options)

    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        drv = webdriver.Remote(command_executor=grid_url, options=options)

    elif browser == "safari":
        drv = webdriver.Safari()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    yield drv
    drv.quit()

