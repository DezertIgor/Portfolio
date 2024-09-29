from API_class import Clients
from DB_class import Db
import allure


db = Db("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")


api = Clients('https://x-clients-be.onrender.com/')
token = api.auth()


db.add_company()

company_id = db.company_id()


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


@allure.title("Добавление сотрудника с None в id")
@allure.description("""При добавлении сотрудника обязательное поле 'id'
                    заполняется значением None""")
@allure.feature("Создание сотрудника с невалидно заполненными полями")
@allure.severity("Низкий")
def test_add_without_id():
    before = db.all_strings()
    with allure.step("""Статус-код 500 в ответ на попытку добавления
                     сотрудника с None в id"""):
        assert api.add_employee(token, None, emp["firstName"],
                                emp["lastName"],
                                emp["middleName"],
                                emp["companyId"], emp["email"],
                                emp["url"], emp["phone"],
                                emp["birthdate"], emp["isActive"]
                                ).status_code == 500
    with allure.step("Общее количество сотрудников не изменилось"):
        assert before == db.all_strings()


@allure.title("Добавление сотрудника с пустым id")
@allure.description("""При добавлении сотрудника обязательное поле 'id'
                    заполняется пустой строкой""")
@allure.feature("Создание сотрудника с невалидно заполненными полями")
@allure.severity("Низкий")
def test_add_with_empty_id():
    before = db.all_strings()
    with allure.step(""""Статус-код 500 в ответ на попытку добавления
                     сотрудника с пустой строкой в id"""):
        assert api.add_employee(token, "", emp["firstName"],
                                emp["lastName"], emp["middleName"],
                                emp["companyId"], emp["email"],
                                emp["url"], emp["phone"],
                                emp["birthdate"], emp["isActive"]
                                ).status_code == 500
    with allure.step("Общее количество сотрудников не изменилось"):
        assert before == db.all_strings()


@allure.title("Добавление сотрудника с пустым именем")
@allure.description("""При добавлении сотрудника обязательное поле 'firstName'
                    заполняется пустой строкой""")
@allure.feature("Создание сотрудника с невалидно заполненными полями")
@allure.severity("Низкий")
def test_add_without_firstName():
    before = db.all_strings()
    with allure.step(""""Статус-код 400 в ответ на попытку добавления
                     сотрудника без имени"""):
        assert api.add_employee(token, emp["id"], '',
                                emp["lastName"], emp["middleName"],
                                emp["companyId"], emp["email"],
                                emp["url"], emp["phone"],
                                emp["birthdate"], emp["isActive"]
                                ).status_code == 400
    with allure.step("Общее количество сотрудников не изменилось"):
        assert before == db.all_strings()


@allure.title("Добавление сотрудника с пустой фамилией")
@allure.description("""При добавлении сотрудника обязательное поле 'lastName'
                    заполняется пустой строкой""")
@allure.feature("Создание сотрудника с невалидно заполненными полями")
@allure.severity("Низкий")
def test_add_without_lastName():
    before = db.all_strings()
    with allure.step(""""Статус-код 400 в ответ на попытку добавления
                     сотрудника без фамилии"""):
        assert api.add_employee(token, emp["id"], emp["firstName"],
                                '', emp["middleName"],
                                emp["companyId"], emp["email"],
                                emp["url"], emp["phone"],
                                emp["birthdate"], emp["isActive"]
                                ).status_code == 400
    after = db.all_strings()
    with allure.step("Общее количество сотрудников не изменилось"):
        assert before == after


@allure.title("Добавление сотрудника с пустым отчеством")
@allure.description("""При добавлении сотрудника необязательное поле
                    'middleName' заполняется пустой строкой""")
