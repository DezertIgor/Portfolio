from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()))
browser.maximize_window()
browser.get(
        "https://www.saucedemo.com/")

browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
browser.find_element(By.CSS_SELECTOR, '#login-button').click()

browser.find_element(By.CSS_SELECTOR,
                     '#add-to-cart-sauce-labs-backpack').click()
browser.find_element(By.CSS_SELECTOR,
                     '#add-to-cart-sauce-labs-bolt-t-shirt').click()
browser.find_element(By.CSS_SELECTOR,
                     '#add-to-cart-sauce-labs-onesie').click()
browser.find_element(By.CSS_SELECTOR,
                     '.shopping_cart_link').click()

browser.find_element(By.CSS_SELECTOR,
                     '#checkout').click()

browser.find_element(By.CSS_SELECTOR, '#first-name').send_keys('Игорь')
browser.find_element(By.CSS_SELECTOR, '#last-name').send_keys('Васюта')
browser.find_element(By.CSS_SELECTOR, '#postal-code').send_keys('344091')
browser.find_element(By.CSS_SELECTOR, '#continue').click()
total = browser.find_element(By.CSS_SELECTOR, '.summary_total_label').text

print(total)

browser.quit()


def test():
    assert total.replace('Total: ', '') == '$58.29'
