from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://automated.pythonanywhere.com/login/"

def driverPrepare():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    return driver

def login(url: str):
    username = "automated"
    password = "automatedautomated"

    driver = driverPrepare()
    driver.get(url)
    element = driver.find_element("id", "id_username")
    element.send_keys(username)

    element = driver.find_element("id", "id_password")
    element.send_keys(password)
    element.submit()

    # element = driver.find_element("class name", "navbar-brand")
    element = driver.find_element("link text", "Home")
    element.click()
    time.sleep(3)
    temperature = driver.find_element("id", "displaytimer")
    with open("./Temperature.txt", 'w') as file:
        file.write(temperature.text)

    return 0
def main():
    login(url)
    return 0

if __name__ == "__main__":
    main()
