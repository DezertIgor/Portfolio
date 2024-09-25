from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))


class Form():

    def get(self):
        """
            UI. Переход на страницу с формой
        """
        browser.maximize_window()
        browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def filling(self):
        """
            UI. Заполнение всех полей формы, кроме поля "Zip code"
        """
        list = [
            ('[name="first-name"]', 'Иван'),
            ('[name="last-name"]', 'Петров'),
            ('[name="address"]', 'Ленина, 55-3'),
            ('[name="zip-code"]', ''),
            ('[name="city"]', 'Москва'),
            ('[name="country"]', 'Россия'),
            ('[name="e-mail"]', 'test@skypro.com'),
            ('[name="phone"]', '+7985899998787'),
            ('[name="job-position"]', 'QA'),
            ('[name="company"]', 'SkyPro')
        ]
        for locator, value in list:
            browser.find_element(By.CSS_SELECTOR, locator).send_keys(value)

    def click(self):
        """
            UI. Нажатие на кнопку "Submit"
        """
        browser.find_element(By.TAG_NAME, "button").click()

    def color_of_red_element(self) -> str:
        """
            UI. Получение цвета поля "Zip code"
        """
        must_be_red = browser.find_element(By.CSS_SELECTOR, "#zip-code"
                                           ).value_of_css_property(
                                               'background-color')
        return must_be_red

    def color_of_green_elements(self) -> list:
        """
            UI. Получение списка цветов всех полей, кроме "Zip code"
        """
        must_be_green = browser.find_elements(By.CSS_SELECTOR,
                                              ".alert:not(#zip-code)")
        list_of_colors = []
        for elem in must_be_green:
            list_of_colors.append(elem.value_of_css_property(
                "background-color"))
        browser.quit()
        return list_of_colors


class Calculator():

    def get(self):
        """
            UI. Переход на страницу с калькулятором
        """
        browser.maximize_window()
        browser.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def calculate_and_wait(self) -> str:
        """
            UI. Получение итогового значения
        """
        browser.find_element(By.CSS_SELECTOR, '#delay').clear()
        browser.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')
        browser.find_element(By.CSS_SELECTOR,
                             '.keys > :nth-child(1)').click()
        browser.find_element(By.CSS_SELECTOR,
                             '.keys > :nth-child(4)').click()
        browser.find_element(By.CSS_SELECTOR,
                             '.keys > :nth-child(2)').click()
        browser.find_element(By.CSS_SELECTOR,
                             '.keys > :nth-child(15)').click()
        WebDriverWait(browser, 46).until(EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), '15'))
        result = browser.find_element(By.CSS_SELECTOR, '.screen').text
        browser.quit()
        return result


class Shop():

    def get(self):
        """
            UI. Переход на страницу авторизации магазина "Swag Labs"
        """
        browser.maximize_window()
        browser.get(
            "https://www.saucedemo.com/")

    def auth(self):
        """
            UI. Авторизация пользователя
        """
        browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys(
            'standard_user')
        browser.find_element(By.CSS_SELECTOR, '#password').send_keys(
            'secret_sauce')
        browser.find_element(By.CSS_SELECTOR, '#login-button').click()

    def pick(self):
        """
            UI. Добавление товаров в корзину
        """
        browser.find_element(By.CSS_SELECTOR,
                             '#add-to-cart-sauce-labs-backpack').click()
        browser.find_element(By.CSS_SELECTOR,
                             '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        browser.find_element(By.CSS_SELECTOR,
                             '#add-to-cart-sauce-labs-onesie').click()

    def cart(self):
        """
            UI. Переход к оплате
        """
        browser.find_element(By.CSS_SELECTOR,
                             '.shopping_cart_link').click()
        browser.find_element(By.CSS_SELECTOR,
                             '#checkout').click()

    def form_and_order(self) -> str:
        """
            UI. Заполнение формы оплаты
        """
        browser.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Игорь')
        browser.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Васюта')
        browser.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(
            '344091')
        browser.find_element(By.CSS_SELECTOR, '#continue').click()
        total = browser.find_element(By.CSS_SELECTOR, '.summary_total_label'
                                     ).text
        print(total)
        browser.quit()
        return total
