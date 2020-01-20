import pytest
from sources.utilities.webdriver_factory import WebDriverFactory

@pytest.yield_fixture()
def setUp():
    print("run BEFORE every method")
    yield
    print("run AFTER every method")


# taking driver instance from webdriver Factory class
@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

# taking the user request of the browser
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    print("Close the browser")
    # driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser", help="to run on different browser")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")
