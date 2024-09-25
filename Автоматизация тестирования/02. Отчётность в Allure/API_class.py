import requests


class Clients:

    def __init__(self, url) -> None:
        self.url = url

    def auth(self) -> str:
        """
            API. Авторизация пользователя
        """
        login = {"username": "leonardo", "password": "leads"}
        return {'x-client-token': requests.post(self.url + 'auth/login',
                                                json=login).json()['userToken']
                }

    def add_company(self, token: str = ''):
        """
            API. Создание компании
        """
        return requests.post(self.url + 'company',
                             headers=token, json={"name": "Компания",
                                                  "description": "Описание"})

    def add_employee(self, token: str = '', id: int = '', fName: str = '',
                     lName: str = '', mName: str = '', cId: int = '',
                     mail: str = '', url: str = '', phone: str = '',
                     birth: str = '', active: bool = None):
        """
            API. Добавление сотрудника
        """
        employee = {
          "id": id,
          "firstName": fName,
          "lastName": lName,
          "middleName": mName,
          "companyId": cId,
          "email": mail,
          "url": url,
          "phone": phone,
          "birthdate": birth,
          "isActive": active
        }

        return requests.post(self.url + 'employee', headers=token,
                             json=employee)

    def employee_list(self, id: int) -> list:
        """
            API. Получение списка сотрудников по id компании
        """
        return requests.get(self.url + 'employee',
                            params={'company': str(id)})

    def edit_employee(self, id: int = '', token: str = '', lName: str = '',
                      mail: str = '', url: str = '',
                      phone: str = '', active: bool = ''):
        """
            API. Редактирование информации о сотруднике
        """
        changes = {
            "lastName": lName,
            "email": mail,
            "url": url,
            "phone": phone,
            "isActive": active
        }
        return requests.patch(self.url + 'employee/' + str(id),
                              headers=token, json=changes)

    def employee(self, id: int = ''):
        """
            API. Получение информации о пользователе по его id
        """
        return requests.get(self.url + 'employee/' + str(id))

    def delete_company(self, token: str, id: int):
        """
            API. Удаление компании по её id
        """
        return requests.get(self.url + 'company/delete/' + str(id),
                            headers=token)
