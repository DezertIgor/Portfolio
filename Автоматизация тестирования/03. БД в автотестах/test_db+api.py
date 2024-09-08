from api import Clients
from db import Db
from time import sleep


db = Db("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")


api = Clients('https://x-clients-be.onrender.com/')
token = api.auth()


db.add_company()
print(db.all_company()[-1])

sleep(30)

company_id = db.company_id()
print(company_id)


emp = {
  "id": 0,
  "firstName": "Игнат",
  "lastName": "Васюков",
  "middleName": "Прохорович",
  "companyId": company_id,
  "email": "pochta@mail.com",
  "url": "https://upload.wikimedia.org/wikipedia/ru/6/69/My_Little_Pony_Friendship_Is_Magic_mobile_game_cover_art.jpg",
  "phone": "7-999-888-77-55",
  "birthdate": "2024-08-18T19:50:41.659Z",
  "isActive": True
}

change = {
  "lastName": 'фон Триер',
  "email": 'toptop@pochta.ru',
  "url": 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZxO5K95EXJvvO1reJwK3WakT8b7tuvsMBXgs',
  "phone": '0',
  "isActive": False
}


def test_add_without_id():
    before = db.all_strings()
    assert api.add_employee(token, None, emp["firstName"],
                            emp["lastName"],
                            emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 500
    assert before == db.all_strings()


def test_add_with_empty_id():
    before = db.all_strings()
    assert api.add_employee(token, "", emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 500
    assert before == db.all_strings()


def test_add_without_firstName():
    before = db.all_strings()
    assert api.add_employee(token, emp["id"], '',
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 400
    assert before == db.all_strings()


def test_add_without_lastName():
    before = db.all_strings()
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            '', emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 400
    after = db.all_strings()
    assert before == after


def test_add_withou_middleName():
    before = db.all_strings()
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], '',
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 201
    assert db.all_strings() == before + 1


def test_add_empty_companyId():
    before = db.all_strings()
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            None, emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 500
    assert db.all_strings() == before


def test_add_without_companyId():
    before = db.all_strings()
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            "", emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 400
    assert db.all_strings() == before


def test_add_without_email():
    before = db.all_strings()
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], "",
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 400
    assert db.all_strings() == before


def test_add_without_avatar():
    before = db.all_strings()
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], emp["email"],
                            "", emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 201
    assert db.all_strings() == before + 1


def test_add_without_phone():
    before = db.all_strings()
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], "",
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 201
    assert db.all_strings() == before + 1


def test_add_without_birth():
    before = db.all_strings()
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            "", emp["isActive"]
                            ).status_code == 500
    assert db.all_strings() == before


def test_add_empty_isActive():
    before = db.all_strings()
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], ""
                            ).status_code == 500
    assert db.all_strings() == before


def test_add_without_isActive():
    before = db.all_strings()
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], None
                            ).status_code == 500
    assert db.all_strings() == before


def test_add_without_all_values():
    before = db.all_strings()
    assert api.add_employee(token
                            ).status_code == 400
    assert db.all_strings() == before


def test_add_employee():
    before = db.all_strings()
    assert api.add_employee(token,
                            emp["id"],
                            emp["firstName"],
                            emp["lastName"],
                            emp["middleName"],
                            emp["companyId"],
                            emp["email"],
                            emp["url"],
                            emp["phone"],
                            emp["birthdate"],
                            emp["isActive"]
                            ).status_code == 201
    assert emp['firstName'] == db.last_string()[4]
    assert emp['lastName'] == db.last_string()[5]
    assert emp['middleName'] == db.last_string()[6]
    assert emp['companyId'] == db.last_string()[11]
    # assert emp['email'] == db.last_string()[2]
    assert emp['url'] == db.last_string()[10]
    assert emp['phone'] == db.last_string()[7]
    assert str(emp['birthdate'])[:10] == str(db.last_string()[9])
    assert emp['isActive'] == db.last_string()[1]
    # assert emp['id'] == db.last_string()[0]
    assert db.all_strings() == before + 1


