from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Google Chrome

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                 install()))

browser.maximize_window()
browser.get("http://the-internet.herokuapp.com/add_remove_elements/")
add_Element = browser.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
for i in range(0, 5):
    add_Element.click()

sleep(5)

delete = browser.find_elements(By.CSS_SELECTOR, '.added-manually')
print(f'Количество кнопок "Delete" в браузере Google Chrome = {len(delete)}')


# Firefox

browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().
                                                   install()))

browser.maximize_window()
browser.get("http://the-internet.herokuapp.com/add_remove_elements/")
add_Element = browser.find_element(By.CSS_SELECTOR, '[onclick="addElement()"]')
for i in range(0, 5):
    add_Element.click()

sleep(5)

delete = browser.find_elements(By.CSS_SELECTOR, '.added-manually')
print(f'Количество кнопок "Delete" в браузере Firefox = {len(delete)}')
