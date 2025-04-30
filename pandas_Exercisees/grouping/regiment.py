# %%
import pandas as pd
# %%
raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}
# %%Step 3. Assign it to a variable called regiment.
regiment = pd.DataFrame(raw_data, columns = raw_data.keys())
regiment

# %%Step 4. What is the mean preTestScore from the regiment Nighthawks?
mean_of_protestscore = regiment.groupby('regiment')['preTestScore'].mean()
mean_of_protestscore

# %%
regiment[regiment['regiment'] == 'Nighthawks']['preTestScore'].mean()


# %%Step 5. Present general statistics by company
regiment.groupby('company').describe()
# %%Step 6. What is the mean of each company's preTestScore?
a = regiment.groupby('company').preTestScore.mean()
a
# %% Step 7. Present the mean preTestScores grouped by regiment and company
regiment.groupby(['company','regiment']).preTestScore.mean()


# %% Step 8. Present the mean preTestScores grouped by regiment and company without heirarchical indexing
regiment.groupby(['regiment','company']).preTestScore.mean().unstack()

# %%
regiment.head()
# %% Step 9. Group the entire dataframe by regiment and company
regiment.groupby(['regiment', 'company']).mean()

# %%
regiment.groupby(['regiment', 'company'])['preTestScore'].mean()

# %% Step 10. What is the number of observations in each regiment and company
regiment.groupby(['company', 'regiment']).size()

# %%Step 11. Iterate over a group and print the name and the whole data from the regiment
# Group the dataframe by regiment, and for each regiment,
for name, group in regiment.groupby('regiment'):
    # print the name of the regiment
    print(name)
    # print the data of that regiment
    print(group)

# %%
for name, group in regiment.groupby('regiment'):
    # print the name of the regiment
    print(name)
# %%
for name, group in regiment.groupby('name'):
    # print the name of the regiment

    # print the data of that regiment
    print(group)
# %% extra example - step 1: regiment + company로 그룹 나눠서 하나씩 출력해보기
for group_name, group_data in regiment.groupby(['regiment','company']):
    print(f" 그룹이름 : {group_name}")
    print(group_data)
    print ('-' *40)
# %% ✅ Step 2: 각 그룹별로 평균만 출력하고 싶으면?
for group_NAME2, group_DATA2 in regiment.groupby(['regiment','company']):
    avg = group_DATA2['preTestScore'].mean()
    print(f"{group_NAME2} 그룹의 preTestScore 평균: {avg}")


# %%
