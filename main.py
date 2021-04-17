import requests
from datetime import datetime

def getDate(timestamp: str):
    return datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')


r = requests.get("https://api.alternative.me/fng/?limit=2").json()
for day in r['data']:
    print(day)

