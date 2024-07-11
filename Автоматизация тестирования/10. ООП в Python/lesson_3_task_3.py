from address import Address
from mailing import Mailing

mailing = Mailing(Address('000001', "г. Ростов-на-Дону", "ул. Большая Садовая",
                          161, 5),
                  Address("000002", "г. Москва", "ул. Кузнецкий мост", 13, 8),
                  5.55,
                  "S322")

print(f'''Отправление {mailing.track} из {mailing.from_.index}, {mailing.from_.
                                                                 city},
      {mailing.from_.street}, {mailing.from_.house} - {mailing.from_.flate} в
      {mailing.to_.index}, {mailing.to_.city},
      {mailing.to_.street}, {mailing.to_.house} - {mailing.to_.flate}.
      Стоимость {mailing.cost} рублей.''')
