from pages.login_page import LoginPage
from utils.data_loader import load_users
import pytest


@pytest.fixture(scope="module")
def users_data():
    return load_users()


def test_login_valido(driver, users_data):
    login_page = LoginPage(driver)
    user = users_data["valid_user"]

    login_page.open()
    login_page.login(user["username"], user["password"])

    assert "inventory" in driver.current_url


def test_login_invalido(driver, users_data):
    login_page = LoginPage(driver)
    user = users_data["invalid_user"]

    login_page.open()
    login_page.login(user["username"], user["password"])

    error_message = login_page.get_error_message()
    assert "Epic sadface" in error_message
