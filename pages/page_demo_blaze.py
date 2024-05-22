import random
import re
import string
import time
from selenium.webdriver.common.by import By
from utilities.selenium_wrapper import SeleniumWrapper


class DemoBlaze:
    home_page_url = "https://www.demoblaze.com/"

    # Locators
    _link_replaceable = "//a[text()='{}']"
    _link_signup = "//a[text()='Sign up']", By.XPATH
    _link_login = "//a[text()='Log in']", By.XPATH
    _text_signup = "//h5[text()='Sign up']", By.XPATH
    _text_login = "//h5[text()='Log in']", By.XPATH
    _button_signup = "//button[text()='Sign up']", By.XPATH
    _button_login = "//button[text()='Log in']", By.XPATH
    _input_signup_username = "sign-username", By.ID
    _input_login_username = "loginusername", By.ID
    _input_signup_password = "sign-password", By.ID
    _input_login_password = "loginpassword", By.ID
    _btn_close = "(//button[text()='Close'])[2]", By.XPATH
    all_products_titles = "//h4[@class='card-title']/a", By.XPATH
    all_products_prices = "//h4[@class='card-title']/..//h5", By.XPATH
    btn_next = "//button[text()='Next']", By.XPATH
    link_laptop = "//a[text()='Laptops']", By.XPATH
    link_monitor = "//a[text()='Monitors']", By.XPATH
    txt_description = "more-information", By.ID
    link_apple = "//a[text()='Apple monitor 24']", By.XPATH
    txt_cart_products = "//h2[text()='Products']", By.XPATH
    link_cart = "//a[text()='Cart']", By.XPATH
    tbl_items = "tbodyid", By.ID
    _btn_place_order = "//button[text()='Place Order']", By.XPATH
    _container_place_order = "//h5[text()='Place order']/../../../div[@class='modal-content']", By.XPATH
    product_price = "//a[text()='{}']/../..//h5"
    _text_product = "//h2[text()='Products']", By.XPATH
    _text_product_replaceable = "//td[text()='{}']"
    _h3_replaceable = "//h3[text()='{}']"
    _link_delete_replaceable = "//td[text()='{}']/..//a"
    _btn_purchase = "//button[text()='Purchase']", By.XPATH
    _ipt_name = "// input[ @ id = 'name']", By.XPATH
    _ipt_country = "// input[ @ id = 'country']", By.XPATH
    _ipt_city = "// input[ @ id = 'city']", By.XPATH
    _ipt_credit_card = "// input[ @ id = 'card']", By.XPATH
    _ipt_month = "// input[ @ id = 'month']", By.XPATH
    _ipt_year = "// input[ @ id = 'year']", By.XPATH
    _btn_ok = "//button[text()='OK']", By.XPATH
    _txt_total_amount = "//h3[@id='totalp']", By.XPATH
    _txt_txn_detail = "//div[@class='sweet-alert  showSweetAlert visible']", By.XPATH
    _logo_home_page = "//a[@class='navbar-brand']", By.XPATH
    _txt_logout = "//a[text()='Log out']", By.XPATH

    @classmethod
    def basic_text(cls):
        cls.sign_up_successful = "Sign up successful."
        cls.sign_up_unsuccessful = "This user already exist."
        cls.welcome_user = "Welcome {}"
        cls.user_not_exist = "User does not exist."
        cls.text_categories = "CATEGORIES"
        cls.text_phones = "Phones"
        cls.text_laptops = "Laptops"
        cls.text_monitors = "Monitors"
        cls.text_add_to_cart = "Add to cart"
        cls.text_product_added = "Product added."
        cls.text_cart = "Cart"

    @staticmethod
    def range_filter(product_proprieties: dict, start: int, end: int):
        return {key: value for key, value in product_proprieties.items() if
                int(value.replace("$", "")) in range(start, end)}

    @staticmethod
    def total_price_calculation(items: dict):
        return sum([int(value.replace("$", "")) for key, value in items.items()])

    def __init__(self, driver):
        self.driver = driver
        self.selenium_wrapper = SeleniumWrapper(self.driver)

    def navigate_demo_blaze(self):
        self.driver.get(self.home_page_url)
        self.selenium_wrapper.is_page_loaded()

    def __navigate_sign_up(self):
        self.selenium_wrapper.wait_till_element_visible(*self._link_signup)
        self.selenium_wrapper.click_element(*self._link_signup)
        assert self.selenium_wrapper.element_visible(*self._text_signup)

    def sign_up(self):
        """
        1. trying to login with invalid credentials
        2. creating new user and logining in
        :return:
        """
        self.basic_text()
        self.__navigate_sign_up()
        self.new_user_sign_in(username="", password="")
        self.selenium_wrapper.wait_till_alert_present()
        page_alert = self.driver.switch_to.alert
        actual_alert_message = page_alert.text
        expected_alert_message = "Please fill out Username and Password."
        page_alert.accept()
        assert expected_alert_message == actual_alert_message
        characters = string.ascii_letters + string.digits
        new_user = ''.join(random.choice(characters) for _ in range(10))
        new_password = random.randint(22222222, 99999999)
        self.new_user_sign_in(username=new_user, password=new_password)
        self.selenium_wrapper.wait_till_alert_present()
        page_alert = self.driver.switch_to.alert
        page_alert.accept()
        return new_user, new_password

    def new_user_sign_in(self, username, password):
        self.selenium_wrapper.wait_till_element_visible(*self._input_signup_username)
        self.selenium_wrapper.send_keys(*self._input_signup_username, username)
        self.selenium_wrapper.wait_till_element_visible(*self._input_signup_password)
        self.selenium_wrapper.send_keys(*self._input_signup_password, password)
        self.selenium_wrapper.wait_till_element_visible(*self._button_signup)
        self.selenium_wrapper.scroll_to_element(*self._button_signup)
        self.selenium_wrapper.click_element(*self._button_signup)

    def __navigate_login(self):
        self.selenium_wrapper.wait_till_element_visible(*self._link_login)
        self.selenium_wrapper.click_element(*self._link_login)
        assert self.selenium_wrapper.element_visible(*self._text_login)

    def login(self, username: str, password: str, case_type=True):
        self.basic_text()
        self.__navigate_login()
        self.selenium_wrapper.wait_till_element_visible(*self._input_login_username)
        self.selenium_wrapper.scroll_to_element(*self._input_login_username)
        self.selenium_wrapper.send_keys(*self._input_login_username, username)
        self.selenium_wrapper.wait_till_element_visible(*self._input_login_password)
        self.selenium_wrapper.scroll_to_element(*self._input_login_password)
        self.selenium_wrapper.send_keys(*self._input_login_password, password)
        self.selenium_wrapper.wait_till_element_visible(*self._button_login)
        self.selenium_wrapper.scroll_to_element(*self._button_login)
        self.selenium_wrapper.click_element(*self._button_login)
        if case_type:
            welcome_user = self.welcome_user.format(username)
            welcome_user_locator = self._link_replaceable.format(welcome_user), By.XPATH
            assert self.selenium_wrapper.element_visible(*welcome_user_locator)
        else:
            page_alert = self.driver.switch_to_alert()
            alert_text = page_alert.text
            page_alert.accept()
            assert alert_text == self.user_not_exist

    def home_page(self):
        self.basic_text()
        categories = self._link_replaceable.format(self.text_categories), By.XPATH
        assert self.selenium_wrapper.element_visible(*categories)
        phones = self._link_replaceable.format(self.text_phones), By.XPATH
        assert self.selenium_wrapper.element_visible(*phones)
        laptops = self._link_replaceable.format(self.text_laptops), By.XPATH
        assert self.selenium_wrapper.element_visible(*laptops)
        monitors = self._link_replaceable.format(self.text_monitors), By.XPATH
        assert self.selenium_wrapper.element_visible(*monitors)
        all_products = self.selenium_wrapper.get_elements_text(*self.all_products_titles)
        all_products_prices = self.selenium_wrapper.get_elements_text(*self.all_products_prices)
        if len(all_products) == 0:
            print("No products are available")
        else:
            print("Total count of products in current page is - ", len(all_products))
            for product, price in zip(all_products, all_products_prices):
                print("Product name : ", product)
                print("Product price : ", price)
                print()

    def __navigate_to_phone(self):
        phones = self._link_replaceable.format(self.text_phones), By.XPATH
        self.selenium_wrapper.wait_till_element_visible(*phones)
        self.selenium_wrapper.click_element(*phones)

    def __add_samsung_mobiles(self):
        self.__navigate_to_phone()
        self.selenium_wrapper.wait_till_element_visible(*self.all_products_titles)
        mobiles = self.selenium_wrapper.get_elements_text(*self.all_products_titles)
        all_mobiles = {}
        for name in mobiles:
            if "Samsung" in name:
                locator = self.product_price.format(name)
                self.selenium_wrapper.wait_till_element_visible(locator)
                price = self.selenium_wrapper.get_text(locator)
                all_mobiles[name] = price
        for mobile in all_mobiles.keys():
            self.__add_item_to_cart(mobile)
        return all_mobiles

    def __add_item_to_cart(self, product_name: str):
        self.basic_text()
        product = self._link_replaceable.format(product_name), By.XPATH
        self.selenium_wrapper.wait_till_element_visible(*product)
        self.selenium_wrapper.scroll_to_element(*product)
        self.selenium_wrapper.js_click_element(*product)
        add_to_cart = self._link_replaceable.format(self.text_add_to_cart), By.XPATH
        self.selenium_wrapper.wait_till_element_visible(*add_to_cart)
        self.selenium_wrapper.scroll_to_element(*add_to_cart)
        self.selenium_wrapper.click_element(*add_to_cart)
        self.driver.back()
        self.driver.back()
        time.sleep(5)

    def add_laptop_to_cart(self):
        self.selenium_wrapper.wait_till_element_visible(*self.link_laptop)
        self.selenium_wrapper.click_element(*self.link_laptop)
        time.sleep(3)
        self.selenium_wrapper.wait_till_element_visible(*self.all_products_prices)
        # laptop_names = self.selenium_wrapper.get_elements_text(*self.all_products_titles)
        laptop_prices_1 = self.selenium_wrapper.get_elements_text(*self.all_products_prices)
        laptop_names_1 = self.selenium_wrapper.get_elements_text(*self.all_products_titles)
        self.selenium_wrapper.scroll_to_element(*self.btn_next)
        self.selenium_wrapper.wait_till_element_visible(*self.btn_next)
        self.selenium_wrapper.click_element(*self.btn_next)
        self.selenium_wrapper.wait_till_element_visible(*self.all_products_prices)
        laptop_prices_2 = self.selenium_wrapper.get_elements_text(*self.all_products_prices)
        laptop_names_2 = self.selenium_wrapper.get_elements_text(*self.all_products_titles)
        list_all_laptop_prices = laptop_prices_1 + laptop_prices_2
        list_all_laptop_names = laptop_names_1 + laptop_names_2
        all_laptops = dict(zip(list_all_laptop_names, list_all_laptop_prices))
        print(all_laptops)
        updated_products = self.range_filter(all_laptops, 450, 750)
        print(updated_products)
        for product in updated_products.keys():
            self.__add_item_to_cart(product)
        return updated_products

    def fetching_apple_monitor_resolution(self):
        self.selenium_wrapper.wait_till_element_visible(*self.link_monitor)
        self.selenium_wrapper.click_element(*self.link_monitor)
        time.sleep(2)
        self.selenium_wrapper.wait_till_element_visible(*self.all_products_titles)
        self.selenium_wrapper.click_element(*self.all_products_titles)
        self.selenium_wrapper.scroll_to_element(*self.txt_description)
        self.selenium_wrapper.wait_till_element_visible(*self.txt_description)
        description = self.selenium_wrapper.get_element(*self.txt_description).text
        resolution_pattern = r'\b\d{4}x\d{3,4}\b'
        match = re.search(resolution_pattern, description)
        return match.group(0) if match else None

    def validate_cart_and_items(self):
        self.selenium_wrapper.wait_till_element_visible(*self.link_cart)
        self.selenium_wrapper.click_element(*self.link_cart)
        self.selenium_wrapper.wait_till_element_visible(*self.txt_cart_products)
        self.selenium_wrapper.wait_till_element_visible(*self.tbl_items)
        all_items = self.selenium_wrapper.get_elements_text(*self.tbl_items)
        print(all_items)

    def add_to_cart(self):
        self.__navigate_to_phone()
        return self.__add_samsung_mobiles()

    def __navigate_to_cart(self):
        self.basic_text()
        cart = self._link_replaceable.format(self.text_cart)
        self.selenium_wrapper.wait_till_element_visible(cart)
        self.selenium_wrapper.click_element(cart)
        self.selenium_wrapper.wait_till_element_visible(*self._text_product)

    def navigate_to_cart(self, all_items: dict):
        self.basic_text()
        self.__navigate_to_cart()
        total_price = self.total_price_calculation(all_items)
        price = self._h3_replaceable.format(total_price)
        self.selenium_wrapper.wait_till_element_visible(price)
        all_flags = []
        for item in all_items.keys():
            locator = self._text_product_replaceable.format(item)
            all_flags.append(self.selenium_wrapper.element_visible(locator))
        print("all products visible in cart" if all(all_flags) else "Products not visible in cart")
        assert all(all_flags)

    def remove_item_in_cart(self, all_items: dict, remove_item: str):
        self.__navigate_to_cart()
        delete_product = self._link_delete_replaceable.format(remove_item)
        self.selenium_wrapper.wait_till_element_visible(delete_product)
        self.selenium_wrapper.click_element(delete_product)
        timeout = self.selenium_wrapper.time_out
        self.selenium_wrapper.time_out = 10
        self.driver.refresh()
        time.sleep(4)
        self.driver.refresh()
        assert not self.selenium_wrapper.element_visible(delete_product)
        self.selenium_wrapper.time_out = timeout
        self.navigate_to_cart(all_items)

    def checkout_items(self):
        self.__navigate_to_cart()
        self.selenium_wrapper.wait_till_element_visible(*self._btn_place_order)
        self.selenium_wrapper.click_element(*self._btn_place_order)
        assert self.selenium_wrapper.element_visible(*self._container_place_order)

    def place_order_error_message_validation(self):
        """
        1. trying to place order using invalid details
        2. placing the order using valid details and validating total amount and credit card number after the
           successful transaction.
        3. validating home page redirect after successful payment
        :return:
        """
        expected_alter_message = "Please fill out Name and Creditcard."
        self.selenium_wrapper.wait_till_element_visible(*self._btn_purchase)
        self.selenium_wrapper.click_element(*self._btn_purchase)
        self.selenium_wrapper.wait_till_alert_present()
        page_alert = self.driver.switch_to.alert
        actual_alert_message = page_alert.text
        page_alert.accept()
        assert expected_alter_message == actual_alert_message
        self.selenium_wrapper.wait_till_element_visible(*self._txt_total_amount)
        total_amount = self.selenium_wrapper.get_element(*self._txt_total_amount).text
        print("total amount to place order :", total_amount)
        self.selenium_wrapper.wait_till_element_visible(*self._ipt_name)
        self.selenium_wrapper.send_keys(*self._ipt_name, "sdfghjkl")
        self.selenium_wrapper.wait_till_element_visible(*self._ipt_country)
        self.selenium_wrapper.send_keys(*self._ipt_country, "India")
        self.selenium_wrapper.wait_till_element_visible(*self._ipt_city)
        self.selenium_wrapper.send_keys(*self._ipt_city, "marathahalli")
        credit_card_num = 2233445577886677
        print("credit card number :", credit_card_num)
        self.selenium_wrapper.wait_till_element_visible(*self._ipt_credit_card)
        self.selenium_wrapper.send_keys(*self._ipt_credit_card, str(credit_card_num))
        self.selenium_wrapper.wait_till_element_visible(*self._ipt_month)
        self.selenium_wrapper.send_keys(*self._ipt_month, "09")
        self.selenium_wrapper.wait_till_element_visible(*self._ipt_year)
        self.selenium_wrapper.send_keys(*self._ipt_year, "2028")
        self.selenium_wrapper.wait_till_element_visible(*self._btn_purchase)
        self.selenium_wrapper.click_element(*self._btn_purchase)
        self.selenium_wrapper.wait_till_element_visible(*self._txt_txn_detail)
        txn_details = self.selenium_wrapper.get_element(*self._txt_txn_detail).text
        self.selenium_wrapper.wait_till_element_visible(*self._btn_ok)
        self.selenium_wrapper.click_element(*self._btn_ok)
        self.selenium_wrapper.wait_till_element_visible(*self._logo_home_page)
        self.selenium_wrapper.wait_till_element_visible(*self._txt_logout)
        self.selenium_wrapper.click_element(*self._txt_logout)
        self.selenium_wrapper.wait_till_element_visible(*self._link_login)
        success_amount = txn_details.split()[8]
        success_card_number = txn_details.split()[12]
        assert str(total_amount) == str(success_amount)
        assert str(credit_card_num) == str(success_card_number)





