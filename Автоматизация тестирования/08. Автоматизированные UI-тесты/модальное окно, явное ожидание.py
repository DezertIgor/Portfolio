from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

# Google Chrome

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                 install()))

browser.maximize_window()
browser.get("http://the-internet.herokuapp.com/entry_ad")

# Явное ожидание
popup = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          '.modal-footer > p')))

cancel = browser.find_element(By.CSS_SELECTOR, '.modal-footer > p')
cancel.click()
sleep(2)


# Firefox

browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().
                                                   install()))

browser.maximize_window()
browser.get("http://the-internet.herokuapp.com/entry_ad")

# Явное ожидание
popup = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR,
                                          '.modal-footer > p')))

cancel = browser.find_element(By.CSS_SELECTOR, '.modal-footer > p')
cancel.click()
sleep(2)
