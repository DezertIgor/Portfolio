from sqlalchemy import create_engine, text


class Db:
    def __init__(self, connection_string):
        self.db = create_engine(connection_string).connect()

    def add_company(self):
        return self.db.execute(text("""insert into company(\"name\") values ('Тестовая компания 556')"""))

    def company_id(self):
        return int(self.db.execute(text("""select * from company
    where name = 'Тестовая компания 556'""")
                                   ).fetchall()[-1][0])

    def last_string(self):
        return self.db.execute(text("select * from employee")).fetchall()[-1]

    def all_strings(self):
        return len(self.db.execute(text("select * from employee")).fetchall())

    def all_company(self):
        return self.db.execute(text("select * from company")).fetchall()

    def add_employee(self, company_id):
        self.emp = {
                    "id": 0,
                    "is_active": True,
                    "first_name": 'Игнат',
                    "last_name": 'Васюков',
                    "middle_name": 'Прохорович',
                    "phone": '7-999-888-77-55',
                    "email": 'pochta@mail.com',
                    "avatar_url": 'https://upload.wikimedia.org/wikipedia/ru/6/69/My_Little_Pony_Friendship_Is_Magic_mobile_game_cover_art.jpg',
                    "company_id": company_id,
                    "birthdate": '2024-08-18T19:50:41.659Z'
                   }
        return self.db.execute(text("""insert into employee("id", "is_active",
                                    "first_name", "last_name", "middle_name",
                                    "phone", "email", "avatar_url",
                                    "company_id", "birthdate") values (:id,
                                    :is_active, :first_name,
                                    :last_name, :middle_name,
                                    :phone, :email, :avatar_url,
                                    :company_id, :birthdate)"""), self.emp)

    def employee_id(self, last_name):
        return int(self.db.execute(text("""select * from employee where last_name = :l_name"""),
                                   {'l_name': last_name}).fetchall()[-1][5])

    def find_employee(self, last_name):
        return self.db.execute(text("""select * from employee where last_name = :l_name"""),
                               {'l_name': last_name}).fetchall()[-1]
