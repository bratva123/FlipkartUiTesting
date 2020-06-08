import pytest
from selenium import webdriver

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="session", autouse=True)
def oneTimeSetUp(request):
        print("Running one time setUp")

        baseURL = "https://www.flipkart.com"
        option = webdriver.ChromeOptions()
        # option.add_argument("--headless")
        option.add_argument("--no-sandbox")
        option.add_argument("--disable-dev-shm-usage")
        option.add_argument("--disable-gpu")
        option.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=option)
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        print("Running tests on FF")
        yield driver
        driver.quit()
        print("Running one time tearDown")
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#     parser.addoption("--osType", help="Type of operating system")
#
# @pytest.fixture(scope="session")
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture(scope="session")
# def osType(request):
#     return request.config.getoption("--osType")
