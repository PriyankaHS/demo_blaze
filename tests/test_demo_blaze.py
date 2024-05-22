import logging
import time
from random import choice
from time import sleep
from pages.page_demo_blaze import DemoBlaze
from pages.page_swag_labs import SwagLabs
import pytest


class TestDemoBlaze:
    @pytest.fixture(autouse=True)
    def setup(self, driver_instance):
        self.driver = driver_instance
        self.demo_blaze = DemoBlaze(self.driver)

    def test_demo_blaze(self):
        """
        Description:- All the scenarios are covered in one test case
        :return:
        """
        self.demo_blaze.navigate_demo_blaze()
        user_name, password = self.demo_blaze.sign_up()
        self.demo_blaze.login(username=user_name, password=password, case_type=True)
        self.demo_blaze.home_page()
        mobile_phones: dict = self.demo_blaze.add_to_cart()
        laptops: dict = self.demo_blaze.add_laptop_to_cart()
        print("Total phone count - ", len(mobile_phones.keys()))
        print("Total laptop count - ", len(laptops.keys()))
        sum_of_phones = self.demo_blaze.total_price_calculation(mobile_phones)
        sum_of_laptops = self.demo_blaze.total_price_calculation(laptops)
        sum_of_both = sum_of_phones + sum_of_laptops
        print("Sum of phones - ", sum_of_phones)
        print("Sum of Laptops - ", sum_of_laptops)
        print("Sum of both - ", sum_of_both)
        all_items = mobile_phones | laptops
        print(all_items)
        self.demo_blaze.navigate_to_cart(all_items)
        random_laptop = choice(list(laptops.keys()))
        remove_item_price = int(all_items.pop(random_laptop).replace("$", ""))
        print("Removed item cost - ", remove_item_price)
        self.demo_blaze.remove_item_in_cart(all_items, random_laptop)
        print("Total cost after removing item - ", self.demo_blaze.total_price_calculation(all_items))
        self.demo_blaze.checkout_items()
        self.demo_blaze.place_order_error_message_validation()

    def test_apple_monitor_resolution(self):
        """
        Checking and printing Apple monitor resolution
        :return:
        """
        self.demo_blaze.navigate_demo_blaze()
        self.demo_blaze.login(username="priyankahs", password="123456", case_type=True)
        resolution = self.demo_blaze.fetching_apple_monitor_resolution()
        print("Apple monitor resolution", resolution)

    def test_validate_cart_and_item(self):
        self.demo_blaze.navigate_demo_blaze()
        self.demo_blaze.login(username="priyankahs", password="123456", case_type=True)
        self.demo_blaze.validate_cart_and_items()
