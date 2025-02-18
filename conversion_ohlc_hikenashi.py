import pandas as pd
import numpy as np
import time
import math
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from mplfinance.original_flavor import candlestick_ohlc

new_df = pd.read_csv("data.csv")
new_df = new_df[['date','open','high','low','close','volume']]
new_df.head()
# date	open	high	low	close	volume
# 0	2018-04-12 09:15:00+05:30	295.00	295.75	293.25	293.80	55378
# 1	2018-04-12 09:20:00+05:30	293.75	293.75	292.55	292.95	32219
# 2	2018-04-12 09:25:00+05:30	292.95	293.40	292.65	292.80	23643
# 3	2018-04-12 09:30:00+05:30	292.80	293.00	292.75	292.80	12313
# 4	2018-04-12 09:35:00+05:30	292.75	292.85	291.50	291.55	32198
def HA(df, ohlc=['open', 'high', 'low', 'close']):
    ha_open = 'HA_' + ohlc[0]
    ha_high = 'HA_' + ohlc[1]
    ha_low = 'HA_' + ohlc[2]
    ha_close = 'HA_' + ohlc[3]

    df[ha_open] = 0.0000
    df[ha_high] = 0.0000
    df[ha_low] = 0.0000
    df[ha_close] = 0.0000
    
    df[ha_close] = (df[ohlc[0]] + df[ohlc[1]] + df[ohlc[2]] + df[ohlc[3]]) / 4

    df[ha_open] = 0.00
    for i in range(0, len(df)):
        if i == 0:
            df[ha_open].iat[i] = (df[ohlc[0]].iat[i] + df[ohlc[3]].iat[i]) / 2
        else:
            df[ha_open].iat[i] = (df[ha_open].iat[i - 1] + df[ha_close].iat[i - 1]) / 2
            
    df[ha_high]=df[[ha_open, ha_close, ohlc[1]]].max(axis=1)
    df[ha_low]=df[[ha_open, ha_close, ohlc[2]]].min(axis=1)
    
    del df['open']
    del df['high']
    del df['low']
    del df['close']
    
    df['open'] = df['HA_open']
    df['high'] = df['HA_high']
    df['low'] = df['HA_low']
    df['close'] = df['HA_close']
    
    df = df[['date','open','high','low','close','volume']]
    df = df.round(1)
    return df
z=HA(new_df)
z.head()             

# Convert date to datetime and then to float for plotting
new_df['date'] = pd.to_datetime(new_df['date'])
new_df['date'] = new_df['date'].apply(mdates.date2num)

# Create a new DataFrame for plotting
plot_df = new_df[['date', 'open', 'high', 'low', 'close']]

# Plotting
fig, ax = plt.subplots()
candlestick_ohlc(ax, plot_df.values, width=0.01, colorup='g', colordown='r')
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('OHLC Chart')
plt.grid(True)
plt.show()