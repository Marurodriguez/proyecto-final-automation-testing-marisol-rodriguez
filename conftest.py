import pytest
from utils.screenshot import take_screenshot


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            take_screenshot(driver, item.name)

from utils.driver_factory import get_driver


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()
