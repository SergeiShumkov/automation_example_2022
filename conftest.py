import os
import pytest
from selenium import webdriver


DRIVER_FOLDER = os.path.expanduser("~\Downloads\drivers")


def pytest_addoption(parser):
   parser.addoption("--browser", default="chrome")
   parser.addoption("--url", default="https://demo.opencart.com")

@pytest.fixture()
def browser(request):
   _browser = request.config.getoption("--browser")
   base_url = request.config.getoption("--url")

   if _browser == "opera":
      driver = webdriver.Opera(executable_path=f"{DRIVER_FOLDER}\operadriver\operadriver.exe")
   elif _browser == "chrome":
      driver = webdriver.Chrome(executable_path=f"{DRIVER_FOLDER}\chromedriver\chromedriver.exe")
   else:
      raise ValueError("Browser not supported")
   
   driver.maximize_window()
   driver.base_url = base_url
   
   yield driver

   driver.quit()

    
