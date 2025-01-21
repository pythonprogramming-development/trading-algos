import pandas as pd
import numpy as np
import time
import math
new_df = pd.read_csv("data.csv")
def minute_conversion(timeframe, data):
    i = 0
    value1, value1_index, value2, value2_index = 0, 0, 0, 0
    count = 0
    new_list = []
    df = data
    day_change_index = []

    for i, x in enumerate(data.date):
        if x[11:] == "00:05:00.000Z":
            day_change_index.append(i)

    for j in day_change_index:
        d = math.ceil((j - i) / timeframe)
        count = 0

        for k in range(i, j + 1, timeframe):
            count += 1

            if count != d:
                m = df.loc[k, "date"]
                n = df.loc[k + (timeframe) - 1, "date"]

                value1_index = df.index[df['date'] == m].tolist()[0]
                value2_index = df.index[df['date'] == n].tolist()[0]

                new_list.append([n, df.loc[value1_index, "open"], max(df.loc[value1_index:value2_index, "high"]),
                                 min(df.loc[value1_index:value2_index, "low"]), df.loc[value2_index, "close"],
                                 sum(df.loc[value1_index:value2_index, "volume"])])

            else:
                m = df.loc[k, "date"]
                n = df.loc[j - 1, "date"]

                value1_index = df.index[df['date'] == m].tolist()[0]
                value2_index = df.index[df['date'] == n].tolist()[0]

                new_list.append([n, df.loc[value1_index, "open"], max(df.loc[value1_index:value2_index, "high"]),
                                 min(df.loc[value1_index:value2_index, "low"]), df.loc[value2_index, "close"],
                                 sum(df.loc[value1_index:value2_index, "volume"])])
        i = j

    new_data = pd.DataFrame(new_list, columns=["date", "open", "high", "low", "close", "volume"])
    return new_data

# Example usage:
a = minute_conversion(72, new_df)
a = a.drop_duplicates()
a = a.reset_index(drop=True)
# b = HA(new_df)

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# Assume 'a' is the DataFrame that has been returned from the minute_conversion function

# Convert 'date' column to datetime format if it's not already
a['date'] = pd.to_datetime(a['date'])

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the open, high, low, and close as candlestick
ax.plot(a['date'], a['open'], label="Open", color='blue', lw=1)
ax.plot(a['date'], a['high'], label="High", color='green', lw=1)
ax.plot(a['date'], a['low'], label="Low", color='red', lw=1)
ax.plot(a['date'], a['close'], label="Close", color='black', lw=2)

# Formatting the x-axis (date)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M'))
ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))
plt.xticks(rotation=45)
plt.xlabel('Date')
plt.ylabel('Price')

# Adding title and legend
plt.title('Financial Data: Open, High, Low, Close')
plt.legend(loc='best')

# Show the plot
plt.tight_layout()
plt.show()
