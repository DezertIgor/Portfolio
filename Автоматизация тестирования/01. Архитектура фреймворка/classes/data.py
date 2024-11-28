import json

with open('C:/Users/Ихарь/Documents/GitHub/Portfolio/Автоматизация тестирования/01. Архитектура фреймворка/test_data.json', encoding='utf-8') as data_js:
    data_py = json.load(data_js)


class Data:
    def __init__(self) -> None:
        self.dict = data_py

    def val(self, key: str) -> str:
        return self.dict.get(key)
