from smartphone import Smartphone
catalog = []

catalog.append(Smartphone('Samsung', 'Galaxy S4', '+79444444444'))
catalog.append(Smartphone('Samsung', 'Galaxy S5', '+79555555555'))
catalog.append(Smartphone('Samsung', 'Galaxy S6', '+79666666666'))
catalog.append(Smartphone('Samsung', 'Galaxy S7', '+79777777777'))
catalog.append(Smartphone('Samsung', 'Galaxy S8', '+79888888888'))

for i in catalog:
    print (f'{i.mark} - {i.model}. {i.number}')
