from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_login_negative():
    # create driver
    driver = webdriver.Chrome()

    # open login page
    driver.get("https://github.com/login")

    # enter wrong/correct email
    login_field = driver.find_element(By.ID, "login_field")
    login_field.send_keys("some_incorrect_email@gmail.com")

    # enter wrong password
    pass_field = driver.find_element(By.ID, "password")
    pass_field.send_keys("dgkhdkkjfkj")

    # click sign in button
    singin_btn = driver.find_element(By.NAME, "commit")
    singin_btn.click()

    # check error message
    

    driver.quit()