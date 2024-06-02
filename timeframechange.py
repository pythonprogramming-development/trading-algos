import pandas as pd
import numpy as np
import time
import math

def minute_conversion(timeframe, data):
    i = 0
    value1, value1_index, value2, value2_index = 0, 0, 0, 0
    count = 0
    new_list = []
    df = data
    day_change_index = []

    for i, x in enumerate(data.date):
        if x[11:] == "00:01:00.000Z":
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
b = HA(new_df)
