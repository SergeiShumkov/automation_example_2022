import os
import requests
from selenium import webdriver


DRIVER_FOLDER = os.path.expanduser("~\Downloads\drivers")

driver = webdriver.Chrome(executable_path=f"{DRIVER_FOLDER}\chromedriver\chromedriver.exe")

driver.get("http://admin:admin@10.2.23.25/index.html")

# "http://10.2.23.25/index.html/cgi-bin/get_system_info.cgi    http://root:root@host   http://fakelogin:fakepassword@www.mysite.com/auth/