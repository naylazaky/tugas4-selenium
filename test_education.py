import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://ultimateqa.com/automation/"

DATA = [
    ("Free Courses", "courses.ultimateqa.com/collections", "All Products"),
    ("Selenium Java", "selenium-java-bootcamp", "Java Bootcamp"),
    ("Video courses", "udemy.com", "Udemy"),
    ("Selenium C#", "selenium-with-c", "Selenium Webdriver with C#"),
    ("Selenium Resources", "best-selenium-webdriver-resources", "Resources to Learn Selenium"),
    ("Automation Exercises", "ultimateqa.com/automation", "Automation Practice"),
]


@pytest.mark.parametrize(
    "nama_menu, url_part, title_part",
    DATA,
    ids=[d[0] for d in DATA],
)
def test_education_dropdown_item(driver, nama_menu, url_part, title_part):
    wait = WebDriverWait(driver, 10)
    driver.get(URL)

    # buka dropdown dengan hover
    menu = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Education")))
    ActionChains(driver).move_to_element(menu).perform()

    # klik item setelah dropdown terlihat
    wait.until(EC.element_to_be_clickable((By.LINK_TEXT, nama_menu))).click()

    wait.until(EC.url_contains(url_part))
    assert url_part in driver.current_url
    assert title_part in driver.title