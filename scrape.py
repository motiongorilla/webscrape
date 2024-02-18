from selenium import webdriver
from selenium.webdriver.edge.service import Service


def get_driver():
    # service = Service('./msedgedriver')
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
    return driver


def main():
    driver = get_driver()
    element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[1]")
    return element

scrape = main()
print(scrape.text)
