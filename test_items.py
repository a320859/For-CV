from selenium.webdriver.common.by import By
import time

def test_busket(browser):
    assert browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket') !=[], 'кнопки нет:('
    time.sleep(5)
    

