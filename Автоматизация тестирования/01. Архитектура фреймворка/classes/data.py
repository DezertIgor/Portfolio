import json

data_js = open('/Users/tk_user/git/Portfolio/Автоматизация тестирования/01. Архитектура фреймворка/test_data.json')
data_py = json.load(data_js)


class Data:
    def __init__(self) -> None:
        self.dict = data_py

    def val(self, key: str) -> str:
        return self.dict.get(key)
