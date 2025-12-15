from utils.driver_factory import get_driver
from pages.login_page import LoginPage


def test_login_valido():
    driver = get_driver()
    login_page = LoginPage(driver)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    assert "inventory" in driver.current_url

    driver.quit()
