from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException  # Добавляем импорт
import time

# Функция для регистрации на странице
def register(driver, url):
    driver.get(url)

    # Находим все необходимые поля ввода по уникальным селекторам
    first_name_input = driver.find_element(By.CSS_SELECTOR, "div.first_block .form-control.first")
    last_name_input = driver.find_element(By.CSS_SELECTOR, "div.first_block .form-control.second")
    email_input = driver.find_element(By.CSS_SELECTOR, "div.first_block .form-control.third")

    # Заполняем поля
    first_name_input.send_keys("Иван")
    last_name_input.send_keys("Иванов")
    email_input.send_keys("ivanov@example.com")

    # Нажимаем на кнопку регистрации
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

# Запуск теста
def test_registration():
    # Настроим драйвер
    driver = webdriver.Chrome()

    # Проверяем страницу с успешной регистрацией
    try:
        register(driver, "http://suninjuly.github.io/registration1.html")
        print("Тест на регистрацию прошел успешно на странице 1.")
    except Exception as e:
        print(f"Ошибка на странице 1: {e}")

    # Проверяем страницу с багом
    try:
        register(driver, "http://suninjuly.github.io/registration2.html")
        print("Тест на регистрацию прошел успешно на странице 2.")
    except Exception as e:
        print(f"Ошибка на странице 2: {e}")
        if isinstance(e, NoSuchElementException):
            print("Ошибка NoSuchElementException подтверждает наличие бага в приложении.")

    time.sleep(5)
    driver.quit()

# Запускаем тест
test_registration()
