from UI_class import Shop
import allure


@allure.title("Интернет-магазин 'Swag Labs'")
@allure.description("Значение поля 'Total' при оформлении заказа")
@allure.feature("Total")
@allure.severity("Высокий")
def test():
    shop = Shop()
    shop.get()
    shop.auth()
    shop.pick()
    shop.cart()
    total = shop.form_and_order()
    with allure.step("Сравнение итоговой стоимости с $58.29"):
        assert total.replace('Total: ', '') == '$58.29'
