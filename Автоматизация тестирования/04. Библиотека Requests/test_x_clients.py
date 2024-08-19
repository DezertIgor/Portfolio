from x_clients import Clients


api = Clients('https://x-clients-be.onrender.com/')
token = api.auth()


company_id = api.add_company(token).json()['id']

emp = {
  "id": 0,
  "firstName": "Иван",
  "lastName": "Иванов",
  "middleName": "Иванович",
  "companyId": company_id,
  "email": "pochta@mail.com",
  "url": "https://upload.wikimedia.org/wikipedia/ru/6/69/My_Little_Pony_Friendship_Is_Magic_mobile_game_cover_art.jpg",
  "phone": "7-999-888-77-55",
  "birthdate": "2024-08-18T19:50:41.659Z",
  "isActive": True
}

change = {
  "lastName": "фон Триер",
  "email": "toptop@pochta.ru",
  "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQZxO5K95EXJvvO1reJwK3WakT8b7tuvsMBXgs",
  "phone": "0",
  "isActive": False
}

employee_id = api.add_employee(token, emp["id"], emp["firstName"],
                               emp["lastName"], emp["middleName"],
                               emp["companyId"], emp["email"],
                               emp["url"], emp["phone"],
                               emp["birthdate"], emp["isActive"]).json()['id']


def test_list():
    last_emp = api.employee_list(company_id).json()[-1]
    assert last_emp["id"] == employee_id
    assert last_emp["isActive"] == emp["isActive"]
    assert last_emp["lastChangedDateTime"] == last_emp["createDateTime"]
    assert last_emp["firstName"] == emp["firstName"]
    assert last_emp["lastName"] == emp["lastName"]
    assert last_emp["middleName"] == emp["middleName"]
    assert last_emp["phone"] == emp["phone"]
    assert last_emp["email"] == emp["email"]
    assert last_emp["birthdate"] == emp["birthdate"][:10]
    assert last_emp["avatar_url"] == emp["url"]
    assert last_emp["companyId"] == company_id


def test_add_without_id():
    assert api.add_employee(token, None, emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 500


def test_add_with_empty_id():
    assert api.add_employee(token, "", emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 400


def test_add_without_firstName():
    assert api.add_employee(token, emp["id"], '',
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 400


def test_add_without_lastName():
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            '', emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 400


def test_add_withou_middleName():
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], '',
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 201


def test_add_empty_companyId():
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            None, emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 500


def test_add_without_companyId():
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            "", emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 400


def test_add_without_email():
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], "",
                            emp["url"], emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 400


def test_add_without_avatar():
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], emp["email"],
                            "", emp["phone"],
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 201


def test_add_without_phone():
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], "",
                            emp["birthdate"], emp["isActive"]
                            ).status_code == 201


def test_add_without_birth():
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            "", emp["isActive"]
                            ).status_code == 500


def test_add_empty_isActive():
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], ""
                            ).status_code == 400


def test_add_without_isActive():
    assert api.add_employee(token, emp["id"], emp["firstName"],
                            emp["lastName"], emp["middleName"],
                            emp["companyId"], emp["email"],
                            emp["url"], emp["phone"],
                            emp["birthdate"], None
                            ).status_code == 500


def test_add_without_all_values():
    assert api.add_employee(token
                            ).status_code == 400


def test_edit_without_all_values():
    assert api.edit_employee(employee_id, token
                             ).status_code == 400


def test_edit__without_lastName():
    assert api.edit_employee(employee_id, token, "",
                             change["email"], change["url"],
                             change["phone"], change["isActive"]
                             ).status_code == 400


def test_edit_without_email():
    assert api.edit_employee(employee_id, token, change["lastName"],
                             "", change["url"],
                             change["phone"], change["isActive"]
                             ).status_code == 400


def test_edit_without_avatar():
    assert api.edit_employee(employee_id, token, change["lastName"],
                             change["email"], "",
                             change["phone"], change["isActive"]
                             ).status_code == 200


def test_edit_without_phone():
    assert api.edit_employee(employee_id, token, change["lastName"],
                             change["email"], change["url"],
                             "", change["isActive"]
                             ).status_code == 200


def test_edit():
    assert api.edit_employee(employee_id, token, change["lastName"],
                             change["email"], change["url"],
                             change["phone"], change["isActive"]
                             ).status_code == 200


def test_employee():
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


def test_edit_without_isActive():
    assert api.edit_employee(employee_id, token, change["lastName"],
                             change["email"], change["url"],
                             change["phone"], None
                             ).status_code == 500


def test_edit_with_empty_isActive():
    assert api.edit_employee(employee_id, token, change["lastName"],
                             change["email"], change["url"],
                             change["phone"], ""
                             ).status_code == 400
