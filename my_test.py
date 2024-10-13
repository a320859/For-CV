from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time, math, pytest

list_links = 'https://stepik.org/lesson/236895/step/1 https://stepik.org/lesson/236896/step/1 https://stepik.org/lesson/236897/step/1\
              https://stepik.org/lesson/236898/step/1 https://stepik.org/lesson/236899/step/1 https://stepik.org/lesson/236903/step/1 \
              https://stepik.org/lesson/236904/step/1 https://stepik.org/lesson/236905/step/1'.split(' ')


@pytest.fixture(scope='function')
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('links', list_links)
def test_text_field(browser, links):
    browser.implicitly_wait(10)
    browser.get(links)
    time.sleep(5)
    browser.find_element(By.ID, 'ember458').click()
    browser.find_element(By.ID, 'id_login_email').send_keys('a320859@gmail.com')
    browser.find_element(By.ID, 'id_login_password').send_keys('6789se')
    time.sleep(5)
    button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.sign-form__btn.button_with-loader')))
    button.click()
    time.sleep(5)
    answer = math.log(int(time.time()))
    browser.find_element(By.TAG_NAME, 'textarea').send_keys(answer)
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    time.sleep(10)
    field = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
    assert field == 'Correct!', 'ТЕКСТ НЕ СОВПАДАЕТ'
    








