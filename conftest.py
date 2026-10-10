import os
import time
import pytest
from selenium import webdriver

GRID_URL = os.getenv("GRID_URL")  # kosong = jalan lokal


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")

    if GRID_URL:
        drv = webdriver.Remote(command_executor=GRID_URL, options=options)
    else:
        drv = webdriver.Chrome(options=options)
        drv.maximize_window()

    yield drv

    time.sleep(2)   # jeda supaya hasil terlihat di video
    drv.quit()