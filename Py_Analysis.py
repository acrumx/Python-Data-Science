import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

pd.set_option('display.width', 600)
pd.set_option('display.max_columns', 18)

sales_df = pd.read_csv("C:/Users/acrum/Documents/train.csv")

print()

print(sales_df.head())

print(sales_df.dtypes)

print(sales_df.describe)

Segmented = sales_df.groupby("Segment")

print(Segmented["Sales"].describe())

print(sales_df.isnull().sum())

print(sales_df[sales_df['Postal Code'].isnull()])

sales_df['Postal Code'] = sales_df['Postal Code'].fillna(5401)

print(sales_df.isnull().sum())

print(sales_df.Category.unique())


# Proportion of All Sales by Segment
sales_df['Segment'].value_counts().plot.pie(subplots = True, autopct='%1.1f%%')
# plt.legend(loc=3) - Created a legend for the three categories in the pie chart 
plt.show()

plt.figure((16, 8))
plt.title("Categories by Revenue", fontsize=12)
plt.bar(sales_df["Category"], sales_df["Sales"], color = '#ff33ec', linewidth=1)
plt.xlabel("Category", fontsize=14)
plt.ylabel("Sales", fontsize=14)
plt.xticks(fontsize=12, rotation=90)
plt.yticks(fontsize=12)

plt.show()