# %%
import pandas as pd
# %%
drinks = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/drinks.csv')
drinks.head()
# %%Step 4. Which continent drinks more beer on average?
drinks.groupby('continent').beer_servings.mean()

# %%Step 5. For each continent print the statistics for wine consumption.
drinks.groupby('continent').wine_servings.describe()

# %%
drinks.groupby('continent').wine_servings.describe(include=all)

# %%
drinks.groupby('continent').wine_servings.corr()
# %%Step 6. Print the mean alcohol consumption per continent for every column
drinks.groupby('continent').mean(numeric_only=True)

# %%Step 7. Print the median alcohol consumption per continent for every column
drinks.groupby('continent').median(numeric_only=True)

# %%Step 8. Print the mean, min and max values for spirit consumption.
drinks.groupby('continent').spirit_servings.agg(['mean','min','max'])

# %%
