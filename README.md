# Demo_blaze Automation Project

# Problem Statement
Automate the procedures for logging in, adding and removing items from the cart, proceeding to checkout, and completing the payment process in Swag Labs.

# Scenario
You have been tasked with automating specific functionalities for a Swag Labs application:

1. Log in
2. Add items to the cart
3. Remove items from the cart
4. Compare items in the cart
5. Proceed to checkout by providing relevant information
6. Complete the payment
7. Log out

The website typically features a sample e-commerce application, and users can perform actions like logging in, adding items to the shopping cart, and completing the checkout process.

# Tech Stacks used in this Framework

1. Python: Primary programming language for writing test scripts and automation code.
2. Selenium WebDriver: Automation tool for interacting with web elements on web pages.
3. pytest: Testing framework for organizing and running test cases efficiently.
4. Html Report: Utilizes pytest-html plugin for generating detailed HTML reports of test execution results.

# Framework Folder Structure
1. Page Object Model (POM) Pages: Modular components that represent web pages and their elements, following the Page Object Model design pattern.
2. Test Files: Python scripts containing test cases written using the pytest framework to validate the application's functionality.
3. Utilities: A collection of helper functions and classes, including a Selenium wrapper class, to assist in test automation tasks.4. conftest.py: Sets up fixtures for the tests
4. Conftest: Configuration file that sets up fixtures for the tests, including WebDriver initialization and teardown.
5. pytest.ini: Configuration file for pytest, defining settings such as test directory, log levels, and plugins.
6. HTML Reporting: Automatically generated HTML reports that provide a visual representation of test execution results, including test outcomes, durations, and any failures encountered during testing.
