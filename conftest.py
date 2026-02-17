import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# ---------------- FIXTURE : DRIVER SETUP ----------------
@pytest.fixture(scope="function")
def setup(request):

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver

    yield

    driver.quit()


# ---------------- SCREENSHOT ON FAILURE ----------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        # get driver from test class
        driver = item.cls.driver

        reports_dir = "reports/screenshots"
        os.makedirs(reports_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"{item.name}_{timestamp}.png"

        driver.save_screenshot(os.path.join(reports_dir, file_name))
