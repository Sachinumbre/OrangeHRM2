import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

time.sleep(2)

driver.find_element(By.NAME ,"username").send_keys('Admin')

driver.find_element(By.NAME,"password").send_keys('admin123')

driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(4)

driver.find_element(By.XPATH,"//img[@alt='profile picture']").click()

driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()

driver.close()
