import yfinance as yf
import pandas as pd

# List of stock symbols in Nifty index
nifty_symbols = ['ADANIPORTS.NS']
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
            stock_data = yf.download(symbol, start=start_date, end=end_date, interval ="90m")
            # Filter required columns
            stock_data = stock_data[['Open', 'High', 'Low', 'Close', 'Volume']]
            data[symbol] = stock_data
            print(f"Fetched data for {symbol}")
        except Exception as e:
            print(f"Failed to fetch data for {symbol}: {e}")
    return data

# Define start and end dates
start_date = '2024-05-27'
end_date = '2024-05-31'

# Fetch stock data for Nifty stocks
nifty_data = fetch_stock_data(nifty_symbols, start_date, end_date)

# Save data to CSV files
for symbol, stock_data in nifty_data.items():
    stock_data.to_csv(f"{symbol}.csv")
    print(f"Saved data for {symbol} to {symbol}.csv")
