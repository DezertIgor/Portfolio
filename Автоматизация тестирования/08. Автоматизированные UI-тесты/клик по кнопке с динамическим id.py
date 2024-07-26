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
browser.get("http://uitestingplayground.com/dynamicid")
blue_button = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
blue_button.click()
sleep(3)


# Firefox

browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().
                                                   install()))

browser.maximize_window()
browser.get("http://uitestingplayground.com/dynamicid")
blue_button = browser.find_element(By.CSS_SELECTOR, '.btn-primary')
blue_button.click()
sleep(3)
