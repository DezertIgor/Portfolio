from classes.ui import UI
from classes.data import Data
import allure

dat = Data().val
ui = UI()


@allure.title("Добавление доски API")
def test_add_board():
    ui.auth()
    assert ui.current_page() == dat("page")
    assert ui.add_board() == dat("board")["name"]


@allure.title("Добавление карточки API")
def test_add_card():
    assert ui.add_card() == dat("card")["name"]


@allure.title("Редактирование карточки API")
def test_redact_card():
    assert ui.redact_card() == dat("color")


@allure.title("Перемещение карточки в другой список API")
def test_drag_and_drop_card():
    ui.drag_card()


@allure.title("Удаление карточки API")
def test_delete_card():
    ui.delete_card()


@allure.title("Удаление доски API")
def test_delete_board():
    ui.delete_board()
