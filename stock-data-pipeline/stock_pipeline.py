import requests
import pandas as pd
from time import sleep
from datetime import date
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")

if not API_KEY:
    raise ValueError("ALPHA_VANTAGE_API_KEY environment variable not set!")

# Create stock_data directory if it doesn't exist
Path('stock_data').mkdir(exist_ok=True)

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

def validate_data(df, symbols):
    """Check if data meets quality standards"""
    issues = []
    
    # Check if we got data for all symbols
    fetched_symbols = df['symbol'].unique()
    missing = set(symbols) - set(fetched_symbols)
    if missing:
        issues.append(f"Missing data for: {missing}")
    
    # Check for null values
    null_counts = df.isnull().sum()
    if null_counts.any():
        issues.append(f"Null values found: {null_counts[null_counts > 0].to_dict()}")
    
    # Check if we have recent data (within last 7 days)
    latest_date = df['date'].max()
    days_old = (pd.Timestamp.now() - latest_date).days
    if days_old > 7:
        issues.append(f"Data is {days_old} days old")
    
    if issues:
        print("DATA QUALITY ISSUES:")
        for issue in issues:
            print(f"  - {issue}")
        return False
    else:
        print("Data quality checks passed")
        return True

# Add this before saving to CSV:
validate_data(time_series_data, symbols)