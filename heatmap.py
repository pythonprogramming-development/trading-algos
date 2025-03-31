import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import yfinance as yf

# Download historical data for the GLD ETF with auto-adjustment for splits and dividends
ticker = "GLD"
data = yf.download(ticker, start="2018-01-01", end="2023-12-31", auto_adjust=True)

# Calculate daily returns
data['Returns'] = data['Close'].pct_change()

# Drop the first row with NaN returns
data = data.dropna()

# Extract year and month, converting month numbers to month names
data['Year'] = data.index.year
data['Month'] = data.index.strftime('%b')

# Calculate average monthly returns
monthly_returns = data.groupby(['Year', 'Month'])['Returns'].mean().unstack()

# Ensure the months are in correct order
monthly_returns = monthly_returns[['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']]

# Plotting the heatmap with red, green, and yellow color scale, centred around 0
plt.figure(figsize=(12, 6))
sns.heatmap(monthly_returns.T, annot=True, fmt=".2%", cmap="RdYlGn", cbar=True, center=0)
plt.title(f"Average Monthly Returns Heatmap for {ticker} (GOLD ETF)")
plt.show()