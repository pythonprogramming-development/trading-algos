import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Loading and Understanding the Data
# Load the Chipotle dataset
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipotle_df = pd.read_csv(url, sep='\t')

# Display the first few rows of the dataset
print(chipotle_df.head())

# Display information about the dataset
print(chipotle_df.info())

# Step 2: Data Cleaning
# Check for missing values
print(chipotle_df.isnull().sum())

# Convert item_price to numeric
chipotle_df['item_price'] = chipotle_df['item_price'].apply(lambda x: float(x[1:]))

# Step 3: Exploratory Data Analysis
# Visualize order frequency
order_freq = chipotle_df.groupby('order_id').size().value_counts().sort_index()
plt.figure(figsize=(10, 6))
sns.barplot(x=order_freq.index, y=order_freq.values, color='skyblue')
plt.title('Order Frequency')
plt.xlabel('Number of Items in Order')
plt.ylabel('Number of Orders')
plt.show()

# Visualize popular items
popular_items = chipotle_df['item_name'].value_counts().nlargest(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=popular_items.values, y=popular_items.index, color='salmon')
plt.title('Top 10 Popular Items')
plt.xlabel('Number of Orders')
plt.ylabel('Item Name')
plt.show()

# Visualize item prices
plt.figure(figsize=(10, 6))
sns.histplot(chipotle_df['item_price'], bins=20, kde=True, color='green')
plt.title('Distribution of Item Prices')
plt.xlabel('Item Price ($)')
plt.ylabel('Frequency')
plt.show()

# Visualize order trends over time
chipotle_df['order_date'] = pd.to_datetime(chipotle_df['order_date'])
chipotle_df['order_date'] = chipotle_df['order_date'].dt.date
order_trend = chipotle_df.groupby('order_date').size()
plt.figure(figsize=(12, 6))
order_trend.plot()
plt.title('Order Trends Over Time')
plt.xlabel('Order Date')
plt.ylabel('Number of Orders')
plt.xticks(rotation=45)
plt.show()
