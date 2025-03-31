import numpy as np
import pandas as pd
import yfinance as yf
from hurst import compute_Hc
import matplotlib.pyplot as plt

# Download historical stock data
ticker = "AAPL"  

df = yf.download (ticker, start="2010-01-01", end="2024-01-01")

# Define rolling window size (e.g., 252 trading days ~ 1 year)

window_size = 252

# Compute rolling Hurst Exponent
rolling_hurst = df.Close.rolling (window=window_size) .apply (lambda x: compute_Hc (x, kind='price', simplified=True) [0], raw=True)

# Plot the results
plt.figure (figsize= (12, 6))
plt.plot (rolling_hurst, label="Rolling Hurst Exponent", color="blue")
plt.axhline (y=0.5, color="black", linestyle="--", label="H = 0.5 (Random Walk)")
plt.axhline (y=0.3, color="red", linestyle="--", label="H = 0.3 (Mean-Reverting)")
plt.axhline (y=0.7, color="green", linestyle="--", label="H = 0.7 (Trending)")
plt.title (f"Rolling Hurst Exponent for {ticker} ({window_size}-day window)")
plt.xlabel ("Date")
plt.ylabel ("Hurst Exponent")
plt.legend ()
plt.show()