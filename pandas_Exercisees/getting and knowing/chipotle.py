# %%
import pandas as pd
import numpy as np


# %%
url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
    
chipo = pd.read_csv(url, sep = '\t')
# %%
chipo.head(10)

# %% what is the number of observation in the dataset?
chipo.shape[0]

# %%
chipo.info()
# %% what is the number of columns in the dataset?
chipo.shape[1]

# %%print the name of all the columns
chipo.columns

# %% how is the dataset indexed?
chipo.index

# %%what was the most -ordered item?
c = chipo.groupby('item_name')
c = c.sum()
c = c.sort_values(['quantity'], ascending = False)
c.head(1)

# %% do it again above stuff
c = chipo.groupby('item_name').sum()
c = c.sort_values(['quantity'], ascending=True)
c.head(1)
# %%how many items were ordered in total?
total_items_orders = chipo.quantity.sum()
total_items_orders

# %% 13 turn the item price into a float
chipo.item_price.dtype
# %%
chipo.order_id.dtype

# %%
chipo.dtypes
# %% create a lambda function and change the type of item price
dollarizer = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(dollarizer)

# %%
chipo.item_price.dtype
# %% how much was the revenue for the period in the dataset?
revenue = (chipo['quantity']*chipo['item_price']).sum()
print ('Revenue was: $' + str(np.round(revenue,2)))
# %% 15. how many orders were made in the period?
orders = chipo.order_id.value_counts()
orders
# %%
orders = chipo.order_id.value_counts().count()
orders
# %%
orders = chipo.order_id.count()
orders
# %% 16. what is the average revenue amount per order?
chipo['revenue'] = chipo['quantity'] * chipo['item_price']
order_grouped = chipo.groupby(by=['order_id']).sum()
order_grouped.mean()
# %%
chipo['item_price'].sum() / 4622
# %%
chipo['item_price'].mean()


# %% 17. how many different items are sold?
chipo.item_name.unique()

# %%
