import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
load_dotenv()

print(os.environ['Username'])
print(os.environ['Password'])

URL = ('https://developer.automationanywhere.com/challenges/AutomationAnywhereLabs-Login.html?'
       '_ga=2.74340240.325012646.1707265495-1646007937.1707151632&_gl=1*1t4hesj*'
       '_ga*MTY0NjAwNzkzNy4xNzA3MTUxNjMy*'
       '_ga_DG1BTLENXK*MTcwNzI2NTQ5NC4yLjEuMTcwNzI3MTA1Ny40NS4wLjA.')
driver = webdriver.Chrome()
driver.get(URL)
sleep(30)
