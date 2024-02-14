import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
load_dotenv()

URL = ('https://developer.automationanywhere.com/challenges/AutomationAnywhereLabs-Login.html?'
       '_ga=2.74340240.325012646.1707265495-1646007937.1707151632&_gl=1*1t4hesj*'
       '_ga*MTY0NjAwNzkzNy4xNzA3MTUxNjMy*'
       '_ga_DG1BTLENXK*MTcwNzI2NTQ5NC4yLjEuMTcwNzI3MTA1Ny40NS4wLjA.')
driver = webdriver.Chrome()
driver.get(URL)
sleep(10)
button_cookie = driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
button_cookie.click()
sleep(10)
username = driver.find_element(By.XPATH, '//*[@id="inputEmail"]')
username.send_keys(os.environ['Username'])
sleep(5)
password = driver.find_element(By.XPATH, '//*[@id="inputPassword"]')
password.send_keys(os.environ['Password'])
sleep(5)
button_login = driver.find_element(By.XPATH, '/html/body/main/div[1]/div/div[2]/div/div/'
                                   'div[2]/div/form/button')
button_login.click()
sleep(5)
driver.quit()
