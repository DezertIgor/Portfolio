from classes.ui import UI
from classes.data import Data

dat = Data().val
ui = UI()


def test_add_board():
    ui.auth()
    assert ui.current_page() == dat("page")
    assert ui.add_board() == dat("board")["name"]


def test_add_card():
    assert ui.add_card() == dat("card")["name"]


def test_redact_card():
    assert ui.redact_card() == dat("color")


def test_drag_and_drop_card():
    ui.drag_card()


def test_delete_card():
    ui.delete_card()


def test_delete_board():
    ui.delete_board()
