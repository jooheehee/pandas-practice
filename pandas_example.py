import pandas as pd

# Create a simple DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}

df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Calculate the average age
average_age = df['Age'].mean()
print(f"Average Age: {average_age}")