@allure.feature("Создание сотрудника с валидно заполненными полями")
@allure.severity("Средний")
def test_add_without_middleName():
    before = db.all_strings()
    with allure.step(""""Статус-код 201 в ответ на попытку добавления
                     сотрудника без отчества"""):
        assert api.add_employee(token, emp["id"], emp["firstName"],
                                emp["lastName"], '',
                                emp["companyId"], emp["email"],
                                emp["url"], emp["phone"],
                                emp["birthdate"], emp["isActive"]
                                ).status_code == 201
    with allure.step("Общее количество сотрудников увеличилось на один"):
        assert db.all_strings() == before + 1


@allure.title("Добавление сотрудника с None в id компании")
@allure.description("""При добавлении сотрудника обязательное поле 'id'
                    заполняется значением None""")
@allure.feature("Создание сотрудника с невалидно заполненными полями")
@allure.severity("Низкий")
def test_add_empty_companyId():
    before = db.all_strings()
    with allure.step(""""Статус-код 500 в ответ на попытку добавления
                     сотрудника с None в companyId"""):
        assert api.add_employee(token, emp["id"], emp["firstName"],
                                emp["lastName"], emp["middleName"],
                                None, emp["email"],
                                emp["url"], emp["phone"],
                                emp["birthdate"], emp["isActive"]
                                ).status_code == 500
    with allure.step("Общее количество сотрудников не изменилось"):
        assert db.all_strings() == before


@allure.title("Добавление сотрудника с пустым id компании")
@allure.description("""При добавлении сотрудника обязательное поле 'id'
                    заполняется пустой строкой""")
@allure.feature("Создание сотрудника с невалидно заполненными полями")
@allure.severity("Низкий")
def test_add_without_companyId():
    before = db.all_strings()
    with allure.step(""""Статус-код 400 в ответ на попытку добавления
                     сотрудника с пустой строкой в companyId"""):
        assert api.add_employee(token, emp["id"], emp["firstName"],
                                emp["lastName"], emp["middleName"],
                                "", emp["email"],
                                emp["url"], emp["phone"],
                                emp["birthdate"], emp["isActive"]
                                ).status_code == 400
    with allure.step("Общее количество сотрудников не изменилось"):
        assert db.all_strings() == before


@allure.title("Добавление сотрудника без почты")
@allure.description("""При добавлении сотрудника обязательное поле 'email'
                    заполняется пустой строкой""")
@allure.feature("Создание сотрудника с невалидно заполненными полями")
@allure.severity("Низкий")
def test_add_without_email():
    before = db.all_strings()
    with allure.step(""""Статус-код 400 в ответ на попытку добавления
                     сотрудника с пустой строкой в email"""):
        assert api.add_employee(token, emp["id"], emp["firstName"],
                                emp["lastName"], emp["middleName"],
                                emp["companyId"], "",
                                emp["url"], emp["phone"],
                                emp["birthdate"], emp["isActive"]
                                ).status_code == 400
    with allure.step("Общее количество сотрудников не изменилось"):
        assert db.all_strings() == before


@allure.title("Добавление сотрудника без аватара")
@allure.description("""При добавлении сотрудника необязательное поле 'url'
                    заполняется пустой строкой""")
@allure.feature("Создание сотрудника с валидно заполненными полями")
@allure.severity("Высокий")
def test_add_without_avatar():
    before = db.all_strings()
    with allure.step(""""Статус-код 201 в ответ на попытку добавления
                     сотрудника без аватара"""):
        assert api.add_employee(token, emp["id"], emp["firstName"],
                                emp["lastName"], emp["middleName"],
                                emp["companyId"], emp["email"],
                                "", emp["phone"],
                                emp["birthdate"], emp["isActive"]
                                ).status_code == 201
    with allure.step("Общее количество сотрудников увеличилось на один"):
        assert db.all_strings() == before + 1


@allure.title("Добавление сотрудника без телефона")
@allure.description("""При добавлении сотрудника необязательное поле 'phone'
                    заполняется пустой строкой""")
