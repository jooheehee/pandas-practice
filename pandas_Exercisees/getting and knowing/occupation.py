# %% import the necessary libraries
import pandas as pd
# %% 2
users = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user' , sep='|' , index_col = 'user_id')
# %%
users.head(25)
# %% 5.
users.tail(10)
# %% 6 observations
users.shape[0]

# %% 7
users.shape[1]

# %%
users.columns
# %%
users.index
# %%
users.dtypes
# %%
users.occupation
# %%
users['occupation']
# %% 12
users.occupation.nunique()
# %% 13
users.occupation.value_counts().head()
# %% 13
users.occupation.value_counts().head(1).index[0]
# %% summarize the  dataframe
users.describe()

# %% Step 15. Summarize all the columns

users.describe(include='all')

# %% Step 16. Summarize only the occupation column
users.occupation.describe()

# %%Step 17. What is the mean age of users?
round(users.age.mean())

# %%Step 18. What is the age with least occurrence?
users.age.value_counts().tail()

# %%
