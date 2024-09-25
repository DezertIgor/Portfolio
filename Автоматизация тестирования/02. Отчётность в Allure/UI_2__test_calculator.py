from UI_class import Calculator


def test():
    calc = Calculator()
    calc.get()
    result = calc.calculate_and_wait()
    assert result == '15'