@allure.feature("Создание сотрудника с валидно заполненными полями")
@allure.severity("Высокий")
def test_add_without_phone():
    before = db.all_strings()
    with allure.step(""""Статус-код 201 в ответ на попытку добавления
                     сотрудника без номера телефона"""):
        assert api.add_employee(token, emp["id"], emp["firstName"],
                                emp["lastName"], emp["middleName"],
                                emp["companyId"], emp["email"],
                                emp["url"], "",
                                emp["birthdate"], emp["isActive"]
                                ).status_code == 201
    with allure.step("Общее количество сотрудников увеличилось на один"):
        assert db.all_strings() == before + 1


@allure.title("Добавление сотрудника без даты рождения")
@allure.description("""При добавлении сотрудника обязательное поле 'birthdate'
                    заполняется пустой строкой""")
@allure.feature("Создание сотрудника с невалидно заполненными полями")
@allure.severity("Низкий")
def test_add_without_birth():
    before = db.all_strings()
    with allure.step(""""Статус-код 500 в ответ на попытку добавления
                     сотрудника без даты рождения"""):
        assert api.add_employee(token, emp["id"], emp["firstName"],
                                emp["lastName"], emp["middleName"],
                                emp["companyId"], emp["email"],
                                emp["url"], emp["phone"],
                                "", emp["isActive"]
                                ).status_code == 500
    with allure.step("Общее количество сотрудников не изменилось"):
        assert db.all_strings() == before


@allure.title("Добавление сотрудника без isActive")
@allure.description("""При добавлении сотрудника обязательное поле 'isActive'
                    заполняется пустой строкой""")
@allure.feature("Создание сотрудника с невалидно заполненными полями")
@allure.severity("Низкий")
def test_add_empty_isActive():
    before = db.all_strings()
    with allure.step(""""Статус-код 500 в ответ на попытку добавления
                     сотрудника с пустой строкой в isActive"""):
        assert api.add_employee(token, emp["id"], emp["firstName"],
                                emp["lastName"], emp["middleName"],
                                emp["companyId"], emp["email"],
                                emp["url"], emp["phone"],
                                emp["birthdate"], ""
                                ).status_code == 500
    with allure.step("Общее количество сотрудников не изменилось"):
        assert db.all_strings() == before


@allure.title("Добавление сотрудника с None в isActive")
@allure.description("""Добавление сотрудника со значением 'None' в обязательном
                    поле 'isActive'""")
@allure.feature("Создание сотрудника с невалидно заполненными полями")
@allure.severity("Низкий")
def test_add_without_isActive():
    before = db.all_strings()
    with allure.step(""""Статус-код 500 в ответ на попытку добавления
                     сотрудника с None в isActive"""):
        assert api.add_employee(token, emp["id"], emp["firstName"],
                                emp["lastName"], emp["middleName"],
                                emp["companyId"], emp["email"],
                                emp["url"], emp["phone"],
                                emp["birthdate"], None
                                ).status_code == 500
    with allure.step("Общее количество сотрудников не изменилось"):
        assert db.all_strings() == before


@allure.title("Добавление сотрудника без зполнения полей")
@allure.description("""При добавлении сотрудника в запросе не передаются
                    значения полей""")
@allure.feature("Создание сотрудника с невалидно заполненными полями")
@allure.severity("Низкий")
def test_add_without_all_values():
    before = db.all_strings()
    with allure.step(""""Статус-код 400 в ответ на попытку добавления
                     сотрудника без заполнения полей"""):
        assert api.add_employee(token
                                ).status_code == 400
    with allure.step("Общее количество сотрудников не изменилось"):
        assert db.all_strings() == before


@allure.title("Добавление сотрудника со всеми валидно заполненными полями")
@allure.description("Обычное добавление сотрудника")
@allure.feature("Создание сотрудника с валидно заполненными полями")
@allure.severity("Высокий")
def test_add_employee():
    before = db.all_strings()
    with allure.step("""Статус-код 201 в ответ на добавление сотрудника со
                     всеми валидно заполненными полями"""):
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
    with allure.step("""Сравнение полей информации о пользователе с переданными
                     в запросе значениями"""):
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
    with allure.step("Общее количество сотрудников увеличилось на один"):
        assert db.all_strings() == before + 1


