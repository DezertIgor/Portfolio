from classes.api import Api
from classes.data import Data
import pytest

dat = Data().val
api = Api()


def test_add_board():
    before = api.all_boards()
    assert api.add_board().status_code == 200
    after = api.all_boards()
    assert after - before == 1


def test_add_card():
    assert api.add_card()["id"] == api.last_card()["id"]


def test_redact_card():
    api.change_card()
    assert api.last_card()["cover"]["sharedSourceUrl"] == dat("change_card")[
        "cover"]["url"]


def test_move_card():
    assert api.drag_card()["idList"] == api.last_list()["id"]


def test_delete_card():
    assert api.delete_card().status_code == 200
    with pytest.raises(IndexError):
        api.last_card()


def test_delete_board():
    before = api.all_boards()
    assert api.delete_board() is None
    after = api.all_boards()
    assert before - after == 1
