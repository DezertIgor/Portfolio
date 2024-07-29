from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                 install()))

browser.implicitly_wait(16)
browser.maximize_window()
browser.get("http://uitestingplayground.com/ajax")
browser.find_element(By.CSS_SELECTOR, "#ajaxButton").click()
print(browser.find_element(By.CSS_SELECTOR, ".bg-success").text)
browser.quit()
