from selenium.webdriver.common.by import By


# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])


def test_admin_authorization(browser):
    # chrome = webdriver.Chrome(options=options)
    browser.get(f"{browser.base_url}/admin/")
    
    # Ввести логин
    browser.find_element(By.CSS_SELECTOR, "#input-username").clear()
    browser.find_element(By.CSS_SELECTOR, "#input-username").send_keys("demo")

    # Ввести пароль
    browser.find_element(By.CSS_SELECTOR, "#input-username").clear()
    browser.find_element(By.CSS_SELECTOR, "#input-password").send_keys("demo")

    # Нажать кнопку Login
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    # Проверить, что залогинился    
    browser.find_element(By.CSS_SELECTOR, "#user-profile")

    # alert alert-danger alert-dismissible

def test_admin_reset_password(browser):
    # chrome = webdriver.Chrome(options=options)
    browser.get(f"{browser.base_url}/admin/")
    
   
    browser.find_element(By.LINK_TEXT, "Forgotten Password").click()
    
 
    browser.find_element(By.CSS_SELECTOR, "#input-email").clear()
    browser.find_element(By.CSS_SELECTOR, "#input-email").send_keys("not_existing_mail@mail.ru")


    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    
    
    browser.find_element(By.CSS_SELECTOR, ".alert-danger")

    



