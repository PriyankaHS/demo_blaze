from selenium import webdriver
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import (visibility_of_element_located,
                                                            invisibility_of_element,
                                                            presence_of_all_elements_located,
                                                            element_to_be_clickable, alert_is_present)
from selenium.webdriver.support.wait import WebDriverWait


class SeleniumWrapper:
    def __init__(self, driver: webdriver, time_out=30):
        self.driver: webdriver = driver
        self.time_out = time_out
        self.action_chains = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, self.time_out)

    def goto_url(self, url):
        self.driver.get(url)

    def click_element(self, locator: str, by_type=By.XPATH):
        self.get_element(locator, by_type).click()

    def get_element(self, locator: str, by_type=By.XPATH) -> WebElement:
        return self.driver.find_element(by_type, locator)

    def get_elements(self, locator: str, by_type=By.XPATH) -> list:
        return self.driver.find_elements(by_type, locator)

    def get_elements_text(self, locator: str, by_type=By.XPATH) -> list:
        elements = self.driver.find_elements(by_type, locator)
        return [element.text for element in elements]

    def send_keys(self, locator: str, by_type=By.XPATH, value=""):
        self.get_element(locator, by_type).send_keys(value)

    def scroll_to_element(self, locator: str, by_type=By.XPATH):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});",
                                   self.get_element(locator, by_type))

    def js_click_element(self, locator: str, by_type=By.XPATH):
        self.driver.execute_script("arguments[0].click()", self.get_element(locator, by_type))

    def element_visible(self, locator: str, by_type=By.XPATH) -> bool:
        try:
            self.wait.until(visibility_of_element_located((by_type, locator)))
            return True
        except (TimeoutException, NoSuchElementException):
            return False

    def element_invisible(self, locator: str, by_type=By.XPATH) -> bool:
        try:
            self.wait.until(invisibility_of_element(
                self.get_element(locator, by_type)))
            return True
        except TimeoutException:
            return False

    def wait_till_element_invisible(self, locator: str, by_type=By.XPATH):
        self.wait.until(invisibility_of_element((by_type, locator)))

    def element_present(self, locator: str, by_type=By.XPATH) -> bool:
        try:
            self.wait.until(presence_of_all_elements_located((by_type, locator)))
            return True
        except TimeoutException:
            return False

    def wait_till_element_present(self, locator: str, by_type=By.XPATH):
        self.wait.until(presence_of_all_elements_located((by_type, locator)))

    def move_to_element(self, locator: str, by_type=By.XPATH):
        self.action_chains.move_to_element(self.get_element(locator, by_type)).perform()

    def move_to_offset(self, x_offset=5, y_offset=5):
        self.action_chains.move_by_offset(x_offset, y_offset).perform()

    def get_text(self, locator: str, by_type=By.XPATH) -> str:
        return self.get_element(locator, by_type).text

    def element_clickable(self, locator: str, by_type=By.XPATH) -> bool:
        try:
            self.wait.until(element_to_be_clickable((by_type, locator)))
            return True
        except TimeoutException:
            return False

    def wait_till_element_clickable(self, locator: str, by_type=By.XPATH):
        self.wait.until(element_to_be_clickable((by_type, locator)))

    def get_title(self) -> str:
        return self.driver.title

    def open_new_window(self, index=0):
        self.driver.execute_script("window.open()")
        if not index == 0:
            self.driver.switch_to.window(self.driver.window_handles[index])

    def click_visible_element(self, locator: str, by_type=By.XPATH):
        flag = self.element_visible(locator, by_type)
        if flag:
            self.js_click_element(locator, by_type)
        else:
            raise TimeoutException

    def is_page_loaded(self):
        loaded_flag = self.driver.execute_script("return document.readyState;")
        if loaded_flag == "complete":
            print("Page loaded successfully")
            return True
        else:
            print("Page not loaded")
            return False

    def wait_till_element_visible(self, locator: str, by_type=By.XPATH):
        self.wait.until(visibility_of_element_located((by_type, locator)))
        self.scroll_to_element(locator,by_type)

    def wait_till_alert_present(self):
        self.wait.until(alert_is_present())
