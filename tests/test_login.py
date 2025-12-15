from utils.driver_factory import get_driver
from pages.login_page import LoginPage


def test_login_valido():
    driver = get_driver()
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

    driver.quit()


def test_login_invalido():
    driver = get_driver()
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("locked_out_user", "wrong_password")

    error_message = login_page.get_error_message()
    assert "Epic sadface" in error_message

    driver.quit()
