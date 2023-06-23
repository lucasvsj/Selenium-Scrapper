# Scrapping
## SetUp
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
## Scrapping
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Other
from dotenv import load_dotenv

# Built-in
from time import sleep
from random import random
import os

load_dotenv()

# GLOBAL VARS
URL = f'http://192.168.0.21'
DRIVER = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
WAIT = WebDriverWait(DRIVER, 10)

# MAIN LOGIC
def login(driver, password):
    element = driver.find_element(By.XPATH, "//a[@href='/login/']")
    element.click()
    element = WAIT.until(EC.presence_of_element_located((By.XPATH, "//input[@id='id_username']")))
    element.send_keys("lucasvsj")
    element = driver.find_element(By.XPATH, "//input[@id='id_password']")
    element.send_keys(password)
    element = driver.find_element(By.XPATH, "//button[text()='Log In']")
    element.click()

def logout(driver):
    element = driver.find_element(By.XPATH, "//a[@href='/logout/']")
    element.click()
    element = WAIT.until(EC.presence_of_element_located((By.XPATH, "//h2[text()='You have been log out']")))

def access_vault(driver, vault_name, password):
    vault_name = f'//a[text()="{vault_name}"]'
    element = driver.find_element(By.XPATH, vault_name)
    element.click()
    element = WAIT.until(EC.presence_of_element_located((By.XPATH, "//input[@id='id_key']")))
    element.send_keys(password)
    element = driver.find_element(By.XPATH, "//button[text()='Unlock']")
    element.click()

def add_vault_entry(driver, value=None):
    if value is None:
        value = random()
    element = WAIT.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Add Entry']")))
    element.click()
    element = WAIT.until(EC.presence_of_element_located((By.XPATH, "//input[@id='id_data']")))
    element.send_keys(f"Automated Vault Entry Number: {value}")
    element = driver.find_element(By.XPATH, "//button[text()='Create']")
    element.click()


if __name__ == '__main__':
    # Run Variables
    my_password = api_key = os.getenv("PASSWORD")
    # Main
    DRIVER.get(URL)
    login(DRIVER, my_password)
    access_vault(DRIVER, 'My Personal Vault', my_password)
    add_vault_entry(DRIVER)
    user_input = input('>')
    while user_input in ['redo', 'r']:
        add_vault_entry(DRIVER)
        user_input = input('>')

    logout(DRIVER)
    sleep(1)
    DRIVER.close()