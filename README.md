# Demo_blaze Automation Project

## Problem Statement
Automate the procedures for logging in, adding and removing items from the cart, proceeding to checkout, and completing the payment process in Swag Labs.

## Scenario
You have been tasked with automating specific functionalities for a Swag Labs application:

1. Log in
2. Add items to the cart
3. Remove items from the cart
4. Compare items in the cart
5. Proceed to checkout by providing relevant information
6. Complete the payment
7. Log out

The website typically features a sample e-commerce application, and users can perform actions like logging in, adding items to the shopping cart, and completing the checkout process.

## Tech Stacks used in this Framework

1. Python: Primary programming language for writing test scripts and automation code.
2. Selenium WebDriver: Automation tool for interacting with web elements on web pages.
3. pytest: Testing framework for organizing and running test cases efficiently.
4. Allure Reporting: Generates detailed, interactive reports for test execution results.

## Framework Folder Structure explanation
1. pages: Directory for Page Object Model (POM) Pages, representing web pages and their elements.
2. tests: Directory for Python scripts containing test cases.
3. utilities: Directory for helper functions and classes, including a Selenium wrapper class.
4. gitignore: File specifying files and directories to ignore when committing changes to Git.
5. conftest.py: Configuration file that sets up fixtures for the tests, including WebDriver initialization and teardown.
6. pytest.ini: Configuration file for pytest, defining settings such as test directory, log levels, and plugins.
7. requirements.txt: File listing Python dependencies required for the project.
8. github: Contains GitHub Actions workflow files for automating CI/CD processes.

## Commands

## Create Virtual Environment
python -m venv venv

## Activate Virtual Environment
.\venv\Scripts\activate

## Install Dependencies
pip install -r requirements.txt

## Execute Test Cases
pytest

## Install Allure Reports
npm install -g allure-commandline

## Generate Allure Report
 allure serve .\allure-results\
