from PageObject import Form


def test():
    form = Form()
    form.get()
    form.filling()
    form.click()
    must_be_red = form.color_of_red_element()
    list_of_colors = form.color_of_green_elements()
    assert must_be_red == 'rgba(248, 215, 218, 1)'
    for color in list_of_colors:
        assert color == "rgba(209, 231, 221, 1)"
