from selenium import webdriver
from getpass import getpass

driver = webdriver.Chrome(executable_path='/home/chris/Desktop/InstagramAuto/chromedriver')
driver.get('https://www.instagram.com/')

username = input("Enter in your username: ")
password = getpass("Enter your password: ")

username_textbox = driver.find_element_by_name('username')
username_textbox.send_keys(username)

password_textbox = driver.find_element_by_name('password')
password_textbox.send_keys(password)

login_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
login_button.submit()

import time

time.sleep(6)

notification_button = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
notification_button.click()
