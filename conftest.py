import pytest
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# -------- Add command line option --------
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="browser selection: chrome or edge"
    )


# -------- Fixture --------
@pytest.fixture(scope="function")
def setup(request):

    browser_name = request.config.getoption("browser")

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


    elif browser_name == "edge":
        driver = webdriver.Edge(service=EdgeService("drivers/msedgedriver.exe"))


    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    driver.implicitly_wait(5)

    request.cls.driver = driver

    yield

    driver.quit()


# -------- Screenshot on failure --------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.cls.driver

        reports_dir = "reports/screenshots"
        os.makedirs(reports_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"{item.name}_{timestamp}.png"

        driver.save_screenshot(os.path.join(reports_dir, file_name))
