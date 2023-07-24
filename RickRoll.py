from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://www.youtube.com/watch?v=o-YBDTqX_ZU&ab_channel=MusRest")
driver.maximize_window()
time.sleep(2)
pyautogui.moveTo(20, 20, duration = 0.1)
pyautogui.click()
pyautogui.press("f")
time.sleep(100)
