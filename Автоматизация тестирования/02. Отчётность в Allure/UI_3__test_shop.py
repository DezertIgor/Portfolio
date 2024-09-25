from PageObject import Shop


def test():
    shop = Shop()
    shop.get()
    shop.auth()
    shop.pick()
    shop.cart()
    total = shop.form_and_order()
    assert total.replace('Total: ', '') == '$58.29'
