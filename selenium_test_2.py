from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# try:
#     link = "http://suninjuly.github.io/registration2.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     # Ваш код, который заполняет обязательные поля
#     input1=browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
#     input1.send_keys('Ivan')
#     input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
#     input2.send_keys('Ivan')
#     input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")
#     input3.send_keys('asdasd@asdawd.ru')

#     # Отправляем заполненную форму
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
#     # Проверяем, что смогли зарегистрироваться
#     # ждем загрузки страницы
#     time.sleep(1)
#
#     # находим элемент, содержащий текст
#     welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
#     # записываем в переменную welcome_text текст из элемента welcome_text_elt
#     welcome_text = welcome_text_elt.text
#
#     # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#     assert "Congratulations! You have successfully registered!" == welcome_text
#
# finally:
#     # ожидание чтобы визуально оценить результаты прохождения скрипта
#     time.sleep(10)
#     # закрываем браузер после всех манипуляций
#     browser.quit()


try:
    link='https://suninjuly.github.io/math.html'
    browser=webdriver.Chrome()
    browser.get(link)

    # def calc(x):
    #     return str(math.log(abs(12 * math.sin(int(x)))))
    #
    # x_element=browser.find_element(By.CSS_SELECTOR, '#input_value')
    # x=x_element.text
    # y=calc(x)
    #
    # input=browser.find_element(By.CSS_SELECTOR, '#answer')
    # input.send_keys(y)
    # checkbox=browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
    # checkbox.click()
    # radiobutton=browser.find_element(By.CSS_SELECTOR, '#robotsRule')
    # radiobutton.click()
    # submit=browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    # submit.click()

    # проверяем значение атрибута checked у people_radio
    # people_radio=browser.find_element(By.ID,'peopleRule')
    # people_checked=people_radio.get_attribute('checked')
    # print('value of people radio:', people_checked)
    # assert people_checked == "true", "People radio is not selected by default"

    # проверяем значение атрибута checked у robots_radio
    # robots_radio=browser.find_element(By.ID, 'robotsRule')
    # robots_checked=robots_radio.get_attribute('checked')
    # print('value of robots radio:', robots_checked)
    # assert robots_checked is None

    # проверяем значение атрибута disabled у кнопки Submit
    # button = browser.find_element(By.CSS_SELECTOR, '.btn')
    # button_disabled = button.get_attribute("disabled")
    # print("value of button Submit: ", button_disabled)
    # assert button_disabled is None

    # проверяем значение атрибута disabled у кнопки Submit после таймаута
#     time.sleep(10)
#     button_disabled = button.get_attribute("disabled")
#     print("value of button Submit after 10sec: ", button_disabled)
#     assert button_disabled is not None
#
# finally:
#     time.sleep(10)
#     browser.quit()


# 1. Открыть страницу http://suninjuly.github.io/get_attribute.html.
# 2. Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
# 3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
# 4. Посчитать математическую функцию от x (сама функция остаётся неизменной).
# 5. Ввести ответ в текстовое поле.
# 6. Отметить checkbox "I'm the robot".
# 7. Выбрать radiobutton "Robots rule!".
# 8. Нажать на кнопку "Submit".



# try:
#     link='http://suninjuly.github.io/get_attribute.html'
#     browser=webdriver.Chrome()
#     browser.get(link)
#     box=browser.find_element(By.CSS_SELECTOR, '#treasure')
#     box_x=box.get_attribute('valuex')
#     input1=browser.find_element(By.CSS_SELECTOR, '#answer')
#     def calc(box_x):
#         return str((math.log(abs(12 * math.sin(int(box_x))))))
#     y=calc(box_x)
#     input1.send_keys(y)
#     check_box=browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
#     check_box.click()
#     radiobutton=browser.find_element(By.CSS_SELECTOR, '#robotsRule')
#     radiobutton.click()
#     button=browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
#     button.click()
# finally:
#     time.sleep(10)
#     browser.quit()



# 1. Открыть страницу https://suninjuly.github.io/selects1.html
# 2. Посчитать сумму заданных чисел
# 3. Выбрать в выпадающем списке значение равное расчитанной сумме
# 4. Нажать кнопку "Submit"

# try:
#     link='http://suninjuly.github.io/selects1.html'
#     browser=webdriver.Chrome()
#     browser.get(link)
#     num1=browser.find_element(By.CSS_SELECTOR, '#num1')
#     num2=browser.find_element(By.CSS_SELECTOR, '#num2')
#     num1_text=num1.text
#     num2_text=num2.text
#     s=int(num1_text)+int(num2_text)
#     select=Select(browser.find_element(By.TAG_NAME, 'select'))
#     select.select_by_visible_text(str(s))
#     button=browser.find_element(By.CLASS_NAME, 'btn').click()
# finally:
#     time.sleep(5)


# try:
#     browser = webdriver.Chrome()
#     link = "https://SunInJuly.github.io/execute_script.html"
#     browser.get(link)
#     button = browser.find_element(By.TAG_NAME, "button")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#     button.click()
# finally:
#     time.sleep(5)
#     browser.quit()


# Открыть страницу http://SunInJuly.github.io/execute_script.html.
# Считать значение для переменной x.
# Посчитать математическую функцию от x.
# Проскроллить страницу вниз.
# Ввести ответ в текстовое поле.
# Выбрать checkbox "I'm the robot".
# Переключить radiobutton "Robots rule!".
# Нажать на кнопку "Submit".


