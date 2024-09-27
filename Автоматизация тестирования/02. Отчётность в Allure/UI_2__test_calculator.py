from UI_class import Calculator
import allure


@allure.title("Hands-On Selenium WebDriver with Java")
@allure.description("Результат после ожидания")
@allure.feature("Вычисление с ожиданием")
@allure.severity("Высокий")
def test():
    calc = Calculator()
    calc.get()
    result = calc.calculate_and_wait()
    with allure.step("Сравнение результата с 15"):
        assert result == '15'