@allure.title("Редактирование информации о сотруднике без заполнения полей")
@allure.description("""При редактировании информации о сотруднике в запросе не
                    передаются значения полей""")
@allure.feature("Редактирование сотрудника с невалидным заполнением полей")
@allure.severity("Средний")
def test_edit_without_all_values():
    before = db.all_strings()
    db.add_employee(company_id)
    employee_id = db.employee_id('Васюков')
    with allure.step("Общее количество сотрудников увеличилось на один"):
        assert db.all_strings() == before + 1
    with allure.step("Статус-код 400 в ответ на редактирование"):
        assert api.edit_employee(employee_id, token
                                 ).status_code == 400
    with allure.step("""Сравнение значений всех полей с изначальными (до
                     редактирования)"""):
        assert emp['firstName'] == db.find_employee('Васюков')[4]
        assert emp['lastName'] == db.find_employee('Васюков')[5]
        assert emp['middleName'] == db.find_employee('Васюков')[6]
        assert emp['companyId'] == db.find_employee('Васюков')[11]
        # assert emp['email'] == db.find_employee('Васюков')[2]
        assert emp['url'] == db.find_employee('Васюков')[10]
        assert emp['phone'] == db.find_employee('Васюков')[7]
        assert str(emp['birthdate'])[:10] == str(db.find_employee('Васюков')[9])
        assert emp['isActive'] == db.find_employee('Васюков')[1]


@allure.title("Редактирование информации о сотруднике без заполнения фамилии")
@allure.description("Обязательное поле 'last_name' заполняется пустой строкой")
@allure.feature("Редактирование сотрудника с невалидным заполнением полей")
@allure.severity("Низкий")
def test_edit__without_lastName():
    employee_id = db.employee_id('Васюков')
    with allure.step("Статус-код 400"):
        assert api.edit_employee(employee_id, token, "",
                                 change["email"], change["url"],
                                 change["phone"], change["isActive"]
                                 ).status_code == 400
    with allure.step("""Сравнение значений всех полей с изначальными (до
                     редактирования)"""):
        assert emp['firstName'] == db.find_employee('Васюков')[4]
        assert emp['lastName'] == db.find_employee('Васюков')[5]
        assert emp['middleName'] == db.find_employee('Васюков')[6]
        assert emp['companyId'] == db.find_employee('Васюков')[11]
        # assert emp['email'] == db.find_employee('Васюков')[2]
        assert emp['url'] == db.find_employee('Васюков')[10]
        assert emp['phone'] == db.find_employee('Васюков')[7]
        assert str(emp['birthdate'])[:10] == str(db.find_employee('Васюков')[9]
                                                 )
        assert emp['isActive'] == db.find_employee('Васюков')[1]


@allure.title("Редактирование информации о сотруднике без указания почты")
@allure.description("Обязательное поле 'email' заполняется пустой строкой")
@allure.feature("Редактирование сотрудника с невалидным заполнением полей")
@allure.severity("Низкий")
def test_edit_without_email():
    employee_id = db.employee_id('Васюков')
    with allure.step("Статус-код 400"):
        assert api.edit_employee(employee_id, token, change["lastName"],
                                 "", change["url"],
                                 change["phone"], change["isActive"]
                                 ).status_code == 400
    with allure.step("""Сравнение значений всех полей с изначальными (до
                     редактирования)"""):
        assert emp['firstName'] == db.find_employee('Васюков')[4]
        assert emp['lastName'] == db.find_employee('Васюков')[5]
        assert emp['middleName'] == db.find_employee('Васюков')[6]
        assert emp['companyId'] == db.find_employee('Васюков')[11]
        # assert emp['email'] == db.find_employee('Васюков')[2]
        assert emp['url'] == db.find_employee('Васюков')[10]
        assert emp['phone'] == db.find_employee('Васюков')[7]
        assert str(emp['birthdate'])[:10] == str(db.find_employee('Васюков')[9]
                                                 )
        assert emp['isActive'] == db.find_employee('Васюков')[1]


