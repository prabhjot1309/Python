 #1. Load the dataset and display the first 10 rows.
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/prabhjot1309/Python/refs/heads/main/diamonds.csv')
df.head(10)

#2. Check the shape and column names of the dataset.
df.shape
df.columns
#3. Find and fill missing numeric values with their respective column means.
df.describe()
print(df.isnull().sum())

# 4. Filter rows where `cut` is "Ideal" and `color` is "E".

filtered_df = df[(df['cut'] == 'Ideal') & (df['color'] == 'E')]
print(len(filtered_df))
print(filtered_df)

#5. Group by `cut` and compute the average `price` for each group.
average_price = df.groupby('cut')['price'].mean()
average_price


# 6. Sort the data by `carat` in descending order and show the top 5 rows.
carat=df.sort_values(['carat'],ascending=False).head(5)
print(carat)

# 7. Convert the `price` column to a NumPy array and find its mean, median, and standard deviation.
import pandas as pd
import numpy as np
df = pd.read_csv('https://raw.githubusercontent.com/prabhjot1309/Python/refs/heads/main/diamonds.csv')

price_array = df['price'].to_numpy()
print(price_array)
mean_price = np.mean(price_array)
median_price = np.median(price_array)
std_price = np.std(price_array)
print(f"Mean: {mean_price}")
print(f"Median: {median_price}")
print(f"Standard Deviation: {std_price}")

 #8. Count diamonds with `price > 5000` and `carat > 1` using NumPy conditions.
price_array = df['price'].to_numpy()
carat_array = df['carat'].to_numpy()
condition = (price_array>5000) & (carat_array>1)
count = np.sum(condition)
print("Number of diamonds with 'price>5000' and 'carat>1' is:",count)

# 9. Create a new column `price_updated` by increasing `price` by 10% using NumPy.

df['price_updated'] = df['price'] - (0.1 * df['price'])

print(df)

# 10. Create a `volume` column as `x*y*z` and find the average `price` where `volume > 50`.

df['volume'] = df['x'] * df['y'] * df['z']

avg_price = df[df['volume'] > 50]['price'].mean()
print(df.head())
print(f"Average price: {avg_price}")