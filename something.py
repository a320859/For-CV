from selenium import webdriver
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
browser.quit()




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