@allure.title("Редактирование информации о сотруднике с None в isActive")
@allure.description("Обязательное поле 'isActive' заполняется значением None")
@allure.feature("Редактирование сотрудника с невалидным заполнением полей")
@allure.severity("Низкий")
def test_edit_without_isActive():
    employee_id = db.employee_id('Васюков')
    with allure.step("Статус-код 500"):
        assert api.edit_employee(employee_id, token, change["lastName"],
                                 change["email"], change["url"],
                                 change["phone"], None
                                 ).status_code == 500
    with allure.step("""Сравнение значений всех полей с изначальными (до
                     редактирования)"""):
        assert emp['firstName'] == db.find_employee('Васюков')[4]
        assert emp['lastName'] == db.find_employee('Васюков')[5]
        assert emp['middleName'] == db.find_employee('Васюков')[6]
        assert emp['companyId'] == db.find_employee('Васюков')[11]
        # assert emp['email'] == db.find_employee('Васюков')[2]
        assert emp['url'] == db.find_employee('Васюков')[10]
        assert emp['phone'] == db.find_employee('Васюков')[7]
        assert str(emp['birthdate'])[:10] == str(db.find_employee('Васюков')[9])
        assert emp['isActive'] == db.find_employee('Васюков')[1]


@allure.title("Редактирование информации о сотруднике с пустым isActive")
@allure.description("Обязательное поле 'isActive' заполняется пустой строкой")
@allure.feature("Редактирование сотрудника с невалидным заполнением полей")
@allure.severity("Низкий")
def test_edit_with_empty_isActive():
    employee_id = db.employee_id('Васюков')
    with allure.step("Статус-код 400"):
        assert api.edit_employee(employee_id, token, change["lastName"],
                                 change["email"], change["url"],
                                 change["phone"], ""
                                 ).status_code == 400
    with allure.step("""Сравнение значений всех полей с изначальными (до
                     редактирования)"""):
        assert emp['firstName'] == db.find_employee('Васюков')[4]
        assert emp['lastName'] == db.find_employee('Васюков')[5]
        assert emp['middleName'] == db.find_employee('Васюков')[6]
        assert emp['companyId'] == db.find_employee('Васюков')[11]
        # assert emp['email'] == db.find_employee('Васюков')[2]
        assert emp['url'] == db.find_employee('Васюков')[10]
        assert emp['phone'] == db.find_employee('Васюков')[7]
        assert str(emp['birthdate'])[:10] == str(db.find_employee('Васюков')[9]
                                                 )
        assert emp['isActive'] == db.find_employee('Васюков')[1]


@allure.title("Редактирование информации о сотруднике без указания аватара")
@allure.description("Изображение не является обязательны полем")
@allure.feature("Редактирование сотрудника с валидным заполнением полей")
@allure.severity("Средний")
def test_edit_without_avatar():
    employee_id = db.employee_id('Васюков')
    with allure.step("Статус-код 200"):
        assert api.edit_employee(employee_id, token, change["lastName"],
                                 change["email"], "",
                                 change["phone"], change["isActive"]
                                 ).status_code == 200
    with allure.step("""Сравнение значений всех полей с переданными при
                     редактировании"""):
        assert emp['firstName'] == db.find_employee(change["lastName"])[4]
        assert change['lastName'] == db.find_employee(change["lastName"])[5]
        assert emp['middleName'] == db.find_employee(change["lastName"])[6]
        assert emp['companyId'] == db.find_employee(change["lastName"])[11]
        # assert change['email'] == db.find_employee(change["lastName"])[2]
        assert emp['url'] == db.find_employee(change["lastName"])[10]
        assert change['phone'] == db.find_employee(change["lastName"])[7]
        assert str(emp['birthdate'])[:10] == str(db.find_employee(change[
            "lastName"])[9])
        assert change['isActive'] == db.find_employee(change["lastName"])[1]


