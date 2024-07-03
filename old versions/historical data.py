import requests
import pandas as pd
from datetime import datetime

def fetch_open_interest(symbol, start_time, end_time, interval='8h'):
    url = 'https://fapi.binance.com/futures/data/openInterestHist'
    params = {
        'symbol': symbol,
        'interval': interval,
        'startTime': start_time,
        'endTime': end_time
    }
    response = requests.get(url, params=params)
    try:
        data = response.json()
        if isinstance(data, dict) and 'code' in data:
            print(f"Error fetching open interest data: {data}")
            return []
        return data
    except ValueError as e:
        print(f"Error parsing open interest data: {e}")
        return []

def fetch_funding_rate(symbol, start_time, end_time):
    url = 'https://fapi.binance.com/fapi/v1/fundingRate'
    params = {
        'symbol': symbol,
        'startTime': start_time,
        'endTime': end_time
    }
    response = requests.get(url, params=params)
    try:
        data = response.json()
        if isinstance(data, dict) and 'code' in data:
            print(f"Error fetching funding rate data: {data}")
            return []
        return data
    except ValueError as e:
        print(f"Error parsing funding rate data: {e}")
        return []

def to_timestamp(date_str):
    return int(datetime.strptime(date_str, '%Y-%m-%d').timestamp() * 1000)

def fetch_data(symbol, start_date, end_date):
    start_time = to_timestamp(start_date)
    end_time = to_timestamp(end_date)
    
    oi_data = fetch_open_interest(symbol, start_time, end_time)
    fr_data = fetch_funding_rate(symbol, start_time, end_time)
    
    if not oi_data or not fr_data:
        raise ValueError("One or both datasets are empty.")
    
    print("Open Interest Data:", oi_data[:5])  # Print first 5 entries for inspection
    print("Funding Rate Data:", fr_data[:5])  # Print first 5 entries for inspection
    
    oi_df = pd.DataFrame(oi_data)
    fr_df = pd.DataFrame(fr_data)
    
    if oi_df.empty or fr_df.empty:
        raise ValueError("One or both DataFrames are empty.")
    
    # Convert to datetime for easier manipulation
    oi_df['timestamp'] = pd.to_datetime(oi_df['timestamp'], unit='ms')
    fr_df['fundingTime'] = pd.to_datetime(fr_df['fundingTime'], unit='ms')
    
    # Merge dataframes on time
    merged_df = pd.merge_asof(fr_df.sort_values('fundingTime'), 
                              oi_df.sort_values('timestamp'), 
                              left_on='fundingTime', 
                              right_on='timestamp')
    
    return merged_df

def calculate_weighted_funding_rate(df):
    df['weighted_funding_rate'] = df['openInterest'].astype(float) * df['fundingRate'].astype(float)
    total_oi = df['openInterest'].astype(float).sum()
    weighted_funding_rate = df['weighted_funding_rate'].sum() / total_oi
    return weighted_funding_rate

# Fetch and calculate
symbol = 'BTCUSDT'
start_date = '2023-01-01'
end_date = '2023-12-31'

try:
    data = fetch_data(symbol, start_date, end_date)
    print(data.head())  # Print first few rows to ensure data is correct

    weighted_funding_rate = calculate_weighted_funding_rate(data)
    print(f"Weighted Funding Rate: {weighted_funding_rate}")
except ValueError as e:
    print(e)