# try:
#     browser = webdriver.Chrome()
#     link = "http://SunInJuly.github.io/execute_script.html"
#     browser.get(link)
#     x=browser.find_element(By.CSS_SELECTOR, '#input_value')
#     x=x.text
#     def calc(x):
#         return str((math.log(abs(12 * math.sin(int(x))))))
#     y=calc(x)
#     y_in=browser.find_element(By.CSS_SELECTOR, '#answer')
#     y_in.send_keys(y)
#     box=browser.find_element(By.CSS_SELECTOR, '#robotCheckbox')
#     box.click()
#     browser.execute_script('window.scrollBy(0, 200);')
#     robot_rule=browser.find_element(By.CSS_SELECTOR, '#robotsRule')
#     robot_rule.click()
#     button=browser.find_element(By.CSS_SELECTOR, '.btn')
#     button.click()
# finally:
#     time.sleep(5)
#     browser.quit()




# Открыть страницу http://suninjuly.github.io/file_input.html
# Заполнить текстовые поля: имя, фамилия, email
# Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
# Нажать кнопку "Submit"


# try:
#     browser = webdriver.Chrome()
#     link = "http://suninjuly.github.io/file_input.html"
#     browser.get(link)
#     name=browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
#     name.send_keys('Andrey')
#     lastname=browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
#     lastname.send_keys('ASDASD')
#     email=browser.find_element(By.CSS_SELECTOR, '[name="email"]')
#     email.send_keys('ASDFAFSF')
#     open('newfile.txt', 'a').close()
#     current_dir=os.path.abspath((os.path.dirname(__file__)))
#     file_name='newfile.txt'
#     file_path=os.path.join(current_dir, file_name)
#     element=browser.find_element(By.CSS_SELECTOR,'[type="file"]')
#     element.send_keys(file_path)
#     btn=browser.find_element(By.CSS_SELECTOR, '.btn')
#     btn.click()
#     os.remove('newfile.txt')
# finally:
#     time.sleep(10)
#     browser.quit()


# Открыть страницу http://suninjuly.github.io/alert_accept.html
# Нажать на кнопку
# Принять confirm
# На новой странице решить капчу для роботов, чтобы получить число с ответом

# try:
#     browser=webdriver.Chrome()
#     link='http://suninjuly.github.io/alert_accept.html'
#     browser.get(link)
#     button=browser.find_element(By.CSS_SELECTOR, '.btn')
#     button.click()
#     prompt=browser.switch_to.alert
#     prompt.accept()
#     x=browser.find_element(By.CSS_SELECTOR, '#input_value')
#     x=x.text
#     def calc(x):
#         return str((math.log(abs(12 * math.sin(int(x))))))
#     y=calc(x)
#     s=browser.find_element(By.CSS_SELECTOR, '#answer')
#     s.send_keys(y)
#     submit=browser.find_element(By.CSS_SELECTOR, '.btn')
#     submit.click()
# finally:
#     time.sleep(10)
#     browser.quit()

# Открыть страницу http://suninjuly.github.io/redirect_accept.html
# Нажать на кнопку
# Переключиться на новую вкладку
# Пройти капчу для робота и получить число-ответ

# try:
#     link='http://suninjuly.github.io/redirect_accept.html'
#     browser=webdriver.Chrome()
#     browser.get(link)
#     btn_1=browser.find_element(By.CSS_SELECTOR, '.btn')
#     btn_1.click()
#     new_window=browser.window_handles[1]
#     browser.switch_to.window(new_window)
#     x=browser.find_element(By.CSS_SELECTOR, '#input_value')
#     x=x.text
#     def calc(x):
#         return str((math.log(abs(12 * math.sin(int(x))))))
#     y=calc(x)
#     y_in=browser.find_element(By.CSS_SELECTOR, '#answer')
#     y_in.send_keys(y)
#     btn_2=browser.find_element(By.CSS_SELECTOR, '.btn')
#     btn_2.click()
# finally:
#     time.sleep(10)
#     browser.quit()



# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait1.html")
#
# browser.implicitly_wait(5)                                #Время ожидания
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text


# Открыть страницу http://suninjuly.github.io/explicit_wait2.html
# Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
# Нажать на кнопку "Book"
# Решить уже известную нам математическую задачу (используйте ранее написанный код) и отправить решение

# try:
#     link = 'http://suninjuly.github.io/explicit_wait2.html'
#     browser=webdriver.Chrome()
#     browser.get(link)
#     WebDriverWait(browser, 15).until(
#         EC.text_to_be_present_in_element((By.ID, 'price'), "100")
#     )
#     btn=browser.find_element(By.ID,'book')
#     btn.click()
#     x = browser.find_element(By.CSS_SELECTOR, '#input_value')
#     x=x.text
#     def calc(x):
#         return str((math.log(abs(12 * math.sin(int(x))))))
#     y=calc(x)
#     y_in=browser.find_element(By.CSS_SELECTOR, '#answer')
#     y_in.send_keys(y)
#     btn_2=browser.find_element(By.ID, 'solve')
#     btn_2.click()
# finally:
#     time.sleep(10)
#     browser.quit()