@allure.title("Редактирование информации о сотруднике без указания телефона")
@allure.description("Телефон не является обязательным полем")
@allure.feature("Редактирование сотрудника с валидным заполнением полей")
@allure.severity("Средний")
def test_edit_without_phone():
    db.add_employee(company_id)
    employee_id = db.employee_id('Васюков')
    with allure.step("Статус-код 200"):
        assert api.edit_employee(employee_id, token, change["lastName"],
                                 change["email"], change["url"],
                                 "", change["isActive"]
                                 ).status_code == 200
    with allure.step("""Сравнение значений всех полей с переданными при
                     редактировании"""):
        assert emp['firstName'] == db.find_employee(change["lastName"])[4]
        assert change['lastName'] == db.find_employee(change["lastName"])[5]
        assert emp['middleName'] == db.find_employee(change["lastName"])[6]
        assert emp['companyId'] == db.find_employee(change["lastName"])[11]
        # assert change['email'] == db.find_employee(change["lastName"])[2]
        assert change['url'] == db.find_employee(change["lastName"])[10]
        assert emp['phone'] == db.find_employee(change["lastName"])[7]
        assert str(emp['birthdate'])[:10] == str(db.find_employee(change[
            "lastName"])[9])
        assert change['isActive'] == db.find_employee(change["lastName"])[1]


@allure.title("""Редактирование информции о сотруднике со всеми валидно
              заполненными полями""")
@allure.description("Редактирование всех полей информации о сотруднике")
@allure.feature("Редактирование сотрудника с валидным заполнением полей")
@allure.severity("Высокий")
def test_edit():
    db.add_employee(company_id)
    employee_id = db.employee_id('Васюков')
    with allure.step("Статус-код 200"):
        assert api.edit_employee(employee_id, token, change["lastName"],
                                 change["email"], change["url"],
                                 change["phone"], change["isActive"]
                                 ).status_code == 200
    with allure.step("""Сравнение значений всех полей с переданными при
                     редактировании"""):
        assert emp['firstName'] == db.find_employee(change["lastName"])[4]
        assert change['lastName'] == db.find_employee(change["lastName"])[5]
        assert emp['middleName'] == db.find_employee(change["lastName"])[6]
        assert emp['companyId'] == db.find_employee(change["lastName"])[11]
        # assert change['email'] == db.find_employee(change["lastName"])[2]
        assert change['url'] == db.find_employee(change["lastName"])[10]
        assert change['phone'] == db.find_employee(change["lastName"])[7]
        assert str(emp['birthdate'])[:10] == str(db.find_employee(change[
            "lastName"])[9])
        assert change['isActive'] == db.find_employee(change["lastName"])[1]


@allure.title("Поля отредактированного сотрудника")
@allure.description("""Совпадение значения полей информации о сотруднике с
                    заданными при редактировании значениями""")
@allure.feature("Просмотр информации о сотруднике")
@allure.severity("Высокий")
def test_employee():
    employee_id = db.employee_id(change["lastName"])
    employee = api.employee(employee_id).json()
    with allure.step("""Сравнение значений всех полей с переданными при
                     редактировании"""):
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


@allure.title("Удаление компании")
@allure.description("Удаление тестовых данных после проведения тест-рана")
@allure.feature("Зачистка")
@allure.severity("Высокий")
def test_delete():
    before_company = len(db.all_company())
    before_employee = db.all_strings()
    with allure.step("API. Удаление компании"):
        assert api.delete_company(token, company_id).status_code == 200
    with allure.step("DB. Общее количество компаний уменьшилось на один"):
        assert len(db.all_company()) == before_company - 1
    with allure.step("DB. Общее количество сотрудников стало меньше"):
        assert db.all_strings() < before_employee
    with allure.step("""DB. Фамилия последнего сотрудника не совпадает с той,
                     которая принадлежала последнему созданному в автотестах
                     сотруднику"""):
        assert db.last_string()[0] != db.find_employee(change["lastName"])
