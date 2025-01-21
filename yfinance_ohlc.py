import yfinance as yf
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

# List of stock symbols in Nifty index
nifty_symbols = ["SBIN.NS"]
# 'ASIANPAINT.NS', 'AXISBANK.NS', 'BAJAJ-AUTO.NS', 'BAJFINANCE.NS', 
#                  'BAJAJFINSV.NS', 'BPCL.NS', 'BHARTIARTL.NS', 'INFRATEL.NS', 'BRITANNIA.NS', 
#                  'CIPLA.NS', 'COALINDIA.NS', 'DRREDDY.NS', 'EICHERMOT.NS', 'GAIL.NS', 'GRASIM.NS', 
#                  'HCLTECH.NS', 'HDFCBANK.NS', 'HEROMOTOCO.NS', 'HINDALCO.NS', 'HINDUNILVR.NS', 
#                  'HDFC.NS', 'ICICIBANK.NS', 'ITC.NS', 'IOC.NS', 'INDUSINDBK.NS', 'INFY.NS', 
#                  'JSWSTEEL.NS', 'KOTAKBANK.NS', 'LT.NS', 'M&M.NS', 'MARUTI.NS', 'NTPC.NS', 
#                  'NESTLEIND.NS', 'ONGC.NS', 'POWERGRID.NS', 'RELIANCE.NS', 'SBIN.NS', 'SUNPHARMA.NS', 
#                  'TCS.NS', 'TATAMOTORS.NS', 'TATASTEEL.NS', 'TECHM.NS', 'TITAN.NS', 'UPL.NS', 
#                  'ULTRACEMCO.NS', 'VEDL.NS', 'WIPRO.NS', 'ZEEL.NS'
# Function to fetch stock data
def fetch_stock_data(symbols, start_date, end_date):
    data = {}
    for symbol in symbols:
        try:
            # Fetch data from Yahoo Finance API 
            # Valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
            stock_data = yf.download(symbol, start=start_date, end=end_date, interval ="5m")
            # Filter required columns
            stock_data = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']]
            data[symbol] = stock_data
            print(f"Fetched data for {symbol}")
        except Exception as e:
            print(f"Failed to fetch data for {symbol}: {e}")
    return data

# Define start and end dates
start_date = '2025-01-16'
end_date = '2025-01-17'

# Fetch stock data for Nifty stocks
nifty_data = fetch_stock_data(nifty_symbols, start_date, end_date)

# Save data to CSV files
for symbol, stock_data in nifty_data.items():
    stock_data.to_csv(f"{symbol}.csv")
    print(f"Saved data for {symbol} to {symbol}.csv")
# Prepare data
    # stock_data.reset_index(inplace=True)
    # stock_data['Date'] = stock_data['Date'].apply(mdates.date2num)
    # ohlc = stock_data[['Date', 'Open', 'High', 'Low', 'Close']]

    # # Plotting
    # fig, ax = plt.subplots()
    # candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='g', colordown='r')
    # ax.xaxis_date()
    # ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # plt.xticks(rotation=45)
    # plt.xlabel('Date and Time')
    # plt.ylabel('Price')
    # plt.title(f'OHLC Chart for {symbol}')
    # plt.grid(True)
    # plt.show()
