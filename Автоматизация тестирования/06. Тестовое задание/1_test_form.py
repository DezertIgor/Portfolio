from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))

browser.maximize_window()
browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

list = [
    ('[name="first-name"]', 'Иван'),
    ('[name="last-name"]', 'Петров'),
    ('[name="address"]', 'Ленина, 55-3'),
    ('[name="zip-code"]', ''),
    ('[name="city"]', 'Москва'),
    ('[name="country"]', 'Россия'),
    ('[name="e-mail"]', 'test@skypro.com'),
    ('[name="phone"]', '+7985899998787'),
    ('[name="job-position"]', 'QA'),
    ('[name="company"]', 'SkyPro')
]
for locator, value in list:
    browser.find_element(By.CSS_SELECTOR, locator).send_keys(value)

browser.find_element(By.CSS_SELECTOR, '[type="submit"]').click()


must_be_red = browser.find_element(By.CSS_SELECTOR, "#zip-code"
                                   ).value_of_css_property('background-color')


def test_red():
    assert must_be_red == 'rgba(248, 215, 218, 1)'


must_be_green = browser.find_elements(By.CSS_SELECTOR, ".alert:not(#zip-code)")

list_of_colors = []
for elem in must_be_green:
    list_of_colors.append(elem.value_of_css_property("background-color"))


def test_green():
    for color in list_of_colors:
        assert color == "rgba(209, 231, 221, 1)"


browser.quit()