def test_edit_without_all_values():
    before = db.all_strings()
    db.add_employee(company_id)
    employee_id = db.employee_id('Васюков')
    assert db.all_strings() == before + 1
    assert api.edit_employee(employee_id, token
                             ).status_code == 400
    assert emp['firstName'] == db.find_employee('Васюков')[4]
    assert emp['lastName'] == db.find_employee('Васюков')[5]
    assert emp['middleName'] == db.find_employee('Васюков')[6]
    assert emp['companyId'] == db.find_employee('Васюков')[11]
    # assert emp['email'] == db.find_employee('Васюков')[2]
    assert emp['url'] == db.find_employee('Васюков')[10]
    assert emp['phone'] == db.find_employee('Васюков')[7]
    assert str(emp['birthdate'])[:10] == str(db.find_employee('Васюков')[9])
    assert emp['isActive'] == db.find_employee('Васюков')[1]


def test_edit__without_lastName():
    employee_id = db.employee_id('Васюков')
    assert api.edit_employee(employee_id, token, "",
                             change["email"], change["url"],
                             change["phone"], change["isActive"]
                             ).status_code == 400
    assert emp['firstName'] == db.find_employee('Васюков')[4]
    assert emp['lastName'] == db.find_employee('Васюков')[5]
    assert emp['middleName'] == db.find_employee('Васюков')[6]
    assert emp['companyId'] == db.find_employee('Васюков')[11]
    # assert emp['email'] == db.find_employee('Васюков')[2]
    assert emp['url'] == db.find_employee('Васюков')[10]
    assert emp['phone'] == db.find_employee('Васюков')[7]
    assert str(emp['birthdate'])[:10] == str(db.find_employee('Васюков')[9])
    assert emp['isActive'] == db.find_employee('Васюков')[1]


def test_edit_without_email():
    employee_id = db.employee_id('Васюков')
    assert api.edit_employee(employee_id, token, change["lastName"],
                             "", change["url"],
                             change["phone"], change["isActive"]
                             ).status_code == 400
    assert emp['firstName'] == db.find_employee('Васюков')[4]
    assert emp['lastName'] == db.find_employee('Васюков')[5]
    assert emp['middleName'] == db.find_employee('Васюков')[6]
    assert emp['companyId'] == db.find_employee('Васюков')[11]
    # assert emp['email'] == db.find_employee('Васюков')[2]
    assert emp['url'] == db.find_employee('Васюков')[10]
    assert emp['phone'] == db.find_employee('Васюков')[7]
    assert str(emp['birthdate'])[:10] == str(db.find_employee('Васюков')[9])
    assert emp['isActive'] == db.find_employee('Васюков')[1]


def test_edit_without_isActive():
    employee_id = db.employee_id('Васюков')
    assert api.edit_employee(employee_id, token, change["lastName"],
                             change["email"], change["url"],
                             change["phone"], None
                             ).status_code == 500
    assert emp['firstName'] == db.find_employee('Васюков')[4]
    assert emp['lastName'] == db.find_employee('Васюков')[5]
    assert emp['middleName'] == db.find_employee('Васюков')[6]
    assert emp['companyId'] == db.find_employee('Васюков')[11]
    # assert emp['email'] == db.find_employee('Васюков')[2]
    assert emp['url'] == db.find_employee('Васюков')[10]
    assert emp['phone'] == db.find_employee('Васюков')[7]
    assert str(emp['birthdate'])[:10] == str(db.find_employee('Васюков')[9])
    assert emp['isActive'] == db.find_employee('Васюков')[1]


def test_edit_with_empty_isActive():
    employee_id = db.employee_id('Васюков')
    assert api.edit_employee(employee_id, token, change["lastName"],
                             change["email"], change["url"],
                             change["phone"], ""
                             ).status_code == 400
    assert emp['firstName'] == db.find_employee('Васюков')[4]
    assert emp['lastName'] == db.find_employee('Васюков')[5]
    assert emp['middleName'] == db.find_employee('Васюков')[6]
    assert emp['companyId'] == db.find_employee('Васюков')[11]
    # assert emp['email'] == db.find_employee('Васюков')[2]
    assert emp['url'] == db.find_employee('Васюков')[10]
    assert emp['phone'] == db.find_employee('Васюков')[7]
    assert str(emp['birthdate'])[:10] == str(db.find_employee('Васюков')[9])
    assert emp['isActive'] == db.find_employee('Васюков')[1]


