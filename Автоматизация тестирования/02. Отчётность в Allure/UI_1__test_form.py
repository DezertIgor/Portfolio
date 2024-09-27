from UI_class import Form
import allure


@allure.title("Hands-On Selenium WebDriver with Java")
@allure.description("Цвет полей при невалидном сценарии")
@allure.feature("Заполнение формы")
@allure.severity("Высокий")
def test():
    form = Form()
    form.get()
    form.filling()
    form.click()
    must_be_red = form.color_of_red_element()
    list_of_colors = form.color_of_green_elements()
    with allure.step("Сравнение цвета поля 'Zip code' с красным"):
        assert must_be_red == 'rgba(248, 215, 218, 1)'
    with allure.step("Сравнение цвета всех полей, кроме 'Zip code', с зелёным"
                     ):
        for color in list_of_colors:
            assert color == "rgba(209, 231, 221, 1)"
