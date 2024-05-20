from time import sleep

import pytest


class TestSwagLabs:
    @pytest.fixture(autouse=True)
    def setup(self, driver_instance):
        self.driver = driver_instance

    def test_add_new(self):
        self.driver.get(r"https://www.google.com")
        sleep(10)
        self.driver.get(r"https://www.google.com")