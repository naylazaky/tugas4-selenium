from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_newsletter_page_opens(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://ultimateqa.com/automation/")

    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Newsletter"))).click()

    wait.until(EC.url_contains("ultimateqa.kit.com"))
    assert "ultimateqa.kit.com" in driver.current_url