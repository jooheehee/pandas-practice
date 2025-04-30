# %%
import pandas as pd

# %%Step 3. Assign it to a variable called baby_names.
baby_names = pd.read_csv('https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/06_Stats/US_Baby_Names/US_Baby_Names_right.csv')
baby_names.info()
# %%
baby_names.describe()	
# %%Step 4. See the first 10 entries
baby_names.head(10)


# %%Step 5. Delete the column 'Unnamed: 0' and 'Id'
del baby_names['Unnamed: 0']
del baby_names['Id']
baby_names.head()

# %%Step 6. Are there more male or female names in the dataset?
baby_names['Gender'].value_counts()

# %%Step 7. Group the dataset by name and assign to names
#del baby_names['Year']
names = baby_names.groupby('Name').sum()
names.head()
print(names.shape)
names.sort_values('Count',ascending=0).head()
# %%
print(names.shape)
names.sort_values('Count',ascending=False)
print(names.head())
# %%Step 8. How many different names exist in the dataset?
len(names)

# %%Step 9. What is the name with most occurrences?
names['Count'].idxmax()

# %%
names.Count.idxmax()

# %%Step 10. How many different names have the least occurrences?
len(names[names.Count==names.Count.min()])

# %%
len(names[names.Count == names.Count.min()])
# %%Step 11. What is the median name occurrence?
names[names.Count == names.Count.median()]

# %%Step 12. What is the standard deviation of names?
names.Count.std()

# %%Step 13. Get a summary with the mean, min, max, std and quartiles.
names.describe()
# %%
del baby_names['Year']

# %%
