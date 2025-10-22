import requests
import pandas as pd
from time import sleep
from datetime import date

API_KEY = "212AZSGNVRKAYG8W"

today_date = date.today().strftime("%Y-%m-%d")
# List of common stock symbols to fetch data for
symbols = ["AAPL", "GOOGL", "TSLA", "NVDA"]

base_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&apikey={API_KEY}'

dfs = []
for i in symbols:
  try:
    r = requests.get(base_url+ f'&symbol={i}')
    sleep(12)  # To respect API rate limits
  except Exception as e:
    print(f"Error fetching data for {i}: {e}")
    continue  
  data = r.json()
  print("Fetched data for symbol:", i)
  time_series = data['Time Series (Daily)']
  df = pd.DataFrame(time_series).transpose().rename(
    {"1. open": "open", 
     "2. high": "high", 
     "3. low": "low",
     "4. close": "close", 
     "5. volume": "volume"}, axis='columns').reset_index().rename(columns={"index":"date"})
  df['symbol'] = i
  dfs.append(df)
time_series_data = pd.concat(dfs, ignore_index=True)
time_series_data.date = pd.to_datetime(time_series_data.date)
numeric_columns = ["open","close", "high", "low", "volume"]
time_series_data[numeric_columns] = time_series_data[numeric_columns].apply(pd.to_numeric)

time_series_data.to_csv(f'stock_data/stock_data_{today_date}.csv', index=False) 
print("Data saved to CSV file.")
print("Data fetching complete.")