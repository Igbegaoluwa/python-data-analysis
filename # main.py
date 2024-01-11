# main.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generate random sales data
np.random.seed(42)

products = ['Product A', 'Product B', 'Product C', 'Product D']
sales_data = {
    'Product': np.random.choice(products, size=100),
    'Sales': np.random.randint(10, 100, size=100)
}

# Create a DataFrame
df = pd.DataFrame(sales_data)

# Display the first few rows of the DataFrame
print("Generated Sales Data:")
print(df.head())

# Calculate total sales for each product
total_sales = df.groupby('Product')['Sales'].sum().reset_index()

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(total_sales['Product'], total_sales['Sales'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Total Sales')
plt.title('Total Sales by Product')
plt.show()
