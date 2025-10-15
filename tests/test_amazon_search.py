import time
from selenium.webdriver.common.by import By

def test_amazon_search(driver):
    driver.get("https://www.amazon.in")
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.clear()
    search_box.send_keys("wireless headphones")
    search_box.submit()

    # give page a few seconds to load results
    time.sleep(5)

    # confirm the search box still contains the same text (meaning search worked)
    value = driver.find_element(By.ID, "twotabsearchtextbox").get_attribute("value")
    assert "headphone" in value.lower()

