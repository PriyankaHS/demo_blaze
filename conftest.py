import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def driver_instance():
    driver = webdriver.Chrome()
    driver.delete_all_cookies()
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()
