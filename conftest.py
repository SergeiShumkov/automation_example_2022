import os
import pytest
from selenium import webdriver


DRIVER_FOLDER = os.path.expanduser("~\Downloads\drivers")


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")

@pytest.fixture()
def browser(request):
   _browser = request.config.getoption("--browser")

   if _browser == "opera":
      driver = webdriver.Opera(executable_path=f"{DRIVER_FOLDER}\operadriver\operadriver.exe")
   elif _browser == "chrome":
      driver = webdriver.Chrome(executable_path=f"{DRIVER_FOLDER}\chromedriver\chromedriver.exe")
   else:
      raise ValueError("Browser not supported")
   
   driver.maximize_window()
   
   yield driver

   driver.quit()

    
