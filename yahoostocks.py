import requests
from datetime import datetime
import time

start_date = input("Enter start date in yyyy/mm/dd format: ")
end_date  = input("Enter end date in yyyy/mm/dd format: ")

stock = input("Input stock name(e.g. MSFT for Microsoft): ")

sd = datetime.strptime(start_date, "%Y/%m/%d")
ed = datetime.strptime(end_date, "%Y/%m/%d")

start_epoch = time.mktime(sd.timetuple())
end_epoch = time.mktime(ed.timetuple())
print(start_epoch)

url = f"https://query1.finance.yahoo.com/v7/finance/download/{stock}?period1={int(start_epoch)}&period2={int(end_epoch)}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url, headers=headers).content

with open("data.csv", 'wb') as file:
    file.write(content)
