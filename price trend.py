import requests

url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart?vs_currency=usd&days=30"

response = requests.get(url)

print("Status code:", response.status_code)

data = response.json()

print(type(data))
print(data.keys())

print(data['prices'][:5])

import pandas as pd

df = pd.DataFrame(data['prices'], columns=['timestamp', 'price'])
print(df.head())

df['date'] = pd.to_datetime(df['timestamp'], unit='ms')
print(df.head())

df = df[['date', 'price']]
print(df.head())


df.to_csv("ethereum_price_30_days.csv", index=False)
print("CSV saved successfully")

import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))
plt.plot(df['date'], df['price'])

plt.xlabel("Date")
plt.ylabel("Ethereum Price (USD)")
plt.title("Ethereum Price Trend – Last 30 Days")

plt.show()

