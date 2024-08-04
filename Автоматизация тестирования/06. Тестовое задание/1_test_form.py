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

browser.find_element(By.TAG_NAME, "button").click()


def test_red():
    assert browser.find_element(
        By.CSS_SELECTOR, "#zip-code"
        ).value_of_css_property('background-color') == 'rgb(248, 215, 218)'


def test_green():
    assert browser.find_element(
        By.CSS_SELECTOR, ".alert:not(#zip-code)"
        ).value_of_css_property('background-color') == 'rgb(209, 231, 221)'


browser.quit()
