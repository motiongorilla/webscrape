from bs4 import BeautifulSoup
import requests

def get_currency(in_currency: str, out_currency: str, amount: float):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={amount}"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    result = soup.find("span", class_="ccOutputRslt").get_text()

    return print(result)

def main():
    from_curr = input("Currency to change from: ")
    to_curr = input("Currency to change to: ")
    amount = float(input("Amount to change: "))
    get_currency(from_curr, to_curr, amount)

if __name__ == "__main__":
    main()
