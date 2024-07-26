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
browser.get("http://the-internet.herokuapp.com/inputs")
input = browser.find_element(By.CSS_SELECTOR, '[type="number"]')

# Ввод в поле
input.send_keys("1000")
sleep(1)
input.clear()
sleep(1)
input.send_keys("999")
sleep(1)


# Firefox

browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().
                                                   install()))

browser.maximize_window()
browser.get("http://the-internet.herokuapp.com/inputs")
input = browser.find_element(By.CSS_SELECTOR, '[type="number"]')

# Ввод в поле
input.send_keys("1000")
sleep(1)
input.clear()
sleep(1)
input.send_keys("999")
sleep(1)
