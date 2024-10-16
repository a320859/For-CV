# pytest -v --tb=line --reruns 1 --browser_name=chrome test_rerun.py - команда для повторного запуска фейловых тестов
# Код в файле conftest, который сам импортируется в нужный исполняемый модуль. Отсюда можно брать готовые элементы
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

def pytest_addoption(parser):  # функция addoption позволяет добавить кастомные параметры в командную строку 
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request): #  Request содержит информацию о текущем тестовом вызове, в том числе доступ к опциям командной строки, метаданным теста и другим полезным данным.
    browser_name = request.config.getoption("browser_name") # request используется не всегда, а только тогда, когда необходимо что-то из вышеописанного 
    browser = None # наприме, без request мы бы не имели доступа к параметрам, которые мы передаём в командной строке 
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()



"""import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('language', ["ru", "en-gb"]) # Пример параметризации тестов ..............................
def test_guest_should_see_login_link(browser, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")"""




"""import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    assert True


@pytest.mark.xfail
def test_not_succeed():
    assert False


@pytest.mark.skip
def test_skipped():
    assert False"""








"""import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    @pytest.mark.smoke # Маркировка...............................................................................
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")"""


"""from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://selenium1py.pythonanywhere.com/"


class TestMainPage1():

    @classmethod
    def setup_class(self): # Этот метод и следующий выполняются один раз для всех тестов сразу (всех функций). То есть, вначале открывается браузер, а в конце всех тестов закрывается, ведь тут есть 
        print("\nstart browser for test suite..") # префикс _class и @classmethod, которые говорят о том, что эти методы испльзуются для всего класса разом
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("quit browser for test suite..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")


class TestMainPage2():

    def setup_method(self): # Этот и следующий методы используются каждый раз во время каждого теста, ведь тут есть префикс _method. То есть, после каждого теста закрывается браузер, а потом открывается снова    
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_guest_should_see_login_link(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self):
        self.browser.get(link)
        self.browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")"""




"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time
browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100')) #ЗАПОМНИТЬ СРОЧНО..............................................
browser.find_element(By.ID, 'book').click()

x = int(browser.find_element(By.ID, 'input_value').text)
browser.find_element(By.ID, 'answer').send_keys(math.log(abs(12*math.sin(x))))
browser.find_element(By.ID, 'solve').click()

time.sleep(5)
browser.quit()"""




"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time
browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

browser.find_element(By.TAG_NAME, 'button').click()

my_windows = browser.window_handles
browser.switch_to.window(my_windows[1])

x = int(browser.find_element(By.ID, 'input_value').text)
browser.find_element(By.ID, 'answer').send_keys(math.log(abs(12*math.sin(x))))

browser.find_element(By.TAG_NAME, 'button').click()

time.sleep(10)
browser.quit()"""










"""import unittest, time
from selenium import webdriver
from selenium.webdriver.common.by import By



class myTestClass(unittest.TestCase):
    def test_number_one(self):
        browser = webdriver.Chrome()
        browser.get('https://suninjuly.github.io/registration1.html')
        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('fdg')
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('fdg')
        browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('fdg')
        browser.find_element(By.CSS_SELECTOR, '.second_block .first').send_keys('fdg')
        browser.find_element(By.CSS_SELECTOR, '.second_block .second').send_keys('fdg')
        browser.find_element(By.TAG_NAME, 'button').click()
        result = browser.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual(result, 'Congratulations! You have successfully registered!')
    
    def test_number_two(self):
        browser = webdriver.Chrome()
        browser.get('https://suninjuly.github.io/registration2.html')
        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('fdg')
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('fdg')
        browser.find_element(By.CSS_SELECTOR, '.first_block .third').send_keys('fdg')
        browser.find_element(By.CSS_SELECTOR, '.second_block .first').send_keys('fdg')
        browser.find_element(By.CSS_SELECTOR, '.second_block .second').send_keys('fdg')
        browser.find_element(By.TAG_NAME, 'button').click()
        result = browser.find_element(By.TAG_NAME, 'h1').text
        self.assertEqual(result, 'Congratulations! You have successfully registered!')

if __name__ == '__main__':
    unittest.main()"""












"""from selenium import webdriver
from selenium.webdriver.common.by import By
import math, time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

browser.find_element(By.TAG_NAME, 'button').click()

browser.switch_to.alert.accept()

x = int(browser.find_element(By.ID, 'input_value').text)
value = math.log(abs(12*math.sin(x)))

browser.find_element(By.ID, 'answer').send_keys(value)
browser.find_element(By.TAG_NAME, 'button').click()

time.sleep(10)
browser.quit()"""




"""import os, time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('dsad')
browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('dsad')
browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('dsad')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

element = browser.find_element(By.CSS_SELECTOR, '[type="file"]')
element.send_keys(file_path)

browser.find_element(By.TAG_NAME, 'button').click()

time.sleep(10) 
browser.quit()"""




"""from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/execute_script.html')
x = browser.find_element(By.ID, 'input_value').text
value = str(math.log(abs(12*math.sin(int(x)))))
browser.find_element(By.ID, 'answer').send_keys(value)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
browser.find_element(By.ID, 'robotCheckbox').click()
browser.find_element(By.ID, 'robotsRule').click()

browser.find_element(By.CLASS_NAME, 'btn').click()

time.sleep(10)

browser.quit()"""




"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time, math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects2.html')

value = int(browser.find_element(By.CSS_SELECTOR, 'h2 .nowrap:nth-child(2)').text) + int(browser.find_element(By.CSS_SELECTOR, 'h2 .nowrap:nth-child(4)').text)
print(value)

select = Select(browser.find_element(By.TAG_NAME, 'select'))
select.select_by_value(str(value))

browser.find_element(By.CLASS_NAME, 'btn').click()

time.sleep(10)
browser.quit()"""



"""from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')

x = browser.find_element(By.TAG_NAME, 'img').get_attribute('valuex')

value = str(math.log(abs(12*math.sin(int(x)))))

browser.find_element(By.ID, 'answer').send_keys(value)

browser.find_element(By.ID, 'robotCheckbox').click()
browser.find_element(By.ID, 'robotsRule').click()

browser.find_element(By.CLASS_NAME, 'btn').click()

time.sleep(10)

browser.quit()"""





"""from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']").send_keys('что-то')
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']").send_keys('что-то')
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']").send_keys('что-то')
    

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()"""









"""from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import time

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/find_xpath_form')

try:
    input1 = browser.find_element(By.TAG_NAME, 'input')
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, 'last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, 'city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")                                                                                                  
    button = browser.find_element(By.XPATH, "//*[text()='Submit']")
    button.click()

finally:
    
    time.sleep(30)
    browser.quit()"""


""""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла"""