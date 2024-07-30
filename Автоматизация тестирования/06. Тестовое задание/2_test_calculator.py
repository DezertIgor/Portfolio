from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
browser.maximize_window()
browser.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

browser.find_element(By.CSS_SELECTOR, '#delay').clear()
browser.find_element(By.CSS_SELECTOR, '#delay').send_keys('45')
browser.find_element(By.CSS_SELECTOR,
                     '.keys > :nth-child(1)').click()
browser.find_element(By.CSS_SELECTOR,
                     '.keys > :nth-child(4)').click()
browser.find_element(By.CSS_SELECTOR,
                     '.keys > :nth-child(2)').click()
browser.find_element(By.CSS_SELECTOR,
                     '.keys > :nth-child(15)').click()


WebDriverWait(browser, 45).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, ".screen"), '15'))


def test():
    assert browser.find_element(By.CSS_SELECTOR, '.screen').text == '15'


browser.quit()
