import logging
import time
from time import sleep
from pages.page_swag_labs import SwagLabs
import pytest


class TestSwagLabs:
    @pytest.fixture(autouse=True)
    def setup(self, driver_instance):
        self.driver = driver_instance
        self.swag_labs = SwagLabs(self.driver)

    def test_login_into_swag_labs(self):
        self.swag_labs.login_into_swag_labs()
        self.swag_labs.validate_logo()

    # def test_add_new(self):
    #     self.driver.get(r"https://www.google.com")
    #     sleep(10)
    #     self.driver.get(r"https://www.google.com")

    def test_sign_up_with_invali_and_valid_credentials(self):
        expected_login_error_message = "Epic sadface: Username and password do not match any user in this service"
        self.swag_labs.login_into_swag_labs(username="priyanka", password="12345")
        actual_error_message = self.swag_labs.fetch_login_error_message()
        assert expected_login_error_message == actual_error_message, "error message missmatch"
        self.swag_labs.login_into_swag_labs()
        self.swag_labs.validate_logo()

    def test_add_and_remove_cart(self):
        self.swag_labs.login_into_swag_labs()
        self.swag_labs.execute_add_items_to_cart("Sauce Labs Backpack")
        assert self.swag_labs.execute_compare_items_to_cart("Sauce Labs Backpack")
        self.swag_labs.execute_remove_items_from_cart("Sauce Labs Backpack")
        assert not self.swag_labs.execute_compare_items_to_cart("Sauce Labs Backpack")
