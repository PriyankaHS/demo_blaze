from utilities.selenium_wrapper import SeleniumWrapper


class SwagLabs:
    home_page = "https://www.saucedemo.com/v1/"

    def __init__(self, driver):
        self.driver = driver
        self.selenium_wrapper = SeleniumWrapper(self.driver)

    def navigate_swag_labs(self):
        self.driver.get(self.home_page)

    def execute_login(self, user_name, password: str) -> None:
        pass

    def execute_logout(self):
        pass

    def execute_add_items_to_cart(self, item_name: str) -> None:
        pass

    def execute_remove_items_to_cart(self, item_name: str) -> None:
        pass

    def execute_compare_items_to_cart(self, item_name: str) -> None:
        pass

    def execute_proceed_to_checkout(self) -> None:
        pass

    def execute_complete_payment(self) -> None:
        pass
