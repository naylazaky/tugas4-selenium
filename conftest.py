import os
import time
import pytest
from selenium import webdriver

GRID_URL = os.getenv("GRID_URL")  # kosong = jalan lokal
HEADLESS = os.getenv("HEADLESS") == "1"


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")

    if HEADLESS:
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    if GRID_URL:
        drv = webdriver.Remote(command_executor=GRID_URL, options=options)
    else:
        drv = webdriver.Chrome(options=options)
        if not HEADLESS:
            drv.maximize_window()

    yield drv

    if not HEADLESS:
        time.sleep(2)   # jeda untuk video, dilewati di CI
    drv.quit()