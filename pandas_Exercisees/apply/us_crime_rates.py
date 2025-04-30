# %%
import pandas as pd
import numpy as np
# %%
url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/US_Crime_Rates/US_Crime_Rates_1960_2014.csv"
crime = pd.read_csv(url)
crime.head()
# %%Step 4. What is the type of the columns?
crime.info()

# %%Step 5. Convert the type of the column Year to datetime64
crime.Year = pd.to_datetime(crime.Year, format = '%Y')
crime.info()

# %%Step 6. Set the Year column as the index of the dataframe
crime = crime.set_index('Year')
crime.head()

# %%
crime = crime.set_index('Year',drop=False)
crime.head()
# %%Step 7. Delete the Total column
del crime['Total']
crime.head()

# %% Step 8. Group the year by decades and sum the values
# Uses resample to sum each decade
crimes = crime.resample('10AS').sum()

# Uses resample to get the max value only for the "Population" column
population = crime['Population'].resample('10AS').max()

# Updating the "Population" column
crimes['Population'] = population

crimes

# %%Step 9. What is the most dangerous decade to live in the US?
crime.idxmax(0)

# %%
crimes.idxmax(0)

# %%
