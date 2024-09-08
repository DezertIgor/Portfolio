from sqlalchemy import create_engine, text

db = create_engine("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0").connect()


def add_company():
    return db.execute(text("""insert into company(\"name\") values ('Тестовая компания 777')"""))


add_company()

print(db.execute(text("select * from company")).fetchall()[-1])
