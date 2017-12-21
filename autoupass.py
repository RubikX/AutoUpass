#!/usr/bin/python

import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime

# SFU Computing ID and password
username = input("Please enter your SFU username: ")
password = getpass.getpass(prompt="Please enter your SFU password: ")

# Driver setup and load Upass webpage
driver = webdriver.PhantomJS()
driver.get("https://upassbc.translink.ca/")

try:
	title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#cityscape > div:nth-child(1) > h1:nth-child(1)')))

except TimeoutException:
	print("Page timeout")

# Navigate through school selection dropdown menu 
driver.find_element_by_css_selector("#PsiId").click()
driver.find_element_by_css_selector("#PsiId > option:nth-child(10)").click()
driver.find_element_by_css_selector("#goButton").click()

try:
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.site-title > h2:nth-child(1)')))

except TimeoutException:
	print("Page timeout")

# Clear username and password input boxes
driver.find_element_by_id("username").clear()
driver.find_element_by_id("password").clear()

# Fill in credentials and submit
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)
driver.find_element_by_css_selector("#fm1 > input:nth-child(3)").click()

try:
    title = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#home-page > div:nth-child(1) > div:nth-child(1) > h1:nth-child(1)')))

except TimeoutException:
	print("Page timeout")

# Request Upass and save screenshot
driver.find_element_by_css_selector("#chk_1").click()
now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
driver.find_element_by_id("requestButton").click()
driver.save_screenshot('screenshot-{}.png'.format(now))
