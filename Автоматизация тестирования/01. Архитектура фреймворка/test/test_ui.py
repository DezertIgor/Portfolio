from classes.ui import UI
from time import sleep

ui = UI()


def test_add_board():
    ui.auth()
    assert ui.current_page() == "https://trello.com/u/user86102176/boards"
    assert ui.add_board() == "+Доска"


def test_add_card():
    assert ui.add_card() == "+Карточка"


def test_redact_card():
    assert ui.redact_card() == "rgba(148, 199, 72, 1)"


def test_delete_card():
    ui.delete_card()


def test_delete_board():
    ui.delete_board()
    sleep(10)