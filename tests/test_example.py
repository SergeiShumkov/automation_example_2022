from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])


def test_first():
    # chrome = webdriver.Chrome(executable_path="D:\Automation\Drivers\chromedriver.exe")

    chrome = webdriver.Chrome(options=options)
    chrome.get("https://yandex.ru")
    assert "Яндекс" in chrome.title
    
# tetst


