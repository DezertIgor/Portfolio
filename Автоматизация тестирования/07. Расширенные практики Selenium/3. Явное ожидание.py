from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().
                                                 install()))

browser.maximize_window()
browser.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
WebDriverWait(browser, 55).until(EC.text_to_be_present_in_element(
    (By.CSS_SELECTOR, '#text'), 'Done!'))
print(browser.find_element(By.CSS_SELECTOR, "#award").get_attribute("src"))
browser.quit()
