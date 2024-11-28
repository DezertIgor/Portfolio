from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from classes.data import Data
import allure
from time import sleep

dat = Data().val


class UI:
    def __init__(self, ui: webdriver = webdriver.Chrome(service=ChromeService(
            ChromeDriverManager().install()))) -> None:
        self.ui = ui

    @allure.step("Поиск элемента")
    def find(self, locator: str) -> str:
        """
        Ищет элемент по CSS-селекторам
        """
        return self.ui.find_element(By.CSS_SELECTOR, locator)

    @allure.step("Одидание видимости элемента")
    def wait(self, locator: str) -> None:
        """
        Явное ожидание видимости элемента на странице
        """
        WebDriverWait(self.ui, 25, 0.2).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, locator)))

    @allure.step("Адрес страницы")
    def current_page(self) -> str:
        """
        Возвращает текущий URL страницы
        """
        return self.ui.current_url

    @allure.step("Нажатие на элемент")
    def click(self, locator: str) -> None:
        """
        Кликает на элемент, найденный по локатору, после явного
        ожидания его кликабельности
        """
        WebDriverWait(self.ui, 25, 0.2).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, locator)))
        self.find(locator).click()

    @allure.step("Ввод текста")
    def write(self, locator: str, text: str):
        """
        Заполнение текстового поля текстом после явного ожидания
        его видимости
        """
        WebDriverWait(self.ui, 25, 0.2).until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, locator)))
        self.find(locator).send_keys(text)

    @allure.step("Авторизация")
    def auth(self) -> None:
        """
        Авторизация по логину и паролю
        """
        self.ui.get("https://id.atlassian.com/login?application=trello&continue=https%3A%2F%2Ftrello.com%2Fauth%2Fatlassian%2Fcallback%3Fdisplay%3DeyJ2ZXJpZmljYXRpb25TdHJhdGVneSI6InNvZnQifQ%253D%253D&display=eyJ2ZXJpZmljYXRpb25TdHJhdGVneSI6InNvZnQifQ%3D%3D")
        self.ui.maximize_window()
        self.write('input#username', dat("login"))
        self.click('#login-submit')
        self.write('input#password', dat("password"))
        self.click('#login-submit')
        self.wait('[data-testid= "header-member-menu-avatar"]')

    @allure.step("Создание доски")
    def add_board(self) -> str:
        """
        Создаёт новую доску
        """
        self.click("div.board-tile.mod-add")
        self.click("li.weB1QxFqJjPDxm.BLhGuhoSSJp4B7.UgkaILhs2YopR2")
        self.write('[data-testid= "create-board-title-input"]', "+Доска")
        self.click('[data-testid= "create-board-submit-button"]')
        self.wait('[data-testid= "board-name-display"]')
        return self.find('[data-testid= "board-name-display"]').text

    @allure.step("Добавление карточки")
    def add_card(self) -> str:
        """
        Создаёт новую карточку
        """
        self.write('[data-testid= "list-card-composer-textarea"]', dat("card")
                   ["name"])
        self.click('[data-testid= "list-card-composer-add-card-button"]')
        return self.find('[data-testid= "card-name"]').text

    @allure.step("Изменение фона карточки")
    def redact_card(self) -> str:
        """
        Изменяет задний фон карточки
        """
        sleep(3)  # Пришлось добавить этот один sleep из-за реального бага в
        # Trello: кнопка карточки видима и кликабельна, но нажатие на неё
        # ничего не даёт в течение примерно двух секунд после добавления
        # карточки. (Соответственно, явные и неявные ожидания не помогают.)
        self.click('[data-testid= "trello-card"]')
        self.wait('section.QI4qitS2RefeF0')
        self.find('div.vasPIpPWWhzu4y').find_element(By.CSS_SELECTOR,
               ":scope > :first-child").find_element(By.CSS_SELECTOR,
                ":scope > :last-child").find_element(By.CSS_SELECTOR,
            ':scope > :nth-last-child(2)').find_element(By.CSS_SELECTOR,
            "button.O6RBvoSEAyiJ4B.bxgKMAm3lq5BpA.PnEv2xIWy3eSui.SEj5vUdI3VvxDc")
        self.click('[data-testid= "card-back-cover-button"]')
        self.click('[data-testid= "color-tile-lime"]')
        self.click('[data-testid= "popover-close"]')
        self.find('div.BXekJYFkPyovJz').find_element(By.CSS_SELECTOR,
            "button.oFGLCx1ywahDGo.qLCa1RhoHzJNkQ.frrHNIWnTojsww.bxgKMAm3lq5BpA.HAVwIqCeMHpVKh.SEj5vUdI3VvxDc").click()
        return self.ui.find_element(By.CSS_SELECTOR,
                                    '[data-testid= "card-front-cover"]'
                                    ).value_of_css_property("background-color")

    @allure.step("Drag'n'Drop карточки")
    def drag_card(self) -> None:
        """
        Перетаскивает карточку в другой список
        """
        draggable = self.find("[data-testid= 'list-card']")
        droppable = self.find(".board-main-content").find_element(By.
            CSS_SELECTOR, '[data-testid= "lists"]').find_element(By.
            CSS_SELECTOR, ':scope > :nth-last-child(2)')
        ActionChains(self.ui).drag_and_drop(draggable, droppable).perform()

    @allure.step("Удаление карточки")
    def delete_card(self) -> None:
        """
        Удаляет карточку
        """
        self.click('[data-testid= "card-name"]')
        self.click('[data-testid= "card-back-archive-button"]')
        self.click('[data-testid= "card-back-delete-card-button"]')
        self.click('[data-testid= "popover-confirm-button"]')

    @allure.step("Удаление доски")
    def delete_board(self) -> None:
        """
        Закрывает и удаляет доску
        """
        self.click('button.GDunJzzgFqQY_3.frrHNIWnTojsww.bxgKMAm3lq5BpA.HAVwIqCeMHpVKh.SEj5vUdI3VvxDc')
        self.wait("button.TJ69T0gm8D5GkA.bxgKMAm3lq5BpA.SEj5vUdI3VvxDc")
        self.find('[data-testid= "board-menu-current-panel"]').find_element(By.
            CSS_SELECTOR, 'ul').find_element(By.CSS_SELECTOR,
            ":scope > :last-child").find_element(By.CSS_SELECTOR,
            'button.TJ69T0gm8D5GkA.bxgKMAm3lq5BpA.SEj5vUdI3VvxDc').click()
        self.click('[data-testid= "popover-close-board-confirm"]')
        self.click('[data-testid= "close-board-delete-board-button"]')
        self.click('[data-testid= "close-board-delete-board-confirm-button"]')
