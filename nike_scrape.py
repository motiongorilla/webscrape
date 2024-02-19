from selenium import webdriver
from selenium.webdriver.common.by import By
import time

url = "https://nike.com/gb/"

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
    driver = driverPrepare()
    driver.get(url)
    time.sleep(1)
    driver.find_element("class name", "dialog-actions-accept-btn").click()
    time.sleep(2)
    menu_elem = driver.find_element("class name", "pre-desktop-menu")
    menu_elem.find_element("link text", "Men").click()
    section_menu = driver.find_element("class name", "_1uZt26F-")
    section_menu.find_element("css selector", '[aria-label="Just Released"]').click()
    time.sleep(3)
    with open("sneakers.txt", 'w') as file:
        for i in range(1, 10):
            if i == 5:
                continue
            pr = driver.find_element("css selector", f'[data-product-position="{i}"]')
            name = pr.find_element("class name", "product-card__title").text
            link = pr.find_element("class name", "product-card__link-overlay").get_attribute("href")
            file.write(f"\n{name} ({link})")

    return 0
def main():
    login(url)
    return 0

if __name__ == "__main__":
    main()