def test_edit_without_avatar():
    employee_id = db.employee_id('Васюков')
    assert api.edit_employee(employee_id, token, change["lastName"],
                             change["email"], "",
                             change["phone"], change["isActive"]
                             ).status_code == 200
    assert emp['firstName'] == db.find_employee(change["lastName"])[4]
    assert change['lastName'] == db.find_employee(change["lastName"])[5]
    assert emp['middleName'] == db.find_employee(change["lastName"])[6]
    assert emp['companyId'] == db.find_employee(change["lastName"])[11]
    # assert change['email'] == db.find_employee(change["lastName"])[2]
    assert emp['url'] == db.find_employee(change["lastName"])[10]
    assert change['phone'] == db.find_employee(change["lastName"])[7]
    assert str(emp['birthdate'])[:10] == str(db.find_employee(change["lastName"])[9])
    assert change['isActive'] == db.find_employee(change["lastName"])[1]


def test_edit_without_phone():
    db.add_employee(company_id)
    employee_id = db.employee_id('Васюков')
    assert api.edit_employee(employee_id, token, change["lastName"],
                             change["email"], change["url"],
                             "", change["isActive"]
                             ).status_code == 200
    assert emp['firstName'] == db.find_employee(change["lastName"])[4]
    assert change['lastName'] == db.find_employee(change["lastName"])[5]
    assert emp['middleName'] == db.find_employee(change["lastName"])[6]
    assert emp['companyId'] == db.find_employee(change["lastName"])[11]
    # assert change['email'] == db.find_employee(change["lastName"])[2]
    assert change['url'] == db.find_employee(change["lastName"])[10]
    assert emp['phone'] == db.find_employee(change["lastName"])[7]
    assert str(emp['birthdate'])[:10] == str(db.find_employee(change["lastName"])[9])
    assert change['isActive'] == db.find_employee(change["lastName"])[1]


def test_edit():
    db.add_employee(company_id)
    employee_id = db.employee_id('Васюков')
    assert api.edit_employee(employee_id, token, change["lastName"],
                             change["email"], change["url"],
                             change["phone"], change["isActive"]
                             ).status_code == 200
    assert emp['firstName'] == db.find_employee(change["lastName"])[4]
    assert change['lastName'] == db.find_employee(change["lastName"])[5]
    assert emp['middleName'] == db.find_employee(change["lastName"])[6]
    assert emp['companyId'] == db.find_employee(change["lastName"])[11]
    # assert change['email'] == db.find_employee(change["lastName"])[2]
    assert change['url'] == db.find_employee(change["lastName"])[10]
    assert change['phone'] == db.find_employee(change["lastName"])[7]
    assert str(emp['birthdate'])[:10] == str(db.find_employee(change["lastName"])[9])
    assert change['isActive'] == db.find_employee(change["lastName"])[1]


def test_employee():
    employee_id = db.employee_id(change["lastName"])
    employee = api.employee(employee_id).json()
    assert employee["id"] == employee_id
    assert employee["isActive"] == change["isActive"]
    assert employee["lastChangedDateTime"] != employee["createDateTime"]
    assert employee["firstName"] == emp["firstName"]
    assert employee["lastName"] == change["lastName"]
    assert employee["middleName"] == emp["middleName"]
    assert employee["phone"] == change["phone"]
    assert employee["email"] == change["email"]
    assert employee["birthdate"] == emp["birthdate"][:10]
    assert employee["avatar_url"] == change["url"]
    assert employee["companyId"] == company_id


def test_delete():
    before_company = len(db.all_company())
    before_employee = db.all_strings()
    assert api.delete_company(token, company_id).status_code == 200
    assert len(db.all_company()) == before_company - 1
    assert db.all_strings() < before_employee
    assert db.last_string()[0] != db.find_employee(change["lastName"])
