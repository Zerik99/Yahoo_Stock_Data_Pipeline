"""an app to get Stock data from Yahoo Finance with the requests module."""
import random
import time
import requests
import pandas as pd

from_period = 1657776000
to_period = 1687862400
interval = "1d"
ticker_symbol = "amd"

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
]

headers = {
    "authority": "finance.yahoo.com",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": random.choice(user_agents),
}


response = requests.get(
    f"https://query1.finance.yahoo.com/v7/finance/download/{ticker_symbol}?period1={from_period}&period2={to_period}&interval={interval}&events=history&includeAdjustedClose=true",
    headers=headers,
    timeout=5,
)

with open(f"temp_csv/{ticker_symbol}.csv", "wb") as f:
    f.write(response.content)
    f.close()


df = pd.read_csv(
    filepath_or_buffer=f"temp_csv/{ticker_symbol}.csv",
    sep=",",
)

print(df)
