# %%
import pandas as pd
# %%

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'

chipo = pd.read_csv(url, sep = '\t') 
# %% 
print(chipo.head(10))

# %%# %% Step 4. How many products cost more than $10.00?
chipo['item_price'] = chipo['item_price'].str.replace('$', '').astype(float)

chipo_filtered = chipo.drop_duplicates(subset=['item_name', 'quantity', 'choice_description'])
chipo_one_prod = chipo_filtered[chipo_filtered['quantity'] == 1]
#chipo_one_prod
unique_item = chipo_one_prod[chipo_one_prod['item_price'] > 10]['item_name'].unique()
#chipo.query('item_price >10').item_name.unique()
# Count how many NaN values are in the item_price column
print(unique_item)

# %%Step 5. What is the price of each item?
chipo['item_name'].sort_values()

# %%
print(chipo.item_name.sort_values().head(20))  # This will show the first 20 rows

# %%
chipo.sort_values(by = "item_name")
# %%Step 7. What was the quantity of the most expensive item ordered?
chipo['sort_value'](by ='item_price',ascending = False).head(1)

# %%
most_expensive_item = chipo.sort_values(by='item_price',ascending=False).head(1)
print(most_expensive_item['quantity'].iloc[0])
# %%
chipo.sort_values(by = "item_price", ascending = False).head(1)

# %%Step 8. How many times was a Veggie Salad Bowl ordered?
chipo_salad = chipo[chipo.item_name == "Veggie Salad Bowl"]
len(chipo_salad)
# %%
chipo.head(30)
# %%
chipo_salad = chipo[chipo.item_name == "Veggie Salad Bowl"]

len(chipo_salad)
# %%
chipo_salad = chipo[chipo.item_name == "Veggie Salad Bowl"]
print(chipo_salad)
# %%
chipo_salad['quantity']
# %% Step 9. How many times did someone order more than one Canned Soda?
chipo_drink_steak_Bowl = chipo[(chipo.item_name == 'Canned Soda') &(chipo.quantity >1)]
print(chipo_drink_steak_Bowl)
# %%
chipo_drink_steak_Bowl = chipo[(chipo.item_name == 'Canned Soda') &(chipo.quantity >1)]
len(chipo_drink_steak_Bowl)
# %%
