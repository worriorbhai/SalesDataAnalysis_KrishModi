import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv('sales_data_sample.csv',encoding='latin1')
df.head()

df.isnull().sum()

df.drop(['ADDRESSLINE2','STATE'],axis=1,inplace=True)

df.duplicated().sum()

df['ORDERDATE'] = pd.to_datetime(df['ORDERDATE'])

df.info()

df.describe()



plt.figure(figsize=(12, 6))
df.groupby('ORDERDATE')['SALES'].sum().plot()
plt.title("Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.grid()
plt.show()



plt.figure(figsize=(10, 5))
sns.barplot(x=monthly_sales.index, y=monthly_sales.values, palette="Blues")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()




top_products = df.groupby('PRODUCTLINE')['SALES'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
top_products.plot(kind='bar', color='green')
plt.title("Top 10 Best-Selling Products")
plt.xlabel("Product Name")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()



plt.figure(figsize=(10, 5))
plt.hist(df['SALES'], bins=30, color='blue', edgecolor='black', alpha=0.7)
plt.title("Sales Distribution")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
