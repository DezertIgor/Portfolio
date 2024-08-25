import requests


class Clients:

    def __init__(self, url) -> None:
        self.url = url

    def auth(self):
        login = {"username": "leonardo", "password": "leads"}
        return {'x-client-token': requests.post(self.url + 'auth/login',
                                                json=login).json()['userToken']
                }

    def add_company(self, token=''):
        return requests.post(self.url + 'company',
                             headers=token, json={"name": "Компания",
                                                  "description": "Описание"})

    def add_employee(self, token='', id='', fName='', lName='', mName='',
                     cId='', mail='', url='', phone='', birth='', active=None):
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

    def employee_list(self, id):
        return requests.get(self.url + 'employee',
                            params={'company': str(id)})

    def edit_employee(self, id='', token='', lName='', mail='', url='',
                      phone='', active=''):
        changes = {
            "lastName": lName,
            "email": mail,
            "url": url,
            "phone": phone,
            "isActive": active
        }
        return requests.patch(self.url + 'employee/' + str(id),
                              headers=token, json=changes)

    def employee(self, id=''):
        return requests.get(self.url + 'employee/' + str(id))

    def delete_company(self, token, id):
        return requests.get(self.url + 'company/delete/' + str(id),
                            headers=token)
