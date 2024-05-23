import allure
import pendulum
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="session")
@allure.title("Prepare for the test")
def driver_instance():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.delete_all_cookies()
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    test_case_name = pendulum.now().format("YYYY-MM-DD HH:mm:ss")
    allure.attach(driver.get_screenshot_as_png(),
                  name="/screenshots/" + test_case_name + "_web",
                  attachment_type=AttachmentType.PNG)
    driver.quit()
