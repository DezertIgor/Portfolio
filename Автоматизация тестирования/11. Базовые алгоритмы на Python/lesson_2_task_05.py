def month_to_season(mes):
    match mes:
        case x if x == 12 or (x < 3 and x >0):
            print('Зима')
        case x if x <= 5 and x >= 3:
            print('Весна')
        case x if x <= 8 and x >= 6:
            print('Лето')
        case x if x < 12 and x > 8:
            print('Осень')
        case _:
            print('Нет такого месяца! Введите значение от "1" до "12".')
month_to_season(13)
