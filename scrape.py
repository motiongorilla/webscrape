from selenium import webdriver
import time

def get_driver():
    # service = webdriver.EdgeService(executable_path="~/code/python_automate/webscrape/msedgedriver")
    # Set options for browser
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com")
    print(type(driver))
    return driver

def extractText(text: str):
    """Extract only desired part of the text"""
    left, right = text.split(":")
    right.replace(" ", "")
    return float(right)

def main():
    driver = get_driver()
    time.sleep(2)
    # element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[1]")
    element = driver.find_element(by="id",value="displaytimer")
    return element

scrape = main()
print(extractText(scrape.text))
print(scrape.text)
