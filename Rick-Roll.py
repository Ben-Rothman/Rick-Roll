# code that opens rick-roll
from selenium import webdriver
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install() 

driver = webdriver.Chrome()
driver.get("http://www.youtube.com")
driver.maximize_window()
time.sleep(10)
