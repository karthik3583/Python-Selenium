from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get(
    'https://codility-frontend-prod.s3.amazonaws.com/media/task_static/python_selenium_login_page/9a83bda125cd7398f9f482a3d6d45ea4/static/attachments/reference_page.html')

def LoginPageTest():
    login = driver.find_element_by_id('email-input')
    password = driver.find_element_by_id('password-input')
    submit = driver.find_element_by_id('login-button')
    login.send_keys("jack.sparrow@thepiratebay.se")
    password.send_keys("blackpearl")
    submit.click()
    msg = driver.find_element_by_class_name('message success')


LoginPageTest()
