# %%
import pandas as pd

# %%
users = pd.read_table('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user', sep='|',index_col='user_id')
users.head()
# %% Step 4. Discover what is the mean age per occupation
users.groupby('occupation').age.mean()

# %%Step 5. Discover the Male ratio per occupation and sort it from the most to the least
occupation_gender  = users.groupby('occupation')['gender'].value_counts(normalize=True).unstack().fillna(0)
occupation_gender['male_ratio'] = occupation_gender['M']
occupation_gender.sort_values('male_ratio',ascending=False)
# %%
# create a function
def gender_to_numeric(x):
    if x == 'M':
        return 1
    if x == 'F':
        return 0

# apply the function to the gender column and create a new column
users['gender_n'] = users['gender'].apply(gender_to_numeric)


a = users.groupby('occupation').gender_n.sum() / users.occupation.value_counts() * 100 

# sort to the most male 
a.sort_values(ascending = False)
# %% study above answer
#discover male ratio per occupation

users['gender_n'] = users['gender'].apply(lambda x: 1 if x == 'M' else 0)

male_ratio = users.groupby('occupation')['gender_n'].mean()

#sort to the most male
sorted_male_Ratio = male_ratio.sort_values(ascending = False)
print(sorted_male_Ratio)
# %%
# 1. 직업별 남성 비율 계산 (apply 없이)
male_ratio = users.groupby('occupation')['gender'].apply(lambda x: (x == 'M').mean())

# 2. 남성 비율 높은 순서로 정렬
sorted_male_ratio = male_ratio.sort_values(ascending=False)

# 3. 출력
print(sorted_male_ratio)

# %%
users.head(4)
# %%
male_ratio = users.groupby('occupation')['gender'].apply(lambda x: (x == 'M').mean())
sorted_male_ratio = male_ratio.sort_values(ascending=False)

print(sorted_male_ratio)
# %%
users.head(4)

# %%Step 6. For each occupation, calculate the minimum and maximum ages
users.groupby('occupation').age.agg(['min','max'])

# %%Step 7. For each combination of occupation and gender, calculate the mean age
users.groupby(['occupation','gender']).age.mean()

# %%Step 8. For each occupation present the percentage of women and men
gender_ocup = users.groupby(['occupation','gender']).agg({'gender':'count'})

occup_count = users.groupby(['occupation']).agg('count')

occup_gender = gender_ocup.div(occup_count, level="occupation") * 100


# %%
