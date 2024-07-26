from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Google Chrome

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                 install()))

browser.maximize_window()
browser.get("http://the-internet.herokuapp.com/login")
username = browser.find_element(By.CSS_SELECTOR, '[name="username"]')
password = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
login = browser.find_element(By.CSS_SELECTOR, '.radius')

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
login.click()


# Firefox

browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().
                                                   install()))

browser.maximize_window()
browser.get("http://the-internet.herokuapp.com/login")
username = browser.find_element(By.CSS_SELECTOR, '[name="username"]')
password = browser.find_element(By.CSS_SELECTOR, '[name="password"]')
login = browser.find_element(By.CSS_SELECTOR, '.radius')

username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")
login.click()
