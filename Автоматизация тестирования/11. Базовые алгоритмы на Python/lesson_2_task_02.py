def is_year_leap(year):
    if year % 4 == 0:
        x = True
    else: x = False
    print(f'Год {year}: {x}')
is_year_leap(2007)
