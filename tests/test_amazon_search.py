import time
from selenium.webdriver.common.by import By

def test_amazon_search(driver):
    driver.get("https://www.amazon.in")

    # Wait for page to load
    time.sleep(3)

    # Search for product
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("wireless headphones")
    search_box.submit()

    # Wait for results to load
    time.sleep(5)

    # Verify page loaded successfully
    assert "amazon" in driver.title.lower() or "headphones" in driver.page_source.lower()

