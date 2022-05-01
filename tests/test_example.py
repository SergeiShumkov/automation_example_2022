
# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])


def test_first(browser):
    # chrome = webdriver.Chrome(options=options)
    browser.get("https://www.u-mama.ru")
    assert "о" in browser.title
    



