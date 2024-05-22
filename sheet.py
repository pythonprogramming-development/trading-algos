import pandas as pd
import numpy as np

# Generate example sales data
np.random.seed(0)
start_date = '2023-01-01'
end_date = '2024-12-31'
dates = pd.date_range(start=start_date, end=end_date, freq='D')
sales = np.random.randint(1000, 5000, size=len(dates))

# Create DataFrame
sales_data = pd.DataFrame({'Date': dates, 'Sales': sales})

# Save to CSV
sales_data.to_csv('sales_data.csv', index=False)
