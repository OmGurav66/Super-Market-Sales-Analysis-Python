# -*- coding: utf-8 -*-
"""Supermarket_sales-1650.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qeu0w8IR3k08tGaNqPbqIcAoRt1lypcb
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sales=pd.read_csv("/content/supermarket_sales.csv")

sales.head()

sales.isnull().sum()

sales.shape

sales.columns

sales.describe()

sales['Time'] = pd.to_datetime(sales['Time'])

sales['Hour'] = (sales['Time']).dt.hour

sales['Hour'].nunique()

sales['Hour'].unique()

categorical_columns = [cname for cname in sales.columns if sales[cname].dtype == "object"]

categorical_columns

sales.dtypes

sns.set(style="darkgrid")
sns.barplot(x="Gender",y="Total", data =sales)
plt.title("Gender_Count")
plt.show()

"""Conclusion : By plotting this graph we have founded  a  Gender Count, in this graph we can see that there are more female customer  in supermarket sales datasets.


"""

sns.lineplot(x="Hour",  y = 'Quantity',data =sales)
plt.title("Product Sales per Hour")
plt.show()

"""Conclusion : Below we can see how each branch's sales quantity looks like by the hour in a monthly fashion"""

sales.groupby(['Customer type']).agg({'Total':'sum'})

sns.barplot(x='Customer type', y='Total', data =sales)
plt.title("Customer Type")
plt.show()

"""Conclusion: In this data of customer type there are more member customers than normal customers. Member customer means a member who is at the time of admission to membership a Customer and is so designated by the Board
Normal customer a person who purchases products or services from a person or business frequently


"""

sns.countplot(x="Customer type", hue = "Branch", data =sales)
plt.title("Customer Type by Branch")
plt.show()

"""Conclusion: Branch C  has more member customer and in branch A more normal customers."""

#Products Analysis

sns.barplot(y = 'Product line',x='Quantity',data=sales)
plt.title("Products sales")
plt.show()

"""
Conclusion : From the above visual, Health and Beauty ,Electronic accessories, Home and lifestyle, Sports and travel have a better average quantity sales that food and beverages as well as Fashion accessories.



"""

sns.stripplot(y ='Product line',x= 'Total', hue = "Gender", data = sales)
plt.title("Gender wise sales")
plt.xlabel('Count')
plt.ylabel('Product Type')
plt.show()

"""
Conclusion : This graph shows the gender wise sales. In health and beauty there are more male customers than female customers. In fashion and accessories
there are more females than males, after that we can See that there are lower
number of customers in home and lifestyle in  both male and female category.   By visualising the we can see that more number of females customers are there.

"""

sns.barplot(x='Rating', y='Product line', data =sales)
plt.title("Product rating")
plt.show()

"""Conclusion :  Food and Beverages have the highest average rating while sports and travel the lowest




"""

sns.countplot(y ='Product line', hue = "City", data = sales)
plt.title("City wise products sales")
plt.xlabel('Count')
plt.ylabel('Product Type')
plt.show()

"""Conclusion : Well, Yangon leads at Home & Lifestyle and Electronic accessories.
Naypyitaw  leads at Food & Beverages and Fashion accessories.
Mandalay leads at Sports & Travel and Health & Beauty.




"""

sns.boxplot(x="Branch", y = "Rating" ,data =sales)
plt.title("Ratings by Branch")
plt.show()

"""Conclusion : In this boxplot there are three branches in different colours.
The highest rated branches are A and C, the B becomes the lowest rated branch. We have to work on branch B to get more ratings and profit.






"""

sns.countplot(x="Payment", data =sales)
plt.title("Payment mode")
plt.show()

"""Conclusion: In this graph we found that most of the customer prefer to do payment through Ewallet. The second most is used is Cash payment,most low payments are done by Credit card. We  need to increase more Ewallet payments.



"""

sns.countplot(y ='Product line', hue = "Branch", data = sales)
plt.title("Finding Which Branch has better sales in a particular type products")
plt.xlabel('Count')
plt.ylabel('Product Type')
plt.show()

"""Conclusion: Branch A has more number of sale in electronic accessories and home and lifestyle.
Branch C has more number of sales in food and beverages and fashion and accessories.
Branch B has more number of sales in sports and travel and fashion and accessories and have less sales in other product type.

"""

sns.countplot(x ='City', hue = "Payment", data = sales)
plt.title("Payments done by each city")
plt.show()

"""Conclusion: In this graph we are getting to know that which payment mode customer prefer to pay each city. We can see that there is more usage of Ewallet in Yangon city. In  Naypyitaw city there is customers use more cash payment and in Mandalay city there customer  use of  Ewallat."""