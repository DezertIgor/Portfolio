from classes.api import Api
from classes.data import Data
import allure
import pytest


dat = Data().val
api = Api()


@allure.title("Добавление доски UI")
def test_add_board():
    before = api.all_boards()
    assert api.add_board().status_code == 200
    after = api.all_boards()
    assert after - before == 1


@allure.title("Добавление карточки UI")
def test_add_card():
    assert api.add_card()["id"] == api.last_card()["id"]


@allure.title("Редактирование карточки UI")
def test_redact_card():
    api.change_card()
    assert api.last_card()["cover"]["sharedSourceUrl"] == dat("change_card")[
        "cover"]["url"]


@allure.title("Drag'n'Drop карточки в другой список UI")
def test_move_card():
    assert api.drag_card()["idList"] == api.last_list()["id"]


@allure.title("Удаление карточки UI")
def test_delete_card():
    assert api.delete_card().status_code == 200
    with pytest.raises(IndexError):
        api.last_card()


@allure.title("Удаление доски UI")
def test_delete_board():
    before = api.all_boards()
    assert api.delete_board() is None
    after = api.all_boards()
    assert before - after == 1
