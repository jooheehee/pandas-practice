# %%
import pandas as pd

# %%Step 3. Assign it to a variable called df.

csv_url  = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(csv_url)
df.head()
# %% Step 4. For the purpose of this exercise slice the dataframe from 'school' until the 'guardian' column
stud_alcoh = df.loc[:,"school":'guardian']
stud_alcoh.head()
# %% Step 5. Create a lambda function that will capitalize strings.
capitalizer = lambda x: x.capitalize()

# %%
df.head()
# %%Step 6. Capitalize both Mjob and Fjob
stud_alcoh['Mjob'].apply(capitalizer)
stud_alcoh['Fjob'].apply(capitalizer)

# %%
stud_alcoh['Fjob'] = stud_alcoh['Fjob'].apply(capitalizer)
stud_alcoh['Mjob'] = stud_alcoh['Mjob'].apply(capitalizer)

# %%
df.head()
# %%Step 7. Print the last elements of the data set.
stud_alcoh.tail()

# %%Step 8. Did you notice the original dataframe is still lowercase? Why is that? Fix it and capitalize Mjob and Fjob.
stud_alcoh['Fjob'] = stud_alcoh['Fjob'].apply(capitalizer)
stud_alcoh['Mjob'] = stud_alcoh['Mjob'].apply(capitalizer)
stud_alcoh.tail()

# %% 9 Create a function called majority that returns a boolean value to a new column called legal_drinker (Consider majority as older than 17 years old)
def majority (x):
    if x > 17:
        return True
    else:
        return False
stud_alcoh['legal_drinker'] = stud_alcoh['age'].apply(majority)
stud_alcoh.head()

# %%Step 10. Multiply every number of the dataset by 10.
def times10(x):
    if type(x) is int:
        return 10 * x
    return x
stud_alcoh.apply(times10).head()

# %%
def times10(x):
    if type(x) is int:  # x가 숫자일 때만 곱하기
        return 10 * x
    return x

# 'applymap()'을 사용해 데이터프레임의 각 셀에 함수를 적용
stud_alcoh.applymap(times10).head()
# %%
def times10(x):
    if type(x) == int:
        return x * 10
    return x

# apply() 사용하여 모든 셀에 times10 적용 (행(row) 단위로 적용)
df_times10 = df.apply(lambda row: row.apply(times10), axis=1)

# 결과 출력
print(df_times10)
# %%
def times10(x):
    if isinstance(x, int):  # 숫자인 경우만 처리
        return x * 10
    return x

# 각 column에 대해서 apply를 사용해 Series를 처리하고,
# 각 Series 안에서도 다시 apply로 각 값을 처리
stud_alcoh = stud_alcoh.apply(lambda col: col.apply(times10))
stud_alcoh.head()