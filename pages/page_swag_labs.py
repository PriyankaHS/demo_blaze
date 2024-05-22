from selenium.webdriver.common.by import By

from utilities.selenium_wrapper import SeleniumWrapper


class SwagLabs:
    home_page = "https://www.demoblaze.com/"

    # locators
    username_field = "//input[@id='user-name']"
    password_field = "//input[@id='password']"
    login_button = "//input[@id='login-button']"
    error_message = "//h3[@data-test='error']"

    logout_button = "//a[@id='logout_sidebar_link']"
    logo = "//div[text()='Products']"
    remove_from_cart_button = "//button[contains(text(),'REMOVE')]"
    cart_icon = "//a[@class='shopping_cart_link']"
    cart_items = "//div[@class='cart_item']"
    checkout_button = "//button[@id='checkout']"

    def __init__(self, driver):
        self.driver = driver
        self.selenium_wrapper = SeleniumWrapper(self.driver)

    def navigate_swag_labs(self):
        self.driver.get(self.home_page)
        self.selenium_wrapper.is_page_loaded()

    def login_into_swag_labs(self, username="standard_user", password="secret_sauce") -> None:
        """
        launching browser and logging into the swag labs and validating product logo
        """
        self.navigate_swag_labs()
        self.selenium_wrapper.send_keys(self.username_field, value=username)
        self.selenium_wrapper.send_keys(self.password_field, value=password)
        self.selenium_wrapper.click_element(self.login_button)

    def validate_logo(self):
        assert self.selenium_wrapper.element_visible(self.logo)

    def execute_logout(self):
        self.selenium_wrapper.click_element(self.logout_button)

    def execute_add_items_to_cart(self, item_name: str) -> None:
        items = self.selenium_wrapper.get_elements(self.product_list)
        for item in items:
            if item_name in item.text:
                add_to_cart_button_xpath = ("(//div[@class='inventory_item_price']/following-sibling::button[text("
                                            ")='ADD TO CART'])[1]")
                # ".//button[contains(text(),'Add to cart')]"
                self.selenium_wrapper.click_element(add_to_cart_button_xpath, by_type=By.XPATH)

    def execute_remove_items_from_cart(self, item_name: str) -> None:
        items = self.selenium_wrapper.get_elements(self.cart_items)
        for item in items:
            if item_name in item.text:
                remove_button = item.find_element(By.XPATH, self.remove_from_cart_button)
                self.selenium_wrapper.js_click_element(remove_button)

    def execute_compare_items_to_cart(self, item_name: str) -> None:
        pass

    def execute_proceed_to_checkout(self) -> None:
        pass

    def execute_complete_payment(self) -> None:
        pass

    def fetch_login_error_message(self):
        return self.selenium_wrapper.get_element(self.error_message).text


    # def execute_